---
id: kt:rook-endgames
type: EndgameType
title: Rook endgames
aliases: [Rook endings, Rook and pawn endgames, Rook and pawn endings, Rook endgame]
domain: endgames
summary: >-
  Endgames in which each side's remaining pieces are rooks (usually one each) plus pawns; they are the
  most frequent type of endgame in practice, and their outcome depends heavily on the activity of rook
  and king rather than on material alone.
fen: "R7/6k1/P4r2/8/3K4/8/8/8 w - - 0 1"
status: current
volatile: false
verified: 2026-11-10
broader: [kt:chess-endgame]
related: [kt:passed-pawn, kt:endgame-tablebases]
relations:
  - {predicate: hasPart, object: kt:lucena-position}
  - {predicate: hasPart, object: kt:philidor-position}
  - {predicate: hasPart, object: kt:vancura-position}
  - {predicate: usesTechnique, object: kt:cutting-off-the-king}
sources:
  - id: s1
    title: "Understanding Rook Endgames"
    publisher: Karsten Müller and Yakov Konoval, Gambit Publications (2016); New In Chess shop page
    url: https://www.newinchess.com/understanding-rook-endgames
    type: book
    accessed: 2026-11-10
  - id: s2
    title: "Dvoretsky's Endgame Manual, fourth edition (excerpt: contents)"
    publisher: Mark Dvoretsky, Russell Enterprises (2014); excerpt hosted by New In Chess
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/2703.pdf
    type: book
    accessed: 2026-11-10
  - id: s3
    title: "Now For Rook Endings"
    publisher: Tatev Abrahamyan, Chess Life (US Chess), September 2023
    url: https://pubs.royle.com/article/Now+For+Rook+Endings/4628396/800160/article.html
    type: publication
    accessed: 2026-11-10
  - id: s4
    title: "Vancura and Fellas"
    publisher: GM Alex Fishbein, American Chess Magazine no. 43, hosted by chessjournalism.org
    url: https://chessjournalism.org/wp-content/uploads/2025/06/ACM_043_Instructional-Alex-Fishbein-Vancura-and-Fellas-56e5e37b8f240cfeb8342366dd431b5e.pdf
    type: publication
    accessed: 2026-11-10
  - id: s5
    title: "Karsten Müller: Understanding the Vancura draw"
    publisher: ChessBase News (2014)
    url: https://en.chessbase.com/post/karsten-mueller-understanding-the-vancura-draw
    type: publication
    accessed: 2026-11-10
  - id: s6
    title: "Some rook endings are drawn, some are not"
    publisher: Karsten Müller, ChessBase News (2025)
    url: https://en.chessbase.com/post/some-rook-endings-are-drawn-some-are-not
    type: publication
    accessed: 2026-11-10
created: 2026-11-10
---

# Rook endgames

Rook endgames are endings in which the only pieces left besides the kings are rooks, most often one rook each, with pawns. They are the most common class of endgame: Gambit's description of Müller and Konoval's *Understanding Rook Endgames* calls rook-and-pawn endings the most frequently occurring in chess and estimates that they arise in roughly one game in ten.[^s1] Because rooks tend to stay on the board after the minor pieces have been traded, a club player who knows the key methods will use them far more often than knowledge of any other ending.[^s1]

## Structure of the theory

Endgame manuals divide the subject by material. Mark Dvoretsky's *Endgame Manual* has a chapter on rook against pawns (with headings such as cutting the king off, shouldering and outflanking) and a separate chapter on rook endgames that runs from rook and pawn against rook, sorted by how far the pawn has advanced, through rook and rook's pawn against rook, to positions with several pawns.[^s2] The single-pawn case contains the two positions every player must know, the **Lucena position** (the winning method of "building a bridge") and the **Philidor position** (the third-rank drawing defence); Tatev Abrahamyan's *Chess Life* series on rook endings teaches both as the foundation.[^s3] Theory is still moving: Müller and Konoval use six- and seven-piece tablebases to re-evaluate classic rook endings.[^s1]

## Key principles

**Activity before material.** The dominant theme is rook activity. Abrahamyan advises that giving up a pawn is often better than accepting a passive rook, and notes that an extra pawn frequently fails to win.[^s3] Karsten Müller's examples point the same way: some rook endings with two extra pawns are drawn, while some with equal pawns are lost because one side's pieces are much more active.[^s6]

**Rooks behind passed pawns.** The so-called Tarrasch rule says a rook belongs behind a passed pawn, whether it is one's own (to support its advance) or the opponent's (to stop it while staying mobile). Alex Fishbein calls the rule fundamental but notes that it holds most of the time, not always.[^s4] Abrahamyan adds the practical corollary that one's own passed pawns should be pushed, since they grow more dangerous as they advance.[^s3]

**Cut off the king.** A rook on an open rank or file can shut the enemy king out of play, for example on the second or seventh rank, where it also attacks pawns.[^s3] Cutting off the king is also the basic method in rook against pawn, as Dvoretsky's chapter headings show.[^s2]

**Checking distance.** A defending rook needs room. Abrahamyan recommends keeping it at least three squares from the enemy king so that its checks cannot be blocked or escaped by the king approaching it.[^s3] Fishbein stresses side checks, along the ranks, as the defender's main weapon, especially against rook's pawns.[^s4]

## Example: the Vancura draw

Rook's-pawn endings are notoriously drawish, because the attacking king cannot hide from side checks behind its pawn.[^s4] In the basic Vancura position (White king d4, rook a8, pawn a6; Black king g7, rook f6), Black's rook defends from the side, attacking the pawn and checking the white king whenever it approaches, while the black king on g7 rules out tactical tricks on the seventh rank.[^s5] Müller's model line:[^s5]

```pgn
[Event "Vancura position"]
[SetUp "1"]
[FEN "R7/6k1/P4r2/8/3K4/8/8/8 w - - 0 1"]
[Result "1/2-1/2"]

1. Ke5 Rb6 2. Kd5 Rf6 3. Kc5 Rf5+ 4. Kb6 Rf6+ 5. Ka7 Rf7+ 6. Kb8 Rf8+ 7. Kb7 Rf7+ 8. Kc6 Rf6+ 9. Kd5 Rb6 10. a7 Ra6 1/2-1/2
```

The white king finds no shelter from the checks, and once the pawn reaches a7 the black rook simply returns behind it. Josef Vancura, a Czech study composer who died young in 1921, discovered the idea, and it was published in 1924.[^s4]

## Common mistakes

The typical errors are psychological as much as technical: putting the rook passively in front of a pawn to guard material, checking from too close, and assuming the ending is a "sure draw". The witticism that all rook endings are drawn, attributed to Tarrasch or to Tartakower, captures their drawish tendency, but as Müller points out the defender still has to find the right moves.[^s6] Abrahamyan's advice is to drill the basic positions until they can be executed reliably over the board.[^s3]

## Connections

Rook endgames are a major branch of the **chess endgame**. They **contain** the **Lucena** and **Philidor positions**, the two cornerstones of rook and pawn against rook,[^s3] and the **Vancura position**, the side-check defence against a rook's pawn.[^s4] Their most important technique is **cutting off the king**.[^s3] They are largely about the fate of **passed pawns**, which the Tarrasch rule tells the rooks how to handle,[^s4] and their modern theory is being rewritten with **endgame tablebases**.[^s1]

## Sources
[^s1]: K. Müller and Y. Konoval, *Understanding Rook Endgames*, Gambit Publications (2016), publisher's description on New In Chess. https://www.newinchess.com/understanding-rook-endgames (accessed 2026-11-10)
[^s2]: M. Dvoretsky, *Dvoretsky's Endgame Manual*, 4th edition, Russell Enterprises (2014), excerpt. https://www.newinchess.com/media/wysiwyg/product_pdf/2703.pdf (accessed 2026-11-10)
[^s3]: T. Abrahamyan, "Now For Rook Endings", *Chess Life*, September 2023. https://pubs.royle.com/article/Now+For+Rook+Endings/4628396/800160/article.html (accessed 2026-11-10)
[^s4]: A. Fishbein, "Vancura and Fellas", *American Chess Magazine* no. 43. https://chessjournalism.org/wp-content/uploads/2025/06/ACM_043_Instructional-Alex-Fishbein-Vancura-and-Fellas-56e5e37b8f240cfeb8342366dd431b5e.pdf (accessed 2026-11-10)
[^s5]: K. Müller, "Understanding the Vancura draw", ChessBase News (2014). https://en.chessbase.com/post/karsten-mueller-understanding-the-vancura-draw (accessed 2026-11-10)
[^s6]: K. Müller, "Some rook endings are drawn, some are not", ChessBase News (2025). https://en.chessbase.com/post/some-rook-endings-are-drawn-some-are-not (accessed 2026-11-10)
