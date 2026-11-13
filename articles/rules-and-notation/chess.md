---
id: kt:chess
type: Concept
title: Chess
aliases: [Game of chess, Western chess, International chess, Orthodox chess, The royal game]
domain: rules-and-notation
summary: >-
  A two-player strategy board game played on an 8×8 board with sixteen pieces per side, in which
  White moves first and each player tries to checkmate the opponent's king; a game with no chance
  element and perfect information, governed internationally by FIDE's Laws of Chess.
fen: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
status: current
volatile: true
verified: 2026-11-13
broader: [kt:abstract-strategy-game]
related: [kt:history-of-chess, kt:chess-variants, kt:chess-strategy, kt:chess-tactics]
relations:
  - {predicate: governedBy, object: kt:fide-laws-of-chess}
  - {predicate: sanctionedBy, object: kt:fide}
  - {predicate: hasPart, object: kt:checkmate}
  - {predicate: hasPart, object: kt:chess-endgame}
sources:
  - id: s1
    title: "FIDE Laws of Chess (full text, in force from 1 January 2023)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/
    type: governing-body
    accessed: 2026-11-13
  - id: s2
    title: "Article 1: The Nature and Objectives of the Game of Chess"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/article1
    type: governing-body
    accessed: 2026-11-13
  - id: s3
    title: "Chess"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/chess
    type: reference
    accessed: 2026-11-13
  - id: s4
    title: "Programming a Computer for Playing Chess (Philosophical Magazine, 1950), full text"
    publisher: Claude E. Shannon, reproduced by Fermat's Library
    url: https://fermatslibrary.com/s/programming-a-computer-for-playing-chess
    type: primary-record
    accessed: 2026-11-13
  - id: s5
    title: "Chess joins the International World Games Association"
    publisher: FIDE
    url: https://www.fide.com/chess-joins-the-international-world-games-association/
    type: governing-body
    accessed: 2026-11-13
created: 2026-11-13
---

# Chess

Chess is a contest between two players who move pieces on a square board, the chessboard; the player with the light pieces (White) moves first and the two sides then alternate.[^s2] Encyclopaedia Britannica calls it one of the oldest and most popular board games, traces it to India around the 6th century AD, and notes that its rules and the design of the set reached their modern standard in the early 19th century.[^s3] This node is the root of the graph: openings, strategy, tactics, endgames, rules, players and computer chess all describe parts of this one game.

## Board, pieces and moves

The board is an 8×8 grid of 64 alternately light and dark squares, placed so that the corner square nearest each player's right hand is light.[^s1] Each side starts with sixteen pieces: a king, a queen, two rooks, two bishops, two knights and eight pawns, set up as in the key position above.[^s1][^s3] The eight vertical columns are files a–h and the horizontal rows are ranks 1–8, which gives every square a name such as e4 or g8 in algebraic notation.[^s3]

Under Article 3 of the Laws, bishops move along diagonals, rooks along ranks and files, and the queen combines both; none of them may jump over other pieces.[^s1] The knight jumps to one of the nearest squares not on its own rank, file or diagonal, and pawns move straight forward (two squares on their first move if both squares are empty) but capture diagonally.[^s1] Three special rules complete the movement: castling, en passant and pawn promotion, in which a pawn reaching the far rank must become a queen, rook, bishop or knight of its own colour.[^s1]

## Object and results

Each player aims to attack the opponent's king so that the opponent has no legal move to escape; this is checkmate, and the player who achieves it wins.[^s2] A move may never leave one's own king attacked.[^s2] If neither side can possibly give checkmate, the game is drawn.[^s2] The Laws also list resignation, stalemate (no legal move while not in check), a dead position and agreement between the players as ways a game ends.[^s1] In competition a win scores one point, a draw a half and a loss nothing; draws can also arise from threefold repetition or fifty moves without a capture or pawn move.[^s3]

Britannica gives the familiar rough piece values, with the pawn as 1: knight and bishop 3, rook 5, queen 9. It stresses that these shift with pawn structure and tactics, and that the aim is checkmate, not material.[^s3] Treating the table as a law rather than a guide is a classic club-player mistake.

## A game of pure calculation

In his 1950 paper that founded computer chess, Claude Shannon observed that chess has no chance element beyond deciding who moves first, and that both players always have perfect information about the position.[^s4] It follows that every position is, in principle, a forced win for White, a forced win for Black, or a draw, though no practical method of finding out which is known.[^s4] Shannon estimated about 30 legal moves in a typical position and about 40 moves in a typical game, giving roughly 10^120 variations from the start and around 10^43 possible positions, far too many to tabulate.[^s4] That gap between a theoretically solvable game and a practically unsolvable one is why judgement, pattern knowledge and calculation all matter in human play.

## Organized play

Over-the-board competition follows the FIDE Laws of Chess, whose current text took effect on 1 January 2023; beyond the basic rules they cover the touch-move rule, the chess clock, recording moves and penalties.[^s1][^s3] FIDE, the International Chess Federation, administers titles, ratings and the world championship. On 25 April 2026 the International World Games Association admitted FIDE as a member, adding chess to the family of sports in the World Games movement, which is recognised by the International Olympic Committee.[^s5]

## Connections

**History of chess** narrates how the game developed from chaturanga and shatranj into its modern form.[^s3] The rules of play are set out in the **FIDE Laws of Chess** and maintained by **FIDE**.[^s1][^s5] **Checkmate** is the game's objective, while **chess strategy**, **chess tactics** and the **chess endgame** cover how it is played in practice.[^s2][^s3] **Chess variants** change the board, pieces or rules of this game, and chess is one example of an **abstract strategy game** of perfect information with no chance element.[^s4]

## Sources

[^s1]: FIDE Rules Commission, "FIDE Laws of Chess" (full text, in force from 1 January 2023). https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/ (accessed 2026-11-13)
[^s2]: FIDE Rules Commission, "Article 1: The Nature and Objectives of the Game of Chess". https://rcc.fide.com/article1 (accessed 2026-11-13)
[^s3]: Encyclopaedia Britannica, "Chess". https://www.britannica.com/topic/chess (accessed 2026-11-13)
[^s4]: C. E. Shannon, "Programming a Computer for Playing Chess", *Philosophical Magazine* Ser. 7, 41 (314), March 1950; full text at Fermat's Library. https://fermatslibrary.com/s/programming-a-computer-for-playing-chess (accessed 2026-11-13)
[^s5]: FIDE, "Chess joins the International World Games Association" (April 2026). https://www.fide.com/chess-joins-the-international-world-games-association/ (accessed 2026-11-13)
