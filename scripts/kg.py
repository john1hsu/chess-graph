#!/usr/bin/env python3
"""Chess Knowledge Graph builder and validator.

Usage:
  python3 scripts/kg.py check            # validate only (exit 1 on errors)
  python3 scripts/kg.py build            # validate, then regenerate graph/
  python3 scripts/kg.py similar "Title"  # find existing articles close to a candidate topic;
                                         # volatile matches not verified recently are flagged STALE
  python3 scripts/kg.py stale [--days 180] [--domain players]
                                         # list volatile articles due for re-verification, oldest
                                         # first, and the refresh batch for this run (1-2 articles)
  python3 scripts/kg.py moves "1.e4 e5 2.Nf3"   # check a move sequence and print the resulting FEN

Articles live in articles/<domain>/<slug>.md with YAML frontmatter (see SCHEMA.md).
Move sequences (`moves`), positions (`fen`) and ```pgn blocks are checked for legality
with python-chess. Generated outputs (never hand-edit): graph/graph.jsonld,
graph/triples.nt, graph/index.json, graph/frontier.md, graph/stats.md.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from datetime import date, datetime, timedelta, timezone
from collections import Counter, defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML missing: pip install -r requirements.txt --break-system-packages")
try:
    import chess
    import chess.pgn
except ImportError:  # pragma: no cover
    sys.exit("python-chess missing: pip install -r requirements.txt --break-system-packages")
import io
import logging

logging.getLogger("chess.pgn").setLevel(logging.CRITICAL)  # errors are reported by check_chess

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "articles"
GRAPH = ROOT / "graph"
ONTOLOGY = ROOT / "ontology" / "ontology.ttl"

BASE = "https://github.com/john1hsu/chess-graph/id/"
KTO = "https://github.com/john1hsu/chess-graph/ontology#"
SKOS = "http://www.w3.org/2004/02/skos/core#"
PROV = "http://www.w3.org/ns/prov#"
RDF_TYPE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
RDFS_LABEL = "http://www.w3.org/2000/01/rdf-schema#label"
DCT = "http://purl.org/dc/terms/"

ID_RE = re.compile(r"^kt:[a-z0-9]+(?:-[a-z0-9]+)*$")
SOURCE_TYPES = {
    "governing-body",   # FIDE Handbook (Laws of Chess, title and rating regulations), US Chess, ECF, other federations
    "official-project", # an engine or software project's own docs/site (stockfishchess.org, lczero.org), official event sites
    "primary-record",   # official crosstables, FIDE rating profiles, official game broadcasts, original publications of a game
    "archive",          # museums, libraries, historical collections (World Chess Hall of Fame, John G. White Collection)
    "reference",        # edited reference works (Britannica, Oxford Companion to Chess)
    "book",             # published chess literature from a reputable publisher or a titled author
    "peer-reviewed", "academic", # papers, theses, university material (expertise research, computer chess)
    "publication",      # chess press and editorial: New In Chess, ChessBase News, Chess.com/Lichess editorial (weak)
    "database",         # game databases and explorers: chessgames.com, 365chess, Lichess opening explorer (weak)
    "community",        # Chess Programming Wiki, club pages, forums (weak)
    "news",             # reputable general press, for events and announcements only (weak)
}
STRONG_SOURCE_TYPES = SOURCE_TYPES - {"publication", "database", "community", "news"}
GOVERNING_SOURCE_TYPES = {"governing-body"}
NEEDS_GOVERNING = {"Rule", "Title"}            # these classes must cite a governing body
NEEDS_SCHOLARLY = {"CognitiveConcept"}         # these must cite peer-reviewed or academic work
NEEDS_MOVES = {"Opening", "Variation"}         # these must give their defining moves
REQUIRED = ["id", "type", "title", "domain", "summary", "sources", "created", "verified", "status"]
STATUSES = {"current", "historical", "superseded", "contested", "refuted"}
ECO_RE = re.compile(r"^[A-E]\d{2}(?:-[A-E]\d{2})?(?:, ?[A-E]\d{2}(?:-[A-E]\d{2})?)*$")
STALE_DAYS = 180
MAX_REFRESH_BATCH = 2
NEAR_DUP_THRESHOLD = 0.45   # shingle Jaccard on body text
TITLE_DUP_THRESHOLD = 0.85  # token Jaccard on normalized titles/aliases


# ---------------------------------------------------------------- helpers ---
def ontology_terms() -> tuple[set[str], set[str]]:
    text = ONTOLOGY.read_text()
    classes = set(re.findall(r"^kto:(\w+)\s+a owl:Class", text, re.M))
    props = set(re.findall(r"^kto:(\w+)\s+a owl:ObjectProperty", text, re.M))
    return classes, props


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    stop = {"the", "a", "an", "of", "and", "in", "on", "to", "for"}
    return " ".join(w for w in s.split() if w not in stop)


def tokens(s: str) -> set[str]:
    # crude stemming so "defences" ~ "defence"
    return {w[:6] if len(w) > 6 else w.rstrip("s") for w in norm(s).split()}


SPELLING_SIM_THRESHOLD = 0.85  # char ratio counts only for near-identical spellings


def label_sim(a: str, b: str) -> float:
    # Word overlap is the main signal. Character-level similarity only counts when it is very
    # high (typos, punctuation or plural variants); below that it matches unrelated short titles,
    # e.g. two short unrelated titles scoring ~0.5 with no words in common.
    from difflib import SequenceMatcher
    word = jaccard(tokens(a), tokens(b))
    char = SequenceMatcher(None, norm(a), norm(b)).ratio()
    return max(word, char if char >= SPELLING_SIM_THRESHOLD else 0.0)


def shingles(text: str, k: int = 5) -> set[int]:
    words = norm(re.sub(r"\[\^s\d+\]", " ", text)).split()
    return {hash(" ".join(words[i:i + k])) for i in range(max(0, len(words) - k + 1))}


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a and b else 0.0


def iri(node_id: str) -> str:
    return BASE + node_id.split(":", 1)[1]


def load_articles() -> tuple[list[dict], list[str]]:
    arts, errors = [], []
    for path in sorted(ARTICLES.rglob("*.md")):
        rel = path.relative_to(ROOT)
        raw = path.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        if not m:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            errors.append(f"{rel}: bad YAML: {e}")
            continue
        fm["_path"], fm["_body"] = str(rel), m.group(2)
        arts.append(fm)
    return arts, errors


# ------------------------------------------------------------- chess checks ---
def play_moves(moves: str) -> chess.Board:
    """Play a SAN sequence like '1.e4 e5 2.Nf3 Nc6' from the start; raise ValueError if illegal."""
    board = chess.Board()
    text = re.sub(r"\{.*?\}|\(.*?\)", " ", str(moves))
    for tok in text.split():
        tok = re.sub(r"^\d+\.(\.\.)?", "", tok)
        if not tok or tok in {"1-0", "0-1", "1/2-1/2", "*"} or re.fullmatch(r"\$\d+", tok):
            continue
        tok = tok.rstrip("!?")
        try:
            board.push_san(tok)
        except ValueError:
            raise ValueError(f"illegal or ambiguous move '{tok}' after {board.ply()} ply (FEN {board.fen()})")
    if board.ply() == 0:
        raise ValueError("no moves found")
    return board


def check_chess(a: dict, p: str) -> list[str]:
    errs = []
    if a.get("moves"):
        try:
            play_moves(a["moves"])
        except ValueError as ex:
            errs.append(f"{p}: moves: {ex}")
    elif a.get("type") in NEEDS_MOVES:
        errs.append(f"{p}: a {a['type']} must give its defining `moves` in SAN")
    if a.get("fen"):
        try:
            b = chess.Board(str(a["fen"]))
            if not b.is_valid():
                errs.append(f"{p}: fen is not a legal position ({b.status()!r})")
        except ValueError as ex:
            errs.append(f"{p}: bad fen: {ex}")
    if a.get("eco") and not ECO_RE.match(str(a["eco"])):
        errs.append(f"{p}: eco '{a['eco']}' must look like C60 or B90-B99")
    for i, block in enumerate(re.findall(r"```pgn\n(.*?)```", a["_body"], re.S), 1):
        game = chess.pgn.read_game(io.StringIO(block))
        if game is None:
            errs.append(f"{p}: pgn block {i} could not be parsed")
        elif game.errors:
            errs.append(f"{p}: pgn block {i}: {game.errors[0]}")
    return errs


def verified_date(a: dict) -> date | None:
    v = a.get("verified")
    if isinstance(v, date):
        return v
    try:
        return date.fromisoformat(str(v))
    except ValueError:
        return None


# ------------------------------------------------------------- validation ---
def validate(arts: list[dict]) -> list[str]:
    classes, props = ontology_terms()
    errs: list[str] = []
    ids: dict[str, str] = {}
    names: list[tuple[str, str, set]] = []

    for a in arts:
        p = a["_path"]
        for f in REQUIRED:
            if not a.get(f):
                errs.append(f"{p}: missing required field '{f}'")
        aid = a.get("id", "")
        if aid and not ID_RE.match(aid):
            errs.append(f"{p}: id '{aid}' must look like kt:lowercase-slug")
        if aid:
            if aid in ids:
                errs.append(f"{p}: duplicate id {aid} (also {ids[aid]})")
            ids[aid] = p
            slug = aid.split(":", 1)[1]
            if Path(p).stem != slug:
                errs.append(f"{p}: filename must be {slug}.md")
            dom = a.get("domain", "")
            if Path(p).parent.name != dom:
                errs.append(f"{p}: must live in articles/{dom}/")
        if a.get("type") and a["type"] not in classes:
            errs.append(f"{p}: type '{a['type']}' not in ontology classes {sorted(classes)}")

        for key in ("broader", "related"):
            for ref in a.get(key) or []:
                if not ID_RE.match(str(ref)):
                    errs.append(f"{p}: {key} ref '{ref}' is not a kt: id")
        for r in a.get("relations") or []:
            if not isinstance(r, dict) or set(r) != {"predicate", "object"}:
                errs.append(f"{p}: each relation needs exactly predicate + object")
                continue
            if r["predicate"] not in props:
                errs.append(f"{p}: predicate '{r['predicate']}' not in ontology (add it to ontology.ttl first)")
            if not ID_RE.match(str(r["object"])):
                errs.append(f"{p}: relation object '{r['object']}' is not a kt: id")

        if a.get("verified") and not verified_date(a):
            errs.append(f"{p}: verified '{a['verified']}' must be a YYYY-MM-DD date")
        if "volatile" in a and not isinstance(a["volatile"], bool):
            errs.append(f"{p}: volatile must be true or false")
        if a.get("type") == "Player" and "volatile" not in a:
            errs.append(f"{p}: a Player must set volatile (true while they are active or hold titles that can change)")
        if a.get("status") and a["status"] not in STATUSES:
            errs.append(f"{p}: status '{a['status']}' not in {sorted(STATUSES)}")
        if a.get("status") == "superseded" and not any(
                r.get("predicate") == "replacedBy" for r in (a.get("relations") or []) if isinstance(r, dict)):
            errs.append(f"{p}: a superseded node must declare a replacedBy relation")
        errs += check_chess(a, p)

        # --- citations
        srcs = a.get("sources") or []
        sids = set()
        strong = 0
        urls = set()
        for s in srcs:
            if not isinstance(s, dict):
                errs.append(f"{p}: malformed source entry")
                continue
            for f in ("id", "title", "publisher", "url", "type", "accessed"):
                if not s.get(f):
                    errs.append(f"{p}: source {s.get('id', '?')} missing '{f}'")
            if s.get("id"):
                sids.add(s["id"])
            if s.get("url") and not str(s["url"]).startswith("https://"):
                errs.append(f"{p}: source {s.get('id')} url must be https")
            if s.get("url") in urls:
                errs.append(f"{p}: duplicate source url {s.get('url')}")
            urls.add(s.get("url"))
            if s.get("type") not in SOURCE_TYPES:
                errs.append(f"{p}: source {s.get('id')} type '{s.get('type')}' not in {sorted(SOURCE_TYPES)}")
            elif s["type"] in STRONG_SOURCE_TYPES:
                strong += 1
        if len(srcs) < 3:
            errs.append(f"{p}: needs at least 3 sources (has {len(srcs)})")
        stypes = {x.get("type") for x in srcs if isinstance(x, dict)}
        if a.get("type") in NEEDS_GOVERNING and not stypes & GOVERNING_SOURCE_TYPES:
            errs.append(f"{p}: a {a['type']} must cite a governing-body source (e.g. the FIDE Handbook)")
        if a.get("type") in NEEDS_SCHOLARLY and not stypes & {"peer-reviewed", "academic"}:
            errs.append(f"{p}: a {a['type']} must cite a peer-reviewed or academic source")
        if strong < 2:
            errs.append(f"{p}: needs at least 2 sources of a strong type {sorted(STRONG_SOURCE_TYPES)}")
        body = a["_body"]
        cited = set(re.findall(r"\[\^(s\d+)\](?!:)", body))
        defined = set(re.findall(r"^\[\^(s\d+)\]:", body, re.M))
        for sid in sids - cited:
            errs.append(f"{p}: source {sid} is never cited in the body")
        for sid in cited - sids:
            errs.append(f"{p}: body cites [^{sid}] but it is not in frontmatter sources")
        for sid in sids - defined:
            errs.append(f"{p}: missing footnote definition [^{sid}]: in the Sources section")
        # every substantive paragraph must carry a citation
        prose = re.sub(r"```.*?```", " ", body.split("\n## Sources", 1)[0], flags=re.S)
        for para in re.split(r"\n\s*\n", prose):
            t = para.strip()
            if not t or t.startswith("#") or t.startswith(">") or len(t) < 120:
                continue
            if "[^s" not in t:
                errs.append(f"{p}: uncited paragraph: '{t[:70]}...'")
        if len(re.findall(r"\w+", prose)) < 350:
            errs.append(f"{p}: body is under 350 words")

        names.append((p, a.get("title", ""), {norm(x) for x in [a.get("title", "")] + list(a.get("aliases") or [])}))

    # --- uniqueness: titles / aliases
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            pi, ti, ni = names[i]
            pj, tj, nj = names[j]
            if ni & nj:
                errs.append(f"{pi}: title/alias collides with {pj}: {sorted(ni & nj)}")
            elif jaccard(tokens(ti), tokens(tj)) >= TITLE_DUP_THRESHOLD:
                errs.append(f"{pi}: title too similar to {pj} ('{ti}' vs '{tj}')")
    # --- uniqueness: content
    sh = [(a["_path"], shingles(a["_body"])) for a in arts]
    for i in range(len(sh)):
        for j in range(i + 1, len(sh)):
            s = jaccard(sh[i][1], sh[j][1])
            if s >= NEAR_DUP_THRESHOLD:
                errs.append(f"{sh[i][0]}: near-duplicate of {sh[j][0]} (similarity {s:.2f})")
    return errs


# ------------------------------------------------------------------ build ---
def edges(a: dict):
    for b in a.get("broader") or []:
        yield SKOS + "broader", b
    for r in a.get("related") or []:
        yield SKOS + "related", r
    for r in a.get("relations") or []:
        yield KTO + r["predicate"], r["object"]


def lit(s: str) -> str:
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def build(arts: list[dict]) -> None:
    GRAPH.mkdir(exist_ok=True)
    known = {a["id"] for a in arts}
    triples, nodes, index = [], [], []
    inbound: Counter = Counter()
    frontier: dict[str, list[str]] = defaultdict(list)

    for a in arts:
        s = f"<{iri(a['id'])}>"
        triples += [
            f"{s} <{RDF_TYPE}> <{KTO}{a['type']}> .",
            f"{s} <{RDFS_LABEL}> {lit(a['title'])} .",
            f"{s} <{SKOS}prefLabel> {lit(a['title'])} .",
            f"{s} <{SKOS}definition> {lit(a['summary'])} .",
            f"{s} <{DCT}created> {lit(a['created'])} .",
            f"{s} <{KTO}verified> {lit(a['verified'])} .",
            f"{s} <{KTO}status> {lit(a['status'])} .",
            f"{s} <{KTO}domain> {lit(a['domain'])} .",
        ]
        for al in a.get("aliases") or []:
            triples.append(f"{s} <{SKOS}altLabel> {lit(al)} .")
        node = {
            "@id": a["id"], "@type": f"kto:{a['type']}", "skos:prefLabel": a["title"],
            "skos:definition": a["summary"], "kto:domain": a["domain"], "dcterms:created": str(a["created"]),
            "kto:verified": str(a["verified"]), "kto:status": a["status"], "kto:volatile": bool(a.get("volatile")),
            "prov:wasDerivedFrom": [], "kto:file": a["_path"],
        }
        if a.get("aliases"):
            node["skos:altLabel"] = a["aliases"]
        for k in ("eco", "moves", "fen"):
            if a.get(k):
                node[f"kto:{k}"] = str(a[k])
                triples.append(f"{s} <{KTO}{k}> {lit(a[k])} .")
        for pred, obj in edges(a):
            triples.append(f"{s} <{pred}> <{iri(obj)}> .")
            key = pred.replace(SKOS, "skos:").replace(KTO, "kto:")
            node.setdefault(key, []).append({"@id": obj})
            inbound[obj] += 1
            if obj not in known:
                frontier[obj].append(a["id"])
        for src in a["sources"]:
            sid = f"<{BASE}source/{a['id'].split(':', 1)[1]}/{src['id']}>"
            triples += [
                f"{s} <{PROV}wasDerivedFrom> {sid} .",
                f"{sid} <{RDF_TYPE}> <{KTO}Source> .",
                f"{sid} <{DCT}title> {lit(src['title'])} .",
                f"{sid} <{DCT}publisher> {lit(src['publisher'])} .",
                f"{sid} <https://schema.org/url> {lit(src['url'])} .",
                f"{sid} <{KTO}sourceType> {lit(src['type'])} .",
            ]
            node["prov:wasDerivedFrom"].append({"dcterms:title": src["title"], "dcterms:publisher": src["publisher"],
                                                 "schema:url": src["url"], "kto:sourceType": src["type"]})
        nodes.append(node)
        index.append({"id": a["id"], "title": a["title"], "aliases": a.get("aliases") or [], "type": a["type"],
                      "domain": a["domain"], "file": a["_path"], "created": str(a["created"]),
                      "verified": str(a["verified"]), "volatile": bool(a.get("volatile")), "status": a["status"],
                      **({"eco": str(a["eco"])} if a.get("eco") else {}), "source_urls": [x["url"] for x in a["sources"]]})

    (GRAPH / "triples.nt").write_text("\n".join(sorted(set(triples))) + "\n")
    ctx = {"kt": BASE, "kto": KTO, "skos": SKOS, "prov": PROV, "dcterms": DCT, "schema": "https://schema.org/",
           "@base": BASE}
    (GRAPH / "graph.jsonld").write_text(json.dumps({"@context": ctx, "@graph": nodes}, indent=2, ensure_ascii=False) + "\n")
    (GRAPH / "index.json").write_text(json.dumps(sorted(index, key=lambda x: x["id"]), indent=2, ensure_ascii=False) + "\n")

    # frontier: referenced-but-unwritten nodes, best candidates for the next article
    fl = sorted(frontier.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    lines = ["# Frontier", "", "Nodes referenced by existing articles but not yet written, ranked by how many "
             "articles point to them. Generated by `scripts/kg.py build`.", ""]
    if fl:
        lines += ["| Node | Referenced by |", "|---|---|"]
        lines += [f"| `{k}` | {', '.join(f'`{x}`' for x in v)} |" for k, v in fl]
    else:
        lines.append("_Empty._")
    (GRAPH / "frontier.md").write_text("\n".join(lines) + "\n")

    # stats + centrality
    by_type = Counter(a["type"] for a in arts)
    by_dom = Counter(a["domain"] for a in arts)
    out = ["# Graph statistics", "", f"- Articles (nodes written): **{len(arts)}**",
           f"- Frontier nodes (referenced, unwritten): **{len(frontier)}**",
           f"- Edges: **{sum(1 for a in arts for _ in edges(a))}**",
           f"- Citations: **{sum(len(a['sources']) for a in arts)}**", ""]
    try:
        import networkx as nx
        g = nx.DiGraph()
        g.add_nodes_from(a["id"] for a in arts)
        for a in arts:
            for _, o in edges(a):
                g.add_edge(a["id"], o)
        if g.number_of_nodes():
            pr = nx.pagerank(g)
            comps = list(nx.weakly_connected_components(g))
            iso = [n for n in known if g.degree(n) == 0]
            out += [f"- Weakly connected components: **{len(comps)}**",
                    f"- Isolated articles (no edges): **{len(iso)}**", "",
                    "## Most central nodes (PageRank)", "", "| Node | PageRank | Written |", "|---|---|---|"]
            out += [f"| `{n}` | {v:.4f} | {'yes' if n in known else 'no'} |"
                    for n, v in sorted(pr.items(), key=lambda kv: -kv[1])[:15]]
            try:
                comms = nx.algorithms.community.louvain_communities(g.to_undirected(), seed=42)
                out += ["", f"## Communities (Louvain): {len(comms)}", ""]
                for i, c in enumerate(sorted(comms, key=len, reverse=True)[:10], 1):
                    out.append(f"{i}. " + ", ".join(f"`{x}`" for x in sorted(c)[:12]) + (" …" if len(c) > 12 else ""))
            except Exception:
                pass
            out.append("")
    except ImportError:
        out += ["_(install networkx for centrality and community metrics)_", ""]
    out += ["## By type", ""] + [f"- {k}: {v}" for k, v in sorted(by_type.items())]
    out += ["", "## By domain", ""] + [f"- {k}: {v}" for k, v in sorted(by_dom.items())]
    vol = [a for a in arts if a.get("volatile")]
    due = [a for a in vol if (verified_date(a) or date.min) < date.today() - timedelta(days=STALE_DAYS)]
    out += ["", "## Freshness", "", f"- Volatile articles (time-sensitive facts): {len(vol)}",
            f"- Due for re-verification (older than {STALE_DAYS} days): {len(due)}"]
    out += ["", "## By status", ""] + [f"- {k}: {v}" for k, v in sorted(Counter(a["status"] for a in arts).items())]
    (GRAPH / "stats.md").write_text("\n".join(out) + "\n")


def is_stale(a: dict, days: int = STALE_DAYS) -> bool:
    d = verified_date(a)
    return bool(a.get("volatile")) and (d is None or d < date.today() - timedelta(days=days))


def similar(query: str, arts: list[dict]) -> None:
    scored = []
    for a in arts:
        labels = [a.get("title", "")] + list(a.get("aliases") or [])
        best = max(label_sim(query, x) for x in labels)
        if norm(query) in {norm(x) for x in labels}:
            best = 1.0
        scored.append((best, a.get("id"), a.get("title"), str(a.get("verified", "")), is_stale(a)))
    hits = [x for x in sorted(scored, reverse=True) if x[0] > 0][:10]
    if not hits:
        print("No similar articles. Topic looks unique.")
    for sc, i, t, v, st in hits:
        print(f"{sc:.2f}  {i}  {t}  [verified {v}]{'  STALE' if st else ''}")


def stale(arts: list[dict], days: int = STALE_DAYS, domain: str | None = None) -> None:
    rows = sorted(((verified_date(a) or date.min), a["id"], a.get("title", ""), a.get("domain", ""))
                  for a in arts if is_stale(a, days) and (not domain or a.get("domain") == domain))
    if not rows:
        print(f"No stale articles (volatile and verified more than {days} days ago).")
        return
    for v, i, t, d in rows:
        print(f"{v}  {i}  {t}  ({d})")
    # Pair the stalest article with one linked to it or in the same domain, so research overlaps.
    by_id = {a["id"]: a for a in arts}
    top = rows[0]
    links = {o for _, o in edges(by_id[top[1]])}
    rest = sorted(rows[1:], key=lambda r: (0 if r[1] in links else 1 if r[3] == top[3] else 2, r[0]))
    batch = [top] + rest[: MAX_REFRESH_BATCH - 1]
    print()
    print(f"Refresh batch for this run ({len(batch)}):")
    for v, i, t, d in batch:
        print(f"  {i}  {t}  ({d})")

def opt(args: list[str], name: str) -> tuple[str | None, list[str]]:
    if name not in args:
        return None, args
    k = args.index(name)
    val = args[k + 1] if k + 1 < len(args) else None
    return val, args[:k] + args[k + 2:]


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "moves":
        try:
            b = play_moves(" ".join(sys.argv[2:]))
        except ValueError as ex:
            print(f"ILLEGAL: {ex}")
            return 1
        print(f"OK: {b.ply()} ply. FEN: {b.fen()}")
        return 0
    arts, errs = load_articles()
    if cmd == "stale":
        ds, args = opt(sys.argv[2:], "--days")
        domain, args = opt(args, "--domain")
        stale(arts, int(ds) if ds else STALE_DAYS, domain)
        return 0
    if cmd == "similar":
        similar(" ".join(sys.argv[2:]), arts)
        return 0
    errs += validate(arts) if not errs else []
    if errs:
        print(f"{len(errs)} problem(s):")
        for e in errs:
            print("  -", e)
        return 1
    print(f"OK: {len(arts)} article(s) valid.")
    if cmd == "build":
        build(arts)
        print("Graph regenerated in graph/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
