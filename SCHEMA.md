# Article schema

Each article is one **node** in the graph: `articles/<domain>/<slug>.md`, where the filename equals the id's slug and `<domain>` is a key in `topics/seeds.yaml`.

```markdown
---
id: kt:ruy-lopez                       # stable node id: kt: + lowercase-hyphen slug
type: Opening                          # a class from ontology/ontology.ttl
title: Ruy Lopez
aliases: [Spanish Opening, Spanish Game]  # other names; used for duplicate detection
domain: openings                       # a domain key from topics/seeds.yaml
summary: >-                            # 1–2 sentence definition (becomes skos:definition)
  A king's-pawn opening in which White develops the bishop to b5 on move three to pressure the knight defending e5.
eco: C60-C99                           # optional; Openings and Variations only
moves: "1.e4 e5 2.Nf3 Nc6 3.Bb5"       # required for Opening/Variation; SAN, checked for legality
fen: ...                               # optional key position (endgames, motifs, games); checked for legality
status: current                        # current | historical | superseded | contested | refuted
volatile: false                        # true if facts can go out of date (active players, ratings, current rules, engines, organizations)
verified: 2026-11-07                   # date the content was last checked against its sources
broader: [kt:open-games]
related: [kt:italian-game]
relations:                             # typed edges; predicates must exist in the ontology
  - {predicate: leadsTo, object: kt:closed-ruy-lopez-structures}
  - {predicate: namedAfter, object: kt:ruy-lopez-de-segura}
  - {predicate: exemplifiedBy, object: kt:fischer-spassky-1972-game-10}
sources:                               # >= 3 total, >= 2 strong
  - id: s1
    title: "Ruy Lopez"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/...
    type: reference
    accessed: 2026-11-07
created: 2026-11-07
---

# Ruy Lopez

Prose with inline footnote citations after each claim.[^s1]

## Main ideas
...

## Typical plans and pitfalls
...

## Connections
How this node relates to its neighbours, in prose, with citations.[^s3]

## Sources
[^s1]: Encyclopaedia Britannica, "Ruy Lopez". https://www.britannica.com/... (accessed 2026-11-07)
```

Games and longer lines go in fenced `pgn` blocks; `kg.py` parses them and rejects illegal moves:

````markdown
```pgn
[Event "London"]
[White "Adolf Anderssen"]
[Black "Lionel Kieseritzky"]
[Result "1-0"]

1. e4 e5 2. f4 exf4 ...
```
````

## Rules enforced by `scripts/kg.py check`

- Required fields: `id, type, title, domain, summary, sources, created, verified, status`.
- `status` is one of the allowed values; a `superseded` node (an old rule, a replaced regulation) must have a `replacedBy` relation. Use `refuted` for an opening line shown to be unsound, `contested` where strong sources disagree.
- `type` must be a class, and every `relations.predicate` a property, in `ontology/ontology.ttl`.
- Chess legality: `moves` must play legally from the starting position, `fen` must be a legal position, every ```` ```pgn ```` block must parse without errors. `Opening` and `Variation` nodes must have `moves`. `eco` looks like `C60` or `B90-B99`.
- A `Player` must set `volatile`.
- Every edge target is a `kt:` id. Targets with no article yet become **frontier** nodes (`graph/frontier.md`).
- Citations: at least 3 sources; at least 2 of a strong type; `Rule` and `Title` nodes cite a `governing-body` source; `CognitiveConcept` nodes cite a `peer-reviewed` or `academic` source; https only; no duplicate URLs; every source cited in the body and defined in `## Sources`; every substantive paragraph cited.
- Body of at least 350 words (pgn blocks don't count).
- Uniqueness: no duplicate ids, titles or aliases; no near-paraphrase titles; no bodies that overlap another article above the similarity threshold.

## Source types

| type | strong? | examples |
|---|---|---|
| governing-body | yes | FIDE Handbook (Laws of Chess, title and rating regulations), FIDE ratings site, US Chess rulebook, English Chess Federation |
| official-project | yes | an engine's own site or docs (stockfishchess.org, lczero.org, Stockfish GitHub), an event's official site |
| primary-record | yes | official crosstables and broadcasts, FIDE player profiles, the original publication of a game or study |
| archive | yes | World Chess Hall of Fame, Cleveland Public Library's John G. White Collection, other museum and library collections |
| reference | yes | Encyclopaedia Britannica, The Oxford Companion to Chess |
| book | yes | published chess literature from a reputable publisher or titled author (cite the publisher's or a library's page for it) |
| peer-reviewed / academic | yes | papers on expertise and cognition, computer-chess papers (ICGA Journal, arXiv by the authors, Nature/Science), university material |
| publication | no | New In Chess, ChessBase News, Chess.com or Lichess editorial by titled players |
| database | no | chessgames.com, 365chess, Lichess opening explorer (game data only) |
| community | no | Chess Programming Wiki, club pages, forums |
| news | no | reputable general press, for events and announcements only |

Never cite Wikipedia, content farms, AI-generated pages, or uncredited "top 10" listicles.
