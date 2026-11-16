---
id: kt:allumwandlung
type: ProblemTheme
title: Allumwandlung
aliases: [AUW, Allumwandlung theme, Total promotion, Omnipromotion, Four-promotion task]
domain: variants-and-compositions
summary: >-
  A chess composition task, abbreviated AUW, in which promotions to all four possible pieces (queen,
  rook, bishop and knight) occur in the solution of one problem or study.
status: current
volatile: false
verified: 2026-11-16
fen: "7Q/3P2K1/P1PkB3/8/8/8/8/8 w - - 0 1"
broader: [kt:chess-problems]
related: [kt:excelsior, kt:babson-task, kt:endgame-study, kt:selfmate, kt:helpmate, kt:stalemate]
relations:
  - {predicate: dependsOn, object: kt:pawn-promotion}
  - {predicate: usesTechnique, object: kt:underpromotion}
sources:
  - id: s1
    title: "Chess Problems: Tasks and Records (3rd edition), Chapter 14: Pawn Promotion"
    publisher: Jeremy Morse; hosted by the British Chess Problem Society (The Problemist)
    url: https://www.theproblemist.org/dloads/cjm/Chapter_14.pdf
    type: book
    accessed: 2026-11-16
  - id: s2
    title: "Chess Problems: Tasks and Records (3rd edition), Chapter 15: The Babson Task"
    publisher: Jeremy Morse; hosted by the British Chess Problem Society (The Problemist)
    url: https://www.theproblemist.org/dloads/cjm/Chapter_15.pdf
    type: book
    accessed: 2026-11-16
  - id: s3
    title: "Underpromotion Milestones"
    publisher: Harold van der Heijden, ChessBase News (25 October 2024)
    url: https://en.chessbase.com/post/underpromotion-milestones
    type: publication
    accessed: 2026-11-16
  - id: s4
    title: "AUW (Allumwandlung)"
    publisher: Peter Wong, OzProblems
    url: https://www.ozproblems.com/problem-world/auw
    type: community
    accessed: 2026-11-16
  - id: s5
    title: "Endgame Explorations 7: Underpromotion (Part 2)"
    publisher: Noam Elkies, originally in Chess Horizons; hosted at chabris.com (ACJ Extra)
    url: https://www.chabris.com/pub/acj/extra/Elkies/Elkies07.html
    type: publication
    accessed: 2026-11-16
created: 2026-11-16
---

# Allumwandlung

Allumwandlung is German for "total promotion", and problemists abbreviate it to AUW. A composition shows the theme when the solution contains promotions to all four pieces a pawn can become: queen, rook, bishop and knight.[^s4] Jeremy Morse, in his survey of problem tasks and records, notes that this quartet of promotions has always fascinated task composers.[^s1] The promotions may all be made by one pawn in different variations, or shared out among several pawns; when White and Black pawns divide the four promotions between them, the result is called a mixed AUW.[^s4]

## Why it is hard

A queen is the natural promotion, so a composer has to give a concrete reason why each of the other three pieces is the only one that works. The usual motives are avoiding stalemate (a queen or rook would take the last flight squares or leave Black without a move), avoiding a check or guard that spoils the intended mate, and the knight's ability to give check or cover squares no line piece can reach.[^s3][^s5] Noam Elkies points out that a rook promotion is already unusual in practical play and that a forced bishop promotion is rarer still, which is why a single position needing all four is a test of construction.[^s5]

## Forms and history

Morse distinguishes promotions *in parallel*, where one pawn promotes to different pieces in different variations, from *successive* promotions within a single line, which he calls the easier task. White AUW in parallel first appeared, according to Morse, on the second move of a three-mover by Shinkman in 1883, while Black AUW in parallel needs at least four moves and was first achieved by Wurzburg in 1913.[^s1] Harold van der Heijden dates the earliest AUW problems to 1859 and calls Niels Høeg's 1905 three-mover a perfect orthodox example.[^s3] In Høeg's problem the key 1.f7 prepares the promotion on f8, and each of Black's four defences decides which piece the pawn has to become.[^s4]

The endgame study was much slower. Van der Heijden recounts that a thematic tourney in *L'Échiquier* in the late 1920s received no correct AUW study, and that Henri Rinck called it a Himalaya of chess that would never be conquered. Sigurd Clausén published one in 1927 that was later found unsound, and Harold Lommer's 1933 study was long regarded as the first success; in its main lines a queen promotion fails because it stalemates Black.[^s3] Elkies places Lommer's study a year ahead of Herbstmann's 1934 study, in which a single pawn shows the three underpromotions.[^s5]

Composers have also pushed the theme to extremes of economy and length. Morse lists a stalemate-form AUW in only two moves by J. Hartong (*The Problemist*, 1933), a successive AUW by four White pawns in four moves by F. Köhnlein (1903), and doubled and repeated AUWs in selfmates and series-movers.[^s1] Two-move settings exist too: Werner Speckmann (*Schach*, 1963) used four twins so that a pawn on f7 promotes to a different piece in each.[^s4] In helpmates, where both sides cooperate, four-solution settings in two moves are common.[^s4]

## Example: Maslar, mate in three (1962)

Z. Maslar's first-prize problem in *Bilten*, 1962, shows a scattered White AUW with only seven men (FEN above): White Kg7, Qh8, Be6, pawns a6, c6 and d7; Black Kd6.[^s1] The key 1.Qh5 threatens nothing and leaves Black only king moves. After 1...Kc7 2.Qc5 the d-pawn promotes to a queen if the king goes to b8; after 1...Kxe6 it must become a rook; after 1...Kxc6 a bishop; and after 1...Ke7 2.Qc5+ Kxe6 a knight gives mate.[^s1]

```pgn
[Event "Bilten 1962, 1st Prize - mate in 3 (Maslar), queen line"]
[SetUp "1"]
[FEN "7Q/3P2K1/P1PkB3/8/8/8/8/8 w - - 0 1"]
[Result "1-0"]

1. Qh5 Kc7 2. Qc5 Kb8 3. d8=Q# 1-0
```

```pgn
[Event "Bilten 1962, 1st Prize - mate in 3 (Maslar), rook line"]
[SetUp "1"]
[FEN "7Q/3P2K1/P1PkB3/8/8/8/8/8 w - - 0 1"]
[Result "1-0"]

1. Qh5 Kxe6 2. d8=R Ke7 3. Qe8# 1-0
```

```pgn
[Event "Bilten 1962, 1st Prize - mate in 3 (Maslar), bishop line"]
[SetUp "1"]
[FEN "7Q/3P2K1/P1PkB3/8/8/8/8/8 w - - 0 1"]
[Result "1-0"]

1. Qh5 Kxc6 2. d8=B Kd6 3. Qd5# 1-0
```

```pgn
[Event "Bilten 1962, 1st Prize - mate in 3 (Maslar), knight line"]
[SetUp "1"]
[FEN "7Q/3P2K1/P1PkB3/8/8/8/8/8 w - - 0 1"]
[Result "1-0"]

1. Qh5 Ke7 2. Qc5+ Kxe6 3. d8=N# 1-0
```

Setting the position up on a board shows why the minor choices are forced: in both the rook and the bishop lines, 2.d8=Q would leave the Black king with no legal move and give stalemate, so the underpromotion is the only way to keep Black moving into the mate.[^s1][^s3]

## Connections

AUW is a task of the **chess problem** and is built on **pawn promotion**, with **underpromotion** supplying three of its four pieces.[^s1][^s4] Avoiding **stalemate** is the most common motive for the rook and bishop promotions.[^s3][^s5] It has been shown in direct mates, **selfmates**, **helpmates** and series-movers, and in the **endgame study**, where Lommer's 1933 work was long treated as the pioneer.[^s1][^s3][^s4] Task composers combine it with the **Excelsior** pawn walk, and the **Babson task** raises it to its hardest form: Morse defines that task as four parallel variations in which a Black AUW on one square is answered by a matching White AUW on one square.[^s2]

## Sources
[^s1]: Jeremy Morse, *Chess Problems: Tasks and Records* (3rd edition, 2016), Chapter 14 "Pawn Promotion", §14.7 and problems 745–752; chapter PDF hosted by the British Chess Problem Society. https://www.theproblemist.org/dloads/cjm/Chapter_14.pdf (accessed 2026-11-16)
[^s2]: Jeremy Morse, *Chess Problems: Tasks and Records* (3rd edition, 2016), Chapter 15 "The Babson Task", §15.1; chapter PDF hosted by the British Chess Problem Society. https://www.theproblemist.org/dloads/cjm/Chapter_15.pdf (accessed 2026-11-16)
[^s3]: Harold van der Heijden, "Underpromotion Milestones", ChessBase News, 25 October 2024. https://en.chessbase.com/post/underpromotion-milestones (accessed 2026-11-16)
[^s4]: Peter Wong, OzProblems, "AUW (Allumwandlung)", problems 49–54. https://www.ozproblems.com/problem-world/auw (accessed 2026-11-16)
[^s5]: Noam Elkies, "Endgame Explorations 7: Underpromotion (Part 2)", originally in *Chess Horizons*; ACJ Extra at chabris.com. https://www.chabris.com/pub/acj/extra/Elkies/Elkies07.html (accessed 2026-11-16)
