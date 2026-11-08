---
id: kt:quiescence-search
type: Algorithm
title: Quiescence search
aliases: [Quiescent search, Q-search, Qsearch, Capture search]
domain: computer-chess
summary: >-
  A selective extension at the leaves of a chess engine's main search that keeps exploring
  captures (and sometimes checks) until the position is quiet, so that the evaluation function
  is only applied to positions where no immediate tactic is about to change the score.
fen: "r1bqkbnr/pppp1ppp/2n5/4p2Q/4P3/8/PPPP1PPP/RNB1KBNR w KQkq - 2 3"
status: current
volatile: false
verified: 2026-11-08
broader: [kt:game-tree-search]
related: [kt:horizon-effect, kt:evaluation-function, kt:move-ordering, kt:static-exchange-evaluation]
relations:
  - {predicate: counters, object: kt:horizon-effect}
  - {predicate: dependsOn, object: kt:alpha-beta-pruning}
  - {predicate: dependsOn, object: kt:evaluation-function}
  - {predicate: influencedBy, object: kt:claude-shannon}
sources:
  - id: s1
    title: "Programming a Computer for Playing Chess (Philosophical Magazine, 1950), full text"
    publisher: Claude E. Shannon, reproduced by Fermat's Library
    url: https://fermatslibrary.com/s/programming-a-computer-for-playing-chess
    type: primary-record
    accessed: 2026-11-08
  - id: s2
    title: "Giraffe: Using Deep Reinforcement Learning to Play Chess (MSc report, Imperial College London, 2015)"
    publisher: Matthew Lai, arXiv:1509.01549
    url: https://arxiv.org/pdf/1509.01549
    type: academic
    accessed: 2026-11-08
  - id: s3
    title: "ICS 180A, Strategy and board game programming: lecture notes, 29 April 1997"
    publisher: David Eppstein, University of California, Irvine
    url: https://ics.uci.edu/~eppstein/180a/970429.html
    type: academic
    accessed: 2026-11-08
  - id: s4
    title: "Quiescence Search"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org:443/Quiescence_Search
    type: community
    accessed: 2026-11-08
  - id: s5
    title: "A generalised quiescence search algorithm (Artificial Intelligence 43(1), 1990), bibliographic record"
    publisher: Scilit
    url: https://scilit.com/publications/0a2e67498063e52c5cd0434c81dc2819
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s6
    title: "Guide: Quiescent search"
    publisher: Jonatan Pettersson, Mediocre Chess (SourceForge)
    url: https://mediocrechess.sourceforge.net/guides/quiescentsearch.html
    type: community
    accessed: 2026-11-08
created: 2026-11-08
---

# Quiescence search

Quiescence search is the part of a chess engine that refuses to judge a position in the middle of a fight. A depth-limited search stops every line at the same distance from the root, called the horizon, and then asks the evaluation function for a score.[^s2] If that cut-off falls in the middle of an exchange, the score is nonsense: a line ending with a queen taking a defended pawn looks like a pawn won, because the recapture lies beyond the horizon.[^s2] Instead of evaluating at depth zero, the engine enters a special mode that expands only certain kinds of move and evaluates only once it reaches a quiet, relatively stable position.[^s2] Lai describes depth-limited alpha-beta plus quiescence search as the backbone of virtually all classical chess engines.[^s2]

## Origins

The idea is as old as computer chess itself. In his 1950 paper Claude Shannon argued that an evaluation function can only be applied in relatively quiescent positions, and that scoring a position partway through a combination or a series of exchanges is meaningless.[^s1] His proposed "Type B" strategy was to evaluate only at reasonable positions where some quasi-stability had been established.[^s1] Eppstein's lecture notes add that Alan Turing used a related selective search that followed only capturing moves.[^s3] Later research refined the idea; Don Beal's "A generalised quiescence search algorithm" appeared in *Artificial Intelligence* in 1990, one of a line of papers on the subject going back to Larry Harris in 1975.[^s5][^s4]

## How it works

When the main search reaches its depth limit, quiescence search takes over and, in its basic form, considers only captures; in chess it may also include checks, and in other games any move that changes the evaluation sharply.[^s3] The key device is the "stand pat" score, a term borrowed from poker: the static evaluation of the current position is treated as a lower bound, on the assumption that the side to move can at least keep that score by declining further captures.[^s4] This is the "pass" option Eppstein describes, letting either side stop capturing; expansion ends when both sides pass.[^s3]

In alpha-beta terms, if the stand-pat score already reaches beta, the node is cut off at once; if it exceeds alpha, it raises alpha, and the engine then tries captures to see whether any of them does even better.[^s4] Pettersson notes that this early return ends a large share of quiescence nodes immediately, which is why the extension is cheap relative to the strength it adds.[^s6] Standing pat rests on the assumption that the side to move is not in zugzwang, and it is not allowed when that side is in check: then the position is not quiet, and all check evasions must be searched.[^s4]

## Keeping it under control

Quiescence search normally has no depth limit and relies on the capture sequence running out.[^s2] That makes it vulnerable to search explosions: although each individual quiescence search is shallow, together they can account for a large share of all nodes searched.[^s4] Engines therefore order captures carefully, typically by MVV-LVA (most valuable victim, least valuable attacker), so that, say, a pawn taking a queen is tried before a queen taking a pawn.[^s6][^s4] They also prune: captures that lose material by static exchange evaluation are skipped, and delta pruning discards captures that cannot bring the score back up to alpha.[^s4]

What to include beyond winning captures is a judgment call. Lai reports that authors agree on captures but disagree about checks, queen promotions and pawn pushes to the seventh rank: including too much makes the search balloon, while including too little leaves reduced forms of the horizon effect.[^s2] Programs that add non-capturing checks usually restrict them to the first few plies of quiescence.[^s4] A capture-only search also cannot recognise checkmate on its own; that remains the job of the main search.[^s6]

## Example

In the position after 1.e4 e5 2.Qh5 Nc6 (FEN above), White can play 3.Qxe5+. A one-ply search that stopped there would count a pawn won with check. A quiescence search at that leaf would first see that Black is in check and so cannot stand pat, then search Black's evasions, among them the capture 3...Nxe5, which wins the queen. The line is correctly scored as losing, exactly the mid-exchange error Shannon warned against and the defended-pawn trap Lai uses to illustrate the horizon problem.[^s1][^s2][^s4]

## Connections

Quiescence search sits under general **game-tree search** and is layered on top of **alpha-beta pruning**, using the same alpha and beta bounds at its nodes.[^s4][^s6] It is the standard remedy for the **horizon effect**, which Lai notes cannot be fixed just by searching deeper.[^s2] It depends on the **evaluation function** for its stand-pat score, and on **move ordering** and **static exchange evaluation** to stay small.[^s4] Its central principle, evaluating only quiescent positions, goes back to **Claude Shannon**.[^s1]

## Sources
[^s1]: C. E. Shannon, "Programming a Computer for Playing Chess", *Philosophical Magazine*, Ser. 7, Vol. 41, No. 314 (March 1950), reproduced by Fermat's Library. https://fermatslibrary.com/s/programming-a-computer-for-playing-chess (accessed 2026-11-08)
[^s2]: M. Lai, "Giraffe: Using Deep Reinforcement Learning to Play Chess", MSc report, Imperial College London (2015), arXiv:1509.01549. https://arxiv.org/pdf/1509.01549 (accessed 2026-11-08)
[^s3]: D. Eppstein, ICS 180A lecture notes, University of California, Irvine, 29 April 1997. https://ics.uci.edu/~eppstein/180a/970429.html (accessed 2026-11-08)
[^s4]: Chess Programming Wiki, "Quiescence Search". https://www.chessprogramming.org:443/Quiescence_Search (accessed 2026-11-08)
[^s5]: "A generalised quiescence search algorithm", *Artificial Intelligence* 43(1), 85–98 (1990), doi:10.1016/0004-3702(90)90072-8; record at Scilit. https://scilit.com/publications/0a2e67498063e52c5cd0434c81dc2819 (accessed 2026-11-08)
[^s6]: J. Pettersson, "Quiescent search", Mediocre Chess guides (2007). https://mediocrechess.sourceforge.net/guides/quiescentsearch.html (accessed 2026-11-08)
