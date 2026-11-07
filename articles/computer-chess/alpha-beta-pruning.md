---
id: kt:alpha-beta-pruning
type: Algorithm
title: Alpha-beta pruning
aliases: [Alpha-beta search, Alpha-beta algorithm, Alpha-beta heuristic, Alphabeta]
domain: computer-chess
summary: >-
  A refinement of minimax game-tree search that skips branches which provably cannot change the
  value of the root, letting a chess engine reach the same result as full minimax while examining
  far fewer positions.
fen: "r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 4 4"
status: current
volatile: false
verified: 2026-11-07
broader: [kt:minimax, kt:game-tree-search]
related: [kt:move-ordering, kt:iterative-deepening, kt:transposition-table, kt:principal-variation-search]
relations:
  - {predicate: dependsOn, object: kt:minimax}
  - {predicate: developedBy, object: kt:john-mccarthy}
  - {predicate: enables, object: kt:principal-variation-search}
  - {predicate: contrastsWith, object: kt:monte-carlo-tree-search}
sources:
  - id: s1
    title: "The Minimax Algorithm and Alpha-Beta Pruning"
    publisher: Computer History Museum (Mastering the Game exhibit)
    url: https://www.computerhistory.org/chess/the-minimax-algorithm-and-alphabeta-pruning/
    type: archive
    accessed: 2026-11-07
  - id: s2
    title: "An analysis of alpha-beta pruning (Knuth & Moore, Artificial Intelligence, 1975)"
    publisher: AITopics (AAAI) Classics
    url: https://aitopics.org/doc/classics:26AE7F7A
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s3
    title: "CS 440/ECE 448 Lecture notes: Games 3"
    publisher: University of Illinois Urbana-Champaign (Margaret Fleck)
    url: https://courses.grainger.illinois.edu/cs440/fa2021/lectures/games3.html
    type: academic
    accessed: 2026-11-07
  - id: s4
    title: "Alpha-Beta"
    publisher: Chess Programming Wiki
    url: https://www.ChessProgramming.org/Alpha-Beta
    type: community
    accessed: 2026-11-07
  - id: s5
    title: "Alpha-Beta Pruning (Isabelle/HOL formal verification)"
    publisher: Tobias Nipkow, Technical University of Munich (isa-afp.org)
    url: https://www.isa-afp.org/browser_info/current/AFP/Alpha_Beta_Pruning/document.pdf
    type: academic
    accessed: 2026-11-07
created: 2026-11-07
---

# Alpha-beta pruning

Alpha-beta pruning is the search technique at the heart of classical chess engines. A program using minimax looks ahead through a tree of moves and replies, assuming that on its own turn it picks the best move and on the opponent's turn the opponent picks the move worst for it; alpha-beta lets it skip ("prune") branches that cannot lead to a better outcome than one already found.[^s1] The Computer History Museum notes that most two-person game-playing programs combine minimax with alpha-beta pruning.[^s1] Crucially, pruning does not change the answer: with a full window, alpha-beta returns exactly the minimax value of the tree, a result that has even been machine-checked in a formal proof assistant.[^s5]

## How it works

The search runs depth-first and keeps two running bounds. At a node where the side to move is maximising, the children already examined give a lower bound on its value (alpha); at a minimising node they give an upper bound (beta).[^s3] As soon as one child shows that a node is already worse for one side than an alternative that side has elsewhere, the remaining children of that node are irrelevant and are cut off.[^s3] In chess terms: if one opponent reply already refutes a candidate move, the engine does not need to find out whether other replies refute it even more.

Knuth and Moore's 1975 paper in *Artificial Intelligence* gave the method a rigorous footing: it presented the procedure, proved it correct, discussed its history, showed it is optimal in a certain sense and derived bounds on its running time for several kinds of random tree.[^s2] Later variants differ in what they return when the true value lies outside the window. A "fail-hard" search clamps the result to alpha or beta; a "fail-soft" search returns the best score it actually saw, which carries more information.[^s4] Nipkow's formal treatment attributes the fail-hard form to Knuth and Moore and the fail-soft form to Fishburn (1980), and proves fail-soft approximates the true value at least as well.[^s5]

## Why move ordering matters

How much is pruned depends almost entirely on the order in which moves are tried. In a teaching example, reversing the order of children turned a tree with no cutoffs into one with substantial pruning.[^s3] Plain minimax examines on the order of b^d positions for branching factor b and depth d; with perfect ordering alpha-beta needs about b^(d/2), and with random ordering about b^(3d/4).[^s3] Put differently, a well-ordered alpha-beta search can look roughly twice as deep as minimax for the same effort. Levin's exact best-case count, b^⌈d/2⌉ + b^⌊d/2⌋ − 1 leaves, is close to the square root of the minimax count.[^s4]

Because the best move is not known in advance, engines rely on heuristics. A simple scheme for chess is to try captures first, then threats and forward moves, and retreats last.[^s3] Engine authors treat ordering as a central design problem, and support it with iterative deepening, a transposition table and aspiration windows, which the Chess Programming Wiki lists as essential companions to alpha-beta; refinements such as Principal Variation Search build on the same framework.[^s4]

## Example

Take the position after 1.e4 e5 2.Qh5 Nc6 3.Bc4 Nf6 (FEN above). Suppose an engine searching from Black's side is evaluating 3...Nf6 among Black's third-move options. The first White reply it tries, if move ordering puts captures and checks first, is 4.Qxf7#, which is mate. That single reply proves 3...Nf6 is losing, so the engine has no reason to examine any of White's other fourth moves in that line: the branch is cut off, exactly the situation alpha-beta exploits.[^s3]

## Pitfalls

Alpha-beta is only as good as its ordering and its evaluation at the leaves. Poor ordering throws away most of the speed-up, and searching worse moves first can prevent cutoffs altogether.[^s4] The algorithm also inherits the horizon problems of fixed-depth minimax, which is why engines add quiescence search and other selectivity techniques on top.[^s4]

## History

Alpha-beta dates from the late 1950s.[^s5] According to the Chess Programming Wiki's chronology, John McCarthy proposed the idea at the 1956 Dartmouth workshop, Newell and Simon used an approximation in 1958, Hart and Edwards described it in 1961, Alexander Brudno published a description in 1963, and Knuth and Moore's 1975 analysis became the standard reference.[^s4] The Newell, Shaw and Simon (NSS) chess program of 1958 is one of the early programs the Computer History Museum associates with these search ideas, combined with chess heuristics to limit how many moves were explored.[^s1]

## Connections

Alpha-beta is a refinement of **minimax** and depends on it, sitting under general **game-tree search**.[^s1] Its practical strength comes from **move ordering**, supported by **iterative deepening** and a **transposition table**, and it is the base on which **Principal Variation Search** is built.[^s4] Its idea is credited first to **John McCarthy**.[^s4] It is often contrasted with **Monte Carlo tree search**, a separate family of game-tree search methods that samples the tree rather than pruning a fixed-depth minimax search.

## Sources
[^s1]: Computer History Museum, "The Minimax Algorithm and Alpha-Beta Pruning", Mastering the Game. https://www.computerhistory.org/chess/the-minimax-algorithm-and-alphabeta-pruning/ (accessed 2026-11-07)
[^s2]: D. E. Knuth and R. W. Moore, "An analysis of alpha-beta pruning", *Artificial Intelligence* (1975), doi:10.1016/0004-3702(75)90019-3; record at AITopics. https://aitopics.org/doc/classics:26AE7F7A (accessed 2026-11-07)
[^s3]: M. Fleck, CS 440/ECE 448 lecture notes "Games 3", University of Illinois Urbana-Champaign, Fall 2021. https://courses.grainger.illinois.edu/cs440/fa2021/lectures/games3.html (accessed 2026-11-07)
[^s4]: Chess Programming Wiki, "Alpha-Beta". https://www.ChessProgramming.org/Alpha-Beta (accessed 2026-11-07)
[^s5]: T. Nipkow, "Alpha-Beta Pruning", Isabelle/HOL theories. https://www.isa-afp.org/browser_info/current/AFP/Alpha_Beta_Pruning/document.pdf (accessed 2026-11-07)
