---
id: kt:monte-carlo-tree-search
type: Algorithm
title: Monte Carlo tree search
aliases: [Monte-Carlo tree search, MCTS, UCT, Upper Confidence bounds applied to Trees, PUCT, Monte Carlo search]
domain: computer-chess
summary: >-
  A best-first game-tree search that grows an uneven tree by repeated simulations: each iteration
  selects a path from the root, expands a new node, estimates its value (by a random playout or a
  neural network) and backs the result up as an average, so effort concentrates on promising moves.
fen: "6k1/1q3ppp/8/8/8/8/1P3PPP/3R2K1 b - - 0 1"
status: current
volatile: false
verified: 2026-11-08
broader: [kt:game-tree-search]
related: [kt:minimax, kt:alpha-beta-pruning, kt:evaluation-function, kt:horizon-effect, kt:leela-chess-zero]
relations:
  - {predicate: contrastsWith, object: kt:alpha-beta-pruning}
  - {predicate: contrastsWith, object: kt:minimax}
  - {predicate: developedBy, object: kt:remi-coulom}
  - {predicate: dependsOn, object: kt:evaluation-function}
sources:
  - id: s1
    title: "Efficient Selectivity and Backup Operators in Monte-Carlo Tree Search (Computers and Games 2006)"
    publisher: Rémi Coulom, author's page
    url: https://remi-coulom.fr/CG2006
    type: academic
    accessed: 2026-11-08
  - id: s2
    title: "A Survey of Monte Carlo Tree Search Methods (IEEE Transactions on Computational Intelligence and AI in Games 4(1), March 2012)"
    publisher: C. Browne, E. Powley, D. Whitehouse et al., copy hosted by UNAM
    url: https://turing.iimas.unam.mx/~luis/cursos/IA2022-1/lecturas/SurveyMCTS.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s3
    title: "Bandit Based Monte-Carlo Planning (ECML 2006, pp. 282–293)"
    publisher: L. Kocsis and C. Szepesvári, University of Alberta PapersDB record
    url: https://papersdb.cs.ualberta.ca/~papersdb/view_publication.php?pub_id=633
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s4
    title: "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (arXiv:1712.01815, December 2017)"
    publisher: D. Silver, T. Hubert, J. Schrittwieser et al. (DeepMind), arXiv
    url: https://arxiv.org/pdf/1712.01815
    type: academic
    accessed: 2026-11-08
  - id: s5
    title: "Lc0 developer overview"
    publisher: Leela Chess Zero project
    url: https://lczero.org/dev/overview
    type: official-project
    accessed: 2026-11-08
created: 2026-11-08
---

# Monte Carlo tree search

Monte Carlo tree search (MCTS) chooses a move by running many simulations from the current position and keeping statistics in a tree that grows a little with each one. Unlike a fixed-depth minimax search, it does not examine every move to the same depth: the tree grows asymmetrically, towards the lines that have looked best so far, while every other move keeps some chance of being tried.[^s2] The result can be read off at any moment, because the statistics are updated after every iteration and more iterations generally improve the answer.[^s2]

## How it works

The survey by Browne and colleagues describes each iteration in four steps.[^s2] In **selection**, the program walks down from the root, picking a child at each node by a selection policy, until it reaches a node with untried moves. In **expansion**, one or more new children are added. In **simulation**, the new position is scored, classically by playing the game out to the end with a fast default policy (often random moves). In **backpropagation**, that result updates the visit counts and average values of every node on the path. When time runs out, the program typically plays either the child with the best average reward or the most visited child (the "robust child").[^s2]

The usual selection rule is UCT, introduced by Levente Kocsis and Csaba Szepesvári at ECML 2006, which applies multi-armed bandit techniques to guide Monte Carlo planning; they proved it consistent and gave bounds on its sampling error.[^s3] In the survey's notation, a child is scored by its average reward plus an exploration bonus that grows with the log of the parent's visits and shrinks with the child's own visits, weighted by a tunable constant.[^s2] The first term exploits moves that have worked; the second forces the search to keep checking moves it has barely looked at.

## History

The survey credits Bernd Brügmann with applying Monte Carlo methods to computer Go in 1993 and Rémi Coulom with coining the name "Monte Carlo tree search" in 2006.[^s2] Coulom's Computers and Games 2006 paper merged tree search and Monte Carlo evaluation into one framework, with a backup operator that starts as plain averaging and shifts towards minimax as simulations accumulate; his program Crazy Stone, built on it, won the 10th KGS computer-Go tournament on the 9×9 board.[^s1] MCTS then transformed computer Go, where good static evaluation had been hard to write.[^s2]

## Why chess resisted it

For decades MCTS did poorly in chess. The survey notes it was less successful there than in Go and cites work showing that UCT struggles in games full of "trap states", positions that lose within a few moves, where iterative-deepening minimax does relatively well; such traps are common in chess and rarer in Go.[^s2] DeepMind's AlphaZero paper likewise records that earlier MCTS chess programs were much weaker than alpha-beta programs, which had led the field for at least four decades.[^s4]

## The AlphaZero version

AlphaZero kept the tree but dropped random playouts. A neural network takes a position and returns move probabilities and a value estimate; each simulation descends the tree preferring moves with a low visit count, a high prior probability and a high average value, and the network's value scores the leaf.[^s4] Training games used 800 simulations per move, and the move is chosen from the root visit counts.[^s4] In its matches AlphaZero searched about 80 thousand positions per second against roughly 70 million for Stockfish, compensating with far more selective search.[^s4] The authors argue that averaging over a large subtree tends to cancel the network's spurious errors, whereas alpha-beta's explicit minimax carries the largest error up to the root.[^s4] The open-source Leela Chess Zero project follows this approach: its documentation describes its search as mainly MCTS with PUCT, guided by a network with policy and value (win/draw/loss) heads.[^s5]

## Example: a shallow trap

In the diagram (Black: Kg8, Qb7, pawns f7, g7, h7; White: Kg1, Rd1, pawns b2, f2, g2, h2), Black to move can win a pawn with 1...Qxb2??, but 2.Rd8# is mate on the back rank. A plain-playout MCTS samples White's replies more or less at random, so after 1...Qxb2 most playouts do not find 2.Rd8 and the capture can look attractive until enough visits accumulate there. A two-ply minimax search refutes it at once. This is the kind of trap state the survey identifies as hard for UCT.[^s2] A policy network that rates checks and mates highly largely removes the problem, which is one reason AlphaZero-style MCTS works in chess where earlier versions did not.[^s4]

## Connections

MCTS is a branch of **game-tree search** and is usually contrasted with **minimax** and **alpha-beta pruning**: those back up exact maxima and minima over a depth-limited tree, while MCTS backs up averages over an uneven one.[^s2][^s4] Modern chess versions depend on a learned **evaluation function** (the value head) rather than random playouts, and the approach is used by **Leela Chess Zero**.[^s4][^s5] Its name and first tree-based formulation come from **Rémi Coulom**.[^s1][^s2] Because it has no fixed depth, it does not suffer the classical **horizon effect** in the same form, though shallow traps are its own characteristic weakness.[^s2]

## Sources
[^s1]: R. Coulom, "Efficient Selectivity and Backup Operators in Monte-Carlo Tree Search", Computers and Games 2006. https://remi-coulom.fr/CG2006 (accessed 2026-11-08)
[^s2]: C. Browne et al., "A Survey of Monte Carlo Tree Search Methods", *IEEE Transactions on Computational Intelligence and AI in Games* 4(1), March 2012. https://turing.iimas.unam.mx/~luis/cursos/IA2022-1/lecturas/SurveyMCTS.pdf (accessed 2026-11-08)
[^s3]: L. Kocsis and C. Szepesvári, "Bandit Based Monte-Carlo Planning", ECML 2006, pp. 282–293; University of Alberta PapersDB. https://papersdb.cs.ualberta.ca/~papersdb/view_publication.php?pub_id=633 (accessed 2026-11-08)
[^s4]: D. Silver et al., "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm", arXiv:1712.01815, December 2017. https://arxiv.org/pdf/1712.01815 (accessed 2026-11-08)
[^s5]: Leela Chess Zero, "Lc0 developer overview". https://lczero.org/dev/overview (accessed 2026-11-08)
