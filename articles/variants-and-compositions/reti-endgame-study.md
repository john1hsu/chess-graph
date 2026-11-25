---
id: kt:reti-endgame-study
type: Game
title: Réti endgame study
aliases: [Reti endgame study, Réti study, Reti study, Réti's study, Réti 1921 study, Reti's king and pawn study]
domain: variants-and-compositions
summary: >-
  Richard Réti's famous 1921 composition (White Kh8, Pc6; Black Ka6, Ph5; White to play and draw), in
  which a king that seems hopelessly outside the square of Black's pawn saves the game by walking a
  diagonal that threatens two things at once: catching the h-pawn and supporting its own c-pawn.
fen: "7K/8/k1P5/7p/8/8/8/8 w - - 0 1"
status: current
volatile: false
verified: 2026-11-25
broader: [kt:endgame-study, kt:king-and-pawn-endgames]
related: [kt:rule-of-the-square, kt:passed-pawn, kt:saavedra-position, kt:pawn-promotion]
relations:
  - {predicate: authoredBy, object: kt:richard-reti}
  - {predicate: namedAfter, object: kt:richard-reti}
  - {predicate: dependsOn, object: kt:tempo}
sources:
  - id: s1
    title: "The Chess Endgame Studies of Richard Réti"
    publisher: John Beasley (jsbeasley.co.uk)
    url: https://www.jsbeasley.co.uk/ochess/reti_all.pdf
    type: publication
    accessed: 2026-11-25
  - id: s2
    title: "Richard Réti"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/reti1.html
    type: reference
    accessed: 2026-11-25
  - id: s3
    title: "Richard Réti"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/biography/Richard-Reti
    type: reference
    accessed: 2026-11-25
  - id: s4
    title: "Réti Endgame Study"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/R%C3%A9ti_Endgame_Study
    type: community
    accessed: 2026-11-25
  - id: s5
    title: "Ready for Reti (Study of the Month, May 2019)"
    publisher: Siegfried Hornecker, ChessBase News
    url: https://en.chessbase.com/post/study-of-the-month-2019-5
    type: publication
    accessed: 2026-11-25
created: 2026-11-25
---

# Réti endgame study

The Réti endgame study is a four-man position (White king h8 and pawn c6; Black king a6 and pawn h5; White to play and draw) that looks lost at first sight: White's pawn is about to be eaten and Black's h-pawn is far outside the reach of White's king.[^s1][^s4] It was composed by Richard Réti (1889–1929), the Hungarian-born master whom Britannica counts among the chief exponents of the hypermodern school and notes as unusual among leading players for his keen interest in composing problems and studies.[^s3] The king manoeuvre that saves White became known as the "Réti manoeuvre".[^s5]

## The solution

The point is that the king does not have to choose between its two jobs. By walking down the long diagonal it approaches the h-pawn's square and the c-pawn at the same time, and Black cannot deal with both threats in time.[^s1][^s4] John Beasley's collection of Réti's studies gives the main line with 1...Kb6: 1.Kg7 Kb6 2.Kf6 h4 3.Ke5 h3 4.Kd6 h2 5.c7 Kb7 6.Kd7, and both sides promote, a dead draw.[^s1] He notes that Réti himself treated 1...h4 as the principal reply, so both deserve equal weight. After 1...h4 2.Kf6 Black can go back to 2...Kb6 3.Ke5, transposing; if instead 2...h3, the tempting 3.Ke5? loses to 3...h2 4.c7 Kb7 5.Kd6 h1=Q, while 3.Ke7 (or 3.Ke6) gets White's own pawn home in time.[^s1]

```pgn
[Event "Réti endgame study (Deutsch-Österreichische Tages-Zeitung, 1921)"]
[SetUp "1"]
[FEN "7K/8/k1P5/7p/8/8/8/8 w - - 0 1"]
[Result "1/2-1/2"]

1. Kg7 h4 (1... Kb6 2. Kf6 h4 3. Ke5 h3 4. Kd6 h2 5. c7 Kb7 6. Kd7) 2. Kf6 h3 (2... Kb6 3. Ke5) 3. Ke7 h2 4. c7 Kb7 5. Kd7 h1=Q 6. c8=Q+ 1/2-1/2
```

## Why it works

The study rests on a geometric fact about the chessboard: a king that heads from h8 to e5 along the diagonal takes exactly as many moves as one going straight down the h-file, so it loses nothing by detouring towards the centre.[^s4] The Chess Programming Wiki describes the lesson as two ideas at once: a king can make multiple threats with one move, and it can often reach a square by more than one route in the same number of moves.[^s4] Black's king needs two tempi to stop the c-pawn, and every tempo it spends doing so is a tempo White's king gains on the h-pawn.[^s4] A mechanical application of the rule of the square would give up White's game as lost; programmers cite the study as a case where a crude evaluation fails and real search (or a tablebase) is needed, and Mikhail Botvinnik discussed it in a 1993 *ICCA Journal* article.[^s4]

## Publication and origins

The study first appeared anonymously in Albert Becker's endgame column in the Vienna *Deutsch-Österreichische Tages-Zeitung* of 11 September 1921.[^s1][^s2] Réti's own published form had the black pawn on h6 with Black to move, but the Becker setting became the version customarily reprinted under Réti's name.[^s2] Beasley credits the rediscovery of the 1921 newspaper printing to research by Ken Whyld and Michael Ehn, and Winter records that some later books still give *Kagans Neueste Schachnachrichten* as the original source in error.[^s1][^s2] Réti later explained his reluctance to publish it himself: he felt a study should be hard to solve as well as pretty, and Beasley concedes that this one is easy once seen.[^s1]

The idea had forerunners in practical play. Beasley names an 1893 game between Carl Schlechter and Georg Marco as its inspiration, and Hornecker, drawing on a 2018 book by Albin Pötzsch, describes a related king manoeuvre that Alexander Alekhine hoped to use in a 1914 Moscow simultaneous display, though Alekhine never published it as a study.[^s1][^s5] Réti returned to the theme in later compositions, including a 1922 setting and a 1928 study with three Black pawns that was first printed in Artur Mandler's 1931 collection of Réti's studies.[^s1][^s5]

## Lessons for practical play

For a club player the study is a warning against counting tempi along straight lines only. Before resigning a king-and-pawn ending, check whether your king can approach the enemy pawn while also creating a threat of its own, such as supporting a passed pawn, so that the opponent has to spend a move answering it.[^s1][^s4]

## Connections

The Réti study is one of the best-known **endgame studies**, set in **king and pawn endgames**.[^s1] It is **authored by** and **named after** **Richard Réti**.[^s3] It shows the limits of the **rule of the square**, since the king saves the game by combining the chase with support of its own **passed pawn**, and the whole solution **depends on** counting **tempo**.[^s4] Like the **Saavedra position**, its solution ends in a race to **pawn promotion**.[^s1]

## Sources
[^s1]: John Beasley, "The Chess Endgame Studies of Richard Réti", section 1 (pawn studies), jsbeasley.co.uk. https://www.jsbeasley.co.uk/ochess/reti_all.pdf (accessed 2026-11-25)
[^s2]: Edward Winter, "Richard Réti", Chess Notes. https://chesshistory.com/winter/extra/reti1.html (accessed 2026-11-25)
[^s3]: Encyclopaedia Britannica, "Richard Réti". https://www.britannica.com/biography/Richard-Reti (accessed 2026-11-25)
[^s4]: Chess Programming Wiki, "Réti Endgame Study". https://www.chessprogramming.org/R%C3%A9ti_Endgame_Study (accessed 2026-11-25)
[^s5]: Siegfried Hornecker, "Ready for Reti", Study of the Month, ChessBase News, 25 May 2019. https://en.chessbase.com/post/study-of-the-month-2019-5 (accessed 2026-11-25)
