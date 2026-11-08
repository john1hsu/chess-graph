---
id: kt:chess960
type: Variant
title: Chess960
aliases: [Fischer Random Chess, Fischer Random, Fischerandom, Fischer chess, Freestyle Chess, Chess 960, FRC]
domain: variants-and-compositions
summary: >-
  A chess variant devised by Bobby Fischer in which the pieces on the back rank are shuffled before
  each game, under constraints that keep castling possible and the bishops on opposite colours,
  giving 960 possible starting positions; all other rules are those of standard chess.
status: current
volatile: true
verified: 2026-11-08
broader: [kt:chess-variants]
related: [kt:castling, kt:forsyth-edwards-notation, kt:universal-chess-interface, kt:fide-world-fischer-random-chess-championship]
relations:
  - {predicate: developedBy, object: kt:bobby-fischer}
  - {predicate: governedBy, object: kt:fide-laws-of-chess}
  - {predicate: sanctionedBy, object: kt:fide}
  - {predicate: influencedBy, object: kt:shuffle-chess}
sources:
  - id: s1
    title: "FIDE Laws of Chess, Guidelines II. Chess960 Rules"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/guidelinesii/
    type: governing-body
    accessed: 2026-11-08
  - id: s2
    title: "Chess960"
    publisher: Encyclopaedia Britannica
    url: https://britannica.com/topic/chess960
    type: reference
    accessed: 2026-11-08
  - id: s3
    title: "History of Chess960"
    publisher: Susan Polgar, FIDE (fide.com)
    url: https://www.fide.com/history-of-chess960/
    type: publication
    accessed: 2026-11-08
  - id: s4
    title: "Wesley So to defend his FIDE World Fischer Random title"
    publisher: FIDE
    url: https://www.fide.com/wesley-so-to-defend-his-fide-world-fischer-random-title/
    type: official-project
    accessed: 2026-11-08
  - id: s5
    title: "Hikaru Nakamura Wins Fischer Random World Championship"
    publisher: Jack Rodgers, Chess.com News
    url: https://www.chess.com/news/view/wins-fischer-random-world-championship-final-hikaru-nakamura
    type: publication
    accessed: 2026-11-08
  - id: s6
    title: "Chess960"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/Chess960
    type: community
    accessed: 2026-11-08
created: 2026-11-08
---

# Chess960

Chess960, also called Fischer Random Chess or Fischer chess, is a variant invented by former world champion Bobby Fischer in which the pieces on each player's back rank are shuffled before play begins.[^s2] Once the starting position is set, the game is ordinary chess: the pieces move normally and the aim is still to checkmate the opponent's king.[^s1] The point of the shuffle is to take memorised opening theory out of the game and make players think from the first move.[^s4]

## Origins

Randomising the opening array is an old idea. Susan Polgar's history of the variant for FIDE traces proposals back to 1792 and documented "shuffle chess" games to Mannheim in 1842; in the twentieth century David Bronstein (from the late 1940s) and Pal Benko (in the 1970s) promoted versions in which the players placed their pieces in turn.[^s3] Fischer, who returned to chess in 1992, worked out his rules in Budapest with Polgar's help and formally presented "Fischerandom" in Buenos Aires on 19 June 1996.[^s3][^s6] The name Chess960 refers to the number of legal starting arrays, a figure Polgar says was calculated by mathematicians Fischer consulted in Budapest.[^s3] FIDE placed the variant in an appendix to the Laws of Chess in 2008, and since 2024 the name "Freestyle Chess" has also been used for it.[^s3]

## How the start position works

FIDE's Chess960 guidelines keep the pawns on their usual squares and place White's other pieces randomly on the first rank, with three conditions: the king stands somewhere between the two rooks, the two bishops stand on squares of opposite colour, and Black's pieces mirror White's.[^s1] The position may be drawn by computer or by dice, coins or cards.[^s1] The count of 960 follows from those constraints: 4 dark squares times 4 light squares for the bishops, 6 remaining squares for the queen, and 10 ways to place the two knights on the remaining five squares, after which the king and rooks fill the last three squares in the only order that puts the king in the middle (4 × 4 × 6 × 10 = 960). The standard chess array is one of the 960.

## Castling

Castling is where Chess960 differs most from the standard game in practice. Each side may castle once, moving king and rook in a single turn, and the end result is always the same as in classical chess: after queenside castling the king is on c1 (c8) and the rook on d1 (d8); after kingside castling the king is on g1 (g8) and the rook on f1 (f8).[^s1] Depending on where the pieces start, castling may involve both pieces moving, the king and rook swapping places, or only one of them moving, and in some setups it is possible on the very first move.[^s1] All squares between the starting and final squares of both king and rook must be empty except for those two pieces, while squares that must be clear in standard chess (such as b1 or h1) may stay occupied in some arrays.[^s1] On a physical board FIDE recommends taking the king off the board, placing the rook on its final square and then the king, and saying that one intends to castle to avoid disputes.[^s1]

## Practical ideas and pitfalls

- Look for undefended pawns in the initial array. With the bishops in a corner or the queen on an unusual square, a first-move threat against a pawn is common, so check what every piece already attacks before playing a "normal" developing move.
- Opening principles still hold. Control of the centre, quick development and king safety matter as much as ever; what disappears is the memorised move order, not the underlying strategy.[^s4]
- Plan where the king will go. Because castling destinations are fixed, castling from a starting king on b1 or g1 can move the king very little, and the castling side may need several pieces cleared first.
- Be careful with move input. Many software interfaces castle by moving the king onto its own rook, and engines signal Chess960 support through options such as `UCI_Chess960`.[^s6]

## Competition

FIDE recognised a World Fischer Random Chess Championship in 2019. The first edition, organised in Norway, was won by Wesley So, who beat Magnus Carlsen in the final.[^s4] The second, held in Reykjavik in October 2022 to mark the fiftieth anniversary of the Fischer–Spassky match, used a 25-minute-plus-increment time control for its eight-player final stage.[^s4] Hikaru Nakamura won it on 30 October 2022, drawing the four-game final 2–2 with Ian Nepomniachtchi and winning the Armageddon tiebreak; Carlsen took third place.[^s5] Earlier landmarks include the Mainz series run by Hans-Walter Schmitt from 2001 to 2009 and a 2018 Carlsen–Nakamura match in Norway that Carlsen won 14–10.[^s3]

## Connections

Chess960 is one of the **chess variants** and was developed by **Bobby Fischer**, building on earlier **shuffle chess** ideas.[^s3] Its rules form part of the **FIDE Laws of Chess** as guidelines, and **FIDE** sanctions its world championship, the **FIDE World Fischer Random Chess Championship**.[^s1][^s4] Its special **castling** rules are the main difference from standard play, and they also affect **Forsyth–Edwards Notation** (for which Chess960-aware forms such as X-FEN and Shredder-FEN exist) and the **Universal Chess Interface**, through which engines declare Chess960 support.[^s6]

## Sources

[^s1]: FIDE Rules Commission, "FIDE Laws of Chess, Guidelines II. Chess960 Rules". https://rcc.fide.com/guidelinesii/ (accessed 2026-11-08)
[^s2]: Encyclopaedia Britannica, "Chess960". https://britannica.com/topic/chess960 (accessed 2026-11-08)
[^s3]: Susan Polgar, FIDE, "History of Chess960" (2025). https://www.fide.com/history-of-chess960/ (accessed 2026-11-08)
[^s4]: FIDE, "Wesley So to defend his FIDE World Fischer Random title" (2022). https://www.fide.com/wesley-so-to-defend-his-fide-world-fischer-random-title/ (accessed 2026-11-08)
[^s5]: Jack Rodgers, Chess.com News, "Hikaru Nakamura Wins Fischer Random World Championship" (30 October 2022). https://www.chess.com/news/view/wins-fischer-random-world-championship-final-hikaru-nakamura (accessed 2026-11-08)
[^s6]: Chess Programming Wiki, "Chess960". https://www.chessprogramming.org/Chess960 (accessed 2026-11-08)
