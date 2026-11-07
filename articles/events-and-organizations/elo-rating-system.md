---
id: kt:elo-rating-system
type: RatingSystem
title: Elo rating system
aliases: [Elo rating, Elo system, Elo, FIDE rating, ELO rating]
domain: events-and-organizations
summary: >-
  The statistical rating method devised by Arpad Elo and adopted by the US Chess Federation in 1960
  and FIDE in 1970, in which each player's rating moves after every rating period by a K-factor
  times the difference between the actual score and the score the rating difference predicted.
status: current
volatile: true
verified: 2026-11-07
broader: [kt:chess-rating-systems]
related: [kt:us-chess, kt:grandmaster-title, kt:fide]
relations:
  - {predicate: developedBy, object: kt:arpad-elo}
  - {predicate: sanctionedBy, object: kt:fide}
  - {predicate: alternativeTo, object: kt:glicko-rating-system}
sources:
  - id: s1
    title: "FIDE Rating Regulations (approved by FIDE Council on 15/12/2023, applied from 1 March 2024)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/B022024
    type: governing-body
    accessed: 2026-11-07
  - id: s2
    title: "New FIDE Rating and Title Regulations come into effect"
    publisher: FIDE (fide.com news, 2 January 2024)
    url: https://www.fide.com/new-fide-rating-and-title-regulations-come-into-effect/
    type: governing-body
    accessed: 2026-11-07
  - id: s3
    title: "Rating the Chess Rating System"
    publisher: Mark E. Glickman and Albyn C. Jones (Boston University / Reed College), glicko.net
    url: https://www.glicko.net/research/chance.pdf
    type: academic
    accessed: 2026-11-07
  - id: s4
    title: "Arpad Emrick Elo"
    publisher: World Chess Hall of Fame (U.S. Chess Hall of Fame inductee page)
    url: https://develop.worldchesshof.org/node/2359
    type: archive
    accessed: 2026-11-07
  - id: s5
    title: "Arpad Elo and the Elo Rating System"
    publisher: Daniel Ross, ChessBase News (16 December 2007)
    url: https://en.chessbase.com/newsroom/post/arpad-elo-and-the-elo-rating-system?page=0
    type: publication
    accessed: 2026-11-07
created: 2026-11-07
---

# Elo rating system

The Elo rating system is the method by which almost every serious chess player's strength is measured. It was devised by Arpad Elo, a Hungarian-born physics professor at Marquette University and a master-strength player, to replace the Harkness system, which he regarded as arbitrary.[^s4] The US Chess Federation adopted it at its 1960 meeting in Saint Louis and FIDE followed in 1970;[^s4] Elo had chaired the USCF rating committee from 1959.[^s5] His book *The Rating of Chess Players, Past & Present* remains the standard account of the method.[^s4]

## How it works

The model assumes that each player has an unknown current strength, and the rating is an estimate of it.[^s3] The difference between two ratings predicts an expected score: in the usual logistic form, a player rated 200 points below the opponent is expected to score about 0.24 per game, the stronger player about 0.76.[^s3] After a rating period, the new rating is the old rating plus K multiplied by the difference between the points actually scored and the sum of the expected scores.[^s3] Glickman and Jones point out that the underlying statistics are older than Elo: Zermelo (1929) and Good (1955) developed related paired-comparison models.[^s3]

FIDE implements this with tables rather than a formula. Table 8.1.2 of its Rating Regulations converts a rating difference into a scoring probability; for each game the change is the result minus that probability, and the sum over the period is multiplied by K and rounded.[^s1] A worked example: under K = 20, a 1500 player who beats a 1700 player gains roughly 20 × (1 − 0.24) ≈ 15 points, while a loss would cost only about 5, because a loss was the expected result.[^s1][^s3]

## FIDE's current parameters (as of November 2026)

The regulations applied from 1 March 2024 set the K-factor at 40 for a newcomer until 30 games are completed, and for players until the end of the year of their 18th birthday while rated under 2300; at 20 while a player stays under 2400; and at 10 once a published rating has reached 2400.[^s1] K is also capped so that K times the number of games in a period does not exceed 700.[^s1] A first rating needs at least five games against rated opponents, is computed against the opponents' average plus two hypothetical 1800-rated opponents scored as draws, may not exceed 2200, and must be at least 1400.[^s1][^s2] Players who fall below 1400 are shown as unrated, and lists are published on the first day of every month.[^s1]

The 2024 reform also restored the rule that any rating difference above 400 points counts as 400, and applied a one-off adjustment of 0.40 × (2000 − rating) to every standard rating below 2000, compressing the bottom of the list.[^s2] A later amendment, effective from 1 October 2025, limits the 400-point cap to players rated below 2650; above that the actual difference is used.[^s1]

## Limitations and pitfalls

Statisticians have identified several weaknesses. The classical system carries no measure of how reliable a rating is, so a player returning after years away is treated like an active one.[^s3] Using over 225,000 games, Glickman and Jones found that the 400-point scale overpredicted the results of higher-rated players, and that the model ignores the advantage of the white pieces, which Elo himself estimated at about 50 points.[^s3] Pools can also drift: new players usually enter low and departing players are often above average, which deflates the average, and isolated groups such as scholastic pools can produce ratings that are not comparable with the rest of the list.[^s3] Fixes such as bonus points and rating floors have side effects; Glickman and Jones argue that floors weaken ratings as predictors.[^s3] For players, the practical lesson is that a rating is an estimate with noise, and that a K-factor change (for example at 2400) alters how fast it moves.[^s1]

## Connections

The Elo system was **developed by Arpad Elo** and first used by **US Chess** before being **sanctioned by FIDE**, which maintains the international list.[^s4][^s5] It is one of the **chess rating systems**; the **Glicko rating system** is its main **alternative**, and Glickman and Jones's proposed revision adds exactly the reliability measure that classical Elo lacks.[^s3] FIDE's rating rules were revised together with its title regulations, which govern titles such as the **grandmaster title**.[^s2]

## Sources
[^s1]: FIDE Handbook, "FIDE Rating Regulations" (applied from 1 March 2024, with later amendments). https://handbook.fide.com/chapter/B022024 (accessed 2026-11-07)
[^s2]: FIDE, "New FIDE Rating and Title Regulations come into effect", 2 January 2024. https://www.fide.com/new-fide-rating-and-title-regulations-come-into-effect/ (accessed 2026-11-07)
[^s3]: M. E. Glickman and A. C. Jones, "Rating the Chess Rating System". https://www.glicko.net/research/chance.pdf (accessed 2026-11-07)
[^s4]: World Chess Hall of Fame, "Arpad Emrick Elo". https://develop.worldchesshof.org/node/2359 (accessed 2026-11-07)
[^s5]: D. Ross, "Arpad Elo and the Elo Rating System", ChessBase News, 16 December 2007. https://en.chessbase.com/newsroom/post/arpad-elo-and-the-elo-rating-system?page=0 (accessed 2026-11-07)
