# Chess Knowledge Graph — run playbook

This repo is a citation-backed knowledge graph of chess: openings, strategy, tactics, endgames, rules, history, players, events, computer chess, training and compositions. An hourly scheduled run makes **one change** per run: it either adds one new, unique article or re-verifies a small batch (1–2) of time-sensitive articles (see 2a). Follow these steps in order. Read `SCHEMA.md` before writing.

## 1. Sync and orient
```bash
pip install -r requirements.txt --break-system-packages -q
git pull --rebase origin main
python3 scripts/kg.py build      # must print OK; fix the repo first if it doesn't
```
Read `graph/stats.md`, `graph/frontier.md` and `topics/seeds.yaml`. `graph/index.json` lists every existing node (ids, titles, aliases, ECO codes, verified dates, source URLs).

## 2. Pick the topic (graph-driven)
Use the current UTC hour:
- **Even hour → depth.** Take the highest-ranked node in `graph/frontier.md` (referenced by the most articles but not yet written) that fits a domain in `topics/seeds.yaml`. This turns dangling edges into real nodes.
- **Odd hour → refresh first, then breadth.** Run `python3 scripts/kg.py stale`. If it lists a **Refresh batch for this run**, re-verify exactly those articles per step 2a; that is this run's change. Only if nothing is stale, do breadth: take the domain in `topics/seeds.yaml` with the fewest articles (ties: alphabetical, skipping the domain of the most recent commit) and pick an unwritten seed topic, or another important topic in that domain.
- If no frontier node fits (or the graph is empty), do an odd-hour run.

For a new article, prove it is unique:
```bash
python3 scripts/kg.py similar "<candidate title>"
```
- If an existing title or alias names the same thing (or a ≥ 0.5 match is the same subject after review): if that match is flagged `STALE`, **re-verify it** (step 2a) instead; otherwise pick a different topic.
- If any score is ≥ 0.5, **review before skipping**: read the summary and aliases of each matching node. Proceed only if it is clearly a different subject, and record why in the commit message body, one line per match, e.g. `similar: 0.55 vs kt:queens-gambit — opening, not the Queen's Gambit Declined variation`. If unsure, pick a different topic.

Never write a second article on a subject that already has a node: not a rename, a transliteration (Petrov/Petroff, Tchigorin/Chigorin), British vs American spelling (Defence/Defense), a sub-angle that restates it, or a synonym (Spanish Game = Ruy Lopez). Record such names as `aliases`. A variation may have its own node only when it is a well-established named line with its own theory; link it with `broader` to its parent opening.

## 2a. Re-verify a stale article (instead of adding one)
Stale means `volatile: true` and `verified` more than 180 days ago (ratings, titles, active players, current rules, engines, organizations change).
- Keep the file path, `id`, `created` date and existing edges. Never rename or delete the node.
- Re-open every cited source (search for it first, per step 3) and check for changes: new titles or results, rating milestones, rule changes in the current FIDE Laws of Chess, new engine releases, retirements.
- Rewrite only what changed; replace or add sources as needed; update every re-opened source's `accessed` date; set `verified` to today. If a rule or regulation was replaced, set `status: superseded` with a `replacedBy` edge. If a player retired, consider `volatile: false`.
- If nothing changed, still bump `verified` and the `accessed` dates of the sources you re-opened.
- If you cannot open enough sources to re-verify an article, leave it out; if none can be done, pick a new topic instead.

## 3. Research
- Run several web searches; read the actual pages (WebFetch), don't rely on snippets or memory.
- Collect 3–6 credible sources, at least 2 of a strong type (see `SCHEMA.md`). Rules and titles cite the FIDE Handbook (handbook.fide.com) or a national federation; cognition and expertise claims cite peer-reviewed research; engines cite the project's own site or paper; history cites archives, reference works or books. **Never cite Wikipedia**, content farms, AI-generated pages or uncredited listicles.
- Every URL you cite must be one you actually opened this run. Never invent or guess a URL, a FIDE ID, a game date or a result.
- Moves: get opening lines and game scores from a source you opened (a primary record, database or book page), then check them with `python3 scripts/kg.py moves "<SAN>"` before writing. Never write a move sequence from memory without checking it. Name evaluations as the source gives them; don't invent engine numbers.
- Ratings, ages, title counts and "current champion" claims are time-sensitive: give the date ("as of November 2026") and set `volatile: true`.
- Paraphrase. No quotation longer than 15 words; at most one quote per source. Never reproduce whole annotated games or book passages from a source; write your own explanation of the ideas.

## 4. Write the node
- Path `articles/<domain>/<slug>.md`, id `kt:<slug>`. Pick the most specific `type` from the ontology. Use British "Defence" in titles (as FIDE does) and put "Defense" in `aliases`.
- 350–900 words, aimed at a serious club player: what it is, the key ideas or how it works, typical plans, mistakes or pitfalls, a short concrete example (a `moves` line, a `fen` key position or a `pgn` block), and a **Connections** section explaining the edges.
- Openings and variations: give `moves` (the defining line, not deep theory) and `eco` when a source gives it. Endgames, motifs and patterns: give a `fen` for a clear example position. Famous games: a `pgn` block with the full game, from a source you opened.
- Players: only their public chess career (results, titles, style, contributions, notable games). No private life, health or controversies beyond what reputable sources report as chess-relevant (e.g. a sanctioned forfeit). Set `volatile: true` while they are active.
- Every factual paragraph carries footnote citations `[^sN]`; list all sources in `## Sources`.
- Edges: 1–3 `broader`, 2–6 `related` or typed `relations`. Use typed predicates where they fit (`leadsTo`, `transposesTo`, `counters`, `alternativeTo`, `exemplifiedBy` a game, `championedBy` a player, `namedAfter`, `developedBy`, `governedBy` a rule, `holdsTitle`, `playedIn`, `usesTechnique`, …). **Link to existing node ids wherever they fit** (check `graph/index.json`); new target ids are fine and join the frontier.
- If a needed predicate or class is missing, add it to `ontology/ontology.ttl` (with a label and, if applicable, inverse) in the same commit, and a label pair in `PRED` in `scripts/site.py`. Keep the ontology small; reuse before adding.
- Back-links: if the new node is a natural child or relative of an existing article, you may add its id to that article's `related` list. Don't otherwise rewrite existing articles, except through a refresh (step 2a).

## 5. Validate, build, commit, push
```bash
python3 scripts/kg.py build    # fix every reported problem, then re-run until OK
git add -A
git commit -m "Add <Title> (<domain>)"   # refresh: "Re-verify <Title>[, <Title>]"
git pull --rebase origin main && git push origin main
```
In a refresh commit body, list what changed per article, one line each (or `<id>: no content changes; re-verified`). If the push is rejected, pull --rebase, rebuild, and push again (once). Commit generated `graph/` files with the article. The GitHub Pages site rebuilds itself on push.

## Don'ts
- Don't add more than one new article per run, combine an addition with refreshes, delete articles, hand-edit `graph/`, or rewrite history.
- Don't commit if validation fails; leave the repo clean.
- Don't cite a source you didn't open, or state a move, result, rating or date you didn't verify this run.
