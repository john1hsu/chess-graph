---
id: kt:algebraic-notation
type: Notation
title: Algebraic notation
aliases: [Standard algebraic notation, SAN, Algebraic chess notation, Coordinate notation, Long algebraic notation, LAN, Figurine algebraic notation]
domain: rules-and-notation
summary: >-
  The system for recording chess moves in which each square is named by a file letter (a–h) and a
  rank number (1–8) from White's side, and a move is written as the piece letter plus the
  destination square; FIDE recognises it as the only notation for its own events.
fen: "4k3/8/8/8/8/8/8/4NKN1 w - - 0 1"
status: current
volatile: true
verified: 2026-11-09
broader: [kt:fide-laws-of-chess]
related: [kt:descriptive-notation, kt:portable-game-notation, kt:forsyth-edwards-notation, kt:castling, kt:pawn-promotion, kt:philipp-stamma]
relations:
  - {predicate: partOf, object: kt:fide-laws-of-chess}
  - {predicate: replaces, object: kt:descriptive-notation}
  - {predicate: governedBy, object: kt:fide}
sources:
  - id: s1
    title: "Appendix C. Algebraic Notation (FIDE Laws of Chess)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/?p=880
    type: governing-body
    accessed: 2026-11-09
  - id: s2
    title: "Article 8: The recording of the moves (FIDE Laws of Chess)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/?p=866
    type: governing-body
    accessed: 2026-11-09
  - id: s3
    title: "algebraic notation"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/algebraic-notation
    type: reference
    accessed: 2026-11-09
  - id: s4
    title: "Chess Notation"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/notation.html
    type: reference
    accessed: 2026-11-09
  - id: s5
    title: "The Creator of Algebraic Chess Notation (GM Julio Becerra, 4 November 2009)"
    publisher: Chess.com
    url: https://www.chess.com/article/view/the-creator-of-algebraic-chess-notation
    type: publication
    accessed: 2026-11-09
  - id: s6
    title: "Summary of differences between the FIDE Laws of Chess and the US Chess Official Rules of Chess, 7th edition (updated 1 January 2022)"
    publisher: US Chess
    url: https://new.uschess.org/sites/default/files/media/documents/uschess-fide-rules-comparison.pdf
    type: governing-body
    accessed: 2026-11-09
created: 2026-11-09
---

# Algebraic notation

Algebraic notation is the way chess moves are written down today. Encyclopaedia Britannica calls it by far the most widely used form of chess notation: every square is identified from the point of view of the player with the white pieces, and a move is recorded by the piece's initial and its destination square, so Be5 means a bishop moved to e5.[^s3] The system is codified in Appendix C of the FIDE Laws of Chess, which states that FIDE recognises only the algebraic system for its own tournaments and matches and recommends it for chess books and periodicals.[^s1] As of November 2026, Article 8 of the Laws requires each player to record both sides' moves, move by move, in algebraic notation, on a paper scoresheet or a FIDE-certified electronic one.[^s2]

## How squares and pieces are named

The eight files are lettered a to h, read from left to right for White, and the ranks are numbered 1 to 8 from White's side, so White's pieces start on ranks 1 and 2 and Black's on ranks 7 and 8; every square therefore has a unique name such as e4 or g7.[^s1] Pieces take capital letters: K for king, Q for queen, R for rook, B for bishop and N for knight, the N avoiding a clash with the king.[^s1] Players may use the letters of their own language (FIDE's examples are F for the French *fou* and L for the Dutch *loper*, both meaning bishop), while printed periodicals are encouraged to use figurines, small piece symbols that need no translation.[^s1] Pawns get no letter at all: a pawn move is written as the destination square alone, such as e5 or d4.[^s1]

## Writing a move

A piece move is the piece letter followed by the destination square with no hyphen (Nf3, Rd1).[^s1] A capture may insert an x (Bxe5), and a pawn capture must give the file the pawn left from, as in dxe5 or axb5.[^s1] Kingside castling is written 0-0 and queenside castling 0-0-0; computer formats generally use the letter O instead of the digit zero, as in the checked line below.[^s1] Promotion is written by putting the new piece's letter straight after the pawn move (d8Q, exf8N), and an en passant capture may carry the suffix "e.p.".[^s1] The symbols x, + for check, ++ or # for mate, and e.p. are all optional under the Laws, and a draw offer is marked on the scoresheet with (=).[^s1][^s2]

**Long algebraic notation** gives the departure square as well as the arrival square (Ng1f3, e7e5); FIDE accepts it, and its sample game in Appendix C is printed in short, abbreviated and long forms side by side.[^s1]

## Disambiguation

When two identical pieces can reach the same square, the move must say which one moved. If they stand on the same rank, the departure file is added; if they share a file, the departure rank is added; and if they differ in both, the file is preferred.[^s1] In the key position, White's knights on e1 and g1 can both go to f3, so the moves must be written Nef3 and Ngf3; knights on f1 and f5 aiming at e3 would instead give N1e3 and N5e3.[^s1] Captures follow the same method with x inserted, for example Ngxf3.[^s1]

## A short example

The Exchange Variation of the Ruy Lopez shows most of the everyday conventions: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Bxc6 dxc6 5.O-O. Here 4.Bxc6 is a piece capture, 4...dxc6 a pawn capture naming its departure file, and 5.O-O kingside castling, which a handwritten scoresheet would show as 0-0.[^s1]

## Pitfalls for club players

Typical scoresheet slips come from the conventions above: forgetting the departure file on a pawn capture, omitting the extra file or rank when two rooks or knights can reach the same square, and writing a move before playing it. FIDE forbids writing moves in advance except when claiming a draw by repetition or the fifty-move rule, though a player may reply on the board before recording the opponent's last move.[^s2] Players short of time should know the Laws' exception: with under five minutes left in a period and no increment of at least 30 seconds, recording is not required for the rest of that period.[^s2] US Chess rules differ in detail, for instance on when players may stop recording, so national-event players should check their federation's rulebook.[^s6] FIDE also warns that a scoresheet in another system cannot be used as evidence where a scoresheet would normally serve, and arbiters should warn players who use one.[^s1]

## History

GM Julio Becerra credits Philipp Stamma's *Essai sur le Jeu des Echecs* (France, 1737) with introducing algebraic notation, although Stamma marked pieces by the letter of their starting file rather than by their initial and wrote "p" for pawn moves.[^s5] English-speaking countries long preferred descriptive notation (P-K4 rather than e4). Edward Winter's research finds algebraic notation in English books such as R. Lambe's *History of Chess* (1764) and Charles Check's *Easy Guide* (1818), and records that Edward Lasker's use of it in a 1918 American book was controversial.[^s4] Winter also notes that English-language magazines adopted N for the knight in place of Kt only gradually, from the mid-1930s to the 1970s, and that Chess Life & Review printed annotations in algebraic notation in August 1979.[^s4]

## Connections

Algebraic notation is **part of** the **FIDE Laws of Chess** (Appendix C), and FIDE governs its use in rated play through Article 8.[^s1][^s2] It **replaces** **descriptive notation**, the older English-language system.[^s4] It is how **castling** and **pawn promotion** are written on a scoresheet.[^s1] Computer formats build on it: **Portable Game Notation** stores games as algebraic move text, while **Forsyth–Edwards Notation** uses the same file and rank names for squares. Its origins are linked to **Philipp Stamma**.[^s5]

## Sources

[^s1]: FIDE Rules Commission, "Appendix C. Algebraic Notation" (FIDE Laws of Chess). https://rcc.fide.com/?p=880 (accessed 2026-11-09)
[^s2]: FIDE Rules Commission, "Article 8: The recording of the moves" (FIDE Laws of Chess). https://rcc.fide.com/?p=866 (accessed 2026-11-09)
[^s3]: Encyclopaedia Britannica, "algebraic notation". https://www.britannica.com/topic/algebraic-notation (accessed 2026-11-09)
[^s4]: Edward Winter, Chess Notes, "Chess Notation". https://chesshistory.com/winter/extra/notation.html (accessed 2026-11-09)
[^s5]: Julio Becerra, "The Creator of Algebraic Chess Notation", Chess.com, 4 November 2009. https://www.chess.com/article/view/the-creator-of-algebraic-chess-notation (accessed 2026-11-09)
[^s6]: US Chess, "Summary of differences between the FIDE Laws of Chess and the US Chess Official Rules of Chess, 7th edition" (updated 1 January 2022). https://new.uschess.org/sites/default/files/media/documents/uschess-fide-rules-comparison.pdf (accessed 2026-11-09)
