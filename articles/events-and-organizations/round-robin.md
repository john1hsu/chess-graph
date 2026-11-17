---
id: kt:round-robin
type: Rule
title: Round robin
aliases: [Round-robin tournament, Round robin tournament, All-play-all, All-play-all tournament, Double round robin, Single round robin]
domain: events-and-organizations
summary: >-
  A tournament format in which every participant plays every other participant, once in a single round robin or
  twice with colours reversed in a double round robin; FIDE schedules it with the Berger tables of Handbook C.05
  Annex 1 and ranks tied players with round-robin tie-breaks such as Sonneborn-Berger and the Koya system.
status: current
volatile: true
verified: 2026-11-17
broader: [kt:chess-tournament]
related: [kt:tie-break, kt:arbiter, kt:candidates-tournament, kt:tata-steel-chess-tournament]
relations:
  - {predicate: sanctionedBy, object: kt:fide}
  - {predicate: hasPart, object: kt:berger-tables}
  - {predicate: alternativeTo, object: kt:swiss-system}
  - {predicate: alternativeTo, object: kt:knockout-tournament}
  - {predicate: exemplifiedBy, object: kt:candidates-tournament}
sources:
  - id: s1
    title: "C.05 Annex 1: Details of Berger Tables"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/C05Annex1
    type: governing-body
    accessed: 2026-11-17
  - id: s2
    title: "C.07 Play-Off and Tie-Break Regulations (applied from 1 March 2026)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/TieBreakRegulations032026
    type: governing-body
    accessed: 2026-11-17
  - id: s3
    title: "C.05 Annex 2: Details of Varma Tables"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/C05Annex2
    type: governing-body
    accessed: 2026-11-17
  - id: s4
    title: "Regulations for the FIDE Candidates Tournament 2026"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/files/handbook/Regulations_for_the_FIDE_Candidates_Tournament_2026.pdf
    type: governing-body
    accessed: 2026-11-17
  - id: s5
    title: "double round-robin"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/double-round-robin
    type: reference
    accessed: 2026-11-17
  - id: s6
    title: "How old are the Berger round-robin tables?"
    publisher: US Chess Forum (thread citing The Oxford Companion to Chess)
    url: https://forum.uschess.org/t/how-old-are-the-berger-round-robin-tables/6841
    type: community
    accessed: 2026-11-17
created: 2026-11-17
---

# Round robin

A round robin, or all-play-all, is the tournament format in which every participant meets every other participant. In a single round robin each pairing is played once; in a double round robin each pair of players plays twice, once with White and once with Black.[^s5] Because everyone faces the same opposition, the final table is a direct comparison of results rather than a product of pairing luck, which is why the format is the classic choice for small elite fields and qualification events. FIDE does not leave the schedule to the organiser's imagination: Annex 1 of Handbook chapter C.05 publishes fixed Berger tables that say who plays whom in every round.[^s1]

## How the schedule works

**Number of rounds.** With an even number of players *n*, a single cycle takes *n* − 1 rounds; with an odd number it takes *n* rounds, because one player sits out each round. FIDE handles odd fields simply: the table for the next even number is used and the highest number counts as a bye, so seven players use the eight-player table and whoever would have met number 8 rests that round.[^s1]

**Pairings by starting number.** Players receive numbers (normally by drawing lots) and the table does the rest. In the eight-player table, round one is 1–8, 2–7, 3–6, 4–5, round two is 8–5, 6–4, 7–3, 1–2, and round seven closes with 4–8, 5–3, 6–2, 7–1.[^s1] Number 8 switches side of the pairing every round (second, first, second, first …), and the other numbers rotate around it, so every pair meets exactly once in seven rounds.[^s1]

**Double round robin.** The second cycle repeats the first with colours reversed. FIDE recommends swapping the order of the last two rounds of the first cycle, because otherwise the join between the cycles would give some players three games in a row with the same colour.[^s1]

**Separating compatriots.** When several players come from the same federation, FIDE's Varma tables offer a restricted drawing of lots: the arbiter prepares envelopes holding predetermined sets of starting numbers, the largest federation draws first, and its players all draw from the same set. The tables cover fields of 9 to 24 players.[^s3] The Candidates Tournament takes a related approach from the other direction, requiring that, where possible, players from the same federation meet each other early in each half of the event before facing the rest of the field.[^s4]

## Example: the 2026 Candidates

FIDE's regulations for the 2026 Candidates Tournament set out a textbook double round robin: eight players, fourteen rounds, scored one point for a win, half for a draw and nothing for a loss, with the draw for pairings and colours made by the chief arbiter at least four weeks before the start.[^s4] A tie for first place is settled by rapid play-offs; if two players are tied they play a two-game match, while three or more play a single round robin at faster time controls, followed if needed by blitz and a knockout.[^s4] Ties for other places are broken by Sonneborn-Berger, then number of wins, then the games between the tied players, then lots.[^s4]

## Tie-breaks in a round robin

Since everyone has the same opponents, the Buchholz family of tie-breaks (sum of opponents' scores) tells you nothing, and FIDE's C.07 says those tie-breaks must not be used in round robins.[^s2] Instead the usual tools are:

- **Sonneborn-Berger**: multiply each opponent's final score by the points you took from that opponent and add the products, so wins against the leaders count for more than wins against the tail.[^s2]
- **Koya system**: the points a player scored against opponents who finished on at least half the maximum score; organisers may move that threshold by half a point.[^s2]
- **Direct encounter**: if all the tied players have played each other, which in a complete round robin they have, their mutual results rank them.[^s2]
- **Number of wins** and **games with Black**, which reward decisive play and the harder colour.[^s2]

A worked case: in a six-player single round robin, a player who beat the winner (4 points), drew with a 3-point player and lost the rest scores 4 + 1.5 = 5.5 Sonneborn-Berger. For events with fixed pairings such as round robins, forfeits are generally treated like ordinary results, with exceptions for some tie-breaks.[^s2]

## Strengths and pitfalls

The format's fairness comes at a cost: the number of rounds grows with the field, so a sixteen-player event already needs fifteen rounds, and the Berger tables in the Handbook stop at sixteen.[^s1] Withdrawals also distort the table, because the remaining games against the withdrawn player turn into forfeits; C.07 counts forfeits in pre-paired events as ordinary results for most purposes, but keeps forfeit losses as unplayed rounds for win-count tie-breaks and ignores all forfeits in rating-based ones.[^s2] For club players the practical points are to read the event's tie-break order in advance and to remember that, under Sonneborn-Berger, half a point against a leader is worth more than a win against the player who finishes last.[^s2][^s4]

## History

The pairing tables FIDE now calls Berger tables were, according to *The Oxford Companion to Chess* as cited in a US Chess forum discussion, first published by Richard Schurig in the *Deutsche Schachzeitung* in 1886, and later popularised by the Graz author Johann Berger in his chess yearbooks of the 1890s.[^s6] The name stuck to Berger even though Schurig came first.[^s6]

## Connections

The round robin is one of the formats of a **chess tournament**, the main **alternative** to the **Swiss system** and to the **knockout tournament**, and it is **sanctioned by** **FIDE** through Handbook chapter C.05, whose **Berger tables** form its schedule.[^s1] Ties are resolved under the **tie-break** regulations of C.07, applied by the **arbiter**, who also conducts the drawing of lots.[^s2][^s3] The **Candidates Tournament** is the best-known example, run as an eight-player double round robin to choose the world title challenger.[^s4]

## Sources

[^s1]: FIDE Handbook, "C.05 Annex 1: Details of Berger Tables". https://handbook.fide.com/chapter/C05Annex1 (accessed 2026-11-17)
[^s2]: FIDE Handbook, "C.07 Play-Off and Tie-Break Regulations" (approved 2 February 2026, applied from 1 March 2026). https://handbook.fide.com/chapter/TieBreakRegulations032026 (accessed 2026-11-17)
[^s3]: FIDE Handbook, "C.05 Annex 2: Details of Varma Tables". https://handbook.fide.com/chapter/C05Annex2 (accessed 2026-11-17)
[^s4]: FIDE, "Regulations for the FIDE Candidates Tournament 2026". https://handbook.fide.com/files/handbook/Regulations_for_the_FIDE_Candidates_Tournament_2026.pdf (accessed 2026-11-17)
[^s5]: Encyclopaedia Britannica, "double round-robin". https://www.britannica.com/topic/double-round-robin (accessed 2026-11-17)
[^s6]: US Chess Forum, "How old are the Berger round-robin tables?" (thread citing The Oxford Companion to Chess). https://forum.uschess.org/t/how-old-are-the-berger-round-robin-tables/6841 (accessed 2026-11-17)
