---
id: kt:passed-pawn
type: StrategicConcept
title: Passed pawn
aliases: [Passer, Passed pawns, Free pawn, Outside passed pawn, Distant passed pawn, Protected passed pawn, Connected passed pawns]
domain: endgames
summary: >-
  A pawn with no enemy pawn in front of it on its own file or on either adjacent file, so that no
  pawn can stop it from reaching the promotion square; its value grows as pieces are exchanged and
  it is often the decisive factor in endgames.
fen: "8/5pk1/6p1/P7/8/6P1/5PK1/8 w - - 0 1"
status: current
volatile: false
verified: 2026-11-10
broader: [kt:pawn-structure, kt:chess-endgame]
related: [kt:king-and-pawn-endgames, kt:rule-of-the-square, kt:rook-endgames, kt:breakthrough]
relations:
  - {predicate: leadsTo, object: kt:pawn-promotion}
  - {predicate: counteredBy, object: kt:blockade}
  - {predicate: championedBy, object: kt:aron-nimzowitsch}
sources:
  - id: s1
    title: "Passed Pawn"
    publisher: Chess.com (Chess Terms)
    url: https://www.chess.com/terms/passed-pawn
    type: publication
    accessed: 2026-11-10
  - id: s2
    title: "Chess Fundamentals (1921), Project Gutenberg eBook #33870"
    publisher: José Raúl Capablanca, Harcourt, Brace and Howe; Project Gutenberg
    url: https://gutenberg.org/cache/epub/33870/pg33870-images.html
    type: book
    accessed: 2026-11-10
  - id: s3
    title: "Chess Strategy (1915), Project Gutenberg eBook #5614"
    publisher: Edward Lasker; Project Gutenberg
    url: https://gutenberg.org/cache/epub/5614/pg5614-images.html
    type: book
    accessed: 2026-11-10
  - id: s4
    title: "My System (excerpt)"
    publisher: Aron Nimzowitsch, Quality Chess (2007 edition)
    url: https://qualitychess.co.uk/wp-content/uploads/2024/02/MySystem-excerpt.pdf
    type: book
    accessed: 2026-11-10
  - id: s5
    title: "Dvoretsky's Endgame Manual, fifth edition (excerpt with table of contents)"
    publisher: Mark Dvoretsky, revised by Karsten Müller, Russell Enterprises (2020)
    url: https://shop.chess-tigers.de/cdn/shop/files/dem5_excerpt.pdf
    type: book
    accessed: 2026-11-10
  - id: s6
    title: "The Passed Pawn: Power of the Passer (publisher's description)"
    publisher: Efstratios Grivas, Thinkers Publishing (2022)
    url: https://chess-tigers.de/products/the-passed-pawn
    type: book
    accessed: 2026-11-10
created: 2026-11-10
---

# Passed pawn

A passed pawn, or "passer", is a pawn that no enemy pawn can stop on its way to promotion: there is no opposing pawn in front of it on its own file or on either neighbouring file.[^s1] A pawn on c5 is passed if Black has no pawns on the b-, c- or d-files ahead of it; a pawn on d5 facing a black pawn on d6 is not, however strong it looks.[^s1] Because a passer that reaches the last rank becomes a queen (or another piece), every passed pawn is a standing threat, and much of endgame play is about creating, escorting or stopping one.

## Why passed pawns matter

Capablanca put the key principle simply: a passed pawn gains strength as the number of pieces on the board goes down, and an isolated passer is either very weak or very strong, its strength or weakness growing as it advances.[^s2] In the middlegame a passer may be little more than a target, but once the pieces are traded there are fewer defenders able to stop it.[^s1] Nimzowitsch, who gave the passed pawn its own chapter in *My System*, wrote that he felt it possessed a soul, and spoke of its "lust to expand".[^s4] Even when it does not promote, an advanced passer ties down enemy pieces and controls squares in the enemy camp; a protected passer on d5 covers c6 and e6.[^s1]

## Kinds of passed pawn

Endgame manuals treat several types separately. Dvoretsky's manual has sections on the outside passed pawn, the protected passed pawn and two connected passed pawns, alongside the king-versus-passed-pawns material on the rule of the square and pawn races.[^s5]

- **Outside (distant) passed pawn.** A passer on a wing far from the other pawns, usually on the a- or h-file.[^s1] Edward Lasker called the distant passed pawn the most important type of passed-pawn ending: the defending king must go and capture it, and meanwhile the attacking king walks into the abandoned pawns on the other wing.[^s3] In the constructed position in the `fen`, White's a-pawn is such a passer; Black's king must leave the kingside to stop it.
- **Protected passed pawn.** A passer defended by another pawn, such as a d5-pawn guarded from e4. The enemy king cannot simply capture it.[^s1]
- **Connected passed pawns.** Two passers on adjacent files protect each other as they advance. Lasker noted that two passed pawns that have reached the sixth rank win even when their king is far away, and advised moving united pawns, when attacked by a bishop, to squares of the bishop's opposite colour.[^s3]

## Creating a passed pawn

A passer usually comes from a pawn majority on one wing or from a pawn **breakthrough**. Capablanca noted that whenever three or more pawns face each other there is a chance for one side to obtain a passed pawn.[^s2] His classic example has White pawns on a5, b5 and c5 against Black pawns on a7, b7 and c7; with White to move, advancing the middle pawn forces a queen.[^s2]

```pgn
[Event "Breakthrough (after Capablanca, Chess Fundamentals, example 24)"]
[SetUp "1"]
[FEN "6k1/ppp5/8/PPP5/8/8/8/6K1 w - - 0 1"]
[Result "*"]

1. b6 axb6 (1... cxb6 2. a6 bxa6 3. c6) 2. c6 bxc6 3. a6 *
```

Whichever pawn Black uses to capture, one white pawn runs through and the kings are too far away. Capablanca adds that with Black to move, Black should not try for a passer of his own, as White's pawns would then be nearer to queening, and the position should be drawn with correct play.[^s2] When both sides have passers, he and Lasker both recommend simply counting the moves each pawn needs to queen.[^s2][^s3]

## Stopping a passed pawn

The defender's first resource is the king: if it can reach and command the queening square, it can usually hold.[^s3] Pieces are the second line of defence. Nimzowitsch's chapter is built around **blockading** the passer, with sections on the functions of the blockading piece and on the struggle against it.[^s4] In rook endings, Lasker showed that a rook placed behind a passed pawn condemns the opposing rook to passivity, a theme Dvoretsky's manual develops in sections on the rook behind, in front of and beside the pawn.[^s3][^s5] Grivas's monograph covers both middlegame and endgame play with passers, including blockade techniques and the exchanges that increase a passed-pawn advantage.[^s6]

## Common mistakes

Pushing a passer too early, before it is supported, often just loses it; Nimzowitsch devoted a section to when a passed pawn should advance and when it can be considered ready to move.[^s4] The opposite error is to trade pieces carelessly when the opponent has the passer, since each exchange makes it stronger.[^s2] Finally, against an outside passer the defender must count precisely whether his king can catch it and still return in time.[^s3]

## Connections

The passed pawn is a feature of **pawn structure** and one of the central themes of the **chess endgame**. It **leads to** **pawn promotion**, is **countered by** the **blockade**, and was **championed** as a strategic theme by Aron Nimzowitsch.[^s4] It dominates **king and pawn endgames**, where the **rule of the square** tells whether the king can catch it, and **rook endgames**, where the rook's placement relative to the passer is critical; a **breakthrough** is a common way to create one.[^s2][^s5]

## Sources
[^s1]: Chess.com, "Passed Pawn" (Chess Terms). https://www.chess.com/terms/passed-pawn (accessed 2026-11-10)
[^s2]: J. R. Capablanca, *Chess Fundamentals* (1921), Project Gutenberg eBook #33870. https://gutenberg.org/cache/epub/33870/pg33870-images.html (accessed 2026-11-10)
[^s3]: E. Lasker, *Chess Strategy* (1915), Project Gutenberg eBook #5614. https://gutenberg.org/cache/epub/5614/pg5614-images.html (accessed 2026-11-10)
[^s4]: A. Nimzowitsch, *My System*, Quality Chess (2007 edition), excerpt. https://qualitychess.co.uk/wp-content/uploads/2024/02/MySystem-excerpt.pdf (accessed 2026-11-10)
[^s5]: M. Dvoretsky, *Dvoretsky's Endgame Manual*, fifth edition, rev. K. Müller, Russell Enterprises (2020), excerpt. https://shop.chess-tigers.de/cdn/shop/files/dem5_excerpt.pdf (accessed 2026-11-10)
[^s6]: E. Grivas, *The Passed Pawn: Power of the Passer*, Thinkers Publishing (2022), publisher's description. https://chess-tigers.de/products/the-passed-pawn (accessed 2026-11-10)
