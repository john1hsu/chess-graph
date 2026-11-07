---
id: kt:evaluation-function
type: Algorithm
title: Evaluation function
aliases: [Static evaluation, Static evaluation function, Position evaluation, Positional evaluation function, Eval function, Heuristic evaluation function]
domain: computer-chess
summary: >-
  The part of a chess program that assigns a numerical score to a position without searching further,
  estimating how good it is for one side; a search such as minimax backs these frontier scores up to
  choose a move.
fen: "3r2k1/ppp2ppp/8/8/8/2P5/P1P2PPP/3R2K1 w - - 0 1"
status: current
volatile: true
verified: 2026-11-07
broader: [kt:game-tree-search]
related: [kt:nnue, kt:quiescence-search, kt:alphazero]
relations:
  - {predicate: enables, object: kt:minimax}
  - {predicate: enables, object: kt:alpha-beta-pruning}
  - {predicate: influencedBy, object: kt:claude-shannon}
sources:
  - id: s1
    title: "Programming a Computer for Playing Chess (Philosophical Magazine, 1950), full text"
    publisher: Claude E. Shannon, reproduced by Fermat's Library
    url: https://www.fermatslibrary.com/s/programming-a-computer-for-playing-chess
    type: primary-record
    accessed: 2026-11-07
  - id: s2
    title: "Deep Blue (Artificial Intelligence 134, 2002)"
    publisher: M. Campbell, A. J. Hoane Jr., F. Hsu (copy hosted by Northern Arizona University)
    url: https://www.cefns.nau.edu/~edo/Classes/CS470-570_WWW/Readings/Campbell2002.pdf
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s3
    title: "Introducing NNUE Evaluation"
    publisher: The Stockfish developers (stockfishchess.org)
    url: https://stockfishchess.org/blog/2020/introducing-nnue-evaluation/
    type: official-project
    accessed: 2026-11-07
  - id: s4
    title: "Stockfish 16.1"
    publisher: The Stockfish developers (stockfishchess.org)
    url: https://stockfishchess.org/blog/2024/stockfish-16-1/
    type: official-project
    accessed: 2026-11-07
  - id: s5
    title: "A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play (Science 362, 2018)"
    publisher: D. Silver et al., UCL Discovery repository record
    url: https://discovery.ucl.ac.uk/id/eprint/10069050/
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s6
    title: "CS221 Games module: Evaluation functions (slides)"
    publisher: Stanford University
    url: https://stanford-cs221.github.io/autumn2023-extra/modules/games/evaluation-functions.pdf
    type: academic
    accessed: 2026-11-07
  - id: s7
    title: "src/evaluate.cpp (Stockfish source code, master branch)"
    publisher: The Stockfish developers (official GitHub repository)
    url: https://github.com/official-stockfish/Stockfish/blob/master/src/evaluate.cpp
    type: official-project
    accessed: 2026-11-07
created: 2026-11-07
---

# Evaluation function

An evaluation function is a chess program's judgement of a position at a glance. When a search stops at its depth limit it cannot know the true game-theoretic value of the position it has reached, so it substitutes an estimate; Stanford's CS221 course describes this estimate as a possibly very weak approximation of the minimax value, playing the same role as a heuristic in ordinary search problems.[^s6] Unlike the heuristics used with A*, such an estimate comes with no guarantee about how large its error may be.[^s6] Engines report the result in pawn units or centipawns, from White's point of view, which is the number club players see beside an engine line.[^s7]

## Shannon's blueprint

Claude Shannon's 1950 paper gave the first concrete recipe. His f(P) counts material with weights of 200 for the king, 9 for the queen, 5 for a rook, 3 for a bishop or knight and 1 for a pawn, subtracts half a pawn for each doubled, backward or isolated pawn, and adds a tenth of a pawn per legal move of mobility, with each term taken as the difference between White and Black; he marked the formula as open-ended and called the small coefficients rough estimates.[^s1] His appendix lists further factors a stronger function should weigh: control of the centre, passed pawns, weak pawns near the king, pawns fixed on the bishop's colour, advanced protected knights, rooks on open files and the seventh rank, pieces tied to defensive duties, and pins.[^s1] Shannon also warned that the score is meaningless in the middle of a combination or exchange sequence, and that the opening and endgame need different principles from the middlegame.[^s1]

Textbook versions still follow this shape: a weighted sum of features such as material, mobility, king safety and centre control, where the weights encode domain knowledge.[^s6]

## Handcrafted evaluation at scale

Deep Blue, the machine of the 1997 match against Garry Kasparov, shows how far the handcrafted approach went. Its custom chess chip recognised roughly 8,000 patterns, with 8,150 adjustable parameters, up from about 6,400 features in the previous chip.[^s2] A fast evaluation computed the easy terms, chiefly piece values adjusted by square, in a single clock cycle; a slower pass scanned the board file by file for square control, pins, x-rays, king safety, pawn structure, outposts and rooks on the seventh.[^s2] Some weights were scaled by the material left on the board, so king-safety terms faded towards the endgame, which nudged the machine to trade pieces when its own king was the more exposed.[^s2] The designers called the size of the feature set an embarrassment of riches, because tuning thousands of interacting weights was hard; most were set by hand, with automated tools used to find insensitive features and to show that pawn-shelter values had been set too low.[^s2]

## Learned evaluation

Two developments moved evaluation from hand-tuned features to trained networks. AlphaZero (2018) replaced the handcrafted features and expert-tuned weights of conventional programs with a deep network whose value output estimates the expected game result from −1 to +1, learned purely from self-play.[^s5] It examined about 60,000 positions per second against Stockfish's roughly 60 million, relying on the network to focus its search.[^s5]

Stockfish took a different route. In August 2020 its developers introduced NNUE, an "efficiently updatable" network ported from shogi, which runs fast on ordinary CPUs because a typical move changes only part of its input; it was trained on millions of positions evaluated by moderate-depth search and measured at more than 80 Elo stronger than the classical evaluation in the project's tests.[^s3] The classical and neural evaluations coexisted until Stockfish 16.1 (February 2024), which removed the handcrafted evaluation entirely and added a second, smaller network for positions that are easily decided.[^s4] As of November 2026 this makes the strongest alpha-beta engines and the AlphaZero family alike dependent on learned evaluation.

## Example

In the diagram position (White: Kg1, Rd1, pawns a2, c2, c3, f2, g2, h2; Black: Kg8, Rd8, pawns a7, b7, c7, f7, g7, h7) material is level, so Shannon's material terms cancel. His pawn terms then count against White, whose c-pawns are doubled and, with no b- or d-pawn beside them, isolated, as is the a-pawn; Black's queenside majority is intact.[^s1] Counting legal moves gives White 23 and, with Black to move, Black 26, so the mobility term is 0.1 × (23 − 26) = −0.3. A Shannon-style function therefore scores the position as a small edge for Black, which matches a club player's judgement that White's broken pawns are a lasting weakness.

## Pitfalls

An evaluation is only as reliable as the position it is applied to. Shannon's own answer to tactical noise was to extend forcing lines until the position became quiet before scoring it, the idea behind quiescence search.[^s1] Deep Blue's team found that bolting a missing concept onto a fixed evaluation in software (opposite-coloured bishops, in Deep Thought 2) slowed the program and caused search anomalies.[^s2] Players reading engine output should also remember that Stockfish deliberately damps its score as the fifty-move counter rises and keeps static scores outside the range reserved for tablebase wins and losses, so the number is a practical guide rather than a proof.[^s7]

## Connections

The evaluation function is what makes depth-limited **minimax** and **alpha-beta pruning** usable: they supply the look-ahead, it supplies the values at the frontier of the **game-tree search**.[^s6] Its design goes back to **Claude Shannon**, and it is normally applied only after **quiescence search** has resolved captures and checks.[^s1] Modern engines use learned versions: **NNUE** in Stockfish and the value network of **AlphaZero**.[^s3][^s5]

## Sources
[^s1]: C. E. Shannon, "Programming a Computer for Playing Chess", *Philosophical Magazine* 41 (1950); full text at Fermat's Library. https://www.fermatslibrary.com/s/programming-a-computer-for-playing-chess (accessed 2026-11-07)
[^s2]: M. Campbell, A. J. Hoane Jr. and F. Hsu, "Deep Blue", *Artificial Intelligence* 134 (2002). https://www.cefns.nau.edu/~edo/Classes/CS470-570_WWW/Readings/Campbell2002.pdf (accessed 2026-11-07)
[^s3]: Stockfish developers, "Introducing NNUE Evaluation", 7 August 2020. https://stockfishchess.org/blog/2020/introducing-nnue-evaluation/ (accessed 2026-11-07)
[^s4]: Stockfish developers, "Stockfish 16.1", 24 February 2024. https://stockfishchess.org/blog/2024/stockfish-16-1/ (accessed 2026-11-07)
[^s5]: D. Silver et al., "A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play", *Science* 362 (2018) 1140–1144, doi:10.1126/science.aar6404. https://discovery.ucl.ac.uk/id/eprint/10069050/ (accessed 2026-11-07)
[^s6]: Stanford University CS221, "Evaluation functions" (Games module slides, Autumn 2023). https://stanford-cs221.github.io/autumn2023-extra/modules/games/evaluation-functions.pdf (accessed 2026-11-07)
[^s7]: Stockfish developers, `src/evaluate.cpp`, official Stockfish repository on GitHub. https://github.com/official-stockfish/Stockfish/blob/master/src/evaluate.cpp (accessed 2026-11-07)
