---
id: kt:blitz-chess
type: TimeControl
title: Blitz chess
aliases: [Blitz, Lightning chess, Speed chess, Five-minute chess, Blitz time control]
domain: rules-and-notation
summary: >-
  A form of chess in which each player has 10 minutes or less for the whole game, counting 60
  times any per-move increment; FIDE governs it through Appendix B of the Laws of Chess, rates it
  on a separate list and stages an annual World Blitz Championship.
status: current
volatile: true
verified: 2026-11-15
broader: [kt:fide-laws-of-chess, kt:chess-clock]
related: [kt:rapid-chess, kt:fischer-increment, kt:time-management-in-games, kt:arbiter, kt:bughouse, kt:chess-expertise]
relations:
  - {predicate: governedBy, object: kt:fide-laws-of-chess}
  - {predicate: alternativeTo, object: kt:rapid-chess}
  - {predicate: exemplifiedBy, object: kt:world-blitz-championship}
sources:
  - id: s1
    title: "Arbiters' Manual 2024 (Laws of Chess with commentary, Appendices A and B)"
    publisher: FIDE Arbiters' Commission
    url: https://arbiters.fide.com/wp-content/uploads/Publications/Manual/Arbiters_Manual_2024.pdf
    type: governing-body
    accessed: 2026-11-15
  - id: s2
    title: "FIDE Rapid and Blitz Rating Regulations (applied from 1 March 2024)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/B02RBRegulations2024
    type: governing-body
    accessed: 2026-11-15
  - id: s3
    title: "Regulations for the FIDE World Rapid and Blitz Championships 2025 (Open)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/files/handbook/wrbc_regulations_2025_open.pdf
    type: governing-body
    accessed: 2026-11-15
  - id: s4
    title: "Magnus Carlsen and Bibisara Assaubayeva win World Blitz crowns"
    publisher: FIDE
    url: https://www.fide.com/magnus-carlsen-and-bibisara-assaubayeva-win-world-blitz-crowns/
    type: primary-record
    accessed: 2026-11-15
  - id: s5
    title: "History of the World Blitz Championship"
    publisher: FIDE World Rapid and Blitz Championships 2019 (official site)
    url: https://worldrapidandblitz2019.fide.com/history/1
    type: official-project
    accessed: 2026-11-15
  - id: s6
    title: "The Effects of Speed on Skilled Chess Performance (Bruce D. Burns, Psychological Science, 2004)"
    publisher: Association for Psychological Science
    url: https://www.psychologicalscience.org/journals/psychological-science/j.0956-7976.2004.00699.x/
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Blitz chess

Blitz is the fastest form of chess that FIDE regulates as a distinct category. Appendix B.1 of the FIDE Laws of Chess defines a blitz game as one in which every move must be completed in a fixed time of 10 minutes or less per player, or in an allotted time plus 60 times any increment that adds up to 10 minutes or less.[^s1] Anything above that, up to but not including 60 minutes, is rapid chess under Appendix A.1.[^s1] The classic blitz game gives each player five minutes for all moves; in Bruce Burns's 2004 study that works out to about 7.5 seconds a move, under 5% of the time of a normal tournament game.[^s6]

## How the Laws treat blitz

Blitz has no rulebook of its own. Appendix B.3 says that apart from its own clauses, play is governed by the rapid chess provisions of Appendix A (A.2, A.3 and A.5), which in turn sit on top of the ordinary Laws.[^s1] The practical consequences, as the FIDE Arbiters' Manual (2024 edition, checked November 2026) explains them, are:

- **No scoresheet is required.** Players need not record the moves but keep their rights to claims that would normally rely on a scoresheet; a player may ask to see the arbiter's or assistant's record on their own move, up to five times a game, and further requests count as distracting the opponent.[^s1]
- **Illegal moves.** If the arbiter sees a completed illegal move before the opponent replies, the arbiter applies the illegal-move article; if not, the opponent may claim before moving. Once the opponent has moved, the illegal move stands unless the players themselves agree to correct it. As in rapid, the time penalties of Articles 7 and 9 are one minute instead of two, and a second illegal move by the same player loses the game.[^s1]
- **Flag falls.** A player claims a win on time by pausing the clock and telling the arbiter, but the game is drawn if the claimant could not checkmate by any series of legal moves. The arbiter also calls a flag fall that he or she observes.[^s1]
- **Clock settings are frozen after move ten.** Once each player has made ten moves, an incorrect clock setting is no longer changed unless it would harm the event schedule.[^s1]

Event regulations choose between this default and the stricter **Competition Rules**. Appendix B.2 lets the standard Laws apply in full only where one arbiter supervises a single game and every move is recorded, whereas rapid needs one arbiter per three games; the regulations must state the choice in advance for the whole event, not just for the final rounds.[^s1]

## Rating blitz games

FIDE keeps a separate blitz rating under its Rapid and Blitz Rating Regulations (applied from 1 March 2024, checked November 2026). For rating, a game is blitz when each player has more than 3 and at most 10 minutes, counting base time plus 60 times the increment; games of 3 minutes or less per player, and games in which the two players have different controls, are not rated.[^s2] A new list is produced on the first of every month, and the development coefficient starts at K = 40 for newcomers and juniors, falling to 20 and then 10 once a player reaches 2400.[^s2]

**Worked example.** Five minutes plus three seconds counts as 5 + 3 = 8 minutes, so it is blitz and blitz-rated. Two minutes plus one second counts as 2 + 1 = 3 minutes: it is still blitz under the Laws, but too fast to be FIDE-rated.[^s1][^s2]

## The World Blitz Championship

FIDE recognises the 1988 event in St John's, Canada, a 32-player knockout of four-game matches won by Mikhail Tal, as the first official World Blitz Championship; regular editions resumed in 2006, and since 2012 the event has been held together with the World Rapid Championship.[^s5] The 2025 Open edition in Doha used 3 minutes plus a 2-second increment from move one, with a 19-round Swiss stage followed by a four-player knockout of four-game matches and, for a tied match, one sudden-death game in which a draw counts as a win for Black.[^s3] Magnus Carlsen won it on 30 December 2025, beating Nodirbek Abdusattorov 2½–1½ in the final for his ninth World Blitz title; Bibisara Assaubayeva took the women's title for the third time (both as of November 2026).[^s4]

## What blitz reveals about skill

Blitz has become a natural laboratory for chess psychology. Burns compared players' blitz results with their normal ratings and found that blitz performance accounted for up to 81% of the variance in skill, even with less than 5% of the usual thinking time.[^s6] He interpreted this as evidence that fast processes such as pattern recognition carry much of the difference between strong and weak players, while noting that restricting search did narrow the gap between them.[^s6]

## Practical pitfalls

- **Treat the clock as part of the position.** Because a win on time needs only a claim and a theoretical mating possibility, a lost-looking position can still be saved, or a won one thrown away, on the clock alone.[^s1]
- **Move first, press second, with the same hand.** At the 2025 championship Carlsen lost a game after knocking pieces over in time trouble and resetting them while pressing the clock, which was ruled illegal.[^s4]
- **Know the event's rule set.** Whether an arbiter intervenes on every illegal move depends on whether the Competition Rules or the Appendix B default apply.[^s1]

## Connections

Blitz is a time control **governed by** Appendix B of the **FIDE Laws of Chess** and played on a **chess clock**, very often with a **Fischer increment**, whose 60-move formula decides where blitz ends and its **alternative**, **rapid chess**, begins.[^s1][^s2] The **arbiter**'s role is lighter than in standard play unless the Competition Rules apply.[^s1] Its showpiece, **exemplified by** the **World Blitz Championship**, has been dominated by **Magnus Carlsen**.[^s4][^s5] Blitz shapes **time management in games**, links to fast team variants such as **bughouse**, and is a tool for studying **chess expertise**.[^s6]

## Sources

[^s1]: FIDE Arbiters' Commission, "Arbiters' Manual 2024" (Laws of Chess with commentary, Appendices A and B). https://arbiters.fide.com/wp-content/uploads/Publications/Manual/Arbiters_Manual_2024.pdf (accessed 2026-11-15)
[^s2]: FIDE Handbook, "FIDE Rapid and Blitz Rating Regulations" (applied from 1 March 2024). https://handbook.fide.com/chapter/B02RBRegulations2024 (accessed 2026-11-15)
[^s3]: FIDE Handbook, "Regulations for the FIDE World Rapid and Blitz Championships 2025 (Open)". https://handbook.fide.com/files/handbook/wrbc_regulations_2025_open.pdf (accessed 2026-11-15)
[^s4]: FIDE, "Magnus Carlsen and Bibisara Assaubayeva win World Blitz crowns" (December 2025). https://www.fide.com/magnus-carlsen-and-bibisara-assaubayeva-win-world-blitz-crowns/ (accessed 2026-11-15)
[^s5]: FIDE World Rapid and Blitz Championships 2019, "History of the World Blitz Championship". https://worldrapidandblitz2019.fide.com/history/1 (accessed 2026-11-15)
[^s6]: Bruce D. Burns, "The Effects of Speed on Skilled Chess Performance", Psychological Science (2004). https://www.psychologicalscience.org/journals/psychological-science/j.0956-7976.2004.00699.x/ (accessed 2026-11-15)
