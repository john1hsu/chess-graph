---
id: kt:king-and-pawn-endgames
type: EndgameType
title: King and pawn endgames
aliases: [Pawn endgames, Pawn endings, King and pawn endings, King-and-pawn endgame, K+P endgames, Pure pawn endings]
domain: endgames
summary: >-
  Endgames in which only kings and pawns remain on the board. Because no pieces can make waiting moves
  or stop a passed pawn from a distance, they turn on exact counting of tempi, king activity, the
  opposition and the creation of passed pawns.
fen: "6k1/ppp5/8/PPP5/8/8/8/6K1 w - - 0 1"
status: current
volatile: false
verified: 2026-11-10
broader: [kt:chess-endgame]
related: [kt:pawn-promotion, kt:passed-pawn, kt:key-squares, kt:stalemate]
relations:
  - {predicate: usesTechnique, object: kt:opposition}
  - {predicate: usesTechnique, object: kt:triangulation}
  - {predicate: dependsOn, object: kt:zugzwang}
  - {predicate: hasPart, object: kt:rule-of-the-square}
sources:
  - id: s1
    title: "Chess Fundamentals (1921), Project Gutenberg eBook #33870"
    publisher: José Raúl Capablanca, Harcourt, Brace and Howe; Project Gutenberg
    url: https://gutenberg.org/cache/epub/33870/pg33870-images.html
    type: book
    accessed: 2026-11-10
  - id: s2
    title: "Chess Strategy (1915), Project Gutenberg eBook #5614"
    publisher: Edward Lasker; Project Gutenberg
    url: https://gutenberg.org/cache/epub/5614/pg5614-images.html
    type: book
    accessed: 2026-11-10
  - id: s3
    title: "Dvoretsky's Endgame Manual, fifth edition (excerpt with table of contents)"
    publisher: Mark Dvoretsky, revised by Karsten Müller, Russell Enterprises (2020)
    url: https://shop.chess-tigers.de/cdn/shop/files/dem5_excerpt.pdf
    type: book
    accessed: 2026-11-10
  - id: s4
    title: "Square Rule"
    publisher: Chess.com (Chess Terms)
    url: https://www.chess.com/terms/square-rule-chess
    type: publication
    accessed: 2026-11-10
created: 2026-11-10
---

# King and pawn endgames

A king and pawn endgame, or pawn ending, is a position in which every piece except the kings has left the board. It is the simplest kind of endgame in material terms but one of the most unforgiving: with no rooks, bishops or knights to make spare moves or stop a pawn from a distance, a single tempo usually decides between a win, a draw and a loss. Capablanca opened his teaching of the endgame with these positions, and modern manuals still put them first; Dvoretsky's manual devotes its opening chapter to pawn endgames before any piece ending.[^s1][^s3]

## The king becomes an attacker

The defining feature of pawn endings is the role of the king. Capablanca contrasted the king's defensive job in the middlegame with its offensive role once most of the material has been exchanged, when handling it well becomes paramount.[^s1] Edward Lasker likewise named the active part played by the king as one of the main characteristics of endgames.[^s2] In a pawn ending the king is the only piece that can attack pawns, escort its own pawn or blockade an enemy one, so the side whose king reaches the critical squares first usually wins. Manuals accordingly treat the active king, king routes such as shouldering the enemy king aside, and widening a foothold in the enemy camp as core techniques.[^s3]

## Basic tools

**King and pawn against king.** Capablanca's rule is that the attacking king should stand in front of its pawn with at least one square between them, while a defending king directly in front of the pawn draws; his method is to advance the king as far as the pawn's safety allows and to push the pawn only when its own safety requires it.[^s1] Lasker added that the defender draws if his king controls the queening square, and that the rook's pawn is the great exception, because a king in the corner cannot be driven out and the attacker often ends up giving stalemate.[^s2] Which side wins these duels is settled by the opposition and, more generally, by corresponding squares and triangulation.[^s3]

**The rule of the square.** When a passed pawn runs with no king to escort it, the defender need not calculate: draw an imaginary square with one side running from the pawn to its promotion square. If the defending king can step inside that square, it catches the pawn; if not, the pawn queens.[^s4] Endgame manuals treat it alongside related king-against-pawns themes such as Réti's idea, the "floating square" and three connected pawns.[^s3]

**Counting.** When both sides have passed pawns, the result is found by counting the moves each needs to queen, and checking whether the first new queen can immediately check or control the other's queening square. Capablanca gives races in which the side to move wins, and Lasker settles distant-pawn endings the same way, by counting moves on each wing.[^s1][^s2]

## Typical plans

The main winning plan with an extra pawn, or with an unbalanced structure, is to create a passed pawn. Lasker's rule is to exchange pawns on the wing where you have the majority until the extra pawn is passed; a passed pawn far from the main action then ties the enemy king down while your own king wins pawns on the other side.[^s2] With pawns on both wings, Capablanca advises acting first on the side where you have the superior forces.[^s1] The classic "outside passed pawn" and the protected passed pawn are standard winning advantages for exactly this reason, and positions are often decided by reserve tempi, spare pawn moves that one side can use to put the other in zugzwang.[^s3]

A breakthrough can create a passed pawn even against equal numbers. In the key position above (White pawns a5, b5, c5; Black pawns a7, b7, c7; kings far away), Capablanca's lesson is to advance the centre pawn: 1.b6! axb6 2.c6 bxc6 3.a6, and the a-pawn queens; if 1...cxb6 then 2.a6 bxa6 3.c6 does the same on the other side. With Black to move, 1...b6 stops the trick and the position is drawn.[^s1]

## Common mistakes

Exchanging into a pawn ending is irreversible, so it must be calculated to the end rather than judged by general impressions; Capablanca stresses that some of his examples can be won only by one exact sequence.[^s1] Other frequent errors are pushing the pawn too early instead of advancing the king, choosing the wrong square for the defending king on the back rank, forgetting the rook's pawn exception, and overlooking stalemate, which manuals list as a recurring defensive resource.[^s1][^s2][^s3]

## Connections

Pawn endings are the most basic family of endgames and the place where the opposition, triangulation and zugzwang are first learned; those techniques decide whether a king can gain or lose the tempo it needs.[^s3] Key squares describe where the attacking king must arrive, and the rule of the square tells whether a lone passed pawn can be caught.[^s3][^s4] The goal of almost every plan is pawn promotion, and stalemate is the defender's chief saving resource, especially with a rook's pawn.[^s2]

## Sources

[^s1]: José Raúl Capablanca, *Chess Fundamentals* (1921), Project Gutenberg eBook #33870. https://gutenberg.org/cache/epub/33870/pg33870-images.html (accessed 2026-11-10)
[^s2]: Edward Lasker, *Chess Strategy* (1915), chapter V "The End-game", Project Gutenberg eBook #5614. https://gutenberg.org/cache/epub/5614/pg5614-images.html (accessed 2026-11-10)
[^s3]: Mark Dvoretsky, *Dvoretsky's Endgame Manual*, fifth edition, revised by Karsten Müller (Russell Enterprises, 2020), excerpt with table of contents, chapter 1 "Pawn Endgames". https://shop.chess-tigers.de/cdn/shop/files/dem5_excerpt.pdf (accessed 2026-11-10)
[^s4]: Chess.com, "Square Rule" (Chess Terms). https://www.chess.com/terms/square-rule-chess (accessed 2026-11-10)
