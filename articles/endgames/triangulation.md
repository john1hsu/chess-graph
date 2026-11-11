---
id: kt:triangulation
type: Technique
title: Triangulation
aliases: [Triangulating, Triangle manoeuvre, Triangle maneuver, Losing a tempo with the king]
domain: endgames
summary: >-
  An endgame king manoeuvre in which the king walks around three neighbouring squares and so returns
  to the same position in three moves instead of two, handing the move to an opponent who cannot
  copy the manoeuvre and is left in zugzwang.
fen: "8/5k2/5P1p/5K1P/8/8/8/8 w - - 0 1"
status: current
volatile: false
verified: 2026-11-11
broader: [kt:king-and-pawn-endgames]
related: [kt:opposition, kt:zugzwang, kt:corresponding-squares, kt:key-squares]
relations:
  - {predicate: dependsOn, object: kt:zugzwang}
  - {predicate: contrastsWith, object: kt:opposition}
  - {predicate: partOf, object: kt:corresponding-squares}
sources:
  - id: s1
    title: "Chess Endgames for Kids (sample pages, Lesson 14: Triangulation and More Opposition)"
    publisher: Karsten Müller, Gambit Publications (2015); excerpt hosted by Chess Tigers
    url: https://chess-tigers.de/cdn/shop/files/Chess_Endgames_for_Kids.pdf
    type: book
    accessed: 2026-11-11
  - id: s2
    title: "Nunn's Chess Endings (excerpt)"
    publisher: John Nunn, Gambit Publications (2010); excerpt hosted by New in Chess
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/5025.pdf
    type: book
    accessed: 2026-11-11
  - id: s3
    title: "Dvoretsky's Endgame Manual, fifth edition (excerpt with table of contents)"
    publisher: Mark Dvoretsky, revised by Karsten Müller, Russell Enterprises (2020)
    url: https://shop.chess-tigers.de/cdn/shop/files/dem5_excerpt.pdf
    type: book
    accessed: 2026-11-11
  - id: s4
    title: "Chess Strategy (1915), Project Gutenberg eBook #5614"
    publisher: Edward Lasker; Project Gutenberg
    url: https://gutenberg.org/files/5614/5614-h/5614-h.htm
    type: book
    accessed: 2026-11-11
created: 2026-11-11
---

# Triangulation

Triangulation is the standard way for a king to lose a tempo in the endgame. In many king-and-pawn positions the whole game turns on who has to move: the side to move must give ground, so a player who could simply pass would win. Chess has no pass, but a king that walks around a triangle of three adjacent squares comes back to its starting square in three moves, where a direct shuttle would take two. Because three is odd, the same position reappears with the other side to move.[^s1] The manoeuvre works only when the opponent cannot answer it with a triangle of his own, usually because a pawn or the edge of the board takes away the squares he would need, and the result is a decisive zugzwang.[^s1]

## How it works

The idea is a matter of parity. A move that changes nothing about the position is wasted by most pieces only if they can return to their square in an odd number of moves. Edward Lasker pointed out that a knight can never gain a tempo in this way: any square it can reach in an odd number of moves cannot be reached in an even number, so a knight always arrives back with the same side to move.[^s4] A king has no such restriction, because three mutually adjacent squares form a closed loop. In endings with pieces, Lasker shows a bishop losing a move by itself; in pure pawn endings, where a side that runs out of pawn moves must give way with the king, the king's own route is often the only way to pass the move.[^s4]

Endgame manuals treat triangulation as a special case of the theory of corresponding squares. Dvoretsky's manual places it in its pawn-endgame chapter immediately after opposition, corresponding squares and "mined squares", and before other cases of correspondence.[^s3] Seen this way, each square of the attacking king has a matching square the defending king must occupy; triangulation is the attacker's route between such squares that the defender cannot mirror, so he falls out of step.[^s1]

## Key example

In the diagram position (White Kf5, pawns f6 and h5; Black Kf7, pawn h6), White to move would like it to be Black's turn. With Black to move, any king step lets White in: the black king has to give ground and the white king reaches g6 and the h6-pawn, or e6 and the promotion square.[^s1] White therefore goes round a triangle: 1.Ke5 Kf8 2.Kf4 Ke8 3.Ke4. Black cannot keep pace, because the pawn on f6 covers e7 and g7, so his king can only shuffle along the back rank. After 3...Kf7 4.Kf5 the starting position is back with Black to move, and the white king breaks through to g6.[^s1]

Müller gives a queenside example of the same kind. A king on c3 supporting pawns on a2 and b4 against a king on d5 and pawn on b5 walks a short circuit and comes back to c3 with Black to move, reaching the zugzwang that decides the game.[^s1]

## Pitfalls in practice

Triangulation is easy to miss even at grandmaster level, because the winning move looks aimless: the king goes sideways or backwards rather than forwards. Nunn's endgame book uses the game Lutz–Nisipeanu from the 2005/06 Bundesliga. Nunn notes that the critical position could arise with White to move, and then the win required a triangle first. The triangle had to be completed with 7 Kf3, but the game went 7 Kd3, after which Black could hold the draw.[^s2] The usual lessons are to work out which side would be in zugzwang before advancing and to check whether the opponent has squares to answer the triangle with.[^s1] Spare pawn moves matter for the same reason: Lasker shows a defender who holds the opposition but loses because he has no pawn moves left to wait with.[^s4]

## Connections

Triangulation is a technique of king-and-pawn endgames and, like the opposition, depends on zugzwang. The opposition is a static relation between the kings. Triangulation is the dynamic means of transferring the move when the side that wants the opposition does not have it.[^s1] Endgame manuals file it under the theory of corresponding squares,[^s3] and in Müller's teaching it sits beside the opposition as a way of fighting for the key squares in front of a pawn.[^s1]

## Sources

[^s1]: Karsten Müller, *Chess Endgames for Kids* (Gambit Publications, 2015), sample pages including Lesson 14 "Triangulation and More Opposition". https://chess-tigers.de/cdn/shop/files/Chess_Endgames_for_Kids.pdf (accessed 2026-11-11)
[^s2]: John Nunn, *Nunn's Chess Endings* (Gambit Publications, 2010), excerpt including section 2.2.3 "Triangulation" in the contents and the Lutz–Nisipeanu example. https://www.newinchess.com/media/wysiwyg/product_pdf/5025.pdf (accessed 2026-11-11)
[^s3]: Mark Dvoretsky, *Dvoretsky's Endgame Manual*, fifth edition, revised by Karsten Müller (Russell Enterprises, 2020), excerpt with table of contents. https://shop.chess-tigers.de/cdn/shop/files/dem5_excerpt.pdf (accessed 2026-11-11)
[^s4]: Edward Lasker, *Chess Strategy* (1915), chapter V "The End-game", Project Gutenberg eBook #5614. https://gutenberg.org/files/5614/5614-h/5614-h.htm (accessed 2026-11-11)
