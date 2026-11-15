---
id: kt:chess-clock
type: Equipment
title: Chess clock
aliases: [Chessclock, Game clock, Chess timer, Analogue chess clock, Digital chess clock, Mechanical chess clock]
domain: rules-and-notation
summary: >-
  A timing device with two connected time displays, only one of which runs at a time, used to
  limit each player's thinking time; a player pauses their own clock and starts the opponent's
  after each move, and the expiry of a player's time is signalled by a "flag".
fen: "8/8/4k3/8/8/2K5/8/R7 w - - 0 1"
status: current
volatile: true
verified: 2026-11-15
broader: [kt:chess-equipment]
related: [kt:blitz-chess, kt:time-management-in-games, kt:arbiter]
relations:
  - {predicate: governedBy, object: kt:fide-laws-of-chess}
  - {predicate: enables, object: kt:fischer-increment}
  - {predicate: enables, object: kt:bronstein-delay}
sources:
  - id: s1
    title: "FIDE Laws of Chess (full text, applied from 1 January 2023)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/
    type: governing-body
    accessed: 2026-11-15
  - id: s2
    title: "Arbiters' Manual 2024"
    publisher: FIDE Arbiters' Commission
    url: https://arbiters.fide.com/wp-content/uploads/Publications/Manual/Arbiters_Manual_2024.pdf
    type: governing-body
    accessed: 2026-11-15
  - id: s3
    title: "Chess Equipment without Electronic Components (applied from 1 March 2026)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/ChessEquipmentWithoutElectronicComponenets032026
    type: governing-body
    accessed: 2026-11-15
  - id: s4
    title: "US Chess Federation's Official Rules of Chess, 7th edition (online edition, chapters 1–8)"
    publisher: US Chess
    url: https://new.uschess.org/sites/default/files/media/documents/us-chess-rule-book-online-only-edition-chp-1-8-24-20.pdf
    type: governing-body
    accessed: 2026-11-15
  - id: s5
    title: "Chess: The time element and competition"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/chess/The-time-element-and-competition
    type: reference
    accessed: 2026-11-15
  - id: s6
    title: "Chess before the 20th century (Fattorini & Sons chess clock)"
    publisher: FIDE Chess Museum
    url: https://museum.fide.com/thematic_collections/chess-before-the-20th-century
    type: archive
    accessed: 2026-11-15
created: 2026-11-15
---

# Chess clock

A chess clock is the device that limits how long each player may think. The FIDE Laws of Chess (approved in 2022 and applied from 1 January 2023, checked November 2026) define it in Article 6.1 as a clock with two time displays connected so that only one can run at a time, and define "flag-fall" as the expiry of a player's allotted time.[^s1] Every serious over-the-board game, from a three-minute blitz game to a world championship, is played with one.[^s1][^s5]

## From sandglasses to pendulums

Encyclopaedia Britannica records that the first time limits were introduced in 1861, using sandglasses, in the Anderssen–Kolisch match and at a tournament in Bristol, with a control of 24 moves in two hours.[^s5] Sandglasses proved clumsy and inexact, and at London 1883 they were replaced by a pair of mechanical clocks mounted on a pendulum-like seesaw: tilting one's own side stopped that clock and started the other.[^s5] The FIDE Chess Museum holds an example of this design by Fattorini & Sons of Bradford, a firm it credits with the first chess clock of two linked pendulum clocks in 1883; the museum's model, made between 1887 and 1904, has two clocks on an iron rocker above a heavy iron base.[^s6] Britannica adds that the modern layout of two parallel timers, each with its own button, made severe time trouble survivable, and that a flag lifted by the minute hand at the end of the hour was added later to settle disputes over whether a limit had been exceeded.[^s5] Digital clocks appeared in the 1980s.[^s5]

## How the clock is used under the Laws

Article 6.2 sets the routine: having made a move on the board, a player pauses their own clock, which starts the opponent's.[^s1] The clock must be pressed with the same hand that made the move; a player may not keep a finger on it or hover over it, press it forcibly, pick it up, knock it over or press it before moving.[^s1] Only the player whose clock is running may adjust the pieces.[^s1] The arbiter decides where the clock stands, and White's clock is started at the scheduled start time.[^s1] The Arbiters' Manual explains that in individual events the clock normally goes on the right of the player with Black, with boards laid out so that the arbiter can watch many clocks at once.[^s2]

The clock's readings are treated as conclusive unless it is evidently defective; a defective clock is replaced, and if a setting is found to be wrong either player or the arbiter must pause the clock at once so that the arbiter can correct it.[^s1][^s2] A player may pause the clock only to call the arbiter, for instance when the piece needed for a promotion is not available.[^s1]

## The flag

Under Article 6.8 a flag counts as fallen only when the arbiter observes it or a player makes a valid claim, so a result reached on the board before anyone notices the fall stands.[^s1][^s2] A player who has not completed the required moves in the allotted time loses, unless the opponent could not checkmate by any series of legal moves, in which case the game is drawn.[^s1]

**Example.** In the key position (FEN 8/8/4k3/8/8/2K5/8/R7 w), White, with king and rook, oversteps the time limit. Black has only a king and can never checkmate, so under Article 6.9 the game is drawn rather than lost for White.[^s1]

## Analogue and digital clocks

FIDE's equipment standard for mechanical clocks, applied from 1 March 2026, requires a flag or similar device that shows clearly when an hour has elapsed, a non-glare face, and levers that operate at no more than 40 dB at one metre; the same model should normally be used throughout a tournament.[^s3] Appendix D of the Laws still allows a specially adapted analogue clock for visually impaired players, with raised dots marking the minutes and a flag that can be felt.[^s1] US Chess, by contrast, prefers digital clocks in all cases, noting that they run silently, time precisely and can give both players identical time; it ranks which clock is the "standard timer" for increment, delay and plain controls, falling back to an analogue clock only when nothing better is available.[^s4] Its rules also let a digital clock signal flag-fall by a beep, light or all-zero display, and make players responsible for setting their own digital clocks correctly.[^s4]

## Pitfalls for club players

- **Pressing with the other hand** or pressing before the move is complete breaks Article 6.2, which the arbiter enforces.[^s1]
- **Not claiming.** A fallen flag means nothing until it is observed or claimed, so watch the opponent's display in a scramble.[^s1][^s2]
- **Wrong settings.** If the time or move count looks wrong, pause the clock immediately and call the arbiter rather than playing on.[^s1][^s2]

## Connections

The chess clock is a piece of **chess equipment** whose use is **governed by** Article 6 of the **FIDE Laws of Chess**, and whose settings and disputes are handled by the **arbiter**.[^s1][^s2] Modern clocks **enable** controls with added time per move, the **Fischer increment** and **Bronstein delay**, both recognised by FIDE and US Chess.[^s1][^s4] Fast play such as **blitz chess** depends on it entirely, and managing its readout is the core of **time management in games**.[^s5]

## Sources

[^s1]: FIDE Rules Commission, "FIDE Laws of Chess" (full text, applied from 1 January 2023). https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/ (accessed 2026-11-15)
[^s2]: FIDE Arbiters' Commission, "Arbiters' Manual 2024". https://arbiters.fide.com/wp-content/uploads/Publications/Manual/Arbiters_Manual_2024.pdf (accessed 2026-11-15)
[^s3]: FIDE Handbook, "Chess Equipment without Electronic Components" (applied from 1 March 2026). https://handbook.fide.com/chapter/ChessEquipmentWithoutElectronicComponenets032026 (accessed 2026-11-15)
[^s4]: US Chess, "US Chess Federation's Official Rules of Chess", 7th edition, online edition, chapters 1–8. https://new.uschess.org/sites/default/files/media/documents/us-chess-rule-book-online-only-edition-chp-1-8-24-20.pdf (accessed 2026-11-15)
[^s5]: Encyclopaedia Britannica, "Chess: The time element and competition". https://www.britannica.com/topic/chess/The-time-element-and-competition (accessed 2026-11-15)
[^s6]: FIDE Chess Museum, "Chess before the 20th century" (Fattorini & Sons chess clock). https://museum.fide.com/thematic_collections/chess-before-the-20th-century (accessed 2026-11-15)
