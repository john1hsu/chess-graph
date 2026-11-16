---
id: kt:bronstein-delay
type: TimeControl
title: Bronstein delay
aliases: [Bronstein mode, Delay mode, Time delay, Time-delay mode, Delay clock, Simple delay, US delay]
domain: rules-and-notation
summary: >-
  A way of running a chess clock in which each player receives a fixed extra time with every move
  that is used up before the main thinking time starts to fall, so quick moves cost nothing but
  can never add to the clock; proposed by David Bronstein and recognised in the FIDE Laws of Chess
  and the US Chess rules.
status: current
volatile: true
verified: 2026-11-16
broader: [kt:chess-clock, kt:fide-laws-of-chess]
related: [kt:fischer-increment, kt:time-management-in-games, kt:arbiter, kt:us-chess, kt:rapid-chess, kt:blitz-chess]
relations:
  - {predicate: developedBy, object: kt:david-bronstein}
  - {predicate: namedAfter, object: kt:david-bronstein}
  - {predicate: governedBy, object: kt:fide-laws-of-chess}
  - {predicate: alternativeTo, object: kt:fischer-increment}
sources:
  - id: s1
    title: "FIDE Laws of Chess (full text, applied from 1 January 2023)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/
    type: governing-body
    accessed: 2026-11-16
  - id: s2
    title: "Arbiters' Manual 2024"
    publisher: FIDE Arbiters' Commission
    url: https://arbiters.fide.com/wp-content/uploads/Publications/Manual/Arbiters_Manual_2024.pdf
    type: governing-body
    accessed: 2026-11-16
  - id: s3
    title: "US Chess Federation's Official Rules of Chess, 7th edition (online edition, chapters 1–8, revised 24 August 2020)"
    publisher: US Chess
    url: https://new.uschess.org/sites/default/files/media/documents/us-chess-rule-book-online-only-edition-chp-1-8-24-20.pdf
    type: governing-body
    accessed: 2026-11-16
  - id: s4
    title: "Which 'extra time per move' methods are there?"
    publisher: DGT (Digital Game Technology)
    url: https://digitalgametechnology.com/faq/chess-clocks/which-extra-time-per-move-methods-are-there
    type: official-project
    accessed: 2026-11-16
  - id: s5
    title: "DGT 3000 quick guide (English)"
    publisher: DGT, hosted by the Swiss Chess Federation
    url: https://www.swisschess.ch/tl_files/ssb/srk/manuals/clocks/DGT-3000-qg-en.pdf
    type: official-project
    accessed: 2026-11-16
created: 2026-11-16
---

# Bronstein delay

Bronstein delay is a clock setting in which every move comes with a few seconds of "free" time. The FIDE Laws of Chess (applied from 1 January 2023, checked November 2026) describe the time-delay mode in Article 6.3.2: both players have a main thinking time and also receive a fixed extra time with every move, and the main time only starts to count down once that extra time has run out. If the player presses the clock before the extra time expires, the main thinking time is unchanged, however much of the extra time was used.[^s1] The FIDE glossary lists the setting as "delay (Bronstein) mode" and treats an increment of 2 to 60 seconds per move as running in either delay or cumulative (Fischer) mode.[^s1]

## Origin

The clock manufacturer DGT credits Grandmaster David Bronstein with the earliest proposal for adding time per move, dating it to 1969, and describes his method as applying from the first move and giving a fixed amount of time to complete each move before the principal thinking time is touched.[^s4] DGT's clock guide likewise notes that the method is called Bronstein delay after Bronstein, who first proposed it.[^s5] The aim, shared with later per-move methods, was to let games finish in a single session without players losing won positions simply because the clock ran out.[^s4]

## How it works: Bronstein and simple delay

FIDE's Arbiters' Manual distinguishes two kinds of delay. With **Bronstein delay**, the clock adds time back after the move is completed: the full delay if the player used at least that much, otherwise exactly the time the move took. With **simple (US) delay**, the main time does not start counting until the delay countdown has expired.[^s2] The manual stresses that both methods have the same overall effect, and that a player using delay can never end a move with more time than at its start; any unused part of the bonus is lost.[^s2] The difference is only in the display: DGT's guide explains that in Bronstein mode the screen shows the main time plus the delay, while in US-delay mode it shows only the main time and simply pauses at the start of each turn.[^s5]

**Worked example.** DGT's preset of 25 minutes plus 10 seconds per move shows 25:10 at the start of a turn. A player who moves after 4 seconds sees the display return to 25:10, so the move cost nothing; a player who takes 15 seconds spends the 10 free seconds and loses 5 seconds of main time.[^s5] Under a Fischer increment the same quick move would have left the player 6 seconds richer.[^s2]

## Rules and notation

For classifying games, the FIDE Laws count the allotted time plus 60 times any per-move addition: 10 minutes or less is blitz, more than 10 and less than 60 minutes is rapid.[^s1] The Arbiters' Manual confirms that delay and increment are treated alike for this calculation.[^s2] US Chess writes delay controls with "d/" (for example "G/30 d/5"), uses "d/0" for no delay or increment, and counts total time the same way, so G/60 d/5 is 65 minutes.[^s3] Its rules make a delay-capable clock the standard timer for a delay control, and a tournament director's tip gives 5 seconds as the standard delay for normal play and 3 seconds for quick chess.[^s3] Rule 16B2 tells directors to set a Bronstein or delay mode for delay controls, starting from move one unless announced otherwise.[^s3]

## Practical effects and pitfalls

- **No banking.** Because delay never raises the clock above its level at the start of the move, fast play in simple positions cannot build a reserve for later, as it can with an increment.[^s2]
- **Reaction time in sudden death.** US Chess explains that the time given by a delay or increment on each move serves as reaction time, which is why its procedure for claiming insufficient losing chances (rule 14H) is not available when a properly set delay or increment clock is in use.[^s3]
- **Wrong setting.** A US Chess tip warns that using the "Fischer" setting instead of the proper "Bronstein" setting is a common error, and rule 16P1 covers games where a required delay or increment was not set.[^s3]
- **Flag display.** US Chess also notes that manufacturers apply delay and flag-fall procedures in slightly different ways, so arbiters must know the device in use.[^s3]

## Connections

Bronstein delay is a mode of the **chess clock**, **governed by** Article 6 of the **FIDE Laws of Chess**, and it is **named after** and was first proposed (**developed by**) **David Bronstein**.[^s1][^s4][^s5] It is the main **alternative to** the **Fischer increment**, the cumulative mode that does let players gain time.[^s1][^s2] Through the 60-move formula it helps decide whether a game counts as **rapid** or **blitz**; **US Chess** and the **arbiter** apply it under their own regulations, and it shapes **time management in games**, since quick moves save no time for later.[^s1][^s3]

## Sources

[^s1]: FIDE Rules Commission, "FIDE Laws of Chess" (full text, applied from 1 January 2023). https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/ (accessed 2026-11-16)
[^s2]: FIDE Arbiters' Commission, "Arbiters' Manual 2024". https://arbiters.fide.com/wp-content/uploads/Publications/Manual/Arbiters_Manual_2024.pdf (accessed 2026-11-16)
[^s3]: US Chess, "US Chess Federation's Official Rules of Chess", 7th edition, online edition, chapters 1–8 (revised 24 August 2020). https://new.uschess.org/sites/default/files/media/documents/us-chess-rule-book-online-only-edition-chp-1-8-24-20.pdf (accessed 2026-11-16)
[^s4]: DGT, "Which 'extra time per move' methods are there?". https://digitalgametechnology.com/faq/chess-clocks/which-extra-time-per-move-methods-are-there (accessed 2026-11-16)
[^s5]: DGT, "DGT 3000 quick guide" (English), hosted by the Swiss Chess Federation. https://www.swisschess.ch/tl_files/ssb/srk/manuals/clocks/DGT-3000-qg-en.pdf (accessed 2026-11-16)
