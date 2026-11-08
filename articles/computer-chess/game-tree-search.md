---
id: kt:game-tree-search
type: Algorithm
title: Game-tree search
aliases: [Game tree search, Game tree, Adversarial search, Search tree, Tree search in games]
domain: computer-chess
summary: >-
  The family of methods by which a program chooses a move by exploring the tree of positions
  reachable from the current one, where nodes are positions, edges are moves and each level is
  a ply; in chess the tree is far too large to explore fully, so searches are cut off and guided.
fen: "rnbqkb1r/pppppppp/5n2/8/2P5/5N2/PP1PPPPP/RNBQKB1R b KQkq - 0 2"
status: current
volatile: false
verified: 2026-11-08
broader: [kt:computer-chess]
related: [kt:minimax, kt:alpha-beta-pruning, kt:evaluation-function, kt:monte-carlo-tree-search, kt:solving-chess]
relations:
  - {predicate: hasPart, object: kt:iterative-deepening}
  - {predicate: usesTechnique, object: kt:transposition-table}
  - {predicate: hasPart, object: kt:proof-number-search}
  - {predicate: influencedBy, object: kt:claude-shannon}
sources:
  - id: s1
    title: "ICS 180A: Strategy and board game programming, lecture of 17 April 1997"
    publisher: University of California, Irvine (David Eppstein)
    url: https://ics.uci.edu/~eppstein/180a/970417.html
    type: academic
    accessed: 2026-11-08
  - id: s2
    title: "ES.268 The Mathematics in Toys and Games, Session 4: AI (lecture notes)"
    publisher: MIT OpenCourseWare
    url: https://ocw.mit.edu/courses/es-268-the-mathematics-in-toys-and-games-spring-2010/7e2bc0702dcc4718b597f3a98592aa09_MITES_268S10_Ses4_AI.pdf
    type: academic
    accessed: 2026-11-08
  - id: s3
    title: "6.034 Artificial Intelligence, Fall 2010, Lecture 6: Search: Games, Minimax, and Alpha-Beta (transcript)"
    publisher: MIT OpenCourseWare (Patrick Winston)
    url: https://live.ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/7524b662aa86938e45c10c74d3a1ad41_STjW3eH0Cik.pdf
    type: academic
    accessed: 2026-11-08
  - id: s4
    title: "Checkers Is Solved (Science 317, 2007)"
    publisher: J. Schaeffer et al., hosted by McGill University
    url: https://www.cs.mcgill.ca/~dprecup/courses/AI/Materials/checkers_is_solved.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s5
    title: "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm"
    publisher: D. Silver et al. (DeepMind), arXiv
    url: https://arxiv.org/pdf/1712.01815
    type: peer-reviewed
    accessed: 2026-11-08
created: 2026-11-08
---

# Game-tree search

A game tree is a rooted tree in which each node is a position and the children of a node are the positions reachable from it in one move; the leaves are finished games, and levels alternate between the two players.[^s1] One level of the tree is a *ply*, a single move by one side.[^s2] Game-tree search is the umbrella term for the ways a program explores such a tree to pick a move, and nearly every chess engine, from the first paper designs to modern neural-network programs, is built around one.[^s1][^s5]

## Why the tree cannot be searched completely

The size of a game tree is governed by the branching factor *b*, the number of moves available in a typical position, and the depth *d*; a uniform tree searched to depth *d* has about *b*^*d* nodes.[^s1][^s2] David Eppstein's course notes put chess at about 30 moves per position, against as few as three for some checkers positions and hundreds for Go.[^s1] Patrick Winston's MIT lecture, citing Claude Shannon, uses the figure of about 10^120 leaf nodes for the full chess tree and shows that even if every atom in the universe evaluated a position every nanosecond since the Big Bang, the job would still not be done.[^s3] Exhaustive search is therefore out of the question, and every practical program searches only a small, carefully chosen part of the tree.[^s1][^s3]

The growth is easy to see from the opening position. Counting with the repository's move checker (python-chess), White has 20 legal first moves, there are 400 move sequences after one move by each side, 8,902 after three plies and 197,281 after four: roughly the multiplication by the branching factor at each ply that the *b*^*d* estimate predicts.[^s1]

## Trees and graphs

Strictly speaking, chess forms a graph rather than a tree, because the same position can be reached by different move orders. In the tree model such a position simply appears more than once.[^s1] The diagrammed position, for instance, arises from both 1.Nf3 Nf6 2.c4 and 1.c4 Nf6 2.Nf3. Programs exploit these repeats by hashing positions so that a result found once can be reused wherever the position recurs, which is the idea behind the transposition table.[^s1]

## Main families of search

**Depth-first minimax search.** The classical approach evaluates a node by recursively evaluating its children, storing only the current path, which is far more memory-efficient than building the tree level by level breadth-first.[^s1] The search stops at a fixed depth and scores the frontier with an evaluation function; alpha-beta pruning then skips subtrees that cannot change the result, cutting the effective branching factor towards its square root in the best case and roughly doubling the reachable depth.[^s1][^s3] Iterative (or progressive) deepening repeats the search one ply deeper each time, so the program always has a move ready when time runs out, at a cost close to that of the final iteration alone.[^s1][^s3] Winston describes Deep Blue as combining these elements with parallel hardware, an opening book, endgame knowledge and uneven tree growth that searched dynamic positions more deeply.[^s3] The AlphaZero paper describes Stockfish in the same terms: alpha-beta search with quiescence search at the leaves and many enhancements such as move ordering, pruning, extensions and reductions.[^s5]

**Monte Carlo tree search.** AlphaZero instead ran many simulated games from the root, choosing moves with a low visit count, a high prior probability from its neural network and a high average value, and finally played the most visited move.[^s5] Its authors report that in chess it examined about 80 thousand positions per second against Stockfish's 70 million, and that averaging values over a subtree, rather than taking the minimax value, tends to cancel out evaluation errors instead of passing the largest ones up the tree.[^s5]

**Proof-oriented search.** When the goal is to prove a result rather than pick a good move, programs use searches such as proof-number search, which labels nodes as wins or losses on an AND-OR tree instead of assigning numeric scores.[^s2] Schaeffer's team used a proof-number-based manager, alpha-beta solvers and endgame databases to show in 2007 that checkers is a draw with perfect play.[^s4]

## Limits and pitfalls

Because cost grows exponentially, a faster computer buys only a few extra plies.[^s1] Winston's rule of thumb is that a program looking about seven or eight plies ahead plays poorly, while one reaching fifteen or sixteen can beat a world champion.[^s3] Chess itself is far beyond being solved: Schaeffer and colleagues place its number of positions somewhere between 10^40 and 10^50, roughly the square of checkers' 5 × 10^20, and expect it to stay unsolved for a long time without new technology.[^s4] They distinguish games solved ultraweakly (result known), weakly (result and a strategy from the start known) and strongly (result known for every position).[^s4]

## Connections

Game-tree search is the parent concept of **minimax**, **alpha-beta pruning** and **Monte Carlo tree search**, and it depends on an **evaluation function** wherever the search is cut off.[^s1][^s5] **Iterative deepening** and the **transposition table** are standard parts of practical searches, and **proof-number search** is the proof-oriented branch used to solve games.[^s1][^s2][^s4] The question of **solving chess** is the limiting case of the whole subject, and **Claude Shannon**'s estimate of the tree's size framed it from the beginning.[^s3][^s4]

## Sources
[^s1]: D. Eppstein, ICS 180A lecture notes, 17 April 1997, University of California, Irvine. https://ics.uci.edu/~eppstein/180a/970417.html (accessed 2026-11-08)
[^s2]: MIT OpenCourseWare, ES.268 The Mathematics in Toys and Games (Spring 2010), Session 4 lecture notes on AI. https://ocw.mit.edu/courses/es-268-the-mathematics-in-toys-and-games-spring-2010/7e2bc0702dcc4718b597f3a98592aa09_MITES_268S10_Ses4_AI.pdf (accessed 2026-11-08)
[^s3]: P. Winston, MIT 6.034 Artificial Intelligence (Fall 2010), lecture "Search: Games, Minimax, and Alpha-Beta", transcript, MIT OpenCourseWare. https://live.ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/7524b662aa86938e45c10c74d3a1ad41_STjW3eH0Cik.pdf (accessed 2026-11-08)
[^s4]: J. Schaeffer et al., "Checkers Is Solved", *Science* 317 (2007), 1518–1522. https://www.cs.mcgill.ca/~dprecup/courses/AI/Materials/checkers_is_solved.pdf (accessed 2026-11-08)
[^s5]: D. Silver et al., "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm", arXiv:1712.01815 (2017). https://arxiv.org/pdf/1712.01815 (accessed 2026-11-08)
