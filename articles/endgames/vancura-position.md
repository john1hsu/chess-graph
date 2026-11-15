---
id: kt:vancura-position
type: EndgameType
title: Vancura position
aliases: [Vančura position, Vancura draw, Vančura draw, Vancura defence, Vancura defense, Vančura defence]
domain: endgames
summary: >-
  The standard drawing method in rook and rook's pawn against rook when the attacking rook stands in
  front of a pawn on the sixth rank: the defending rook attacks the pawn from the side and gives
  lateral checks, while the defending king waits on the far side near g7/h7.
fen: "R7/6k1/P7/8/8/5K2/8/r7 b - - 0 1"
status: current
volatile: false
verified: 2026-11-15
broader: [kt:rook-endgames]
related: [kt:philidor-position, kt:lucena-position, kt:fortress]
relations:
  - {predicate: partOf, object: kt:rook-endgames}
  - {predicate: namedAfter, object: kt:josef-vancura}
  - {predicate: contrastsWith, object: kt:philidor-position}
  - {predicate: usesTechnique, object: kt:side-checks}
sources:
  - id: s1
    title: "Karsten Müller: Understanding the Vancura draw"
    publisher: GM Karsten Müller, ChessBase News (2014)
    url: https://en.chessbase.com/post/karsten-mueller-understanding-the-vancura-draw
    type: publication
    accessed: 2026-11-15
  - id: s2
    title: "Vancura and Fellas"
    publisher: GM Alex Fishbein, American Chess Magazine no. 43, hosted by chessjournalism.org
    url: https://chessjournalism.org/wp-content/uploads/2025/06/ACM_043_Instructional-Alex-Fishbein-Vancura-and-Fellas-56e5e37b8f240cfeb8342366dd431b5e.pdf
    type: publication
    accessed: 2026-11-15
  - id: s3
    title: "100 Endgames You Must Know, sixth edition (excerpt: contents and Ending 76)"
    publisher: Jesús de la Villa, New In Chess (2023); excerpt hosted by Chess Tigers
    url: https://shop.chess-tigers.de/cdn/shop/files/100endgames.pdf
    type: book
    accessed: 2026-11-15
  - id: s4
    title: "Dvoretsky's Endgame Manual, fifth edition (excerpt: contents)"
    publisher: Mark Dvoretsky, revised by Karsten Müller, Russell Enterprises (2020); excerpt hosted by Chess Tigers
    url: https://shop.chess-tigers.de/cdn/shop/files/dem5_excerpt.pdf
    type: book
    accessed: 2026-11-15
  - id: s5
    title: "Check Czech Chess: Father and son Josef Vančura"
    publisher: ChessBase News, Study of the Month (July 2020)
    url: https://en.chessbase.com/post/study-of-the-month-2020-07
    type: publication
    accessed: 2026-11-15
  - id: s6
    title: "Josef Vančura"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/vancura.html
    type: publication
    accessed: 2026-11-15
created: 2026-11-15
---

# Vancura position

The Vancura position (also "Vancura draw" or "Vancura defence") is the key drawing set-up in the ending of rook and rook's pawn against rook when the stronger side's rook stands **in front of** its pawn and the pawn has reached the sixth rank. The defending rook does not stand behind the pawn or in front of it; it attacks the pawn **from the side**, along the sixth rank, and is ready to give checks along the files. The defending king, meanwhile, stays on the opposite wing, typically on g7 or h7 against an a-pawn.[^s1] Endgame manuals treat this as its own sub-case: Dvoretsky's *Endgame Manual* has separate sections for the rook in front of a rook's pawn on the seventh rank and on the sixth rank, and de la Villa's *100 Endgames You Must Know* lists "Pawn on the 6th rank. The Vancura Defence" as one of its hundred essential endings.[^s4][^s3]

## Why it holds

With White's rook on a8 and pawn on a6, White would like to march the king to b7 to free the rook. Black's rook on the f-file (or on f6, hitting the pawn sideways) prevents this: whenever the white king approaches the pawn, it is checked from the side, and on the open queenside there is no shelter, because the white rook itself occupies the only covering file.[^s1][^s2] If White instead pushes the pawn to a7, the black rook simply swings to a6 and then behind the pawn, reaching a well-known draw in which the white rook is buried on a8.[^s1][^s2]

The black king's post is not a detail. With the king on g7 or h7, White cannot use the standard trick of pushing a7, offering the rook on the h-file and then winning the black rook with a skewer check on the seventh rank. Müller calls g7/h7 (or g8/h8 when the white rook is on the seventh) the drawing zone; a king on f7 loses to 1.a7 Ra6 2.Rh8! Rxa7 3.Rh7+.[^s1] The ChessBase study column makes the same point about the f7 square.[^s5]

## Example

Alex Fishbein's teaching position (White Kf3, Ra8, a6; Black Kg7, Ra1, Black to move) shows the method. The rook leaves the passive square behind the pawn, gets to the f-file with check, and settles on f6:[^s2]

```pgn
[Event "Vancura position, side-check defence"]
[SetUp "1"]
[FEN "R7/6k1/P7/8/8/5K2/8/r7 b - - 0 1"]
[Result "1/2-1/2"]

1... Rf1+ 2. Ke4 Rf6 3. Kd5 Rf5+ 4. Kc6 Rf6+ 5. Kb5 Rf5+ 6. Kb6 Rf6+ 7. Ka7 Rf7+ 8. Kb8 Rf8+ 9. Kb7 Rf7+ 1/2-1/2
```

The white king can hide nowhere, and if it retreats to escort the pawn, the black rook goes back to attacking it from f6.[^s2]

## Pitfalls for the defender

- **The wrong file for the rook.** Müller shows that checking from the h-file instead of the f-file fails: after ...Rh6? the white king walks to b7 and the checks run out, since the rook is too close to its own king and too far from the action.[^s1]
- **The wrong king square.** Any king move out of the g7/h7 zone, such as ...Kf7, allows the a7 and Rh8 skewer idea above.[^s1][^s5]
- **Staying passive.** A rook kept on the a-file behind or beside the pawn too long lets the attacking king approach; the point of the defence is to transfer the rook to the side in time.[^s2]

The set-up is not only an exercise. Müller cites Carlsen–Aronian, Sinquefield Cup 2014, where White missed a win with 46.h6?? and Black reached the Vancura formation, holding even with White having an extra h-pawn; and Radjabov–Nakamura, Shamkir 2014, where Black saved the game by putting the king on g7 in time.[^s1] De la Villa extends the idea further, showing a Vancura-type set-up that draws against rook and two pawns.[^s3]

## History

The position is named after Josef Vančura (1898–1921), a Prague study composer who died aged 23; the ChessBase study column dates its publication to 1924, after his death, in the Prague daily *28. říjen*, and says it overturned many earlier analyses of the ending.[^s5][^s1] Edward Winter notes that the precise original source and its relationship to earlier analysis by Tarrasch remain unclear, so the dating is best treated as conventional.[^s6] Some sources wrongly give his first name as "Jan".[^s5]

## Connections

The Vancura position is **part of** the theory of **rook endgames**, specifically the rook's-pawn branch that Dvoretsky's manual sets apart.[^s4] It **contrasts with** the **Philidor position** and sits beside the **Lucena position**: those two belong to the general rook-and-pawn-against-rook section of the manuals, while the Vancura defence is specific to a rook's pawn with the enemy rook in front of it, and depends on lateral attack rather than on blocking the pawn's path.[^s4][^s1] It is **named after** Josef Vančura.[^s5] Its core **technique** is the side check, and like a **fortress** it is a set-up the defender can hold indefinitely once established.[^s1][^s2]

## Sources

[^s1]: K. Müller, "Understanding the Vancura draw", ChessBase News (2014). https://en.chessbase.com/post/karsten-mueller-understanding-the-vancura-draw (accessed 2026-11-15)
[^s2]: A. Fishbein, "Vancura and Fellas", *American Chess Magazine* no. 43. https://chessjournalism.org/wp-content/uploads/2025/06/ACM_043_Instructional-Alex-Fishbein-Vancura-and-Fellas-56e5e37b8f240cfeb8342366dd431b5e.pdf (accessed 2026-11-15)
[^s3]: J. de la Villa, *100 Endgames You Must Know*, 6th ed., New In Chess (2023), excerpt. https://shop.chess-tigers.de/cdn/shop/files/100endgames.pdf (accessed 2026-11-15)
[^s4]: M. Dvoretsky, *Dvoretsky's Endgame Manual*, 5th ed., Russell Enterprises (2020), excerpt. https://shop.chess-tigers.de/cdn/shop/files/dem5_excerpt.pdf (accessed 2026-11-15)
[^s5]: "Check Czech Chess: Father and son Josef Vančura", ChessBase News (2020). https://en.chessbase.com/post/study-of-the-month-2020-07 (accessed 2026-11-15)
[^s6]: E. Winter, "Josef Vančura", Chess Notes. https://chesshistory.com/winter/extra/vancura.html (accessed 2026-11-15)
