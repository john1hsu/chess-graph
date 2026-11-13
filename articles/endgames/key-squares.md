---
id: kt:key-squares
type: Concept
title: Key squares
aliases: [Key square, Critical squares, Critical square, Key squares of a pawn]
domain: endgames
summary: >-
  In king-and-pawn endgames, the squares that the attacking king needs to reach to force the pawn
  through: once the king stands on a key square, the pawn promotes whoever is to move, unless the
  defender can capture the pawn at once.
fen: "8/3k4/8/3K4/3P4/8/8/8 b - - 0 1"
status: current
volatile: false
verified: 2026-11-13
broader: [kt:king-and-pawn-endgames]
related: [kt:opposition, kt:corresponding-squares, kt:triangulation, kt:rule-of-the-square]
relations:
  - {predicate: enables, object: kt:pawn-promotion}
  - {predicate: dependsOn, object: kt:zugzwang}
  - {predicate: usesTechnique, object: kt:opposition}
sources:
  - id: s1
    title: "Chess Fundamentals (1921), Project Gutenberg eBook #33870"
    publisher: José Raúl Capablanca, Harcourt, Brace and Howe; Project Gutenberg
    url: https://gutenberg.org/cache/epub/33870/pg33870-images.html
    type: book
    accessed: 2026-11-13
  - id: s2
    title: "Chess Strategy (1915), Project Gutenberg eBook #5614"
    publisher: Edward Lasker; Project Gutenberg
    url: https://gutenberg.org/files/5614/5614-h/5614-h.htm
    type: book
    accessed: 2026-11-13
  - id: s3
    title: "Chess Endgames for Kids (sample pages, contents and Lesson 14: Triangulation and More Opposition)"
    publisher: Karsten Müller, Gambit Publications (2015); excerpt hosted by Chess Tigers
    url: https://chess-tigers.de/cdn/shop/files/Chess_Endgames_for_Kids.pdf
    type: book
    accessed: 2026-11-13
  - id: s4
    title: "Dvoretsky's Endgame Manual, sixth edition (excerpt with table of contents)"
    publisher: Mark Dvoretsky, revised by Karsten Müller and Alex Fishbein, Russell Enterprises (2025); excerpt hosted by De Beste Zet
    url: https://www.debestezet.nl/catalog/images/PDF/Dvoretskys%20Endgame%20Manual%206th%20Edition.pdf
    type: book
    accessed: 2026-11-13
  - id: s5
    title: "No road to Rome"
    publisher: Karsten Müller, ChessBase News (2020-06-30)
    url: https://en.chessbase.com/post/endgame-blog-karsten-mueller-2020_26
    type: publication
    accessed: 2026-11-13
  - id: s6
    title: "Coach Dante's Endgame Crash Course! -- Pawns: Key Squares"
    publisher: CoachDVS88, Chess.com blog
    url: https://www.chess.com/blog/CoachDVS88/coach-dante-s-endgame-crash-course-pawns-key-squares
    type: community
    accessed: 2026-11-13
  - id: s7
    title: "Pawn Endgame in Chess: Getting It Right!"
    publisher: Shaun Sedice, US Chess Sales blog
    url: https://www.uscfsales.com/chess-blog/pawn-endgame-in-chess-getting-it-right/
    type: community
    accessed: 2026-11-13
created: 2026-11-13
---

# Key squares

Key squares answer the first question of every king-and-pawn ending: where does the attacking king have to get to? A key square is a square from which the attacking king forces promotion no matter whose move it is, provided the defending king cannot simply take the pawn.[^s6] The idea turns the vague advice "bring the king in front of the pawn" into a precise target, and it is the natural partner of the opposition, which is the means by which the attacker fights his way onto those squares and the defender keeps him off them.[^s3] Karsten Müller presents opposition and key squares together as the two concepts a player must master to handle pawn endgames, which he calls the foundation of endgame theory.[^s5]

## Where the key squares are

For a pawn that has not yet crossed the middle of the board (on its second, third or fourth rank), there are three key squares: the square two ranks in front of the pawn and its two neighbours on that rank. A white pawn on d4 has key squares c6, d6 and e6; a pawn on g3 has f5, g5 and h5.[^s6][^s7] Once the pawn has crossed into the opponent's half (fifth or sixth rank), the key squares grow to six: the three squares directly in front of the pawn and the three on the rank beyond, so a pawn on d5 has c6, d6, e6, c7, d7 and e7.[^s6] The rook's pawn is the exception. Lasker explained that the defending king draws whenever it reaches the corner where the pawn would queen, because it cannot be driven out again.[^s2] For an h-pawn the only squares that win are g7 and g8 (b7 and b8 for an a-pawn), cutting the defender off from the corner.[^s7]

These geometric rules restate a principle the classic writers gave in words. Capablanca's advice was to keep the king in front of the pawn with at least one square between them, and to advance the king as far as the pawn's safety allows rather than pushing the pawn early; a defending king standing directly in front of the pawn, he noted, cannot be beaten.[^s1] Lasker drew the decisive line between a king one rank ahead of its pawn, where the outcome depends on who gets the opposition, and a king more than one rank ahead, which he said can always win.[^s2] A king two ranks in front of a pawn on the fourth rank or lower is standing on a key square.

## How the fight goes

Because a key square wins by itself, play in these endings revolves around access to it. The attacker tries to reach any one of the key squares; the defender tries to stand opposite the attacking king so that every approach is blocked. Müller describes the opposition as the main fighting method for the key squares, and shows that the attacker cannot normally gain a tempo by triangulating when the defender can triangulate in reply.[^s3] When the kings are far apart, a practical method is to list the key squares and steer for the one farthest from the defending king, counting the moves.[^s6] Modern manuals treat key squares early in their pawn-endgame chapters, ahead of corresponding squares and the opposition.[^s4][^s3]

## Example

In the key position (White Kd5, Pd4; Black Kd7) the pawn is on the fourth rank, so its key squares are c6, d6 and e6, and the white king is one step away from all three. With Black to move, Black is in zugzwang: 1...Ke7 2.Kc6 (or 1...Kc7 2.Ke6) puts the king on a key square, and after 2...Ke6 3.d5+ Ke7 4.Kc7 the pawn runs through. With White to move, Black holds: 1.Kc5 Kc7 keeps the opposition, and after 2.d5 Kd7 3.d6 Kd8 4.Kc6 Kc8 5.d7+ Kd8 6.Kd6 the result is stalemate. The same position is won or drawn depending only on who must give way, which is why the key squares and the opposition are taught together.[^s3][^s2]

## Common mistakes

The usual error is to push the pawn too soon. Every pawn advance moves the key squares forward with it, so a hasty pawn move can put them out of the king's reach; Capablanca's rule of advancing the king first and the pawn only when needed avoids this.[^s1] A second error is to forget the capture exception: a king on a key square does not win if the defender can take the pawn immediately.[^s6] With the rook's pawn, attackers often head for the usual squares in front of the pawn, but only the squares that shut the defender out of the corner count.[^s7][^s2]

## Connections

Key squares belong to the theory of king-and-pawn endgames, where they define the attacker's goal and the opposition supplies the method of reaching it.[^s3] They rest on zugzwang, since a position like the example is decided by which side must move.[^s3] When simple opposition is not enough, endgame manuals move on to corresponding squares and triangulation, the general tools for winning or losing a tempo.[^s4][^s3] Müller's course teaches the rule of the square, for pawns racing without their king, in the lesson just before key squares, and the whole point of both is pawn promotion.[^s3][^s1]

## Sources

[^s1]: José Raúl Capablanca, *Chess Fundamentals* (1921), chapter 2, Project Gutenberg eBook #33870. https://gutenberg.org/cache/epub/33870/pg33870-images.html (accessed 2026-11-13)
[^s2]: Edward Lasker, *Chess Strategy* (1915), chapter V "The End-game", Project Gutenberg eBook #5614. https://gutenberg.org/files/5614/5614-h/5614-h.htm (accessed 2026-11-13)
[^s3]: Karsten Müller, *Chess Endgames for Kids* (Gambit, 2015), sample pages with contents and Lesson 14. https://chess-tigers.de/cdn/shop/files/Chess_Endgames_for_Kids.pdf (accessed 2026-11-13)
[^s4]: Mark Dvoretsky, *Dvoretsky's Endgame Manual*, sixth edition, revised by Karsten Müller and Alex Fishbein (Russell Enterprises, 2025), excerpt with table of contents. https://www.debestezet.nl/catalog/images/PDF/Dvoretskys%20Endgame%20Manual%206th%20Edition.pdf (accessed 2026-11-13)
[^s5]: Karsten Müller, "No road to Rome", ChessBase News, 30 June 2020. https://en.chessbase.com/post/endgame-blog-karsten-mueller-2020_26 (accessed 2026-11-13)
[^s6]: CoachDVS88, "Coach Dante's Endgame Crash Course! -- Pawns: Key Squares", Chess.com blog. https://www.chess.com/blog/CoachDVS88/coach-dante-s-endgame-crash-course-pawns-key-squares (accessed 2026-11-13)
[^s7]: Shaun Sedice, "Pawn Endgame in Chess: Getting It Right!", US Chess Sales blog. https://www.uscfsales.com/chess-blog/pawn-endgame-in-chess-getting-it-right/ (accessed 2026-11-13)
