---
id: kt:transposition-table
type: Technique
title: Transposition table
aliases: [Hash table (chess engine), TT, Transposition hash table]
domain: computer-chess
summary: >-
  A large hash table in which a chess engine caches the results of positions it has already
  searched (score or bound, search depth and best move), so that a position reached again by a
  different move order, or in a later iteration, need not be searched from scratch.
fen: "rnbqkbnr/ppp2ppp/4p3/3p4/3PP3/8/PPP2PPP/RNBQKBNR w KQkq - 0 3"
status: current
volatile: false
verified: 2026-11-15
broader: [kt:game-tree-search]
related: [kt:alpha-beta-pruning, kt:iterative-deepening, kt:move-ordering, kt:stockfish, kt:endgame-tablebases]
relations:
  - {predicate: dependsOn, object: kt:zobrist-hashing}
  - {predicate: enables, object: kt:iterative-deepening}
sources:
  - id: s1
    title: "A New Hashing Method With Application for Game Playing (Technical Report TR88, 1970)"
    publisher: Albert L. Zobrist, University of Wisconsin–Madison, Computer Sciences Department
    url: https://research.cs.wisc.edu/techreports/viewreport.php?report=88
    type: academic
    accessed: 2026-11-15
  - id: s2
    title: "The Anatomy of Chess Programs (1995)"
    publisher: T. A. Marsland, University of Alberta
    url: https://webdocs.cs.ualberta.ca/~tony/ICCA/anatomy.html
    type: academic
    accessed: 2026-11-15
  - id: s3
    title: "Parallel Game-tree Search (Technical Report TR85-1)"
    publisher: T. A. Marsland and F. Popowich, University of Alberta
    url: https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR85-1.pdf
    type: academic
    accessed: 2026-11-15
  - id: s4
    title: "Learning Search Decisions (PhD thesis, 2003)"
    publisher: Levente Kocsis, Maastricht University
    url: https://cris.maastrichtuniversity.nl/ws/files/847817/guid-fb7fc02b-f018-40c2-9253-e6112141c356-ASSET1.0.pdf
    type: academic
    accessed: 2026-11-15
  - id: s5
    title: "Mac Hack"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org:443/Mac_Hack
    type: community
    accessed: 2026-11-15
created: 2026-11-15
---

# Transposition table

A **transposition table** is the memory of a chess engine's search. Different move orders often lead to the same position, a *transposition*, and the table lets the engine recognise a position it has already examined and reuse the result instead of searching the same subtree again. Marsland describes it as a cache of previously visited positions, each entry tied to a position and holding its value, the best move found there and the depth of the search that produced them.[^s2] Marsland and Popowich define it as a direct-access table of results for subtrees already examined, noting that a fuller version also stores bounds on the subtree's value.[^s3]

## How it works

The board position is reduced to a large integer, a hash key, which selects a slot in the table. The standard way of computing that key was published by Albert Zobrist in a 1970 University of Wisconsin report, which presented a general hash-coding method for board-game programs (checkers, chess and Go) together with an auxiliary scheme for detecting retrieval errors whose error rate can be traded against table space.[^s1] Because a key can be updated incrementally as moves are made and unmade, the engine can probe the table at every node at little cost.

When the search arrives at a position it first probes the table. If a stored entry was searched at least as deeply as the current requirement, its score may be returned at once, or, when only a bound was stored, used to narrow the alpha-beta window and produce extra cutoffs.[^s3] Even when the stored depth is too shallow, the stored best move is valuable: trying it first is one of the strongest move-ordering heuristics, and Marsland notes that tables of this kind let the program search the previous iteration's principal variation first.[^s2] Kocsis's study of search decisions in the programs MIA and Crafty likewise has the transposition-table move tried first.[^s4]

## Size, replacement and errors

Memory is finite, so a new result must sometimes overwrite an old one, and Marsland and Popowich observe that this can make later retrievals impossible when a table is overloaded.[^s3] Their experiments compared storing every node with storing only subtrees searched more than two ply deep, and the partial policy performed better.[^s3] Later engines refined this into replacement schemes that weigh the depth and age of entries; MIA, for example, used a two-deep table that keeps two candidates per slot.[^s4] Marsland's 1995 survey put a typical entry at about 10 bytes and table sizes between roughly 32,000 and one million entries, limited mainly by available memory.[^s2]

Because many positions share a slot, entries carry extra key bits so that the engine can tell when it has found a different position in the right place. Zobrist's report already treated such retrieval errors as something to be measured and controlled rather than ignored.[^s1]

## Example

After either 1.e4 e6 2.d4 d5 or 1.d4 e6 2.e4 d5, the position in the FEN above (a French Defence) arises with White to move. An engine that has stored the first order's result recognises the second order as the same position and reuses the entry. In the endgame transpositions become even more frequent, and Marsland notes the tables help the search reach much greater depth there.[^s2]

## History

The Chess Programming Wiki credits Richard Greenblatt's Mac Hack VI, written at MIT in 1966–67, as the first chess program to use a transposition table; it reports that Zobrist's paper mentions Mac Hack's 32K-entry hash table.[^s5] Zobrist's 1970 method then became the usual way of computing the key.[^s1]

## Pitfalls for engine authors

Common mistakes are trusting a stored score from a shallower search, treating a stored bound as an exact value, and letting the table become overloaded so that useful entries are overwritten. Each one either wastes the table or corrupts the search result, which is why bound types, depth and replacement policy matter as much as the table itself.[^s3][^s2]

## Connections

The transposition table is a component of **game-tree search** that makes **alpha-beta pruning** much more effective through better move ordering and narrowed windows.[^s3] It enables efficient **iterative deepening**, since each iteration seeds the next with best moves.[^s2] It depends on **Zobrist hashing** for its keys,[^s1] and was first used in Greenblatt's program.[^s5] It differs from **endgame tablebases**, which store exact precomputed results rather than results found during a search.

## Sources
[^s1]: Albert L. Zobrist, "A New Hashing Method With Application for Game Playing", Technical Report TR88, University of Wisconsin–Madison, 1970. https://research.cs.wisc.edu/techreports/viewreport.php?report=88 (accessed 2026-11-15)
[^s2]: T. A. Marsland, "The Anatomy of Chess Programs", University of Alberta, 1995. https://webdocs.cs.ualberta.ca/~tony/ICCA/anatomy.html (accessed 2026-11-15)
[^s3]: T. A. Marsland and F. Popowich, "Parallel Game-tree Search", University of Alberta Technical Report TR85-1. https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR85-1.pdf (accessed 2026-11-15)
[^s4]: Levente Kocsis, "Learning Search Decisions", PhD thesis, Maastricht University, 2003. https://cris.maastrichtuniversity.nl/ws/files/847817/guid-fb7fc02b-f018-40c2-9253-e6112141c356-ASSET1.0.pdf (accessed 2026-11-15)
[^s5]: Chess Programming Wiki, "Mac Hack". https://www.chessprogramming.org:443/Mac_Hack (accessed 2026-11-15)
