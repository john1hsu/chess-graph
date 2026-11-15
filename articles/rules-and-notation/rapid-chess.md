---
id: kt:rapid-chess
type: TimeControl
title: Rapid chess
aliases: [Rapid, Rapid play, Rapidplay, Active chess, Rapid time control]
domain: rules-and-notation
summary: >-
  A form of chess in which each player has more than 10 and less than 60 minutes for the whole
  game, counting 60 times any per-move increment; FIDE governs it through Appendix A of the Laws
  of Chess, rates it on a separate list and holds an annual World Rapid Championship.
status: current
volatile: true
verified: 2026-11-15
broader: [kt:fide-laws-of-chess, kt:chess-clock]
related: [kt:blitz-chess, kt:fischer-increment, kt:arbiter, kt:time-management-in-games, kt:tie-break, kt:chess-expertise]
relations:
  - {predicate: governedBy, object: kt:fide-laws-of-chess}
  - {predicate: alternativeTo, object: kt:blitz-chess}
  - {predicate: exemplifiedBy, object: kt:world-rapid-championship}
sources:
  - id: s1
    title: "Laws of Chess, Appendix A. Rapid Chess"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/?p=876
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
    title: "Carlsen and Goryachkina take World Rapid titles in Doha"
    publisher: FIDE World Rapid and Blitz Championships 2025 (official site)
    url: https://worldrapidandblitz2025.fide.com/?p=1711
    type: primary-record
    accessed: 2026-11-15
  - id: s5
    title: "From Mazatlan to Luzhniki (history of the World Rapid Championship)"
    publisher: FIDE World Rapid and Blitz Championships 2019 (official site)
    url: https://worldrapidandblitz2019.fide.com/history/2
    type: official-project
    accessed: 2026-11-15
  - id: s6
    title: "Forward search, pattern recognition and visualization in expert chess: A reply to Chabris and Hearst (2003) (Fernand Gobet)"
    publisher: Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/1391/1/Chabris_Hearst_Reply.pdf
    type: academic
    accessed: 2026-11-15
created: 2026-11-15
---

# Rapid chess

Rapid chess sits between blitz and standard (classical) play. Appendix A.1 of the FIDE Laws of Chess defines a rapid game as one in which each player has a fixed time of more than 10 minutes but less than 60 minutes for all moves, or an allotted time plus 60 times any increment that falls in the same window.[^s1] The FIDE Rapid and Blitz Rating Regulations (applied from 1 March 2024, checked November 2026) use the same boundaries to decide which games count for the rapid rating list.[^s2] Older sources sometimes call the format "active chess": FIDE's own history of the event describes Anatoly Karpov, winner of the first official title in 1988, as the "Active Chess Champion".[^s5]

## The 60-move formula in practice

Because the definition counts the increment as if a game lasted 60 moves, the label of a time control is not the sum of its two numbers in minutes and seconds, but base minutes plus increment seconds.[^s1][^s2]

- **15 minutes + 10 seconds** counts as 15 + 10 = 25 minutes: rapid. This is the control FIDE used for the 2025 World Rapid Championship.[^s3]
- **10 minutes + 5 seconds** counts as 15 minutes: rapid.
- **5 minutes + 5 seconds** counts as exactly 10 minutes, which does not exceed 10, so it is blitz, not rapid; the rating regulations use this very example.[^s2]
- **45 minutes + 15 seconds** counts as exactly 60 minutes, which is not less than 60, so it falls outside rapid and is treated as standard play.[^s1]

## How Appendix A changes the Laws

Rapid games are played under the ordinary Laws with a short list of adjustments.[^s1] Players do not have to keep score, yet they keep their rights to claims that would normally depend on a scoresheet, and may ask the arbiter for a scoresheet at any time in order to start writing.[^s1] The time penalties of Articles 7 and 9 (for example, the time added to the opponent after an illegal move) are one minute instead of two.[^s1]

Appendix A then offers organisers two regimes, and the event regulations must say in advance which one applies to the whole event.[^s1]

- **Full Competition Rules (A.4)** apply only when one arbiter supervises at most three games, and each game is recorded by the arbiter or an assistant, electronically where possible. A player may then ask to see that record on their own move up to five times a game; more requests may be treated as distracting the opponent.[^s1]
- **The rapid default (A.5)** applies otherwise. Once each player has made ten moves, an incorrect clock setting stays unless it would harm the schedule, and claims about a wrongly set-up board are not accepted (a misplaced king or rook only loses the corresponding castling right). An illegal move is penalised only if the arbiter acts, or the opponent claims, before the opponent's next move; after that it stands unless the players agree to correct it themselves. A player claiming a win on time pauses the clock and informs the arbiter, but the game is a draw if the claimant could not mate by any legal sequence. The arbiter also calls any flag fall he or she sees, and if both kings are in check or a pawn stands on its last rank and the position is still illegal after the next move, the game is drawn.[^s1]

## Rating rapid games

FIDE publishes rapid ratings on a separate list prepared on the first day of each month.[^s2] A newcomer's rating is published after at least five games against rated opponents, and published ratings start at 1400.[^s2] The development coefficient is K = 40 for new players (until 30 games) and for players under 2300 up to the end of the year they turn 18, K = 20 below 2400, and K = 10 once a published rating has reached 2400; if games multiplied by K would exceed 700 in one period, K is reduced.[^s2]

## The World Rapid Championship

FIDE dates the official title to Mazatlán, Mexico, in 1988, where Karpov and Viktor Gavrikov tied their final 5–5 and Karpov was declared champion on additional criteria.[^s5] There was no official edition for about fifteen years until Viswanathan Anand won in Cap d'Agde in 2003; the event was revived at Astana in 2012 with the time cut from 25 to 15 minutes (Sergey Karjakin won), and since 2013 it has been a large open Swiss.[^s5] The 2025 edition in Doha was a 13-round Swiss at 15 minutes plus 10 seconds, with tie-breaks and, for a tie on first place, a blitz play-off.[^s3] Magnus Carlsen won it on 28 December 2025 with 10½/13, a point clear, for his sixth World Rapid title; Aleksandra Goryachkina took her first women's title after a blitz play-off against Zhu Jiner (both as of November 2026).[^s4]

## What rapid reveals about skill

Rapid play has been used to separate the roles of calculation and pattern recognition. Chabris and Hearst compared grandmaster games played at classical and rapid speeds and counted computer-identified blunders: about 5.0 per thousand moves in classical play against 6.9 in rapid, even though rapid gave players roughly a sixth of the thinking time.[^s6] Fernand Gobet argued in reply that so modest a rise after so large a cut in search time fits pattern-recognition accounts of expertise at least as well as search-based ones.[^s6]

## Practical pitfalls

- **Know which regime applies.** Under the A.5 default, an illegal move that neither the arbiter nor the opponent catches in time simply stands.[^s1]
- **Check the clock early.** After move ten a wrong setting is normally left as it is.[^s1]
- **A flag is not always a win.** Without any possible mating sequence, a time claim only draws.[^s1]

## Connections

Rapid is a time control **governed by** Appendix A of the **FIDE Laws of Chess** and played on a **chess clock**, almost always with a **Fischer increment**, whose 60-move equivalence fixes where rapid ends and its **alternative**, **blitz chess**, begins.[^s1][^s2] How much the **arbiter** intervenes depends on whether the event adopts the Competition Rules.[^s1] Rapid events settle ties on points with a **tie-break** system and, for first place, faster play-off games, as the World Rapid Championship regulations show.[^s3] The format is **exemplified by** the **World Rapid Championship**, won six times by **Magnus Carlsen** and first by **Anatoly Karpov**.[^s4][^s5] It shapes **time management in games** and offers a natural experiment in **chess expertise**.[^s6]

## Sources

[^s1]: FIDE Rules Commission, "Laws of Chess, Appendix A. Rapid Chess". https://rcc.fide.com/?p=876 (accessed 2026-11-15)
[^s2]: FIDE Handbook, "FIDE Rapid and Blitz Rating Regulations" (applied from 1 March 2024). https://handbook.fide.com/chapter/B02RBRegulations2024 (accessed 2026-11-15)
[^s3]: FIDE Handbook, "Regulations for the FIDE World Rapid and Blitz Championships 2025 (Open)". https://handbook.fide.com/files/handbook/wrbc_regulations_2025_open.pdf (accessed 2026-11-15)
[^s4]: FIDE World Rapid and Blitz Championships 2025, "Carlsen and Goryachkina take World Rapid titles in Doha" (December 2025). https://worldrapidandblitz2025.fide.com/?p=1711 (accessed 2026-11-15)
[^s5]: FIDE World Rapid and Blitz Championships 2019, "From Mazatlan to Luzhniki". https://worldrapidandblitz2019.fide.com/history/2 (accessed 2026-11-15)
[^s6]: Fernand Gobet, "Forward search, pattern recognition and visualization in expert chess: A reply to Chabris and Hearst (2003)", Brunel University Research Archive. https://bura.brunel.ac.uk/bitstream/2438/1391/1/Chabris_Hearst_Reply.pdf (accessed 2026-11-15)
