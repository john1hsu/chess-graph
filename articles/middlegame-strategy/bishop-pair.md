---
id: kt:bishop-pair
type: StrategicConcept
title: Bishop pair
aliases: [Two bishops, The two bishops, Advantage of the two bishops, Bishop-pair advantage]
domain: middlegame-strategy
summary: >-
  The possession of both bishops when the opponent has given up one or both of theirs for a knight;
  because the two bishops together cover squares of both colours, the pair is usually reckoned a
  lasting advantage worth roughly half a pawn, growing as the position opens and pawns come off.
status: current
volatile: false
verified: 2026-11-11
broader: [kt:material-advantage, kt:chess-strategy]
related: [kt:nimzo-indian-defence, kt:good-and-bad-bishops, kt:pawn-structure, kt:opposite-coloured-bishops]
relations:
  - {predicate: championedBy, object: kt:wilhelm-steinitz}
  - {predicate: exemplifiedBy, object: kt:englisch-versus-steinitz-london-1883}
sources:
  - id: s1
    title: "The Evaluation of Material Imbalances"
    publisher: Larry Kaufman, Chess.com (updated 17 November 2008)
    url: https://www.chess.com/article/view/the-evaluation-of-material-imbalances-by-im-larry-kaufman
    type: publication
    accessed: 2026-11-11
  - id: s2
    title: "Chess game data mining: exploring the advantage of the bishop pair with pgn-extract"
    publisher: David J. Barnes (author of pgn-extract), University of Kent blogs
    url: https://blogs.kent.ac.uk/djb
    type: academic
    accessed: 2026-11-11
  - id: s3
    title: "Chess Imbalances: A Grandmaster Guide (sample pages, chapter 4 'The Bishop Pair')"
    publisher: Mauricio Flores Rios, Quality Chess, excerpt hosted by New In Chess
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/82117.pdf
    type: book
    accessed: 2026-11-11
  - id: s4
    title: "Britannica: The Evolution of Chess Theory (Part 2)"
    publisher: Andrew Soltis, Encyclopaedia Britannica, republished by ChessBase (19 October 2019)
    url: https://en.chessbase.com/newsroom/post/britannica-the-development-of-chess-theory-2?page=0
    type: reference
    accessed: 2026-11-11
  - id: s5
    title: "Understanding before Moving 60: The advantage of having the two bishops"
    publisher: Herman Grooten, ChessBase News (2 January 2022)
    url: https://en.chessbase.com/newsroom/post/understanding-before-moving-60-the-advantage-of-having-the-two-bishops?page=0
    type: publication
    accessed: 2026-11-11
  - id: s6
    title: "Englisch vs Steinitz, London 1883 (study chapter)"
    publisher: Lichess study
    url: https://lichess.org/study/embed/MQt5Tzls/yQiLRprR
    type: database
    accessed: 2026-11-11
created: 2026-11-11
---

# Bishop pair

A side "has the bishop pair" (or "the two bishops") when it still owns both bishops and the opponent has exchanged at least one of theirs for a knight. Material is nominally level, yet the pair is usually treated as an advantage in its own right, one that can be nursed for a whole game.[^s3][^s5] In the classical account of positional play, Wilhelm Steinitz counted two bishops against two knights among the small, lasting advantages he accumulated before attacking.[^s4]

## Why the pair is strong

Most pairs of identical pieces duplicate each other, but two bishops do not: one covers the light squares and the other the dark, so together they reach every square and leave no colour where enemy pieces can hide.[^s1] Each bishop is long-range, which makes the pair especially effective when the position is open, when play spreads to both wings, and in races between passed pawns on opposite flanks.[^s3] Flores Rios argues that a bishop-and-knight team rarely holds a systematic edge against the pair, so the defender is often playing for a draw at best.[^s3] Grooten adds a practical point: the side with the bishops can often choose which endgame to liquidate into, trading one bishop at the right moment.[^s5]

## How much is it worth?

Larry Kaufman's study of nearly 300,000 games between players rated 2300+ put the average value of the pair at about half a pawn. The figure was remarkably stable across different piece configurations, a little lower with most pawns on the board and higher once half or more had gone.[^s1] His rule of thumb: the pair plus an opponent's bad lone bishop is full compensation for a pawn.[^s1] He also reconciled this with grandmasters' readiness to concede the pair early: in the opening a knight is often slightly better than a bishop anyway, so giving up a bishop for a knight costs less than half a pawn at that stage.[^s1]

A later data-mining exercise by David Barnes, using about 1.95 million deduplicated games from 1990 onward (players 2000+), isolated some 25,000 games where bishop pair faced knight pair with otherwise level material. The side with the bishops scored 45% wins, 28% draws and 27% losses, and its loss rate fell steadily as pawns were exchanged, from about 31% with seven pawns each to about 5% with two.[^s2]

## Playing with the bishops

Flores Rios gives a four-step method for converting the pair.[^s3]

- **Fix pawns on the colour of the enemy bishop.** One of your bishops will be hemmed in by your own pawns anyway; putting them on the opponent's bishop's colour restricts that piece instead.[^s3]
- **Gain space on both flanks**, widening the diagonals and provoking weaknesses.[^s3]
- **Centralise the king**, which the bishops make hard for the opponent to match.[^s3]
- **Trade a pair of bishops at the right moment**, reaching a bishop-versus-knight ending that the remaining bishop wins.[^s3]

Fighting the pair is the mirror image: keep your pawns on the colour of your own bishop, claim space first, avoid weaknesses and positions where the bishops can cooperate, and seek pawn exchanges that head for a drawn ending.[^s3]

## When it does not count

The pair is not automatic. A serious positional weakness can neutralise it, as can a structure in which the two bishops have no way to work together on adjacent diagonals or in crossfire against the king.[^s3] It is also less potent in symmetrical pawn structures, which demand more exact technique.[^s3] Many openings deliberately concede it: in a line of the Accelerated Dragon, Black gives up the light-squared bishop for a knight and must then defend a queenless position against the bishops; Grooten notes that closer analysis has made that ending look more dangerous for Black than theory once believed.[^s5] Kaufman cites the Petroff and the Marshall Attack as lines where Black gives up a pawn largely to obtain the pair.[^s1]

## Example: Englisch–Steinitz, London 1883

Flores Rios uses this game to illustrate the final step.[^s3] After 13.Bxg4 Bxg4 Black held both bishops against bishop and knight; Steinitz advanced his kingside pawns, then traded dark-squared bishops with 31...Bg5 32.Bxg5; after the rooks came off, his king and bishop dominated, and 38...Bxe2 gave up the last bishop for the knight to enter a won king-and-pawn ending.[^s6][^s3]

```pgn
[Event "London"]
[Date "1883.??.??"]
[White "Berthold Englisch"]
[Black "Wilhelm Steinitz"]
[Result "0-1"]

1. e4 e5 2. Nf3 Nc6 3. Bb5 g6 4. d4 exd4 5. Nxd4 Bg7 6. Be3 Nf6 7. Nc3 O-O 8. O-O Ne7 9. Qd2 d5 10. exd5 Nexd5 11. Nxd5 Qxd5 12. Be2 Ng4 13. Bxg4 Bxg4 14. Nb3 Qxd2 15. Nxd2 Rad8 16. c3 Rfe8 17. Nb3 b6 18. h3 Be6 19. Rfd1 c5 20. Bg5 f6 21. Bf4 Kf7 22. f3 g5 23. Rxd8 Rxd8 24. Be3 h6 25. Re1 f5 26. f4 Bf6 27. g3 a5 28. Nc1 a4 29. a3 Bc4 30. Kf2 gxf4 31. Bxf4 Bg5 32. Bxg5 hxg5 33. Ke3 Kf6 34. h4 gxh4 35. gxh4 Re8+ 36. Kf2 Rxe1 37. Kxe1 Ke5 38. Ne2 Bxe2 39. Kxe2 Kf4 40. c4 Kg4 41. Ke3 f4+ 42. Ke4 f3 43. Ke3 Kg3 0-1
```

## Connections

The bishop pair is a positional form of **material advantage**: no material is up, but the evaluation shifts by about half a pawn.[^s1] It is one of the classic elements of **chess strategy** that Steinitz (**championed by**) built his method around.[^s4] Its value depends on **pawn structure**, open lines and the colour of fixed pawns, which is why it is closely tied to **good and bad bishops**.[^s3] The **Nimzo-Indian Defence** is the standard opening where Black trades bishop for knight on c3, handing White the pair in exchange for structural targets, and **Englisch versus Steinitz, London 1883** is the textbook conversion.[^s3][^s6] Trading one pair of bishops can also leave **opposite-coloured bishops**, so the timing of the exchange matters.[^s3]

## Sources
[^s1]: L. Kaufman, "The Evaluation of Material Imbalances", Chess.com (updated 17 November 2008). https://www.chess.com/article/view/the-evaluation-of-material-imbalances-by-im-larry-kaufman (accessed 2026-11-11)
[^s2]: D. J. Barnes, "Chess game data mining: exploring the advantage of the bishop pair with pgn-extract", University of Kent blogs. https://blogs.kent.ac.uk/djb (accessed 2026-11-11)
[^s3]: M. Flores Rios, *Chess Imbalances: A Grandmaster Guide*, Quality Chess, sample pages (chapter 4, "The Bishop Pair"). https://www.newinchess.com/media/wysiwyg/product_pdf/82117.pdf (accessed 2026-11-11)
[^s4]: A. Soltis, "The Evolution of Chess Theory (Part 2)", Encyclopaedia Britannica, republished by ChessBase, 19 October 2019. https://en.chessbase.com/newsroom/post/britannica-the-development-of-chess-theory-2?page=0 (accessed 2026-11-11)
[^s5]: H. Grooten, "Understanding before Moving 60: The advantage of having the two bishops", ChessBase News, 2 January 2022. https://en.chessbase.com/newsroom/post/understanding-before-moving-60-the-advantage-of-having-the-two-bishops?page=0 (accessed 2026-11-11)
[^s6]: Lichess study, "Englisch vs Steinitz, London 1883". https://lichess.org/study/embed/MQt5Tzls/yQiLRprR (accessed 2026-11-11)
