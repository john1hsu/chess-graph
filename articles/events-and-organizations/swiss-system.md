---
id: kt:swiss-system
type: Rule
title: Swiss system
aliases: [Swiss-system tournament, Swiss tournament, Swiss pairing system, Swiss pairings, Swiss system pairings, Müller system, Mueller system]
domain: events-and-organizations
summary: >-
  A tournament pairing method in which a fixed number of rounds is played and, each round, players on equal or
  similar scores are paired without repeat games and with balanced colours; FIDE regulates it in Handbook chapter
  C.04, whose standard algorithm is the Dutch system, with Dubov, Burstein and Lim as approved alternatives.
status: current
volatile: true
verified: 2026-11-16
broader: [kt:chess-tournament]
related: [kt:tie-break, kt:arbiter, kt:chess-olympiad, kt:fide-world-cup]
relations:
  - {predicate: sanctionedBy, object: kt:fide}
  - {predicate: developedBy, object: kt:julius-muller}
  - {predicate: hasPart, object: kt:dutch-system}
  - {predicate: hasPart, object: kt:baku-acceleration}
  - {predicate: alternativeTo, object: kt:round-robin}
sources:
  - id: s1
    title: "C.04.3 FIDE (Dutch) System (effective from 1 February 2026)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/C0403202602
    type: governing-body
    accessed: 2026-11-16
  - id: s2
    title: "C.04.7 FIDE-Approved Accelerated Systems (effective from 1 February 2026)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/C0407202602
    type: governing-body
    accessed: 2026-11-16
  - id: s3
    title: "Other FIDE-Approved Pairing Systems"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/OtherApprovedPairingSystems202602
    type: governing-body
    accessed: 2026-11-16
  - id: s4
    title: "C.04.4.1 Dubov System (effective from 1 February 2026)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/C040401202602
    type: governing-body
    accessed: 2026-11-16
  - id: s5
    title: "Most Swiss-system tournaments are unfair: Evidence from chess"
    publisher: arXiv (László Csató, HUN-REN SZTAKI and Corvinus University of Budapest)
    url: https://arxiv.org/html/2410.19333v2
    type: academic
    accessed: 2026-11-16
  - id: s6
    title: "125 years Swiss System"
    publisher: ChessBase News (André Schulz, 17 June 2020)
    url: https://en.chessbase.com/newsroom/post/125-years-swiss-system?page=0
    type: publication
    accessed: 2026-11-16
created: 2026-11-16
---

# Swiss system

The Swiss system is the pairing method behind almost every large open chess tournament. The number of rounds is set in advance, usually far fewer than an all-play-all would need, and before each round the players are re-sorted by score and matched against opponents on the same or a similar score, so that the leaders keep meeting each other while nobody is eliminated.[^s5] Three constraints run through every version: two players never meet twice, colours are kept as balanced as possible, and an odd player out receives a bye.[^s1][^s5]

## Origin

ChessBase credits the method to Julius Müller (1857–1917), a teacher from Brugg near Zurich, and notes that it could fairly be called the Müller system.[^s6] Most accounts date it to the 5th Swiss Chess Tournament in Zurich in June 1895, won by the organiser Max Pestalozzi, although a history of the Zurich chess society argues that Müller tried an early version at the first Swiss tournament of 1889, which had 74 entrants.[^s6] Its appeal was practical: as chess spread in the late nineteenth century it let large fields finish on a fixed schedule, and it became the standard format for amateur events.[^s6] The format has since spread beyond chess to badminton, croquet and esports.[^s5]

## How a Dutch-system round is paired

FIDE does not prescribe one algorithm; it approves several, and its standard one is the FIDE (Dutch) System, chapter C.04.3, whose current text applies from 1 February 2026.[^s1][^s3] The Dutch rules work as follows:[^s1]

- **Ranking.** Players are sorted by score, then by ascending tournament pairing number (TPN).[^s1]
- **Scoregroups and brackets.** Everyone on the same score forms a scoregroup. Pairing starts with the top group and works downwards; a player who cannot be paired in one bracket *downfloats* into the next, where they are paired first.[^s1]
- **Halves.** In a bracket, the upper half (S1) is paired against the lower half (S2) in order: first of S1 against first of S2, second against second, and so on.[^s1]
- **Repairs.** If the result breaks a rule, the program tries reorderings of S2, then exchanges between the halves, until it finds the best candidate.[^s1]
- **Absolute and quality criteria.** No rematches, no second bye, and no pairing of two non-topscorers who both *must* have the same colour. Below those come ranked quality criteria: fewer and lower-scoring floaters, then colour preferences, then avoiding the same player floating repeatedly.[^s1]
- **Colours.** A player whose White–Black difference exceeds one, or who has had the same colour twice running, has an absolute preference; a difference of exactly one gives a strong preference. When both players want the same colour, the stronger preference wins, then alternation from their last differing round, then the higher-ranked player.[^s1]

**Example.** Eight players reach round three on 1½ points, with no rematches or colour clashes. S1 holds the four highest-ranked and S2 the other four, so the pairings are 1–5, 2–6, 3–7 and 4–8: the top player meets the best of the lower half rather than the weakest player in the group.[^s1]

## Variants and acceleration

FIDE also approves the Dubov, Burstein and Lim systems for individuals, a Double-Swiss system, and a separate Swiss Team Pairing System.[^s3] The Dubov system starts from a different idea of fairness: it tries to equalise the average rating of opponents within a scoregroup, giving players whose opponents have so far been weak the stronger pairings.[^s4]

Because early rounds of a big open pit top seeds against much weaker players with predictable results, FIDE's C.04.7 approves the Baku acceleration method to make norms easier to achieve.[^s2] The top half of the starting list (rounded up to an even number) gets *virtual points* used only for pairing: a full win's worth in the first accelerated rounds and half that later, until halfway through the event. In a nine-round event, that means one point in rounds one to three and half a point in rounds four and five.[^s2]

## Fairness and pitfalls

- **Odd numbers of rounds.** Most Swiss events have an odd number of rounds so that colours can stay balanced, which leaves roughly half the field with one extra White.[^s6] László Csató's study of 52 nine- and eleven-round events from 2016 to 2024 found that the extra White was worth about 15–30 rating points and raised the chance of a top score; he proposes even-length events with balanced colours.[^s5]
- **Ranking depends on tie-breaks.** With few rounds, many players share a score, so the final order rests on the published tie-break list.[^s5]
- **Byes.** A pairing-allocated bye scores a win unless the regulations say otherwise, and nobody may receive two.[^s1]

## Connections

The Swiss system is one of the formats of a **chess tournament** and the reason opponent-score **tie-breaks** such as Buchholz exist.[^s5] It is **sanctioned by** **FIDE** through Handbook chapter C.04, applied by the **arbiter** with approved pairing software; its parts include the **Dutch system** and **Baku acceleration**, and it is the **alternative** to the all-play-all **round robin**.[^s1][^s2][^s3] It was **developed by** Julius Müller, and team events such as the **Chess Olympiad** use the team version.[^s3][^s6]

## Sources

[^s1]: FIDE Handbook, "C.04.3 FIDE (Dutch) System" (approved 28 October 2025, effective from 1 February 2026). https://handbook.fide.com/chapter/C0403202602 (accessed 2026-11-16)
[^s2]: FIDE Handbook, "C.04.7 FIDE-Approved Accelerated Systems" (effective from 1 February 2026). https://handbook.fide.com/chapter/C0407202602 (accessed 2026-11-16)
[^s3]: FIDE Handbook, "Other FIDE-Approved Pairing Systems". https://handbook.fide.com/chapter/OtherApprovedPairingSystems202602 (accessed 2026-11-16)
[^s4]: FIDE Handbook, "C.04.4.1 Dubov System" (effective from 1 February 2026). https://handbook.fide.com/chapter/C040401202602 (accessed 2026-11-16)
[^s5]: László Csató, "Most Swiss-system tournaments are unfair: Evidence from chess", arXiv:2410.19333v2 (24 September 2025). https://arxiv.org/html/2410.19333v2 (accessed 2026-11-16)
[^s6]: André Schulz, "125 years Swiss System", ChessBase News, 17 June 2020. https://en.chessbase.com/newsroom/post/125-years-swiss-system?page=0 (accessed 2026-11-16)
