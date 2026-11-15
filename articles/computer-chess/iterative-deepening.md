---
id: kt:iterative-deepening
type: Algorithm
title: Iterative deepening
aliases: [Depth-first iterative deepening, DFID, Iterative deepening search, Iterated search, ID search]
domain: computer-chess
summary: >-
  A search control scheme in which a chess engine runs a series of complete depth-limited searches,
  one ply, then two, then three and so on, until its time runs out, using each finished iteration
  both as a ready answer and as move-ordering information for the next.
status: current
volatile: false
verified: 2026-11-15
broader: [kt:game-tree-search]
related: [kt:alpha-beta-pruning, kt:transposition-table, kt:move-ordering, kt:aspiration-window, kt:progressive-deepening]
relations:
  - {predicate: enables, object: kt:move-ordering}
  - {predicate: enables, object: kt:time-management-in-games}
  - {predicate: dependsOn, object: kt:alpha-beta-pruning}
  - {predicate: contrastsWith, object: kt:progressive-deepening}
  - {predicate: developedBy, object: kt:chess-4-5}
sources:
  - id: s1
    title: "Depth-First Iterative-Deepening: An Optimal Admissible Tree Search (Artificial Intelligence 27, 1985)"
    publisher: Richard E. Korf, copy hosted by the University of South Carolina
    url: https://cse.sc.edu/~mgv/csce580f11/gradPres/korf_IDAStar_1985.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s2
    title: "Heuristic Search in One and Two Player Games (revised for ACM Computing Surveys)"
    publisher: T. Anthony Marsland and Alexander Reinefeld, University of Alberta technical report TR93-02
    url: https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR93-02.pdf
    type: academic
    accessed: 2026-11-15
  - id: s3
    title: "The Anatomy of Chess Programs (8th World Computer Chess Championship brochure, 1995)"
    publisher: T. Anthony Marsland, University of Alberta
    url: https://webdocs.cs.ualberta.ca/~tony/ICCA/anatomy.html
    type: academic
    accessed: 2026-11-15
  - id: s4
    title: "Iterative Deepening"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org:443/Iterative_Deepening
    type: community
    accessed: 2026-11-15
  - id: s5
    title: "GNU Chess manual: Search algorithm"
    publisher: GNU Project, Free Software Foundation
    url: https://www.gnu.org/software/chess/manual/html_node/Search-algorithm.html
    type: official-project
    accessed: 2026-11-15
created: 2026-11-15
---

# Iterative deepening

Iterative deepening is the outer loop of almost every classical chess engine. Instead of deciding in advance how deep to search, the program searches the position to one ply, then searches it again to two plies, then three, and keeps going until the time allotted for the move is used up.[^s4][^s3] When the clock forces it to stop, it plays the best move from the deepest iteration it finished, so it always has an answer ready.[^s4] Marsland describes the effect as giving the best move that the time limit allows.[^s3]

## Origins

The scheme was born in computer chess as a way of keeping the cost of search within bounds. Marsland and Reinefeld credit John Scott with introducing it, in a program whose searches of one, two, three plies and so on continued until the time allotment was exhausted, with each iteration's best move tried first in the next.[^s2] The Chess Programming Wiki records that Jim Gillogly, author of the Tech program, coined the name "iterative deepening" to separate this full-width search to increasing depths from the more selective, focused deepening Adriaan de Groot had observed in human players.[^s4] Richard Korf, in his 1985 analysis, states that the algorithm first appears in the literature in David Slate and Larry Atkin's program Chess 4.5, where each new iteration first retraced the previous best line and then extended it by a ply.[^s1][^s4]

## Why repeating work is cheap

Throwing away a finished search and starting again sounds wasteful, but in a tree that grows exponentially the last iteration dominates. Korf shows that nodes at the final depth are generated once, those one level shallower twice, and so on, and that the total is still only a constant multiple of the work for the deepest search; the constant is b/(b-1) for branching factor b, which approaches 1 as b grows.[^s1] With ten moves per position, for example, that bound is about 1.11, so all the shallower iterations together cost roughly a tenth of the final one. Korf also proves that, among brute-force methods, depth-first iterative deepening is asymptotically optimal in time and needs only memory proportional to the depth.[^s1] He notes that Patrick Winston had already shown the extra computation to be insignificant in two-player search when only terminal evaluations are counted.[^s1]

## What chess engines gain

The first gain is **time control**. The time needed for the next ply is unknown in advance, so an engine can abort an iteration and fall back on the move from the last completed one.[^s1] Because the previous best move is searched first in the new iteration, even a partly finished iteration can be used if that move has already been examined.[^s4] The wiki adds that a sharp drop in score is a reason to allocate extra time rather than stop.[^s4]

The second gain, which surprised early programmers, is **move ordering**. Alpha-beta prunes most when the best move is tried first, and the previous iteration supplies exactly that guess: the principal variation, the best move stored in the transposition table, and refutations of the alternatives.[^s2][^s3] Korf cites experiments by Hans Berliner in which the best move from one iteration turned out best in the next about 70% of the time.[^s1] Marsland and Reinefeld explain that with such memory functions the repeated shallow work pays for itself, and the iterated search can even be faster than a direct search to the same depth.[^s2] The wiki notes that, combined with a transposition table, iterative deepening gives a depth-first alpha-beta search best-first characteristics.[^s4]

## Pitfalls and refinements

The savings depend on memory. Marsland and Reinefeld stress that iterative schemes only come out ahead when tables carry information forward, and report that a transposition table that was too small became overloaded at nine plies and slowed the search.[^s2] Each iteration's score also provides an estimate for the next, which aspiration search exploits by searching a narrow window, about half a pawn either side in Marsland's description, around it and re-searching if the true value falls outside.[^s3][^s2] In their comparison, principal variation search proved more efficient than aspiration search.[^s2]

## Example

Suppose an engine has ten seconds. It completes depths 1 to 11 quickly, each time storing the best line. Midway through depth 12 the time runs out; the engine discards the unfinished iteration (or keeps it if the first-searched move already returned a better score) and plays the depth-11 choice.[^s4] Production engines still work this way: the GNU Chess manual describes its main search as principal variation search with iterative deepening, backed by a transposition table.[^s5]

## Connections

Iterative deepening is a control layer within **game-tree search** that depends on **alpha-beta pruning**, which it makes far more efficient by enabling good **move ordering**.[^s1][^s2] It works hand in hand with the **transposition table**, which carries best moves between iterations, and with the **aspiration window**, which uses the last score as an estimate.[^s2][^s3] It is the basis of an engine's **time management**.[^s1] Its name was chosen to contrast with de Groot's **progressive deepening** of human thought, and its first documented use was in **Chess 4.5**.[^s4][^s1]

## Sources
[^s1]: R. E. Korf, "Depth-First Iterative-Deepening: An Optimal Admissible Tree Search", *Artificial Intelligence* 27 (1985), 97–109. https://cse.sc.edu/~mgv/csce580f11/gradPres/korf_IDAStar_1985.pdf (accessed 2026-11-15)
[^s2]: T. A. Marsland and A. Reinefeld, "Heuristic Search in One and Two Player Games", University of Alberta TR93-02 (revised for *ACM Computing Surveys*). https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR93-02.pdf (accessed 2026-11-15)
[^s3]: T. A. Marsland, "The Anatomy of Chess Programs", 8th World Computer Chess Championship brochure, Hong Kong (1995). https://webdocs.cs.ualberta.ca/~tony/ICCA/anatomy.html (accessed 2026-11-15)
[^s4]: Chess Programming Wiki, "Iterative Deepening". https://www.chessprogramming.org:443/Iterative_Deepening (accessed 2026-11-15)
[^s5]: GNU Chess manual, "Search algorithm", GNU Project. https://www.gnu.org/software/chess/manual/html_node/Search-algorithm.html (accessed 2026-11-15)
