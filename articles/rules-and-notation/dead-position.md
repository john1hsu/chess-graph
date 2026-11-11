---
id: kt:dead-position
type: Rule
title: Dead position
aliases: [Dead position rule, Insufficient material, Insufficient mating material, Draw by insufficient material, Article 5.2.2]
domain: rules-and-notation
summary: >-
  The FIDE rule that a game is drawn the moment a position arises in which neither player can
  checkmate the opponent's king by any series of legal moves; it covers bare-king and
  insufficient-material endings as well as locked positions with many pieces left.
fen: "4k3/8/8/1p1p1p1p/pPpPpPpP/P1P1P1P1/8/4K3 w - - 0 1"
status: current
volatile: true
verified: 2026-11-11
broader: [kt:fide-laws-of-chess, kt:draw]
related: [kt:stalemate, kt:checkmate, kt:helpmate, kt:arbiter, kt:retrograde-analysis]
relations:
  - {predicate: partOf, object: kt:fide-laws-of-chess}
  - {predicate: contrastsWith, object: kt:stalemate}
  - {predicate: dependsOn, object: kt:helpmate}
  - {predicate: developedBy, object: kt:fide}
sources:
  - id: s1
    title: "Laws of Chess, Article 5: The Completion of the Game"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/article5/
    type: governing-body
    accessed: 2026-11-11
  - id: s2
    title: "FIDE Laws of Chess (effective 1 January 2018)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/wp-content/uploads/2022/12/Laws_of_Chess-2018_ENG-2.pdf
    type: governing-body
    accessed: 2026-11-11
  - id: s3
    title: "FIDE Laws of Chess (effective 1 July 1997)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/wp-content/uploads/2022/12/Laws_of_Chess-1997_ENG.pdf
    type: governing-body
    accessed: 2026-11-11
  - id: s4
    title: "FIDE Laws of Chess (effective 1 July 2001)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/wp-content/uploads/2022/12/Laws_of_Chess-2001_ENG.pdf
    type: governing-body
    accessed: 2026-11-11
  - id: s5
    title: "Dead position"
    publisher: Jirina Prokopova, European Chess Union
    url: https://www.europechess.org/dead-position/
    type: publication
    accessed: 2026-11-11
  - id: s6
    title: "ECU: What should the arbiter do?"
    publisher: Prodromos Gerontopoulos, ChessBase News / European Chess Union
    url: https://en.chessbase.com/post/ecu-what-should-the-arbiter-do
    type: publication
    accessed: 2026-11-11
created: 2026-11-11
---

# Dead position

A dead position is one in which neither player can checkmate the opponent's king by any series of legal moves. Under Article 5.2.2 of the FIDE Laws of Chess, as published by the FIDE Rules Commission in November 2026, such a game is drawn and ends at once, provided the move that produced the position was legal under Article 3 and Articles 4.2 to 4.7.[^s1] No claim is needed: the draw happens automatically, like checkmate or stalemate, rather than on request like the fifty-move or repetition rules.[^s1][^s5]

## What counts as "dead"

The test is not whether a player could force mate, but whether mate could happen at all, even with the opponent cooperating. The 1997 Laws spelled this out by saying the draw applied even with the most unskilled play.[^s3] So the obvious material cases are dead: two bare kings, king and knight against king, and king and bishop against king.[^s5] By the same test, a position that is hopeless to win against good defence is not dead if some sequence of legal moves, however absurd, still ends in mate.[^s1][^s3] That is why the rule is better called "dead position" than "insufficient material": deciding it is a helpmate question in disguise.

Material is not the only route. European Chess Union arbiter Jirina Prokopova shows positions with many pieces still on the board that are dead because the pawns are locked and neither king can get through, and notes that players in such cases normally agree a draw anyway.[^s5] The key position above is a constructed example of that kind: every pawn is blocked, no pawn can capture, and each king is shut out of the opposing side, so only king moves remain and mate is impossible for either side.

## Why it matters in practice

The rule matters most when the clock runs out. Article 6.9 says a player whose flag falls loses, except that the game is drawn if the opponent cannot checkmate by any possible series of legal moves, and Article 7.5.5 uses the same test after a second illegal move.[^s2] Because a dead position ends the game at once, a flag that falls afterwards changes nothing.[^s5]

Two ECU arbiter cases show the point. In one, White played 48.Nc2+, after which the only legal continuation was 48...Qxc2+ 49.Kxc2 with stalemate; Prokopova rules that the game was already over and a later flag fall is irrelevant.[^s5] In another, analysed by IA Prodromos Gerontopoulos, Black checked with 46...Rc1+ and his flag fell before he pressed the clock; every remaining move was forced into a stalemate, so the arbiter should declare a draw rather than give White the win on time.[^s6] The lesson for club players: when short of time, a forcing line into a dead position or stalemate is a real defence, and a time-forfeit claim can fail if no mate was possible.

## History

The idea is older than the name. The 1997 Laws already drew any game in which no sequence of legal moves could produce mate, and drew a flag fall when the opponent could not mate.[^s3] The 2001 Laws, in force from 1 July 2001, put the rule in Article 5.2(b) and called it a "dead position", with the flag-fall exception moved to Article 6.10.[^s4] The 2018 Laws kept the wording as Article 5.2.2, and the same test is used for rapid and blitz time claims in Appendix A.4.3.[^s2] Article 5.1.2 now also turns a resignation into a draw if the resigning side could not be mated by any legal sequence.[^s1]

## Connections

The dead-position rule is part of the **FIDE Laws of Chess** (Article 5) and one of the ways a game ends in a **draw**. It **contrasts with stalemate**, where the side to move has no legal move at all, whereas a dead position may still allow many moves; the two often meet, as when a forced sequence ends in stalemate.[^s1][^s6] Because the test asks whether any cooperative mate exists, it **depends on** the same question a **helpmate** asks, and it is applied in **retrograde analysis** problems. In play it is the **arbiter** who must recognise a dead position, especially when deciding flag-fall claims.[^s5][^s6]

## Sources

[^s1]: FIDE Rules Commission, "Laws of Chess, Article 5: The Completion of the Game". https://rcc.fide.com/article5/ (accessed 2026-11-11)
[^s2]: FIDE Rules Commission, FIDE Laws of Chess (effective 1 January 2018). https://rcc.fide.com/wp-content/uploads/2022/12/Laws_of_Chess-2018_ENG-2.pdf (accessed 2026-11-11)
[^s3]: FIDE Rules Commission, FIDE Laws of Chess (effective 1 July 1997). https://rcc.fide.com/wp-content/uploads/2022/12/Laws_of_Chess-1997_ENG.pdf (accessed 2026-11-11)
[^s4]: FIDE Rules Commission, FIDE Laws of Chess (effective 1 July 2001). https://rcc.fide.com/wp-content/uploads/2022/12/Laws_of_Chess-2001_ENG.pdf (accessed 2026-11-11)
[^s5]: Jirina Prokopova, European Chess Union, "Dead position" (2019). https://www.europechess.org/dead-position/ (accessed 2026-11-11)
[^s6]: Prodromos Gerontopoulos, ChessBase News / European Chess Union, "ECU: What should the arbiter do?" (2021). https://en.chessbase.com/post/ecu-what-should-the-arbiter-do (accessed 2026-11-11)
