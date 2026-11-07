---
id: kt:lucena-position
type: EndgameType
title: Lucena position
aliases: [Lucena's position, Lucena, Building a bridge, Bridge-building, Der Brückenbau, Salvio position]
domain: endgames
summary: >-
  The basic winning position in rook and pawn against rook: the stronger side's non-rook pawn stands
  on the seventh rank with its own king on the queening square and the defending king cut off, and
  the win is forced by "building a bridge" with the rook to shelter the king from checks.
fen: "6K1/3k2P1/8/8/8/8/7r/4R3 w - - 0 4"
status: current
volatile: false
verified: 2026-11-07
broader: [kt:rook-endgames]
related: [kt:philidor-position, kt:pawn-promotion, kt:king-and-pawn-endgames]
relations:
  - {predicate: namedAfter, object: kt:luis-ramirez-de-lucena}
  - {predicate: contrastsWith, object: kt:philidor-position}
  - {predicate: usesTechnique, object: kt:cutting-off-the-king}
sources:
  - id: s1
    title: "The Lucena Position"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/lucena.html
    type: reference
    accessed: 2026-11-07
  - id: s2
    title: "Theoretical Rook Endgames (sample pages)"
    publisher: Sam Shankland, Quality Chess (excerpt hosted by New In Chess)
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/8903.pdf
    type: book
    accessed: 2026-11-07
  - id: s3
    title: "100 Endgames You Must Know, sixth edition (sample pages)"
    publisher: Jesús de la Villa, New In Chess (excerpt hosted by Chess Tigers)
    url: https://shop.chess-tigers.de/cdn/shop/files/100endgames.pdf
    type: book
    accessed: 2026-11-07
  - id: s4
    title: "Lucena Position"
    publisher: Chess.com (Chess Terms)
    url: https://www.chess.com/terms/lucena-position-chess
    type: publication
    accessed: 2026-11-07
  - id: s5
    title: "The Two Rook Endings You Must Know"
    publisher: GM Daniel Naroditsky, Chess.com
    url: https://www.chess.com/article/view/the-two-rook-endings-you-must-know
    type: publication
    accessed: 2026-11-07
  - id: s6
    title: "\"Simple\" Rook and Pawn vs Rook - Part 1: Cases Where the Pawn Wins"
    publisher: Charlotte Chess Center
    url: https://www.charlottechesscenter.org/post/simple-rook-and-pawn-vs-rook-part-1-cases-where-the-pawn-wins
    type: community
    accessed: 2026-11-07
created: 2026-11-07
---

# Lucena position

The Lucena position is the target every player with an extra pawn in a rook ending is trying to reach. The attacker's pawn has reached the seventh rank, but its own king stands on the queening square in front of it; the attacking rook cuts the defending king off by at least one file, and the defending rook waits on the far side of the pawn ready to give checks.[^s4] From here the stronger side wins by force, provided the pawn is not a rook pawn.[^s4] Endgame manuals treat it as core knowledge: Jesús de la Villa's *100 Endgames You Must Know* devotes an ending to it under the heading "Lucena Position. The bridge",[^s3] and Sam Shankland's *Theoretical Rook Endgames* opens with a chapter on it.[^s2]

## The problem and the idea

The difficulty is that the pawn cannot advance while its own king blocks it, and as soon as the king steps aside the defending rook starts checking from behind and from the side.[^s4] The king cannot simply run away from the checks, because it must stay close enough to protect the pawn.[^s4] The solution, usually called "building a bridge", is to bring the rook to the fourth rank (the fifth when the attacker has Black). The king then walks out towards the checking rook, and when the checks run out of space the rook interposes on the fourth rank, shielding the king and leaving the pawn free to queen.[^s4] Naroditsky stresses that the mechanism works wherever the other pieces stand, as long as the pawn is not on the a- or h-file.[^s5]

A teaching sequence from the Charlotte Chess Center breaks the method into four ordered steps: cut the defending king off from the pawn's file, advance the pawn to the seventh, check the king further away, and then build the bridge.[^s6] Doing these out of order can throw away the win.[^s6]

## Example

In the diagram position (FEN above) White has king g8, pawn g7 and rook e1 against Black's king d7 and rook h2, with White to move. This position arises in the Charlotte Chess Center's first exercise after 3...Kd7, and their solution continues 4.Re4 Rh1 5.Kf7 Rf1+ 6.Kg6 Rg1+ 7.Kf6 Rf1+ 8.Kg5 Rg1+ 9.Rg4, when the rook blocks the last check and the pawn cannot be stopped.[^s6] Note the zig-zag king walk: the king alternates between the f- and g-files so that every check brings it one rank nearer to the rook on e4.[^s6]

```pgn
[Event "Lucena position: building a bridge"]
[SetUp "1"]
[FEN "6K1/3k2P1/8/8/8/8/7r/4R3 w - - 0 4"]
[Result "*"]

4. Re4 Rh1 5. Kf7 Rf1+ 6. Kg6 Rg1+ 7. Kf6 Rf1+ 8. Kg5 Rg1+ 9. Rg4 *
```

## Pitfalls and limits

Two practical traps are worth knowing. If the defending king approaches the rook on the fourth rank, the attacker can switch the rook to the eighth rank to guard the queening square and then chase the enemy rook with the king; and if the defender simply waits, putting the rook on the fifth rank instead of the fourth can allow the pawn to be captured.[^s4] With a rook pawn the bridge does not work, because the defending king has room to step aside; Shankland notes that a single rook pawn on the seventh wins only if the defending king is badly misplaced,[^s2] and the Charlotte Chess Center adds that such cases need the king cut off much further away, with a different rook manoeuvre.[^s6] Many rook endings with a pawn further back are won precisely by steering into the Lucena position: several of Shankland's examples end with the note that the Lucena position is coming.[^s2]

## History of the name

The name is a historical mistake. Edward Winter summarises research by John Roycroft (*BCM*, 1982) showing that the position does not appear in Luis Ramírez de Lucena's 1497 book.[^s1] Roycroft found it in Alessandro Salvio's *Il Puttino* (1634), where it is credited to Scipione Genovino, and Thomas Niessen later pointed to an older, probably sixteenth-century manuscript containing it.[^s1] Niessen traced the misattribution to Constantin Schwede's 1880 edition of the *Handbuch des Schachspiels*, from where it passed into Berger's endgame book and Reuben Fine's *Basic Chess Endings* (1941).[^s1] The German term *Der Brückenbau* ("building a bridge") appeared in Nimzowitsch's *Mein System* (1925).[^s1]

## Connections

The Lucena position is the central winning case of **rook endgames**, and its natural counterpart is the **Philidor position**, the "third-rank defence" that Naroditsky presents alongside it as a drawing tool: one shows how the attacker breaks through, the other how the defender holds.[^s5] The whole method rests on **cutting off the king** with the rook, the first of the four steps,[^s6] and ends in **pawn promotion**. It is **named after Luis Ramírez de Lucena**, though the attribution is wrong.[^s1] If the rooks are exchanged along the way, the play reduces to a **king and pawn endgame** in which the pawn simply queens.[^s4]

## Sources
[^s1]: E. Winter, "The Lucena Position", Chess Notes. https://chesshistory.com/winter/extra/lucena.html (accessed 2026-11-07)
[^s2]: S. Shankland, *Theoretical Rook Endgames*, Quality Chess, sample pages. https://www.newinchess.com/media/wysiwyg/product_pdf/8903.pdf (accessed 2026-11-07)
[^s3]: J. de la Villa, *100 Endgames You Must Know*, 6th edition, New In Chess (2023), sample pages. https://shop.chess-tigers.de/cdn/shop/files/100endgames.pdf (accessed 2026-11-07)
[^s4]: Chess.com, "Lucena Position", Chess Terms. https://www.chess.com/terms/lucena-position-chess (accessed 2026-11-07)
[^s5]: D. Naroditsky, "The Two Rook Endings You Must Know", Chess.com. https://www.chess.com/article/view/the-two-rook-endings-you-must-know (accessed 2026-11-07)
[^s6]: Charlotte Chess Center, "\"Simple\" Rook and Pawn vs Rook - Part 1: Cases Where the Pawn Wins". https://www.charlottechesscenter.org/post/simple-rook-and-pawn-vs-rook-part-1-cases-where-the-pawn-wins (accessed 2026-11-07)
