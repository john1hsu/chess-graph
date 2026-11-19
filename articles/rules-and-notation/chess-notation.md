---
id: kt:chess-notation
type: Notation
title: Chess notation
aliases: [Chess notation systems, Game notation, Move notation, Notation of chess games]
domain: rules-and-notation
summary: >-
  The family of written systems used to record the moves of a chess game, describe positions and
  mark evaluations, from algebraic and descriptive move notation to numeric, figurine and
  position-description schemes; FIDE recognises only algebraic notation for its own events.
status: current
volatile: true
verified: 2026-11-19
broader: [kt:chess]
related: [kt:forsyth-edwards-notation, kt:portable-game-notation, kt:numeric-annotation-glyphs, kt:correspondence-chess, kt:annotating-your-games, kt:philipp-stamma]
relations:
  - {predicate: hasPart, object: kt:algebraic-notation}
  - {predicate: hasPart, object: kt:descriptive-notation}
  - {predicate: governedBy, object: kt:fide-laws-of-chess}
sources:
  - id: s1
    title: "Chess Notation"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/notation.html
    type: reference
    accessed: 2026-11-19
  - id: s2
    title: "Appendix C. Algebraic Notation (FIDE Laws of Chess)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/?p=880
    type: governing-body
    accessed: 2026-11-19
  - id: s3
    title: "Article 8: The recording of the moves (FIDE Laws of Chess)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/article8/
    type: governing-body
    accessed: 2026-11-19
  - id: s4
    title: "Chess"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/chess
    type: reference
    accessed: 2026-11-19
  - id: s5
    title: "ICCF Playing Rules Guidelines (valid from 1 January 2015)"
    publisher: International Correspondence Chess Federation
    url: https://webfiles.iccf.com/rules/ICCF%20Playing%20Rules%20Guidelines%2001.01.2015.pdf
    type: governing-body
    accessed: 2026-11-19
  - id: s6
    title: "The Creator of Algebraic Chess Notation (Julio Becerra, 4 November 2009)"
    publisher: Chess.com
    url: https://www.chess.com/article/view/the-creator-of-algebraic-chess-notation
    type: publication
    accessed: 2026-11-19
created: 2026-11-19
---

# Chess notation

Chess notation is the umbrella term for the conventions players, publishers and arbiters use to write chess down. Britannica explains its double purpose: notation records games while they are being played and lets them be analysed in print afterwards.[^s4] Over the centuries many competing schemes have existed, and Edward Winter's survey lists not only the familiar algebraic and descriptive systems but also numeric, figurine, shorthand, Esperanto and Hebrew variants, together with one-off proposals such as a new notation suggested by Emanuel Lasker in 1901.[^s1] Today one system dominates: FIDE recognises only algebraic notation for its own tournaments and matches and recommends it for chess literature in general.[^s2]

## What a notation has to do

Any workable system must solve three problems. First, it must give every square a name; algebraic notation does this with a file letter and a rank number seen from White's side, so each of the 64 squares has exactly one label.[^s2][^s4] Second, it must say which unit moved and where, including the special cases of captures, castling, en passant and promotion.[^s2] Third, it must resolve ambiguity when two identical pieces can reach the same square; FIDE's rule is to add the departure file, or the departure rank if the pieces share a file.[^s2] Winter's examples show what happens when a system handles the last point badly: in descriptive scores, he notes, ambiguity was a chronic problem, and one nineteenth-century game cannot be read without guessing which knight moved.[^s1]

## The main families

**Algebraic notation** is now standard. Winter traces English uses back to R. Lambe's *History of Chess* (1764) and Charles Check's *Easy Guide* (1818), while Chess.com's GM Julio Becerra credits Philipp Stamma's 1737 *Essai sur le Jeu des Echecs* with introducing an early algebraic form that named pieces by their starting file rather than by initial letter.[^s1][^s6] FIDE allows a short form (Nf3), a long form that also gives the departure square (Ng1f3), and national piece letters such as the French F for the bishop, while asking printed periodicals to use figurines.[^s2]

**Descriptive notation**, which names squares after the pieces that start on them and counts ranks from each player's side, was the English-language standard in the classics of Alekhine, Nimzowitsch and Capablanca.[^s1] Its long fight with algebraic produced side debates such as whether the knight should be Kt, S or N.[^s1]

**Numeric notation** replaces letters with digits so that a move is a string of numbers and is independent of language. Winter records W. Moffat's 1915 proposal to number squares by file and rank (e1 as 51, c8 as 38) and an earlier 1827 scheme that numbered the squares 1 to 64.[^s1] Correspondence players still use a numeric system: ICCF's postal guidelines let opponents agree to use more than one notation, such as numeric and algebraic together, and accept final game scores in either PGN or numeric form.[^s5]

**Figurine notation** prints small piece symbols instead of letters, which makes a score readable regardless of language. Winter finds an English example in the *Chess Amateur* of March 1912 and a "pure figurine" score in Alekhine's notes of 1929.[^s1]

**Position notations** describe a whole board rather than a sequence of moves. David Forsyth first described his system in the *Glasgow Weekly Herald* in February 1883, and it was soon discussed as a convenient way to set out problems.[^s1]

## Symbols and annotation

Beyond the moves themselves, notation carries commentary. Britannica lists the common marks: castling as 0-0 or 0-0-0, captures with x or a colon, check with + or "ch", mate with # or ++, and evaluation signs such as ! for a good move, !! for an excellent one, ? for a weak move, ?? for a blunder and !? for a double-edged or slightly dubious try.[^s4] FIDE treats x, +, # and e.p. as optional, and adds its own scoresheet symbol, (=), for a draw offer.[^s2][^s3]

## A short example

The Exchange Variation of the Ruy Lopez, 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Bxc6 dxc6 5.O-O, shows how the systems differ. In FIDE's long algebraic form the second move pair is written Ng1f3 Nb8c6 and the fourth Bb5xc6 d7xc6; in Moffat-style numbering the knight's move g1–f3 becomes 71-63.[^s1][^s2] A figurine edition would print a knight symbol instead of N. Learning to switch between these forms is the practical skill: older books, correspondence scores and engine output each favour a different one.

## Notation in competition

Recording is a legal obligation, not just a habit. Under Article 8 of the FIDE Laws, as of November 2026, each player must write down both sides' moves, in algebraic notation on paper or on a FIDE-certified electronic scoresheet, and may not record a move before playing it except to claim a draw or adjourn.[^s3] A player with under five minutes left in a period and no increment of at least 30 seconds is excused from recording for the rest of that period.[^s3] Appendix C adds that scoresheets kept in another system may not be used as evidence where a scoresheet normally would be, and arbiters should tell players who use one.[^s2]

## Connections

Chess notation is a broad topic within **chess**, and **has parts** that have their own nodes: **algebraic notation**, the current standard, and **descriptive notation**, its English-language predecessor.[^s1][^s2] It is **governed by** the **FIDE Laws of Chess** through Article 8 and Appendix C.[^s2][^s3] The **Forsyth–Edwards notation** grew out of Forsyth's position scheme, **Portable Game Notation** and numeric scores are the formats used in **correspondence chess**, and evaluation marks lead to **numeric annotation glyphs** and the craft of **annotating your games**.[^s1][^s4][^s5] **Philipp Stamma** is credited with an early algebraic system.[^s6]

## Sources

[^s1]: Edward Winter, Chess Notes, "Chess Notation". https://chesshistory.com/winter/extra/notation.html (accessed 2026-11-19)
[^s2]: FIDE Rules Commission, "Appendix C. Algebraic Notation" (FIDE Laws of Chess). https://rcc.fide.com/?p=880 (accessed 2026-11-19)
[^s3]: FIDE Rules Commission, "Article 8: The recording of the moves" (FIDE Laws of Chess). https://rcc.fide.com/article8/ (accessed 2026-11-19)
[^s4]: Encyclopaedia Britannica, "Chess". https://www.britannica.com/topic/chess (accessed 2026-11-19)
[^s5]: International Correspondence Chess Federation, "ICCF Playing Rules Guidelines" (valid from 1 January 2015). https://webfiles.iccf.com/rules/ICCF%20Playing%20Rules%20Guidelines%2001.01.2015.pdf (accessed 2026-11-19)
[^s6]: Julio Becerra, "The Creator of Algebraic Chess Notation", Chess.com, 4 November 2009. https://www.chess.com/article/view/the-creator-of-algebraic-chess-notation (accessed 2026-11-19)
