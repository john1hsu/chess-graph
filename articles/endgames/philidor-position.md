---
id: kt:philidor-position
type: EndgameType
title: Philidor position
aliases: [Philidor's position, Third-rank defence, Third-rank defense, Philidor's third-rank defence, Philidor drawing method]
domain: endgames
summary: >-
  The basic drawing method in rook and pawn against rook: with the defending king on the queening
  square, the defending rook holds its third rank to keep the attacking king out, and once the pawn
  advances it drops to the far end of the board to check from behind.
fen: "4k3/R7/8/4PK2/8/8/1r6/8 b - - 0 1"
status: current
volatile: false
verified: 2026-11-08
broader: [kt:rook-endgames]
related: [kt:lucena-position, kt:king-and-pawn-endgames, kt:pawn-promotion]
relations:
  - {predicate: contrastsWith, object: kt:lucena-position}
  - {predicate: namedAfter, object: kt:francois-andre-danican-philidor}
  - {predicate: usesTechnique, object: kt:cutting-off-the-king}
  - {predicate: alternativeTo, object: kt:passive-rook-defence}
sources:
  - id: s1
    title: "Philidor Position"
    publisher: Chess.com (Chess Terms)
    url: https://chess.com/terms/philidor-position-chess
    type: publication
    accessed: 2026-11-08
  - id: s2
    title: "The Two Rook Endings You Must Know"
    publisher: GM Daniel Naroditsky, Chess.com
    url: https://www.chess.com/article/view/the-two-rook-endings-you-must-know
    type: publication
    accessed: 2026-11-08
  - id: s3
    title: "You thought you knew the Philidor Position"
    publisher: GM Alex Fishbein, American Chess Magazine no. 34 (2023), hosted by chessjournalism.org
    url: https://chessjournalism.org/wp-content/uploads/2024/06/ACM_34-Instructional-A.-Fishbein_You-thought-you-knew-the-Philidor-Position.pdf
    type: publication
    accessed: 2026-11-08
  - id: s4
    title: "100 Endgames You Must Know, fourth edition (sample pages)"
    publisher: Jesús de la Villa, New In Chess (2015)
    url: https://download.boekhuis.nl/9789056916176_fragm-docb.pdf
    type: book
    accessed: 2026-11-08
  - id: s5
    title: "Analysis of the game of chess; a new edition, greatly enlarged (London: P. Elmsley, 1777)"
    publisher: Max Planck Digital Library eBooks catalogue (Eighteenth Century Collections Online, British Library copy)
    url: https://ebooks.mpdl.mpg.de/ebooks/Record/EB000465577
    type: archive
    accessed: 2026-11-08
  - id: s6
    title: "Philidor's \"L'Analyze des Echecs\""
    publisher: Thomas W. Ewers, ChessBase News (2016)
    url: https://en.chessbase.com/post/philidor-s-l-analyze-des-echecs
    type: publication
    accessed: 2026-11-08
created: 2026-11-08
---

# Philidor position

The Philidor position is the defender's half of rook and pawn against rook. The weaker side's king stands on the pawn's queening square, the attacker's pawn has not yet reached the defender's third rank, and the defending rook can move freely along that third rank (the sixth rank when Black defends).[^s1] Handled correctly it is a dead draw. Grandmaster Alex Fishbein calls it the most important theoretical position in rook endings,[^s3] Daniel Naroditsky teaches it as one of the two rook endings every improving player must know,[^s2] and Jesús de la Villa's *100 Endgames You Must Know* gives it its own entry, Ending 52, in the chapter on rook and pawn against rook.[^s4]

## How the defence works

The method has two phases. In the first, the defending rook sits on its third rank and simply waits there, shuttling along the rank if necessary. From there it cuts the attacking king off: the king cannot step in front of its pawn to the sixth rank, so it has no route to the threatening squares beside the defending king.[^s1] Checking straight away is wrong, because the attacking king can then walk up behind its own pawn and use it as a shield while creating mating threats.[^s1] Rook checks on the rank are answered by stepping aside, and waiting moves by waiting moves; as long as the rook stays on the third rank, the defender is safe.[^s1]

The second phase starts when the attacker, having no other way to make progress, pushes the pawn onto the third rank. Now the pawn no longer gives its king any cover, so the defending rook drops to the far end of the board and checks from behind; the attacking king can neither hide nor approach its pawn without abandoning it.[^s1] If instead the attacking king drifts away from the pawn, the defender simply wins the pawn.[^s1] The other attempt, putting the attacking rook on the third rank to contest it, leads to a rook trade and a drawn king and pawn ending.[^s2]

## Example

In Fishbein's diagram, labelled "Philidor Position, 1777", White has king f5, rook a7 and pawn e5, Black has king e8 and rook b2, and it is Black to move.[^s3] The correct defence is 1...Rb6, occupying the sixth rank. White's best is a rook trade into a drawn pawn ending, and if the pawn advances with 2.e6, then 2...Rb1 goes to the back of the board and the White king has nowhere to escape the checks from behind.[^s3]

```pgn
[Event "Philidor position: third-rank defence"]
[SetUp "1"]
[FEN "4k3/R7/8/4PK2/8/8/1r6/8 b - - 0 1"]
[Result "*"]

1... Rb6 2. e6 Rb1 *
```

Naroditsky's example, from Black's attacking side, shows the same mechanism: after the pawn push 60...f3, threatening mate with ...Kg3, the defender answers 61.Rc8!, and after 61...Kg3 62.Rg8+ the attacking king can do nothing against the checks.[^s2]

## Pitfalls and refinements

The main practical error is giving up the third rank too early, either by checking at once or by sitting passively on the back rank. Fishbein notes that a purely passive defence works only against a knight or rook pawn,[^s3] so against a central or bishop pawn the third-rank method is the reliable choice. He also shows that the "simple" ending is full of traps at master level, citing errors in games such as Aronian–Carlsen (Moscow 2006) and Kosten–Schroll (Austrian Team Championship 2004), and explains a second method, credited to Max Karstedt (1897), which shows that the diagram position is also drawn with White to move, long thought to be a win.[^s3] Those refinements matter mostly to strong players; for club players the essential lesson is to reach the third-rank set-up before the attacking king gets there.

## A note on the name

François-André Danican Philidor's treatise first appeared in 1749 as *L'analyze des échecs*, and a greatly enlarged edition was published in English in London in 1777.[^s5] Fishbein's diagram is captioned with that 1777 date.[^s3] The name is ambiguous: "Philidor position" is also used for a winning position in rook and bishop against rook, the only endgame analysed in the 1749 edition.[^s6] This article covers the rook and pawn against rook drawing method.

## Connections

The Philidor position is a basic case of **rook endgames** and the natural partner of the **Lucena position**: Naroditsky presents the two together as the drawing and winning ends of the same material balance.[^s2] It works by **cutting off the king**, using the rook on the third rank to keep the attacking king from advancing past its pawn,[^s1] and it is the more active **alternative to passive rook defence** on the back rank, which Fishbein limits to knight and rook pawns.[^s3] When the attacker trades rooks to escape the checks, the game reduces to a drawn **king and pawn endgame**,[^s2] and the whole defence exists to stop **pawn promotion**. It is **named after François-André Danican Philidor**.[^s3]

## Sources
[^s1]: Chess.com, "Philidor Position", Chess Terms. https://chess.com/terms/philidor-position-chess (accessed 2026-11-08)
[^s2]: D. Naroditsky, "The Two Rook Endings You Must Know", Chess.com. https://www.chess.com/article/view/the-two-rook-endings-you-must-know (accessed 2026-11-08)
[^s3]: A. Fishbein, "You thought you knew the Philidor Position", *American Chess Magazine* no. 34 (2023). https://chessjournalism.org/wp-content/uploads/2024/06/ACM_34-Instructional-A.-Fishbein_You-thought-you-knew-the-Philidor-Position.pdf (accessed 2026-11-08)
[^s4]: J. de la Villa, *100 Endgames You Must Know*, 4th edition, New In Chess (2015), sample pages. https://download.boekhuis.nl/9789056916176_fragm-docb.pdf (accessed 2026-11-08)
[^s5]: A. D. Philidor, *Analysis of the game of chess*, new edition, London: P. Elmsley, 1777; catalogue record, Max Planck Digital Library (ECCO). https://ebooks.mpdl.mpg.de/ebooks/Record/EB000465577 (accessed 2026-11-08)
[^s6]: T. W. Ewers, "Philidor's \"L'Analyze des Echecs\"", ChessBase News (2016). https://en.chessbase.com/post/philidor-s-l-analyze-des-echecs (accessed 2026-11-08)
