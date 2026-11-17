---
id: kt:descriptive-notation
type: Notation
title: Descriptive notation
aliases: [English notation, English descriptive notation, Descriptive chess notation]
domain: rules-and-notation
summary: >-
  The older English-language system for recording chess moves, in which each file is named after the
  piece that starts on it (king's bishop file, queen's knight file) and ranks are counted from the
  moving player's own side, so 1.P-K4 means a king's-pawn advance for either colour.
status: historical
volatile: true
verified: 2026-11-17
broader: [kt:chess-notation]
related: [kt:algebraic-notation, kt:portable-game-notation, kt:fide-laws-of-chess, kt:ruy-lopez, kt:edward-lasker]
relations:
  - {predicate: replacedBy, object: kt:algebraic-notation}
  - {predicate: contrastsWith, object: kt:algebraic-notation}
sources:
  - id: s1
    title: "Chess Notation"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/notation.html
    type: reference
    accessed: 2026-11-17
  - id: s2
    title: "chess (Britannica School / Britannica Kids, students' encyclopedia)"
    publisher: Encyclopaedia Britannica
    url: https://kids.britannica.com/students/article/chess/273625
    type: reference
    accessed: 2026-11-17
  - id: s3
    title: "Appendix C. Algebraic Notation (FIDE Laws of Chess)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/?p=880
    type: governing-body
    accessed: 2026-11-17
  - id: s4
    title: "Article 8: The recording of the moves (FIDE Laws of Chess)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/?p=866
    type: governing-body
    accessed: 2026-11-17
  - id: s5
    title: "How to Read Descriptive Notation (Tom Shupe, updated 3 September 2024)"
    publisher: Chess.com
    url: https://www.chess.com/blog/chess_dot_tom/how-to-read-descriptive-notation
    type: publication
    accessed: 2026-11-17
created: 2026-11-17
---

# Descriptive notation

Descriptive notation, often called English notation, is the system in which most English-language chess books and magazines recorded games for well over a century before algebraic notation took over. Its defining feature is that squares are described rather than given coordinates: each file takes its name from the piece that stands on it at the start of the game, and each rank is numbered from the side of the player making the move.[^s2] A move such as P-KN4 therefore reads "pawn to king's knight four", the move an algebraic score writes as g4.[^s2] Britannica notes that standard (algebraic) notation has nearly replaced the descriptive form in computer programs and in games and matches.[^s2] Anyone who reads older classics, however, still meets it constantly, so a serious player benefits from being able to translate it.[^s5]

## How squares are named

The files are named, from White's left, queen's rook, queen's knight, queen's bishop, queen, king, king's bishop, king's knight and king's rook, abbreviated QR, QN (or QKt), QB, Q, K, KB, KN (or KKt) and KR.[^s2][^s5] Ranks run from 1 to 8 counting outward from each player's own back rank.[^s2] For White the rank numbers coincide with algebraic ones, but for Black they are reversed, so the square White calls K4 (e4) is the square Black calls K5, and Black's K4 is e5.[^s5] Edward Winter points out the obvious consequence: every square has two names, one for each side.[^s1]

## Writing a move

Unlike algebraic notation, the pawn gets its own letter, P, and the other pieces use K, Q, R, B and either Kt or N for the knight.[^s5] A move is the piece letter, a dash and the destination square (N-KB3), and a capture names the captured unit instead of a square, as in PxP or BxN.[^s1][^s5] Check was written "ch" (later also +), castling O-O or O-O-O, en passant "e.p.", and promotion by adding the new piece, for example P-K8(Q).[^s1][^s5] Winter records that English writers used Kt for the knight for a long time: N was proposed in the British Chess Magazine in October 1890, but the BCM itself adopted it only in the 1970s, after Chess Review and CHESS had switched in the 1940s and 1950s.[^s1]

## A short example

The opening moves of the Ruy Lopez show the system at work. In descriptive notation they read 1.P-K4 P-K4 2.N-KB3 N-QB3 3.B-N5 P-QR3 4.B-R4 N-B3 5.O-O, which is 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O in algebraic. The symmetry is visible at once: both sides' first moves are written P-K4, although one pawn goes to e4 and the other to e5.[^s5] Note also how the descriptive score drops the K or Q prefix (B-N5, N-B3) when only one piece of that kind can reach a square of that name, a habit that saves ink but invites errors.[^s1]

## Pitfalls when reading old books

The system's weakness is ambiguity. Because squares are named relative to each player, a bare Q-B3 could mean the queen going to either bishop's third square, and a capture such as KtxP leaves it unclear which pawn was taken when several are attacked; Winter suggests that writers name the pawn's square in such cases.[^s1] He also cites a nineteenth-century game score whose recorded knight move fits two different knights.[^s1] Printers varied too: some used dashes (Q-KN5) and some did not (QKN5), and some old American publications left off the digit 1 for back-rank moves (R-Q for a rook to the queen's file on the first rank).[^s1] When translating, set up the position on a board and check that each move is legal for the side to move, rather than translating square by square in your head.

## Decline

Algebraic notation was long resisted in the English-speaking world. Winter quotes the Chess Amateur's 1915 endorsement of the English method over the German algebraic one, notes that Edward Lasker's use of algebraic in a 1918 American book was attacked in the American Chess Bulletin in 1924, and shows that the BCM was still debating the two systems in 1941.[^s1] Chess Life & Review printed Bent Larsen's annotations in algebraic in August 1979, and the BCM later moved to figurine algebraic.[^s1] Today FIDE recognises only the algebraic system for its tournaments and matches, and a scoresheet kept in another system cannot be used as evidence where a scoresheet normally would; arbiters are told to inform players who use one.[^s3] As of November 2026, Article 8 of the FIDE Laws requires moves to be recorded in algebraic notation, on paper or on a certified electronic scoresheet.[^s4]

## Connections

Descriptive notation is one form of **chess notation** and was **replaced by** **algebraic notation**, with which it is constantly compared because their square names coincide only for White.[^s2][^s5] The **FIDE Laws of Chess** now exclude it from rated FIDE play through Appendix C and Article 8.[^s3][^s4] Computer formats such as **Portable Game Notation** build on algebraic, not descriptive, move text. **Edward Lasker** is linked to the long English-language argument over switching systems, and the **Ruy Lopez** serves above as a worked translation.[^s1]

## Sources

[^s1]: Edward Winter, Chess Notes, "Chess Notation". https://chesshistory.com/winter/extra/notation.html (accessed 2026-11-17)
[^s2]: Encyclopaedia Britannica (Britannica School), "chess". https://kids.britannica.com/students/article/chess/273625 (accessed 2026-11-17)
[^s3]: FIDE Rules Commission, "Appendix C. Algebraic Notation" (FIDE Laws of Chess). https://rcc.fide.com/?p=880 (accessed 2026-11-17)
[^s4]: FIDE Rules Commission, "Article 8: The recording of the moves" (FIDE Laws of Chess). https://rcc.fide.com/?p=866 (accessed 2026-11-17)
[^s5]: Tom Shupe, "How to Read Descriptive Notation", Chess.com, updated 3 September 2024. https://www.chess.com/blog/chess_dot_tom/how-to-read-descriptive-notation (accessed 2026-11-17)
