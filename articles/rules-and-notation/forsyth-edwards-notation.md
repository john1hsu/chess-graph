---
id: kt:forsyth-edwards-notation
type: Notation
title: Forsyth–Edwards Notation
aliases: [FEN, Forsyth-Edwards Notation, Forsyth notation, FEN record, FEN string]
domain: rules-and-notation
summary: >-
  A one-line text format that records a complete chess position in six space-separated fields
  (piece placement, side to move, castling rights, en passant target, halfmove clock and move
  number); it extends David Forsyth's 1883 position notation and was standardised by Steven J.
  Edwards in the 1994 PGN specification.
fen: "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"
moves: "1.e4 c5 2.Nf3"
status: current
volatile: false
verified: 2026-11-09
broader: [kt:algebraic-notation]
related: [kt:portable-game-notation, kt:extended-position-description, kt:en-passant, kt:castling, kt:fifty-move-rule, kt:chess960]
relations:
  - {predicate: namedAfter, object: kt:david-forsyth}
  - {predicate: developedBy, object: kt:steven-j-edwards}
  - {predicate: partOf, object: kt:portable-game-notation}
sources:
  - id: s1
    title: "Standard: Portable Game Notation Specification and Implementation Guide (revised 1994-03-12), sections 9.7 and 16.1–16.2"
    publisher: Steven J. Edwards (coordinator), rec.games.chess; copy distributed with Apple's Chess application
    url: https://opensource.apple.com/source/Chess/Chess-105.0.14/Documentation/PGN-Standard.txt.auto.html
    type: primary-record
    accessed: 2026-11-09
  - id: s2
    title: "David Forsyth (compiled by Alan McGowan, updated 23 January 2019)"
    publisher: Chess Scotland, history archive
    url: https://www.chessscotland.com/documents/history/biographies/forsyth.htm
    type: archive
    accessed: 2026-11-09
  - id: s3
    title: "Chess Notes by Edward Winter, C.N. 5205: Forsyth notation (4 October 2007)"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/winter39.html
    type: reference
    accessed: 2026-11-09
  - id: s4
    title: "FEN Format (ChessBase 18 help)"
    publisher: ChessBase
    url: https://help.chessbase.com/CBase/18/Eng/fen_format.htm
    type: publication
    accessed: 2026-11-09
created: 2026-11-09
---

# Forsyth–Edwards Notation

Forsyth–Edwards Notation (FEN) is the standard way to write down a single chess position as one line of plain ASCII text. Where a game score records how a game unfolded, a FEN record captures a snapshot: which piece stands on which square and the extra state a player or program needs to continue from that moment.[^s1] ChessBase's documentation describes its purpose as giving everything required to restart a game from a particular position.[^s4] Today it is the format club players meet when they paste a position into an analysis board, set up a study or share a puzzle.

## Origins

The notation goes back to David Forsyth (1854–1909), a Scottish solicitor and chess organiser who was a founding member of the Scottish Chess Association.[^s2] Chess Scotland's history archive records that he first published his method of recording positions in the *Glasgow Weekly Herald* of 10 February 1883, and Edward Winter's Chess Notes (C.N. 5205) reproduces that original proposal from page 7 of the same issue.[^s2][^s3] Forsyth read the board rank by rank from a8 to h8, then a7 to h7 and so on, using capital letters for White, lower-case letters for Black, digits for runs of empty squares and slashes between ranks; the archive notes that the *British Chess Magazine* once tried dropping the slashes, but they returned because they cut down errors.[^s2] In the computer era Steven J. Edwards extended Forsyth's scheme for chess software, first implementing it in his SAN Kit, and defined it in section 16.1 of the 1994 Portable Game Notation standard, which he coordinated for the rec.games.chess newsgroup.[^s1]

## The six fields

A FEN record has six fields separated by single spaces.[^s1]

1. **Piece placement.** Ranks run from the eighth down to the first, and each rank from the a-file to the h-file. The letters PNBRQK stand for White's pieces and pnbrqk for Black's, the digits 1–8 count consecutive empty squares, and "/" separates the ranks.[^s1]
2. **Active colour.** "w" if White is to move, "b" if Black is.[^s1]
3. **Castling availability.** "-" if neither side may castle; otherwise up to four letters, K and Q for White's kingside and queenside rights and k and q for Black's, written in that order. The field records whether castling is still possible in the future, not whether it is legal right now, so a right is kept even while castling is temporarily blocked.[^s1]
4. **En passant target square.** The square a pawn skipped over on a two-square advance (on the third rank after a White pawn move, on the sixth after a Black one), or "-". Under the 1994 standard the square is written after every double pawn step, even if no enemy pawn is in place to capture.[^s1]
5. **Halfmove clock.** The number of half-moves (plies) since the last pawn move or capture, kept so that the fifty-move rule can be applied.[^s1]
6. **Fullmove number.** Starts at 1 and goes up by one after each Black move.[^s1]

## A worked example

The standard's own walkthrough starts from the initial position, `rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1`, and follows 1.e4 c5 2.Nf3.[^s1] After 1.e4 the side to move becomes "b" and the en passant field reads e3; after 1...c5 the field changes to c6 and the move number rises to 2.[^s1] After 2.Nf3 the record is the key position above, `rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2`: the en passant field is back to "-", and the halfmove clock shows 1 because a knight move is neither a pawn move nor a capture.[^s1] Forsyth's own scheme already handled study positions compactly; Chess Scotland gives the Saavedra study's placement as `8/8/1KP5/3r4/8/8/8/k7`.[^s2]

## Uses and pitfalls

In a PGN file, a game that begins anywhere other than the normal starting array must carry a SetUp tag with the value 1 and a FEN tag holding the starting position.[^s1] Text files consisting only of FEN records conventionally use the .fen extension.[^s1][^s4] The commonest errors when typing FEN by hand are counting empty squares wrongly (each rank must add up to eight), reading the board from White's first rank instead of the eighth, and leaving castling letters in place after a king or rook has moved. A FEN is also only a snapshot: ChessBase points out that it carries no game history, so it cannot tell whether a threefold-repetition claim is valid, and the richer Extended Position Description is needed for that.[^s4] EPD, developed by John Stanback and Steven Edwards, keeps FEN's first four fields and adds semicolon-terminated "operations" for exchanging positions and commands between programs.[^s1]

## Connections

FEN is a companion to **algebraic notation**, using the same a–h file and 1–8 rank names, and it is **part of** the **Portable Game Notation** standard, where the FEN tag records non-standard starting positions.[^s1] It is **named after** **David Forsyth**, whose 1883 notation it extends, and was **developed by** **Steven J. Edwards**.[^s1][^s2] Its fields encode the state needed by the rules on **castling**, **en passant** and the **fifty-move rule**, while **Extended Position Description** builds on its first four fields.[^s1] A **Chess960** game, which starts from a non-standard array, is exactly the kind of game the standard says must carry a SetUp and FEN tag.[^s1]

## Sources

[^s1]: Steven J. Edwards (coordinator), "Standard: Portable Game Notation Specification and Implementation Guide", revised 12 March 1994, sections 9.7, 16.1 and 16.2. https://opensource.apple.com/source/Chess/Chess-105.0.14/Documentation/PGN-Standard.txt.auto.html (accessed 2026-11-09)
[^s2]: Alan McGowan, "David Forsyth", Chess Scotland history archive (updated 23 January 2019). https://www.chessscotland.com/documents/history/biographies/forsyth.htm (accessed 2026-11-09)
[^s3]: Edward Winter, Chess Notes, C.N. 5205 "Forsyth notation" (4 October 2007). https://chesshistory.com/winter/winter39.html (accessed 2026-11-09)
[^s4]: ChessBase, "FEN Format", ChessBase 18 help. https://help.chessbase.com/CBase/18/Eng/fen_format.htm (accessed 2026-11-09)
