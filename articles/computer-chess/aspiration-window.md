---
id: kt:aspiration-window
type: Algorithm
title: Aspiration window
aliases: [Aspiration windows, Aspiration search, Iterated aspiration search, Aspiration alpha-beta]
domain: computer-chess
summary: >-
  An alpha-beta search technique that starts the root search with a narrow window of bounds centred on
  an expected score, usually the previous iteration's result, to gain extra cutoffs, and re-searches
  with a wider window only when the true score falls outside it.
status: current
volatile: false
verified: 2026-11-17
broader: [kt:alpha-beta-pruning, kt:game-tree-search]
related: [kt:iterative-deepening, kt:principal-variation-search, kt:transposition-table, kt:mtd-f, kt:stockfish]
relations:
  - {predicate: dependsOn, object: kt:alpha-beta-pruning}
  - {predicate: dependsOn, object: kt:iterative-deepening}
  - {predicate: alternativeTo, object: kt:principal-variation-search}
  - {predicate: usesTechnique, object: kt:fail-soft-alpha-beta}
  - {predicate: developedBy, object: kt:david-slate}
sources:
  - id: s1
    title: "A Review of Game-Tree Pruning (ICCA Journal, Vol. 9, No. 1, 1986)"
    publisher: T. A. Marsland, University of Alberta
    url: https://webdocs.cs.ualberta.ca/~tony/OldPapers/icca.Mar1986.pp3-18.pdf
    type: academic
    accessed: 2026-11-17
  - id: s2
    title: "Heuristic Search in One and Two Player Games (University of Alberta TR93-02)"
    publisher: T. Anthony Marsland and Alexander Reinefeld, University of Alberta
    url: https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR93-02.pdf
    type: academic
    accessed: 2026-11-17
  - id: s3
    title: "Using Aspiration Windows for Minimax Algorithms (IJCAI 1991, pp. 192-196)"
    publisher: Reza Shams, Hermann Kaindl and Helmut Horacek, IJCAI Proceedings
    url: https://ijcai.org/proceedings/1991/0029.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "New Advances in Alpha-Beta Searching"
    publisher: Jonathan Schaeffer and Aske Plaat, author copy hosted by Leiden University
    url: https://liacs.leidenuniv.nl/~plaata1/papers/acm-final.pdf
    type: academic
    accessed: 2026-11-17
  - id: s5
    title: "Aspiration Windows"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/Aspiration_Windows
    type: community
    accessed: 2026-11-17
created: 2026-11-17
---

# Aspiration window

An aspiration window is a bet placed by a chess engine before it searches. Plain alpha-beta starts at the root with the widest possible bounds, minus infinity to plus infinity, so that any score can be returned. Aspiration search instead opens the root with narrow bounds that bracket the score the program expects, written as the window from V minus e to V plus e, where V is the estimate and e the expected error.[^s1] In chess the early formulation was simply material balance plus or minus about a pawn.[^s1] The narrower the bounds, the more branches fall outside them and are cut off, so a successful aspiration search usually finishes measurably faster than a full-width one.[^s1]

## How it works

The technique only pays off with a good estimate, and in practice the estimate comes from iterative deepening: each completed depth gives a score that is usually close to the score of the next, deeper iteration.[^s3] Marsland credits Slate and Atkin, the authors of the Northwestern University programs, with the "iterated aspiration search" that came into general use after 1974, in which each iteration's window was centred on the previous iteration's final score; the idea itself had been analysed earlier by Brudno, while Gillogly's experiments with it were not consistently successful.[^s1] Marsland and Reinefeld also name Baudet among its originators.[^s2]

Three outcomes are possible. If the returned value lies inside the window, it is exact and the gamble has paid off. If it fails high (the value is at least the upper bound) or fails low (at most the lower bound), the search only knows a bound, and must be repeated with the window opened in that direction.[^s1] A fail-soft implementation of alpha-beta helps here, because a failed search still returns a meaningful bound rather than just the window edge, which tells the re-search where to set its new limit.[^s2] Failures typically happen when material is being won or lost, which is exactly when a deeper look is worth paying for.[^s1]

## Tuning and pitfalls

Window size is the central trade-off. In a systematic comparison of minimax algorithms, Shams, Kaindl and Horacek found that performance generally improves as the window shrinks, but very small windows trigger costly re-searches, and failing low costs more than failing high; they measured roughly 20 per cent savings for plain alpha-beta and observed re-searches in about 5 per cent of searches in their tournament program.[^s3] Modern engine practice, as summarised by programmers, starts with a window of a fraction of a pawn either side of the guess and, on failure, widens only the bound that failed, often exponentially, because re-searching with both bounds moved can fail again in the other direction due to search instability.[^s5]

A fail low at the root is the awkward case, since it means the expected best move is worse than thought and the program may need to find a different move under time pressure. Schaeffer and Plaat note that the usual remedy is to re-search with a wider window, and report that restarting iterative deepening from shallow depth with transposition-table support found the alternative move faster in their chess tests.[^s4]

## Connections

Aspiration search is an enhancement of alpha-beta pruning and depends on iterative deepening for its estimate.[^s1] It is best understood alongside principal variation search, which uses minimal (null) windows for non-first moves instead of a single guessed window; Marsland judged minimal-window search more efficient and free of assumptions about the window, and Marsland and Reinefeld's model-program comparison favoured PVS because it keeps refining its estimate during the search.[^s1][^s2] The two are not exclusive: aspiration NegaScout combines a root aspiration window with minimal-window searches below it, and MTD(f) takes the idea to its limit by running only minimal-window searches around the previous score, relying on the transposition table to avoid repeated work.[^s4] Current engines such as Stockfish still list aspiration windows among their search features.[^s5]

## Sources
[^s1]: T. A. Marsland, "A Review of Game-Tree Pruning", ICCA Journal 9(1), 1986, section 2.4. https://webdocs.cs.ualberta.ca/~tony/OldPapers/icca.Mar1986.pp3-18.pdf (accessed 2026-11-17)
[^s2]: T. A. Marsland and A. Reinefeld, "Heuristic Search in One and Two Player Games", University of Alberta TR93-02. https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR93-02.pdf (accessed 2026-11-17)
[^s3]: R. Shams, H. Kaindl and H. Horacek, "Using Aspiration Windows for Minimax Algorithms", IJCAI 1991, pp. 192-196. https://ijcai.org/proceedings/1991/0029.pdf (accessed 2026-11-17)
[^s4]: J. Schaeffer and A. Plaat, "New Advances in Alpha-Beta Searching". https://liacs.leidenuniv.nl/~plaata1/papers/acm-final.pdf (accessed 2026-11-17)
[^s5]: Chess Programming Wiki, "Aspiration Windows". https://www.chessprogramming.org/Aspiration_Windows (accessed 2026-11-17)
