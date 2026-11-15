---
id: kt:move-ordering
type: Technique
title: Move ordering
aliases: [Successor ordering, Move sorting, Move reordering, Successor reordering]
domain: computer-chess
summary: >-
  The set of heuristics a chess engine uses to decide in which order to search the moves at each
  node, trying the likely best move first so that alpha-beta pruning cuts off as many branches as
  possible and the search approaches the size of the minimal tree.
fen: "6k1/8/8/3rp3/4P3/5N2/8/3Q2K1 w - - 0 1"
status: current
volatile: false
verified: 2026-11-15
broader: [kt:game-tree-search, kt:alpha-beta-pruning]
related: [kt:iterative-deepening, kt:transposition-table, kt:quiescence-search, kt:static-exchange-evaluation, kt:principal-variation-search]
relations:
  - {predicate: dependsOn, object: kt:iterative-deepening}
  - {predicate: dependsOn, object: kt:transposition-table}
  - {predicate: usesTechnique, object: kt:killer-heuristic}
  - {predicate: usesTechnique, object: kt:history-heuristic}
  - {predicate: usesTechnique, object: kt:mvv-lva}
sources:
  - id: s1
    title: "The Anatomy of Chess Programs (8th World Computer Chess Championship brochure, 1995)"
    publisher: T. Anthony Marsland, University of Alberta
    url: https://webdocs.cs.ualberta.ca/~tony/ICCA/anatomy.html
    type: academic
    accessed: 2026-11-15
  - id: s2
    title: "Heuristic Search in One and Two Player Games (revised for ACM Computing Surveys)"
    publisher: T. Anthony Marsland and Alexander Reinefeld, University of Alberta technical report TR93-02
    url: https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR93-02.pdf
    type: academic
    accessed: 2026-11-15
  - id: s3
    title: "Nearly Optimal Minimax Tree Search? (University of Alberta TR 94-19)"
    publisher: Aske Plaat, Jonathan Schaeffer, Wim Pijls and Arie de Bruin, via arXiv
    url: https://arxiv.org/pdf/1404.1518.pdf
    type: academic
    accessed: 2026-11-15
  - id: s4
    title: "Bibliography (DarkThought computer-chess research pages)"
    publisher: Ernst A. Heinz, MIT CSAIL
    url: https://people.csail.mit.edu/heinz/dt/node102.html
    type: academic
    accessed: 2026-11-15
  - id: s5
    title: "Move Ordering (page revision view)"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/Special:MobileDiff/1299
    type: community
    accessed: 2026-11-15
  - id: s6
    title: "MVV-LVA"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/MVV-LVA
    type: community
    accessed: 2026-11-15
created: 2026-11-15
---

# Move ordering

Move ordering is the part of a chess engine that decides which move to search first, second and so on at every node of the game tree. It does not change the value alpha-beta returns, but it decides how much work is needed to find it. Marsland describes move-reordering mechanisms as the means of making depth-first alpha-beta search efficient.[^s1] The Chess Programming Wiki puts the goal simply: for alpha-beta to perform well, the best moves must be searched first.[^s5]

## Why order matters

Alpha-beta's best and worst cases differ enormously. With perfect ordering, a uniform tree of width W and depth D needs only W^⌈D/2⌉ + W^⌊D/2⌋ − 1 leaf evaluations, the critical (minimal) tree identified by Slagle and Dixon, and no algorithm can examine fewer.[^s2] With poor ordering the saving largely disappears. Knuth and Moore's classification of nodes, later renamed PV, CUT and ALL nodes by Marsland and Popowich, explains where order counts: at a CUT node one good move is enough to refute the opponent's choice, so trying it first ends the node immediately.[^s2] The wiki adds that at ALL nodes, where every move must be searched anyway, ordering matters much less.[^s5] Marsland and Reinefeld stress that directional methods such as alpha-beta and principal variation search gain most when the best successor is found early, and lose their advantage in poorly ordered trees.[^s2]

How close real programs come is measurable. Plaat, Schaeffer, Pijls and de Bruin found that in strong game programs, including the chess program Phoenix, the first move tried produced the cutoff at more than 90 to 95 per cent of cutoff nodes in deeply searched parts of the tree, falling to about 90 per cent near the leaves.[^s3]

## The usual sources of a good first move

**The previous iteration.** Under iterative deepening the principal variation from the last, shallower search is explored first in the next one.[^s1] Plaat and colleagues note that because of this, every level of the tree except the deepest can use a best move remembered from the previous iteration.[^s3]

**The transposition table.** Each entry stores the best move found for that position along with its value, bound type and depth.[^s2] That "hash move" is one of the standard choices for the first move searched, and the wiki suggests internal iterative deepening to find one when the table has none.[^s5] Akl and Newborn's refutation tables are a lighter alternative that keep the principal variation plus one refutation for each alternative.[^s2]

**Captures.** Engines usually try captures before quiet moves.[^s1] The simplest scheme, MVV-LVA, takes the most valuable victim first and, for each victim, the least valuable attacker; because it ignores defenders, many programs refine it with a static exchange evaluation.[^s6] The wiki's typical order runs: previous best move, hash move, winning captures and promotions, equal captures, killer moves, quiet moves sorted by history, with losing captures last or just after the killers.[^s5]

**Killer moves.** A killer is a quiet move that has already caused a cutoff elsewhere in the tree and is therefore tried early in other positions.[^s1] The idea appears in Akl and Newborn's 1977 paper on the principal continuation and the killer heuristic.[^s4]

**The history heuristic.** Jonathan Schaeffer generalised killers into a table, in its simplest form 64 by 64 for from- and to-squares, scoring how often each move has recently caused pruning; quiet moves are then sorted by those scores.[^s1] He published it in the ICCA Journal in 1983 and evaluated it with other alpha-beta enhancements in IEEE Transactions on Pattern Analysis and Machine Intelligence in 1989.[^s4] Marsland and Reinefeld report Schaeffer's finding that this record of past success ordered moves better than hand-written, application-specific knowledge.[^s2]

## Example

In the diagram position (White: Kg1, Qd1, Nf3, pawn e4; Black: Kg8, Rd5, pawn e5), White has three captures. MVV-LVA tries exd5 first (pawn takes rook), then Qxd5+ (queen takes rook), then Nxe5 (knight takes pawn).[^s6] A static exchange check would also flag Nxe5 as a losing capture, since the rook simply recaptures, so a typical engine pushes it behind the killer moves.[^s5][^s6]

## Pitfalls

Exact ordering would itself be expensive, so engines approximate: the wiki notes that pawn-takes-queen needs no exchange analysis, while rook-takes-bishop may.[^s6] Tables must also be sized sensibly; Marsland and Reinefeld show that the benefits of carrying information between iterations depend on memory.[^s2] And ordering helps less in games with few moves per position, which is one reason checkers programs search closer to the minimal tree than chess programs with a branching factor around 35.[^s3]

## Connections

Move ordering is the engine of efficiency inside **game-tree search** and **alpha-beta pruning**.[^s2] It depends on **iterative deepening** and the **transposition table** for its best first guesses, and uses the **killer heuristic**, the **history heuristic** and **MVV-LVA** capture sorting, refined by **static exchange evaluation**.[^s1][^s3][^s6] Good ordering is also what makes **principal variation search** pay off, and capture ordering carries over into **quiescence search**.[^s2][^s5]

## Sources
[^s1]: T. A. Marsland, "The Anatomy of Chess Programs", 8th World Computer Chess Championship brochure, Hong Kong (1995). https://webdocs.cs.ualberta.ca/~tony/ICCA/anatomy.html (accessed 2026-11-15)
[^s2]: T. A. Marsland and A. Reinefeld, "Heuristic Search in One and Two Player Games", University of Alberta TR93-02 (revised for *ACM Computing Surveys*). https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR93-02.pdf (accessed 2026-11-15)
[^s3]: A. Plaat, J. Schaeffer, W. Pijls and A. de Bruin, "Nearly Optimal Minimax Tree Search?", University of Alberta TR 94-19 (1994). https://arxiv.org/pdf/1404.1518.pdf (accessed 2026-11-15)
[^s4]: E. A. Heinz, "Bibliography", DarkThought pages, MIT. https://people.csail.mit.edu/heinz/dt/node102.html (accessed 2026-11-15)
[^s5]: Chess Programming Wiki, "Move Ordering". https://www.chessprogramming.org/Special:MobileDiff/1299 (accessed 2026-11-15)
[^s6]: Chess Programming Wiki, "MVV-LVA". https://www.chessprogramming.org/MVV-LVA (accessed 2026-11-15)
