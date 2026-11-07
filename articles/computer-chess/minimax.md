---
id: kt:minimax
type: Algorithm
title: Minimax
aliases: [Minimax search, Minimax algorithm, Minimaxing, Mini-max]
domain: computer-chess
summary: >-
  The basic decision rule of game-tree search: each side is assumed to choose the move best for
  itself, so values are backed up from the leaves by taking the maximum at the searching side's
  turns and the minimum at the opponent's, and the move leading to the best backed-up value is played.
fen: "6k1/5ppp/4p3/3r4/8/8/5PPP/3Q2K1 w - - 0 1"
status: current
volatile: false
verified: 2026-11-07
broader: [kt:game-tree-search]
related: [kt:negamax, kt:evaluation-function, kt:horizon-effect, kt:quiescence-search, kt:claude-shannon]
relations:
  - {predicate: enables, object: kt:alpha-beta-pruning}
  - {predicate: dependsOn, object: kt:evaluation-function}
  - {predicate: contrastsWith, object: kt:monte-carlo-tree-search}
  - {predicate: influencedBy, object: kt:john-von-neumann}
sources:
  - id: s1
    title: "Programming a Computer for Playing Chess (Philosophical Magazine, 1950), full text"
    publisher: Claude E. Shannon, reproduced by Fermat's Library
    url: https://fermatslibrary.com/s/programming-a-computer-for-playing-chess
    type: primary-record
    accessed: 2026-11-07
  - id: s2
    title: "Early Theorists"
    publisher: Computer History Museum (Mastering the Game exhibit)
    url: https://www.computerhistory.org/chess/early-theorists/
    type: archive
    accessed: 2026-11-07
  - id: s3
    title: "CS 440/ECE 448 Lecture notes: Games 2"
    publisher: University of Illinois Urbana-Champaign (Margaret Fleck)
    url: https://courses.grainger.illinois.edu/cs440/fa2021/lectures/games2.html
    type: academic
    accessed: 2026-11-07
  - id: s4
    title: "ICS 180A: Strategy and board game programming, lecture of 17 April 1997"
    publisher: University of California, Irvine (David Eppstein)
    url: https://ics.uci.edu/~eppstein/180a/970417.html
    type: academic
    accessed: 2026-11-07
  - id: s5
    title: "Mini-max theorem"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/mini-max-theorem
    type: reference
    accessed: 2026-11-07
created: 2026-11-07
---

# Minimax

Minimax is the rule by which a chess program turns look-ahead into a move. It applies to two-player, deterministic, zero-sum games such as chess and assumes the opponent plays as well as possible.[^s3] Positions where the program is to move are "max" nodes, where it takes the highest value among the children; positions where the opponent moves are "min" nodes, where it takes the lowest; values are passed up the tree level by level until the root, whose value is what the program can guarantee and whose best child is the move to play.[^s3] Any game can be described as such a tree, and solving the whole tree would give perfect play, but real game trees are far too large for that.[^s4]

## Origins

The mathematical idea comes from game theory. Encyclopaedia Britannica credits John von Neumann with proving the minimax theorem for finite two-player zero-sum games during his European career in the 1920s, building on earlier work by Émile Borel.[^s5] Its application to chess programs was laid out by Claude Shannon in "Programming a Computer for Playing Chess" (*Philosophical Magazine*, 1950). Shannon assumed that Black would answer each move so as to minimise his evaluation of the position, and that White would choose the move maximising that minimum; he wrote out the max-min-max-min formula for a two-move look-ahead and stressed that the order of maximising and minimising matters.[^s1] The Computer History Museum places Shannon's work about two years after Alan Turing's 1947 paper chess program, which Turing executed by hand.[^s2]

## Depth limits and the evaluation function

A complete minimax search of chess is impossible. Shannon estimated about 30 legal moves per position, roughly 10^120 variations from the starting position, and more than 10^90 years to calculate the first move that way.[^s1] Programs therefore stop at a chosen depth and treat the frontier positions as if they were leaves, scoring them with an evaluation function and backing those estimates up by minimax.[^s3] An exact evaluation would need only three values (win, draw, loss); a practical one returns a range of numbers because it is only an approximation.[^s1][^s4] Shannon's own f(P) combined material with terms for pawn structure and mobility, and Turing's proposal used material counts of roughly 1 for a pawn, 3 for a knight, 5 for a rook and 9 for a queen.[^s1][^s3] Modern evaluations add many positional features, or replace hand-made features with a neural network.[^s3]

The cost grows exponentially. Work is roughly proportional to b^d for branching factor b and depth d, so doubling the speed of the computer adds only a little depth; with about 30 moves per position, chess allows less depth than checkers.[^s4] Shannon's estimate was that a fixed-depth searcher looking three moves deep would need around 10^9 evaluations, more than 16 minutes per move even at one microsecond each.[^s1]

## Type A and Type B

Shannon described two ways to organise the search. A Type A program examines every variation to a fixed depth and minimaxes the results; he judged such a machine both slow and weak.[^s1] A Type B program instead follows forcing lines such as checks and captures as far as needed and screens out pointless moves, so that evaluation is applied only in relatively quiet positions.[^s1] The Computer History Museum notes that almost all two-player game software still uses one of these two strategies.[^s2]

## Example

In the position above (White: Kg1, Qd1, pawns f2, g2, h2; Black: Kg8, Rd5, pawns e6, f7, g7, h7), White to move can play 1.Qxd5. A one-ply search with Turing-style material values sees only that White has won a rook and scores the move about +5.[^s3] A two-ply minimax search also looks at Black's replies: at the min node after 1.Qxd5, the reply 1...exd5 leaves White a queen for a rook down, so the backed-up value of 1.Qxd5 is about −4, and the program rejects it. This is the core of minimax for a club player: a move is only as good as the opponent's best answer to it.

## Pitfalls

Because a depth-limited search trusts the evaluation at its frontier, something decisive just beyond the cutoff can be misjudged; this horizon effect cannot be removed entirely, only reduced with quiescence search, singular extensions and similar devices.[^s3] Shannon already insisted that the evaluation be applied only in relatively quiescent positions.[^s1] Minimax also assumes the opponent always finds the best reply, so it gives no credit to a move that merely sets a trap a human might fall into.[^s3]

## Implementation notes

Engines rarely code separate max and min routines. Negating values at alternate levels lets one routine always maximise (the negamax formulation), and a depth-first recursive search keeps only the current path in memory.[^s4] The line the program expects both sides to follow is the principal variation, and the program plays its first move; iterative deepening repeats the search at increasing depths until time runs out.[^s4]

## Connections

Minimax is the foundation of **game-tree search**, and **alpha-beta pruning** is the refinement that returns the same value while skipping branches that cannot matter, roughly doubling the reachable depth in good cases.[^s4] It depends on an **evaluation function** at its frontier, suffers from the **horizon effect**, and is usually paired with **quiescence search**; its usual code form is **negamax**.[^s3][^s4] Its theoretical root is **John von Neumann**'s minimax theorem, and its application to chess goes back to **Claude Shannon**.[^s5][^s1] It is often set against **Monte Carlo tree search**, a different family of game-tree search methods.

## Sources
[^s1]: C. E. Shannon, "Programming a Computer for Playing Chess", *Philosophical Magazine* 41 (1950); full text at Fermat's Library. https://fermatslibrary.com/s/programming-a-computer-for-playing-chess (accessed 2026-11-07)
[^s2]: Computer History Museum, "Early Theorists", Mastering the Game. https://www.computerhistory.org/chess/early-theorists/ (accessed 2026-11-07)
[^s3]: M. Fleck, CS 440/ECE 448 lecture notes "Games 2", University of Illinois Urbana-Champaign, Fall 2021. https://courses.grainger.illinois.edu/cs440/fa2021/lectures/games2.html (accessed 2026-11-07)
[^s4]: D. Eppstein, ICS 180A lecture notes, 17 April 1997, University of California, Irvine. https://ics.uci.edu/~eppstein/180a/970417.html (accessed 2026-11-07)
[^s5]: Encyclopaedia Britannica, "Mini-max theorem". https://www.britannica.com/topic/mini-max-theorem (accessed 2026-11-07)
