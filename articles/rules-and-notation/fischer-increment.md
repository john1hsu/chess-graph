---
id: kt:fischer-increment
type: TimeControl
title: Fischer increment
aliases: [Fischer clock, Fischer mode, Fischer bonus, Increment, Time increment, Increment time control, Cumulative time control]
domain: rules-and-notation
summary: >-
  A way of running a chess clock in which a fixed amount of time, typically a few seconds to a
  minute, is added to a player's clock for every move, including before the first move; patented
  by Bobby Fischer in 1988 and built into the FIDE Laws of Chess and the US Chess rules.
status: current
volatile: true
verified: 2026-11-14
broader: [kt:chess-clock, kt:fide-laws-of-chess]
related: [kt:bronstein-delay, kt:blitz-chess, kt:rapid-chess, kt:time-management-in-games, kt:arbiter, kt:us-chess, kt:fischer-spassky-1992]
relations:
  - {predicate: developedBy, object: kt:bobby-fischer}
  - {predicate: namedAfter, object: kt:bobby-fischer}
  - {predicate: governedBy, object: kt:fide-laws-of-chess}
  - {predicate: alternativeTo, object: kt:bronstein-delay}
sources:
  - id: s1
    title: "FIDE Laws of Chess (full text, applied from 1 January 2023)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/
    type: governing-body
    accessed: 2026-11-14
  - id: s2
    title: "03. Chess Equipment with Electronic Components (effective from 1 March 2026)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/ChessEquipmentWithElectronicComponenets032026
    type: governing-body
    accessed: 2026-11-14
  - id: s3
    title: "Arbiters' Manual 2024"
    publisher: FIDE Arbiters' Commission
    url: https://arbiters.fide.com/wp-content/uploads/Publications/Manual/Arbiters_Manual_2024.pdf
    type: governing-body
    accessed: 2026-11-14
  - id: s4
    title: "US Chess Federation's Official Rules of Chess, 7th edition (online edition, chapters 1–8)"
    publisher: US Chess
    url: https://new.uschess.org/sites/default/files/media/documents/us-chess-rule-book-online-only-edition-chp-1-8-21-20.pdf
    type: governing-body
    accessed: 2026-11-14
  - id: s5
    title: "Chess: The time element and competition"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/chess/The-time-element-and-competition
    type: reference
    accessed: 2026-11-14
created: 2026-11-14
---

# Fischer increment

A Fischer increment is a fixed amount of time added to a player's clock for each move. The FIDE Laws of Chess (applied from 1 January 2023, checked November 2026) define an increment in their glossary as an amount of time, from 2 to 60 seconds, added from the start before each move for the player, and Article 6.3.1 counts time "added with each move" as part of a player's allotted time.[^s1] Unlike older "x moves in y hours" controls or pure sudden death, an increment guarantees that a player who moves quickly enough can never be forced to lose on time simply because the game ran long.[^s1][^s5]

## Origin

Encyclopaedia Britannica records that Bobby Fischer patented a chess clock in 1988 that added time after each completed move.[^s5] He used it when he returned to play Boris Spassky in their unsanctioned 1992 match in Yugoslavia: each player started with 111 minutes and gained one minute per move, so that after 40 moves a player had received 151 minutes, one more than the 40-moves-in-two-and-a-half-hours control of their 1972 title match.[^s5] Britannica adds that televised and spectator-oriented events, such as the Melody Amber tournament in Monaco, and internet chess clubs took up short increment controls; one Amber format gave four minutes plus ten seconds per move.[^s5] The FIDE Arbiters' Manual notes that the system is still often called the "Fischer bonus" and appears on some clocks as "FISCH".[^s3]

## How it works

Under Article 6.2.1, a player completes a move by pausing their own clock and starting the opponent's.[^s1] In increment mode the clock adds the bonus each time, and the first increment is credited at the very start of the game; FIDE's equipment standard (effective 1 March 2026) requires that a clock in Fischer mode add the increment before the first move.[^s2][^s3] The same standard requires approved electronic clocks to offer preset increment controls, such as three minutes plus two seconds per move, and to let an arbiter enter up to four time periods with their own increments.[^s2]

Because the increment is added whether or not it was used, unused seconds accumulate: a player who replies faster than the bonus actually gains time. This is the key difference from **delay** modes. The Arbiters' Manual describes two kinds, Bronstein and simple (US) delay, and stresses that with delay a player can never end a move with more time than they had at its start.[^s3] FIDE's glossary likewise describes Bronstein mode as a main thinking time plus a fixed extra time per move.[^s1]

## Classifying a control with increment

The Laws use the increment to decide whether a game is rapid or blitz. Appendix A.1 defines rapid as more than 10 but less than 60 minutes per player, either as a fixed time or as the allotted time plus 60 times any increment; Appendix B.1 sets blitz at 10 minutes or less on the same formula.[^s1] The Arbiters' Manual applies the same multiplication by 60 when working out the total length of a playing session.[^s3]

**Worked example.** A control of 3 minutes plus 2 seconds per move counts as 3 minutes + 60 × 2 seconds = 5 minutes, so it is blitz. A control of 10 minutes plus 5 seconds counts as 10 minutes + 60 × 5 seconds = 15 minutes, so it is rapid, even though the base time alone would be blitz.[^s1] US Chess uses the same arithmetic for its totals: G/60 with a 5-second delay counts as 65 minutes.[^s4]

## US Chess practice

US Chess writes increment controls with "inc/" or "+" (for example "G/90 inc/30"), and delay controls with "d/".[^s4] It recommends an increment or delay of 5 to 30 seconds when the base time is 30 minutes or more, 3 seconds for base times between 10 and 30 minutes, and 2 seconds for 10 minutes or less, applied from the first move through every time control.[^s4] When an event specifies an increment, an increment-capable clock is the standard timer, with listed fallbacks if none is available.[^s4] Its definition of time pressure (under five minutes) does not apply when the control has an increment or delay of 30 seconds or more.[^s4]

## Practical points and pitfalls

- **Check the clock before move one.** Because a correctly set clock in Fischer mode shows the first increment before the game starts, players and arbiters can confirm the mode and bonus at a glance.[^s2][^s3]
- **The increment is not "free time".** It is added only after a move is completed by pressing the clock, so a player whose flag falls mid-move gets nothing; under Article 6.9 failing to make the required moves in the allotted time loses the game.[^s1]
- **Games without increment.** Where a quickplay finish has no increment, Guideline III.4 lets a player with under two minutes ask for a five-second increment for both players, a request that also counts as a draw offer.[^s1]
- **Banking time.** Because unused increment accumulates while delay never raises a player's time above its level at the start of the move, quick moves in simple positions can rebuild a reserve only under an increment.[^s3]

## Connections

The Fischer increment is a mode of the **chess clock** **governed by** Article 6 and the appendices of the **FIDE Laws of Chess**, and it was **developed by** and is **named after** **Bobby Fischer**, who played the **1992 Fischer–Spassky match** with it.[^s1][^s5] It is the main **alternative to** **Bronstein delay** and simple delay, both of which US Chess also recognises.[^s3][^s4] Through the 60-move formula it decides whether a game counts as **rapid** or **blitz**, it shapes **time management in games**, and **US Chess** and the **arbiter** apply it under their own regulations.[^s1][^s4]

## Sources

[^s1]: FIDE Rules Commission, "FIDE Laws of Chess" (full text, applied from 1 January 2023). https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/ (accessed 2026-11-14)
[^s2]: FIDE Handbook, "03. Chess Equipment with Electronic Components" (effective from 1 March 2026). https://handbook.fide.com/chapter/ChessEquipmentWithElectronicComponenets032026 (accessed 2026-11-14)
[^s3]: FIDE Arbiters' Commission, "Arbiters' Manual 2024". https://arbiters.fide.com/wp-content/uploads/Publications/Manual/Arbiters_Manual_2024.pdf (accessed 2026-11-14)
[^s4]: US Chess, "US Chess Federation's Official Rules of Chess", 7th edition, online edition, chapters 1–8. https://new.uschess.org/sites/default/files/media/documents/us-chess-rule-book-online-only-edition-chp-1-8-21-20.pdf (accessed 2026-11-14)
[^s5]: Encyclopaedia Britannica, "Chess: The time element and competition". https://www.britannica.com/topic/chess/The-time-element-and-competition (accessed 2026-11-14)
