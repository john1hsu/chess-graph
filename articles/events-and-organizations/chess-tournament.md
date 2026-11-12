---
id: kt:chess-tournament
type: Concept
title: Chess tournament
aliases: [Tournament chess, Chess tournaments, Tournament formats in chess]
domain: events-and-organizations
summary: >-
  A competition in which several players (or teams) play a planned series of games and are ranked by score;
  the main formats are the all-play-all round robin, the Swiss system and the knockout, with tie-break rules
  separating players who finish level, all set out for rated play in Section C of the FIDE Handbook.
status: current
volatile: true
verified: 2026-11-12
broader: [kt:chess]
related: [kt:arbiter, kt:hastings-1895, kt:candidates-tournament, kt:chess-olympiad]
relations:
  - {predicate: sanctionedBy, object: kt:fide}
  - {predicate: governedBy, object: kt:fide-laws-of-chess}
  - {predicate: hasPart, object: kt:swiss-system}
  - {predicate: hasPart, object: kt:tie-break}
sources:
  - id: s1
    title: "C.04.1 Basic Rules for Swiss Systems (applied from 1 February 2026)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/C0401202507
    type: governing-body
    accessed: 2026-11-12
  - id: s2
    title: "C.04.2 General Handling Rules for Swiss Tournaments (applied from 1 February 2026)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/GeneralHandlingRulesForSwissTournaments202602
    type: governing-body
    accessed: 2026-11-12
  - id: s3
    title: "C.05 Annex 1: Details of Berger Tables"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/C05Annex1
    type: governing-body
    accessed: 2026-11-12
  - id: s4
    title: "C.07 Play-Off and Tie-Break Regulations (applied from 1 March 2026)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/TieBreakRegulations032026
    type: governing-body
    accessed: 2026-11-12
  - id: s5
    title: "125 years Swiss System"
    publisher: ChessBase News (André Schulz, 17 June 2020)
    url: https://en.chessbase.com/post/125-years-swiss-system
    type: publication
    accessed: 2026-11-12
  - id: s6
    title: "London 1851"
    publisher: OlimpBase (Wojciech Bartelski)
    url: https://www.olimpbase.org/ind-varia/it-london1851.html
    type: database
    accessed: 2026-11-12
  - id: s7
    title: "175 years ago: Anderssen's Immortal Game is played in London"
    publisher: ChessBase News (André Schulz, 23 June 2026)
    url: https://en.chessbase.com/newsroom/post/175-years-anderssen-immortal
    type: publication
    accessed: 2026-11-12
created: 2026-11-12
---

# Chess tournament

A chess tournament is a competition in which a group of players, or teams, play a pre-arranged series of games and are ranked by the points they score, normally one for a win, half for a draw and nothing for a loss. Unlike a match, where two players meet repeatedly, a tournament needs a pairing method to decide who plays whom in each round and a ranking method to separate players on equal scores. For FIDE-rated events these mechanics are laid down in Section C of the FIDE Handbook: the Swiss rules (C.04), the general regulations for competitions with their Berger tables (C.05) and the play-off and tie-break regulations (C.07).[^s1][^s3][^s4]

## Origins

The first major international tournament was held in London in 1851, organised by Howard Staunton alongside the Great Exhibition, and it is often treated as the start of modern tournament history.[^s7] It was not an all-play-all: sixteen players met in knockout matches, best of three in the first round and best of seven afterwards, with draws not counting, and Adolf Anderssen won every match, beating Staunton in the semi-final and Wyvill in the final.[^s6][^s7] Its knockout format meant that a player could go out after a single short match, a weakness the all-play-all formats that followed avoid.

## The main formats

**Round robin (all-play-all).** Every player meets every other once, or twice in a double round robin with colours reversed. FIDE's Berger tables give a fixed schedule by starting number: with eight players there are seven rounds, and round one pairs 1–8, 2–7, 3–6 and 4–5.[^s3] With an odd number of players the highest number counts as a bye, so the table for seven players is the eight-player table with one slot empty.[^s3] For a double round robin FIDE recommends swapping the order of the last two rounds of the first cycle so that nobody gets the same colour three times running.[^s3] The format is fair but needs n−1 rounds for n players, so it suits small elite fields.

**Swiss system.** A Swiss event fixes the number of rounds in advance and, in general, pairs players against others on the same score, so leaders meet leaders without everyone having to play everyone.[^s1] FIDE's basic rules add that two participants may not meet more than once, that a player's surplus of one colour should stay within two games, and that nobody should get the same colour three times in a row, subject to exceptions defined by each pairing system.[^s1] When the field is odd, one player receives a pairing-allocated bye worth a win unless the regulations say otherwise, and no one can receive it twice.[^s1] From 1 February 2026 FIDE also requires that approved pairings be objective, impartial and reproducible, and forbids altering correct pairings to favour a player.[^s2] The system is credited to Julius Müller, a teacher from Brugg, and dated to a Zurich tournament of 1895, with an earlier trial at the first Swiss Chess Tournament in 1889.[^s5] It became the standard format for large open events because it lets everyone play every round on a fixed schedule.[^s5]

**Knockout.** Players or teams are eliminated in mini-matches, as in London 1851.[^s6] FIDE lists knockout alongside round robin as a possible play-off format, and its tie-break regulations include separate board-count methods for team knockouts.[^s4]

## Tie-breaks and play-offs

Because many players finish on the same score, especially in a Swiss, the regulations must say in advance whether tied players share the place, play off, or are ranked by tie-break.[^s4] FIDE's C.07 (in force from 1 March 2026) lists a menu that includes direct encounter between the tied players, number of wins, Buchholz (the sum of the opponents' scores), Sonneborn–Berger (opponents' scores weighted by the points taken from each) and rating-based measures such as average rating of opponents.[^s4] Some are format-specific: Buchholz-based tie-breaks must not be used in a round robin, where everyone has the same opponents, while the Koya system is designed for round robins.[^s4] Rating-based tie-breaks are dropped when unrated players take part unless the rules provide otherwise.[^s4]

## Practical points for club players

- Read the tournament regulations before round one: they fix the tie-break order, bye points and whether late entries score anything for missed rounds.[^s2][^s4]
- In a Swiss, a win in an early round raises you into a stronger score group; your tie-break depends on how your opponents do, so a loss to an eventual leader can be worth more on Buchholz than a win against a tail-ender.[^s4]
- Report an accidental repeat pairing to the arbiter at once; the chief arbiter may correct published pairings when two players who have already met are paired by mistake.[^s2]

## Connections

Every rated tournament is run by an **arbiter** and played under the **FIDE Laws of Chess**, with its format regulations **sanctioned by** **FIDE** in Handbook Section C.[^s1][^s4] Individual events in the graph are instances of the concept: **Hastings 1895**, the **Candidates Tournament** and the team **Chess Olympiad**, each with its own node, while London 1851 shows the knockout form.[^s6] The **Swiss system** and **tie-break** rules are parts of the tournament machinery that have their own frontier nodes.[^s1][^s4]

## Sources
[^s1]: FIDE Handbook, "C.04.1 Basic Rules for Swiss Systems" (applied from 1 February 2026). https://handbook.fide.com/chapter/C0401202507 (accessed 2026-11-12)
[^s2]: FIDE Handbook, "C.04.2 General Handling Rules for Swiss Tournaments" (applied from 1 February 2026). https://handbook.fide.com/chapter/GeneralHandlingRulesForSwissTournaments202602 (accessed 2026-11-12)
[^s3]: FIDE Handbook, "C.05 Annex 1: Details of Berger Tables". https://handbook.fide.com/chapter/C05Annex1 (accessed 2026-11-12)
[^s4]: FIDE Handbook, "C.07 Play-Off and Tie-Break Regulations" (applied from 1 March 2026). https://handbook.fide.com/chapter/TieBreakRegulations032026 (accessed 2026-11-12)
[^s5]: André Schulz, "125 years Swiss System", ChessBase News, 17 June 2020. https://en.chessbase.com/post/125-years-swiss-system (accessed 2026-11-12)
[^s6]: Wojciech Bartelski, "London 1851", OlimpBase. https://www.olimpbase.org/ind-varia/it-london1851.html (accessed 2026-11-12)
[^s7]: André Schulz, "175 years ago: Anderssen's Immortal Game is played in London", ChessBase News, 23 June 2026. https://en.chessbase.com/newsroom/post/175-years-anderssen-immortal (accessed 2026-11-12)
