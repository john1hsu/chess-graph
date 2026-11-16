---
id: kt:principal-variation-search
type: Algorithm
title: Principal variation search
aliases: [PVS, NegaScout, Nega-Scout, Minimal window search, Null window search, Zero window search, Calphabeta, Palphabeta]
domain: computer-chess
summary: >-
  An enhancement of alpha-beta search that searches the expected best move at each node with a full
  window and tries to prove every other move inferior with a cheap minimal (null) window, re-searching
  only when a move unexpectedly proves better.
status: current
volatile: false
verified: 2026-11-16
broader: [kt:alpha-beta-pruning, kt:game-tree-search]
related: [kt:move-ordering, kt:iterative-deepening, kt:transposition-table, kt:aspiration-window, kt:scout-algorithm]
relations:
  - {predicate: dependsOn, object: kt:alpha-beta-pruning}
  - {predicate: dependsOn, object: kt:move-ordering}
  - {predicate: alternativeTo, object: kt:aspiration-window}
  - {predicate: influencedBy, object: kt:scout-algorithm}
  - {predicate: developedBy, object: kt:tony-marsland}
sources:
  - id: s1
    title: "Parallel Search of Strongly Ordered Game Trees (ACM Computing Surveys, 1982)"
    publisher: T. A. Marsland and M. Campbell, University of Alberta
    url: https://webdocs.cs.ualberta.ca/~tony/OldPapers/strong.pdf
    type: academic
    accessed: 2026-11-16
  - id: s2
    title: "A Review of Game-Tree Pruning (ICCA Journal, Vol. 9, No. 1, 1986)"
    publisher: T. A. Marsland, University of Alberta
    url: https://webdocs.cs.ualberta.ca/~tony/OldPapers/icca.Mar1986.pp3-18.pdf
    type: academic
    accessed: 2026-11-16
  - id: s3
    title: "Heuristic Search in One and Two Player Games (University of Alberta TR93-02)"
    publisher: T. Anthony Marsland and Alexander Reinefeld, University of Alberta
    url: https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR93-02.pdf
    type: academic
    accessed: 2026-11-16
  - id: s4
    title: "A Quantitative Analysis of Minimal Window Search (IJCAI 1987)"
    publisher: Alexander Reinefeld and T. Anthony Marsland, IJCAI Proceedings
    url: https://ijcai.org/proceedings/1987/0196.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s5
    title: "Search algorithm (GNU Chess manual)"
    publisher: GNU Project, Free Software Foundation
    url: https://www.gnu.org/software/chess/manual/html_node/Search-algorithm.html
    type: official-project
    accessed: 2026-11-16
  - id: s6
    title: "Principal Variation Search"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/Principal_Variation_Search
    type: community
    accessed: 2026-11-16
created: 2026-11-16
---

# Principal variation search

Principal variation search (PVS) is a refinement of alpha-beta pruning used by most chess engines. Instead of asking "how good is this move?" for every move at a node, it asks that question only of the move it expects to be best, and for the rest asks the cheaper question "is this move better than what I already have?". Marsland and Campbell describe it as searching the first successor normally and the balance of the tree with a minimal window.[^s1] The Chess Programming Wiki summarises the purpose as using null or zero-width windows at non-PV nodes to prove that a move is no better than the score of the principal variation.[^s6]

## How it works

At each node the first move, normally the best move from the previous iteration or the transposition table, is searched with the full alpha-beta window. Every later move is then searched with a window of width one placed just above the current best score, so the search can only answer "fails low" (not better) or "fails high" (better). If a move fails low, it is discarded at a fraction of the cost of finding its exact value. If it fails high, the move is re-searched with a proper window to obtain its true value, and it becomes the new principal variation.[^s1][^s6] Marsland's review states the underlying idea plainly: proving a subtree inferior is cheaper than determining its exact value.[^s2]

In the vocabulary of node types, the null-window search is used at CUT and ALL nodes and the full search only at PV nodes, a separation that Marsland and Reinefeld note also makes the method easier to parallelise.[^s3] The wiki adds a common implementation detail: re-searches are skipped when the node's own window is already null, because such a node cannot be on the principal variation.[^s6]

## Origins and names

The idea emerged from Judea Pearl's Scout algorithm of 1980, which originally used a separate test procedure rather than a minimal-window alpha-beta call.[^s1] John Fishburn's version was called Palphabeta and later Calphabeta; Marsland and Campbell formalised the name PVS in 1982; and Alexander Reinefeld independently developed NegaScout in 1983.[^s1][^s3][^s6] NegaScout differs mainly in how the re-search window is set, and several researchers quoted by the wiki regard the two as essentially the same search, so this article treats them as one subject.[^s6] Marsland's 1986 review added Reinefeld's refinement that re-searches are only needed when more than two plies remain.[^s2]

## Why it pays off, and when it does not

PVS is a bet on move ordering. Marsland and Campbell warned that on poorly ordered trees it may search more nodes than plain alpha-beta, and that it works better with iterative deepening because the first move tried is then more often best.[^s1] Reinefeld and Marsland's quantitative model found that NegaScout beats alpha-beta when few extra moves must be tried at cut nodes and the principal variation rarely changes; alpha-beta regains the edge only when re-searches become frequent, roughly above 15 per cent in their example, or when the best move tends to come late in the list.[^s4] Since chess programs usually find the cutoff move first, the model predicts that PVS and NegaScout should outperform alpha-beta in practice, and the gain grows in wide trees such as chess.[^s4]

Experimental reports agree. Marsland and Campbell expected roughly a 13 per cent speed improvement over aspiration search from their own experience, and in Marsland's experiments on the Bratko-Kopec test positions PVS beat aspiration search under iterative deepening, coming close to the minimal tree once refutation, transposition and history tables were added.[^s1][^s2] Marsland and Reinefeld explain the advantage: PVS keeps tightening its bound during the search, while aspiration search fixes its guess beforehand.[^s3]

## Pitfalls

The main practical hazard is search instability. A move can fail high on the null window and then fail low on the re-search, because of transposition-table effects or search extensions, and combining PVS with aspiration windows can leave the root with no reliable move or principal variation if the outer window fails as well.[^s6] Implementations therefore differ in their re-search window. The GNU Chess manual, for example, describes its main search as a classical PVS with iterative deepening that deliberately re-searches with the original window rather than one starting from the scout value, a choice its author made for stability.[^s5]

## Example

Suppose an engine at the root has a best move scoring +0.30 from the previous iteration. It searches that move fully and confirms +0.30. For each of the other 30 or so moves it now runs a null-window search asking only whether the move can exceed +0.30. Most quickly fail low because a single refutation is found. If one fails high, say a quiet bishop retreat that the shallower search undervalued, only that move is re-searched with a full window, and if it scores +0.45 it becomes the new best move.[^s1][^s6]

## Connections

PVS is a refinement of **alpha-beta pruning** within **game-tree search**, and it descends from Pearl's **Scout** algorithm.[^s1][^s3] It depends heavily on good **move ordering**, supplied by **iterative deepening** and the **transposition table**, and it competes with, or is combined with, **aspiration windows**.[^s2][^s3][^s6] Its formalisation as PVS is credited to **Tony Marsland** and Murray Campbell.[^s1][^s6]

## Sources
[^s1]: T. A. Marsland and M. Campbell, "Parallel Search of Strongly Ordered Game Trees", *ACM Computing Surveys* (1982). https://webdocs.cs.ualberta.ca/~tony/OldPapers/strong.pdf (accessed 2026-11-16)
[^s2]: T. A. Marsland, "A Review of Game-Tree Pruning", *ICCA Journal* 9(1), March 1986, pp. 3–19. https://webdocs.cs.ualberta.ca/~tony/OldPapers/icca.Mar1986.pp3-18.pdf (accessed 2026-11-16)
[^s3]: T. A. Marsland and A. Reinefeld, "Heuristic Search in One and Two Player Games", University of Alberta TR93-02. https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR93-02.pdf (accessed 2026-11-16)
[^s4]: A. Reinefeld and T. A. Marsland, "A Quantitative Analysis of Minimal Window Search", *Proceedings of IJCAI-87*, pp. 951–953. https://ijcai.org/proceedings/1987/0196.pdf (accessed 2026-11-16)
[^s5]: GNU Project, "Search algorithm", GNU Chess manual. https://www.gnu.org/software/chess/manual/html_node/Search-algorithm.html (accessed 2026-11-16)
[^s6]: Chess Programming Wiki, "Principal Variation Search". https://www.chessprogramming.org/Principal_Variation_Search (accessed 2026-11-16)
