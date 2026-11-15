---
id: kt:tie-break
type: Rule
title: Tie-break
aliases: [Tiebreak, Tie-breaks, Tiebreaks, Tie-break systems, Tie-break regulations, Play-Off and Tie-Break Regulations, FIDE C.07, Breaking ties]
domain: events-and-organizations
summary: >-
  The pre-announced methods a chess competition uses to rank players or teams who finish on the same score,
  either off the board (Buchholz, Sonneborn-Berger, direct encounter, number of wins, rating-based measures and
  others, applied in a fixed order) or over the board by a play-off; FIDE codifies them in Handbook chapter C.07.
status: current
volatile: true
verified: 2026-11-15
broader: [kt:chess-tournament]
related: [kt:arbiter, kt:chess-olympiad, kt:us-chess, kt:us-chess-championship, kt:blitz-chess, kt:candidates-tournament]
relations:
  - {predicate: developedBy, object: kt:fide}
  - {predicate: dependsOn, object: kt:swiss-system}
  - {predicate: alternativeTo, object: kt:play-off}
sources:
  - id: s1
    title: "C.07 Play-Off and Tie-Break Regulations (approved 29 July 2024, applied 1 August 2024 to 28 February 2026)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/TieBreakRegulations082024
    type: governing-body
    accessed: 2026-11-15
  - id: s2
    title: "FIDE reminds organizers and arbiters of updated Play-Off and Tie-Break Regulations effective March 1, 2026"
    publisher: FIDE
    url: https://www.fide.com/fide-reminds-organizers-and-arbiters-of-updated-play-off-and-tie-break-regulations-effective-march-1-2026/
    type: governing-body
    accessed: 2026-11-15
  - id: s3
    title: "US Chess Federation's Official Rules of Chess, 7th edition, free download version (chapters 1, 2, 9, 10, 11; revised 1 January 2026), rule 34 Breaking Ties"
    publisher: US Chess Federation
    url: https://new.uschess.org/sites/default/files/media/documents/us-chess-rule-book-online-2026.pdf
    type: governing-body
    accessed: 2026-11-15
  - id: s4
    title: "Tie Break Regulations"
    publisher: All India Chess Federation
    url: https://aicf.in/tie-break-regulations
    type: governing-body
    accessed: 2026-11-15
created: 2026-11-15
---

# Tie-break

A tie-break is the rule a chess competition uses to decide the order of players, or teams, who end on the same number of points. FIDE's regulations recognise two families of solution: an over-the-board **play-off**, in which the tied players meet again, and an off-the-board **tie-break**, a calculation from the results already played.[^s1] Which one applies, and whether tied players may instead simply share a place, is meant to be written into the tournament regulations; if those say nothing, FIDE's default is to rank by tie-breaks.[^s1]

## How a tie-break list works

Tie-breaks are used as an ordered list. The organiser picks the list, the chief arbiter may extend it, and the complete sequence has to be published before round one; the arbiter then works down the list until the tie is resolved, and only if every criterion fails is the tie settled by drawing lots (unless the rules allow it to stand).[^s1] US Chess gives the same advice from the director's side: one method often fails, so at least the first two should be posted at the site before play starts.[^s3]

FIDE's 2024 text sorts the methods into four kinds: those using only a subset of games, such as the result between the tied players; those using the player's own record; those using opponents' final scores; and those using opponents' pre-event data such as ratings.[^s1] The best-known members are:

- **Direct encounter** – the score in games among the tied players.[^s1]
- **Wins and colour counts** – number of wins, games won over the board, games played with Black, games won with Black.[^s1]
- **Buchholz** – the sum of the opponents' final scores, often with a *Cut-1* (drop the weakest opponent) or *Median* (drop the extremes) modifier.[^s1]
- **Sonneborn-Berger** – opponents' scores weighted by what the player took from each; the **Koya** count, aimed at round robins, totals points scored against opponents who reached 50%.[^s1]
- **Rating-based** – average rating of opponents, tournament performance rating and the average performance of opponents.[^s1]

FIDE revised C.07 again from 1 March 2026, clarifying Buchholz, changing how unplayed games enter Buchholz and Sonneborn-Berger, adding team-knockout provisions and appending extra tie-breaks so that fewer standings fall to lots.[^s2]

## National practice

National federations keep their own defaults. Unless something else is announced, US Chess players should expect Modified Median, Solkoff, Cumulative and Cumulative of Opposition, in that order.[^s3] Modified Median, credited to Kenneth Harkness, discards the least significant opponent scores; Solkoff is the same sum with nothing removed; Cumulative adds the player's running score after each round, rewarding an early lead that brought tougher pairings.[^s3] US Chess does not use tie-breaks for cash: money prizes are split evenly unless a play-off was advertised in advance.[^s3] India's federation, by a 2013 Central Council resolution, ranked round-robin ties by direct encounter, Sonneborn-Berger, number of wins and wins with Black, and Swiss ties by Buchholz Cut 1, Buchholz Cut 2, Sonneborn-Berger and Buchholz Median.[^s4]

## A worked example

Suppose a player scores 2½/4 in a Swiss: wins against opponents who finish on 2 and 1½, a draw with one on 3, and a loss to one on 3½. Her Buchholz (and US Solkoff) is 2 + 1½ + 3 + 3½ = 10; Buchholz Cut-1 drops the 1½ and gives 8½, as does US Modified Median for a plus score.[^s1][^s3] Her Sonneborn-Berger counts the full scores of the two players she beat and half the score of the one she drew: 2 + 1½ + 1½ = 5, with nothing for the loss.[^s3] If her results came in the order win, win, draw, loss, her cumulative total is 1 + 2 + 2½ + 2½ = 8.[^s3]

## Pitfalls

- **Unplayed games.** Byes and forfeits distort opponent-based scores. FIDE scores a player's own unplayed rounds as games against a dummy opponent on the same final score, while US Chess adjusts an opponent's unplayed rounds to half a point each for tie-break purposes.[^s1][^s3]
- **Wrong format.** Sonneborn-Berger ignores losses, which US Chess calls a weakness in a Swiss, where losing to a strong player should count for more; in a round robin everyone faces the same field, so the problem disappears.[^s3]
- **Unrated players.** FIDE removes rating-based tie-breaks when unrated players take part, unless the regulations say how to handle them.[^s1]
- **Perfect scores.** US Chess urges a play-off when several players finish with maximum scores, since no tie-break can show who could have done better.[^s3]

## Connections

Tie-breaks are part of the machinery of a **chess tournament** and are set out by **FIDE** in Handbook chapter C.07, which is applied by the **arbiter**.[^s1] Opponent-score methods such as Buchholz exist because of the **Swiss system**, where players meet different fields; the **play-off**, often at a faster **blitz** or rapid time control, is the over-the-board alternative.[^s1][^s3] **US Chess** keeps its own rulebook order, and team events such as the **Chess Olympiad** use match-point and board-count variants.[^s1][^s3]

## Sources

[^s1]: FIDE Handbook, "C.07 Play-Off and Tie-Break Regulations" (approved 29 July 2024, applied 1 August 2024 to 28 February 2026). https://handbook.fide.com/chapter/TieBreakRegulations082024 (accessed 2026-11-15)
[^s2]: FIDE, "FIDE reminds organizers and arbiters of updated Play-Off and Tie-Break Regulations effective March 1, 2026" (25 March 2026). https://www.fide.com/fide-reminds-organizers-and-arbiters-of-updated-play-off-and-tie-break-regulations-effective-march-1-2026/ (accessed 2026-11-15)
[^s3]: US Chess Federation, *Official Rules of Chess*, 7th edition, free download version revised 1 January 2026, rule 34 "Breaking Ties". https://new.uschess.org/sites/default/files/media/documents/us-chess-rule-book-online-2026.pdf (accessed 2026-11-15)
[^s4]: All India Chess Federation, "Tie Break Regulations" (Central Council resolution of 3 March 2013). https://aicf.in/tie-break-regulations (accessed 2026-11-15)
