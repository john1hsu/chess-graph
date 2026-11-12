#!/usr/bin/env python3
"""Render the knowledge graph as a static website (GitHub Pages).

Usage:
  python3 scripts/site.py            # writes the site to _site/
  python3 scripts/site.py out_dir    # writes it somewhere else

Reads the same articles as scripts/kg.py and never modifies them. The output is
plain HTML/CSS/JS: a home page with search, one page per article (typed connections, back-links, sources),
the frontier and an about page with data downloads. Styles and the search script live in scripts/site_assets/.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kg  # noqa: E402
import chess  # noqa: E402
import chess.svg  # noqa: E402

try:
    import markdown
except ImportError:  # pragma: no cover
    sys.exit("markdown missing: pip install markdown --break-system-packages")

REPO = "john1hsu/chess-graph"
REPO_URL = f"https://github.com/{REPO}"
SITE_TITLE = "Chess Knowledge Graph"
HERE = Path(__file__).resolve().parent
ASSETS = HERE / "site_assets"
ASSET_V = "0"  # set in main() from the asset contents

FONTS_URL = ("https://fonts.googleapis.com/css2?family=Manrope:wght@400..800"
             "&family=Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400..700&display=swap")
THEME = {
    "font_body": "'Newsreader', Georgia, serif",
    "font_display": "'Manrope', system-ui, sans-serif",
    "font_ui": "'Manrope', system-ui, sans-serif",
    "hue_start": 150,
    "light": {
        "paper": "#F3F1EC", "panel": "#FCFBF8", "ink": "#1B1A17", "ink-soft": "#3A3832", "muted": "#68645A",
        "rule": "#DDD8CC", "rule-strong": "#B7AF9E", "accent": "#2F6B4F", "accent-wash": "#DCEBE2",
        "warn": "#A33A2A", "warn-wash": "#F6DFDA", "good": "#1D6B47", "good-wash": "#D8EEE2", "caution": "#8A5A00",
    },
    "dark": {
        "paper": "#141412", "panel": "#1D1C19", "ink": "#ECEAE4", "ink-soft": "#CFCBC1", "muted": "#9A958A",
        "rule": "#2E2C27", "rule-strong": "#4A473F", "accent": "#86C9A4", "accent-wash": "#1F3529",
        "warn": "#F0998B", "warn-wash": "#3D2420", "good": "#7FCFA4", "good-wash": "#1C3529", "caution": "#F0C46B",
    },
}

# (outgoing label, incoming label)
PRED = {
    "broader": ("Part of", "Includes"),
    "related": ("Related", "Related"),
    "partOf": ("Part of", "Includes"),
    "hasPart": ("Includes", "Part of"),
    "dependsOn": ("Depends on", "Needed by"),
    "enables": ("Enables", "Enabled by"),
    "leadsTo": ("Typically leads to", "Often arises from"),
    "transposesTo": ("Can transpose to", "Can transpose to"),
    "counters": ("Counters", "Countered by"),
    "counteredBy": ("Countered by", "Counters"),
    "alternativeTo": ("Alternative to", "Alternative to"),
    "contrastsWith": ("Often confused with", "Often confused with"),
    "replacedBy": ("Superseded by", "Supersedes"),
    "replaces": ("Supersedes", "Superseded by"),
    "exemplifiedBy": ("Shown in game", "Shows"),
    "exemplifies": ("Shows", "Shown in game"),
    "governedBy": ("Governed by", "Governs"),
    "sanctionedBy": ("Awarded by", "Awards"),
    "championedBy": ("Championed by", "Championed"),
    "developedBy": ("Developed by", "Developed"),
    "namedAfter": ("Named after", "Gave its name to"),
    "influencedBy": ("Influenced by", "Influenced"),
    "memberOf": ("Member of", "Members"),
    "holdsTitle": ("Holds title", "Held by"),
    "playedBy": ("Played by", "Played"),
    "playedIn": ("Played in", "Games"),
    "wonBy": ("Won by", "Won"),
    "authoredBy": ("Written by", "Wrote"),
    "organizedBy": ("Organised by", "Organised"),
    "usesTechnique": ("Uses", "Used by"),
    "instanceOf": ("Instance of", "Has instance"),
}
PRED_ORDER = ["Superseded by", "Supersedes", "Part of", "Includes", "Typically leads to", "Often arises from"]
STATUS = {"current": "Current", "historical": "Historical", "superseded": "Superseded", "contested": "Contested",
          "refuted": "Refuted"}
SOURCE_KIND = {"governing-body": "Governing body", "official-project": "Official project",
               "primary-record": "Primary record", "peer-reviewed": "Peer reviewed"}

e = lambda s: html.escape(str(s), quote=True)  # noqa: E731


def slug(node_id: str) -> str:
    return node_id.split(":", 1)[1]


def humanize(s: str) -> str:
    return s.replace("-", " ").replace("_", " ").strip().capitalize()


def domain_label(d: str) -> str:
    small = {"and", "of", "in", "to"}
    out = []
    for i, w in enumerate(d.split("-")):
        if w in {"ai"}:
            out.append(w.upper())
        elif w in small and i:
            out.append(w)
        else:
            out.append(w.capitalize() if i == 0 else w)
    return " ".join(out)


def camel_words(s: str) -> str:
    keep = {"API"}  # noqa: F841
    if s in keep:
        return s
    w = re.sub(r"(?<=[a-z])([A-Z])", r" \1", s)
    w = w[:1] + w[1:].lower()
    return w.replace("Api", "API")


def out_edges(a: dict) -> list[tuple[str, str]]:
    res = [("broader", b) for b in a.get("broader") or []]
    res += [("related", r) for r in a.get("related") or []]
    res += [(r["predicate"], r["object"]) for r in a.get("relations") or []]
    return res


# ---------------------------------------------------------------- page shell
NAV = [("index.html", "Browse", "home"),
       ("frontier.html", "Frontier", "frontier"), ("about.html", "About", "about")]


def page(title: str, body: str, root: str, *, active: str = "", desc: str = "", extra_head: str = "",
         page_class: str = "") -> str:
    links = "".join(
        f'<a href="{root}{h}"{" aria-current=page" if k == active else ""}>{t}</a>' for h, t, k in NAV
    ) + f'<a href="{REPO_URL}">Source on GitHub</a>'
    full = SITE_TITLE if title == SITE_TITLE else f"{title} | {SITE_TITLE}"
    desc = desc or "A cited, cross-linked map of chess: openings, strategy, tactics, endgames, history and computer chess."
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{e(FONTS_URL)}">
<link rel="stylesheet" href="{root}style.css?v={ASSET_V}">
<link rel="icon" href="{root}icon.svg" type="image/svg+xml">
{extra_head}
</head>
<body class="{page_class}">
<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
  <a class="wordmark" href="{root}index.html">{SITE_TITLE}</a>
  <nav aria-label="Site">{links}</nav>
</header>
<main id="main">
{body}
</main>
<footer class="colophon">
  <p>Updated every hour from <a href="{REPO_URL}">{REPO}</a>. Every article links to its sources, and every move sequence is checked for legality; confirm ratings and current rules at the source before you rely on them.</p>
</footer>
</body>
</html>
"""


def theme_css(domains: list[str]) -> str:
    t = THEME

    def tokens(mode):
        return "".join(f"--{k}:{v};" for k, v in t[mode].items())
    css = (f":root{{{tokens('light')}--font-body:{t['font_body']};--font-ui:{t['font_ui']};"
           f"--font-display:{t['font_display']};}}\n"
           f"@media (prefers-color-scheme: dark){{:root:not([data-theme=light]){{{tokens('dark')}}}}}\n"
           f":root[data-theme=dark]{{{tokens('dark')}}}\n")
    n = max(len(domains), 1)
    for i, d in enumerate(domains):
        h = round((t["hue_start"] + i * 360 / n) % 360)
        css += f'[data-domain="{d}"]{{--dc:hsl({h} 48% 42%)}}\n'
        css += (f'@media (prefers-color-scheme: dark){{:root:not([data-theme=light]) [data-domain="{d}"]'
                f'{{--dc:hsl({h} 55% 66%)}}}}\n:root[data-theme=dark] [data-domain="{d}"]{{--dc:hsl({h} 55% 66%)}}\n')
    return css


# ---------------------------------------------------------------- rendering helpers
MD = markdown.Markdown(extensions=["tables", "sane_lists", "smarty"])


def render_body(a: dict, written: dict) -> str:
    body = a["_body"].lstrip()
    body = re.sub(r"^# .*\n", "", body, count=1)                                # title rendered separately
    body = re.split(r"^## Sources\s*$", body, maxsplit=1, flags=re.M)[0]        # sources rendered from frontmatter
    body = re.sub(r"^\[\^s\d+\]:.*$", "", body, flags=re.M)

    def fn(m):
        sid = m.group(1)
        num = re.sub(r"\D", "", sid) or sid
        return f'<sup class="fn"><a href="#src-{sid}" aria-label="Source {num}">{num}</a></sup>'
    body = re.sub(r"\[\^([A-Za-z0-9_-]+)\]", fn, body)

    idpat = r"kt:[a-z0-9-]+"

    def titled(m):
        title, nid = m.group(1), m.group(2)
        if nid in written:
            return f'<a class="idref" href="{slug(nid)}.html"><strong>{title}</strong></a>'
        return f"**{title}**"
    body = re.sub(r"\*\*([^*]+)\*\*\s?\(`(" + idpat + r")`\)", titled, body)
    body = re.sub(r"\s?\(`" + idpat + r"`(?:,\s*`" + idpat + r"`)*\)", "", body)

    def bare(m):
        nid = m.group(1)
        if nid in written:
            return f'<a class="idref" href="{slug(nid)}.html">{e(written[nid]["title"])}</a>'
        return e(humanize(slug(nid)))
    body = re.sub(r"`(" + idpat + r")`", bare, body)
    MD.reset()
    return MD.convert(body)


def node_link(nid: str, written: dict, root: str) -> str:
    if nid in written:
        return f'<a href="{root}articles/{slug(nid)}.html">{e(written[nid]["title"])}</a>'
    return f'<span class="unwritten" title="Not written yet">{e(humanize(slug(nid)))}</span>'


def connections(a: dict, written: dict, incoming: dict) -> str:
    groups: dict[str, list[str]] = defaultdict(list)
    seen = set()
    for p, t in out_edges(a):
        label = PRED.get(p, (camel_words(p), camel_words(p)))[0]
        if (label, t) not in seen:
            seen.add((label, t))
            groups[label].append(t)
    for p, s in incoming.get(a["id"], []):
        label = PRED.get(p, (camel_words(p), camel_words(p)))[1]
        if (label, s) not in seen:
            seen.add((label, s))
            groups[label].append(s)
    if not groups:
        return ""

    def order(label):
        if label in PRED_ORDER:
            return (0, PRED_ORDER.index(label))
        return (2, "") if label == "Related" else (1, label)
    out = []
    for label in sorted(groups, key=order):
        ts = sorted(groups[label], key=lambda t: (t not in written, (written.get(t) or {}).get("title", t).lower()))
        out.append(f"<div><h3>{e(label)}</h3><ul>" + "".join(f"<li>{node_link(t, written, '../')}</li>" for t in ts)
                   + "</ul></div>")
    return f'<aside class="connections" aria-labelledby="conn-h"><h2 id="conn-h">Connections</h2>{"".join(out)}</aside>'


def sources(a: dict) -> str:
    srcs = a.get("sources") or []
    if not srcs:
        return ""
    li = []
    for s in srcs:
        kind = SOURCE_KIND.get(s.get("type", ""), humanize(s.get("type", "")))
        opened = f", opened {e(s.get('accessed'))}" if s.get("accessed") else ""
        li.append(f'<li id="src-{e(s.get("id", ""))}"><a href="{e(s.get("url", ""))}" rel="noopener">{e(s.get("title", ""))}</a>'
                  f'<span class="src-pub">{e(s.get("publisher", ""))}</span>'
                  f'<span class="src-meta">{e(kind)}{opened}</span></li>')
    return f'<section class="block sources" aria-labelledby="src-h"><h2 id="src-h">Sources</h2><ol>{"".join(li)}</ol></section>'


BOARD_COLORS = {"square light": "#EEE6D4", "square dark": "#8FA88F", "margin": "#00000000",
                "coord": "#68645A", "square light lastmove": "#E5D98A", "square dark lastmove": "#B7B86A"}


def board(a: dict) -> str:
    """Diagram of the article's key position: `fen` if given, else the position after `moves`."""
    try:
        if a.get("fen"):
            b, last, cap = chess.Board(str(a["fen"])), None, "Key position"
        elif a.get("moves"):
            b = kg.play_moves(a["moves"])
            last, cap = b.peek(), "Position after " + e(re.sub(r"\s+", " ", str(a["moves"]).strip()))
        else:
            return ""
    except ValueError:
        return ""
    svg = chess.svg.board(b, lastmove=last, size=360, coordinates=True, colors=BOARD_COLORS)
    turn = "White" if b.turn else "Black"
    return (f'<figure class="board" role="img" aria-label="Chess diagram, {turn} to move">{svg}'
            f'<figcaption>{cap}. {turn} to move.</figcaption></figure>')


def data_script(d: dict) -> str:
    return '<script id="kg-data" type="application/json">' + json.dumps(d, ensure_ascii=False).replace("</", "<\\/") + "</script>"


# ---------------------------------------------------------------- main
def main() -> int:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else kg.ROOT / "_site"
    arts, errs = kg.load_articles()
    if errs:
        print("\n".join(errs))
        return 1
    try:
        import yaml
        seeds = yaml.safe_load((kg.ROOT / "topics" / "seeds.yaml").read_text())["domains"]
    except Exception:
        seeds = {}

    written = {a["id"]: a for a in arts}
    by_domain: dict[str, list] = defaultdict(list)
    for a in arts:
        by_domain[a["domain"]].append(a)
    for items in by_domain.values():
        items.sort(key=lambda a: a["title"].lower())
    incoming: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for a in arts:
        for p, t in out_edges(a):
            incoming[t].append((p, a["id"]))
    frontier = sorted(((t, srcs) for t, srcs in incoming.items() if t not in written),
                      key=lambda x: (-len({s for _, s in x[1]}), x[0]))
    domains = [d for d in sorted(set(seeds) | set(by_domain), key=lambda d: (-len(by_domain.get(d, [])), d))]
    live_domains = [d for d in domains if by_domain.get(d)]

    if out.exists():
        shutil.rmtree(out)
    (out / "articles").mkdir(parents=True)
    (out / "data").mkdir()
    css = theme_css(domains) + (ASSETS / "style.css").read_text(encoding="utf-8")
    # Version asset URLs by content so browsers never pair new pages with a cached old stylesheet.
    global ASSET_V
    ASSET_V = hashlib.sha256((css + (ASSETS / "home.js").read_text(encoding="utf-8")).encode()).hexdigest()[:10]
    (out / "style.css").write_text(css, encoding="utf-8")
    shutil.copy(ASSETS / "home.js", out / "home.js")
    shutil.copy(ASSETS / "icon.svg", out / "icon.svg")
    (out / ".nojekyll").write_text("")
    for f in ["graph.jsonld", "triples.nt", "index.json"]:
        if (kg.GRAPH / f).exists():
            shutil.copy(kg.GRAPH / f, out / "data" / f)
    shutil.copy(kg.ONTOLOGY, out / "data" / "ontology.ttl")
    home_script = '<script src="home.js?v=' + ASSET_V + '"></script>'

    n_edges = sum(len(out_edges(a)) for a in arts)
    n_src = len({s["url"] for a in arts for s in a.get("sources") or []})

    # ---- home
    sections = []
    for d in live_domains:
        li = "".join(
            f'<li data-s="{e(slug(a["id"]))}"><a href="articles/{e(slug(a["id"]))}.html">{e(a["title"])}</a>'
            f'<span class="kind">{e(camel_words(a["type"]))}</span></li>' for a in by_domain[d])
        sections.append(
            f'<section class="domain" id="d-{e(d)}" data-domain="{e(d)}">'
            f'<h3><span class="swatch" aria-hidden="true"></span>{e(domain_label(d))}'
            f' <span class="count">{len(by_domain[d])}</span></h3><ul>{li}</ul></section>')
    search_index = {slug(a["id"]): " ".join([a["title"], *(a.get("aliases") or []), a.get("summary", "")])
                    for a in arts}
    latest = sorted(arts, key=lambda a: (str(a.get("created", "")), a["title"]), reverse=True)[:6]
    latest_li = "".join(
        f'<li><a href="articles/{e(slug(a["id"]))}.html">{e(a["title"])}</a><span>{e(a.get("summary", "").strip())}</span></li>'
        for a in latest)
    hd = {"search": [{"s": k, "t": v, "a": "", "m": ""} for k, v in search_index.items()]}
    stat = (f"{len(arts)} articles in {len(live_domains)} areas, connected by {n_edges} links and backed by "
            f"{n_src} cited sources. Every move in it has been checked for legality.")
    home = f"""
<section class="hero">
  <div class="hero-copy">
    <h1>How chess fits together</h1>
    <p class="lede">A cited map of openings, plans, tactics, endgames, players and engines. Each article explains one idea, shows how it connects to the rest of the game, and links to the rulebooks, books and research behind every claim.</p>
    <p class="stat">{e(stat)}</p>
  </div>
</section>

<section class="browse" id="browse" aria-labelledby="browse-h">
  <div class="browse-head">
    <h2 id="browse-h">Browse</h2>
    <label class="search">
      <span class="visually-hidden">Find an article</span>
      <input id="q" type="search" placeholder="Find an article, e.g. Lucena position" autocomplete="off">
    </label>
  </div>
  <p id="nores" class="nores" hidden>No article matches that yet. Try a broader word, or check the <a href="frontier.html">frontier</a> for topics on the way.</p>
  <div class="domains">{"".join(sections)}</div>
</section>

<section class="latest" aria-labelledby="latest-h">
  <h2 id="latest-h">Recently added</h2>
  <ul>{latest_li}</ul>
</section>
{data_script(hd)}
{home_script}"""
    (out / "index.html").write_text(page(SITE_TITLE, home, "", active="home", page_class="p-home"), encoding="utf-8")

    # ---- article pages
    for a in arts:
        aliases = a.get("aliases") or []
        alias_html = f'<p class="aliases">Also called {", ".join(e(x) for x in aliases)}</p>' if aliases else ""
        status = a.get("status", "")
        facts = [("Kind", e(camel_words(a["type"]))),
                 ("Status", f'<span class="status" data-status="{e(status)}">{e(STATUS.get(status, humanize(status)))}</span>'),
                 ("ECO", e(a.get("eco", ""))),
                 ("Verified", e(a.get("verified", ""))),
                 ("Added", e(a.get("created", "")))]
        facts_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts if v)
        facts_html += (f'<div class="source-link"><dt>Markdown</dt><dd><a href="{REPO_URL}/blob/main/{e(a["_path"])}">'
                       f"View on GitHub</a></dd></div>")
        body = f"""
<article class="entry">
  <header class="entry-head">
    <p class="crumb"><a href="../index.html#d-{e(a['domain'])}">{e(domain_label(a['domain']))}</a></p>
    <h1>{e(a['title'])}</h1>
    {alias_html}
    <p class="lede">{e(a.get('summary', '').strip())}</p>
    <dl class="facts">{facts_html}</dl>
  </header>
  {board(a)}
  <div class="entry-grid">
    <div class="prose">
      {render_body(a, written)}
      {sources(a)}
    </div>
    {connections(a, written, incoming)}
  </div>
</article>"""
        (out / "articles" / f"{slug(a['id'])}.html").write_text(
            page(a["title"], body, "../", desc=a.get("summary", "").strip(), page_class="p-entry"), encoding="utf-8")

    # ---- frontier
    rows = "".join(
        f'<tr><td>{e(humanize(slug(t)))}</td><td>{len({s for _, s in srcs})}</td>'
        f'<td>{", ".join(node_link(s, written, "") for s in sorted({s for _, s in srcs}, key=lambda s: written[s]["title"].lower()))}</td></tr>'
        for t, srcs in frontier)
    fbody = (f'<header class="page-head"><h1>Frontier</h1><p class="lede">Topics that existing articles already point to but '
             f'nobody has written yet, most-referenced first. The hourly run works down this list, so these are the '
             f'articles coming next.</p></header>'
             f'<div class="tablewrap"><table class="frontier-table"><thead><tr><th scope="col">Topic</th>'
             f'<th scope="col">Linked from</th><th scope="col">Articles that link to it</th></tr></thead>'
             f'<tbody>{rows}</tbody></table></div>')
    (out / "frontier.html").write_text(page("Frontier", fbody, "", active="frontier", page_class="p-frontier"),
                                       encoding="utf-8")

    # ---- the map was removed; send old /graph.html links to Browse
    (out / "graph.html").write_text('<!doctype html><meta charset="utf-8"><title>Browse</title>'
                                    '<meta http-equiv="refresh" content="0; url=index.html">'
                                    '<link rel="canonical" href="index.html">', encoding="utf-8")

    # ---- about
    readme = (kg.ROOT / "README.md").read_text(encoding="utf-8")
    readme = re.sub(r"^# .*\n", "", readme, count=1)
    about = markdown.markdown(readme, extensions=["tables", "fenced_code"])
    about += ('<h2>Downloads</h2><ul class="downloads"><li><a href="data/graph.jsonld">graph.jsonld</a> (JSON-LD)</li>'
              '<li><a href="data/triples.nt">triples.nt</a> (N-Triples)</li><li><a href="data/index.json">index.json</a></li>'
              '<li><a href="data/ontology.ttl">ontology.ttl</a></li></ul>')
    abody = f'<header class="page-head"><h1>About</h1></header><div class="prose">{about}</div>'
    (out / "about.html").write_text(page("About", abody, "", active="about", page_class="p-about"), encoding="utf-8")

    (out / "404.html").write_text(page(
        "Not found", '<header class="page-head"><h1>That page isn’t here</h1><p class="lede">It may have been renamed. '
        '<a href="index.html">Go to the full article list</a>.</p></header>', "",
        extra_head='<base href="/chess-graph/">'), encoding="utf-8")

    print(f"Site written to {out} ({len(arts)} articles, {len(frontier)} frontier topics).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
