---
id: kt:fair-play-regulations
type: Rule
title: Fair play regulations
aliases: [FIDE Fair Play Regulations, Anti-cheating regulations, FIDE Anti-Cheating Regulations, Anti-cheating rules, Fair play rules, Fair Play Protection Measures]
domain: events-and-organizations
summary: >-
  FIDE's rules for preventing, investigating and sanctioning cheating in rated chess: they define cheating
  and lesser fair-play violations, set statistical thresholds for presumed cheating, route complaints through
  the Fair Play Commission, and grade tournaments into three levels of anti-cheating protection.
status: current
volatile: true
verified: 2026-11-10
broader: [kt:fide-handbook]
related: [kt:fide-laws-of-chess, kt:grandmaster-title, kt:arbiter, kt:computer-chess, kt:elo-rating-system]
relations:
  - {predicate: developedBy, object: kt:fide}
  - {predicate: dependsOn, object: kt:fide-laws-of-chess}
  - {predicate: governedBy, object: kt:fide-ethics-and-disciplinary-code}
  - {predicate: usesTechnique, object: kt:intrinsic-performance-rating}
sources:
  - id: s1
    title: "Fair Play Regulations (approved 10 November 2024, applied from 18 November 2024)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/files/handbook/FPL_Regulations_2024.pdf
    type: governing-body
    accessed: 2026-11-10
  - id: s2
    title: "Fair Play Protection Measures (approved 10 November 2024, applied from 18 November 2024)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/files/handbook/FPL_Protection_Measures_2024.pdf
    type: governing-body
    accessed: 2026-11-10
  - id: s3
    title: "Article 11: The Conduct of the Players"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/?p=872
    type: governing-body
    accessed: 2026-11-10
  - id: s4
    title: "Changes of the article 11.3.b. of the Laws of Chess (Takis Nikolopoulos, 17 September 2014)"
    publisher: FIDE Arbiters' Commission
    url: https://arbiters.fide.com/?p=1410
    type: governing-body
    accessed: 2026-11-10
  - id: s5
    title: "Intrinsic Chess Ratings (Kenneth W. Regan and Guy Haworth, Proceedings of AAAI 2011, pp. 834-839)"
    publisher: University at Buffalo Research Connect
    url: https://researchconnect.buffalo.edu/en/publications/intrinsic-chess-ratings/
    type: peer-reviewed
    accessed: 2026-11-10
created: 2026-11-10
---

# Fair play regulations

FIDE's fair play regulations are the body of rules that deal with cheating in rated chess. As of November 2026 the core texts are the Fair Play Regulations and the companion Fair Play Protection Measures, both approved by the FIDE Council on 10 November 2024 and applied from 18 November 2024.[^s1][^s2] They sit alongside, not inside, the Laws of Chess: the Laws forbid outside help at the board, while the regulations say how suspicions are reported, investigated and passed on for sanction, supplementing the FIDE Charter and the Ethics and Disciplinary Code (EDC).[^s1][^s3]

## What counts as cheating

The regulations define cheating in two families. The first is the deliberate use of electronic devices or other sources of information or advice during a game. The second is manipulation of competitions: fixing results, sandbagging (deliberately playing below one's strength to lower one's rating for a later event), match-fixing, rating fraud, false identity and fictitious tournaments or games. Attempts count as cheating too.[^s1] Below that line are "other fair play violations": bringing a phone or forbidden gadget into the playing hall, refusing to be searched or scanned, or not cooperating with the fair play team; online, disconnecting or playing without the required camera, microphone or screen sharing. These do not by themselves imply cheating but can be penalised on the spot.[^s1]

The over-the-board backbone is Article 11.3 of the Laws of Chess. It bars notes, sources of information or advice, and any electronic device not approved by the arbiter in the playing venue; an event may allow a completely switched-off device in a bag, but a device evidently on a player's person loses the game unless event rules set a lighter penalty. The arbiter may also order a private inspection of clothing, bags or body by someone of the same gender, and refusal is dealt with under Article 12.9.[^s3] The switched-off-in-a-bag option dates from 2014, when the Rules Commission rewrote the article at the request of FIDE's then Anti-Cheating Committee and arbiters were told to apply it from 1 October 2014, though not in World or Continental championships.[^s4]

## Statistics and the burden of proof

The most distinctive feature is a statistical presumption. If an approved method returns a Z-score above the official threshold, cheating is presumed, and once disciplinary proceedings start the player carries the burden of rebutting it.[^s1] As of November 2026 the only approved method is Kenneth Regan's, combining move-matching, equal-top-value moves and average scaled difference; the threshold is 5.00 for over-the-board play and 4.25 online, and a score of 2.50 or more can support a case that also has other evidence.[^s1] The approach grows out of Regan and Guy Haworth's work on "intrinsic" ratings, which estimate playing strength from the quality of moves as judged by a strong engine rather than from results, and which they calibrated against Elo ratings on large sets of tournament games.[^s5] Online, FIDE may also find cheating without decisive statistics if other evidence, such as video or expert opinion from titled players, is strong enough.[^s1]

## Complaints and investigation

Anyone with a FIDE ID may complain, but only in writing, using the regulations' forms: an in-tournament complaint goes to the Chief Fair Play Officer (or the Chief Arbiter if there is none), and a post-tournament complaint must explain why it was not raised during the event.[^s1] Complaints based only on a player seeming stronger than their rating are treated as manifestly unfounded, and reckless accusations can themselves earn a warning or an EDC referral.[^s1] The Fair Play Commission (FPL) may appoint an Investigatory Panel of up to three members; if the panel unanimously finds no case it dismisses the complaint, otherwise it reports with a proposed sanction and the FPL decides by majority whether to send the case to the EDC, which imposes penalties.[^s1] Everything is confidential until the investigation ends, the accused must be told in writing and allowed to respond, and the limitation period is five years (one year for online events).[^s1]

## Protection levels

The Protection Measures sort events into three levels.[^s2] Maximum protection covers FIDE World events, major continental events, very strong round-robins and events with prize funds above EUR 100,000; it brings a dedicated fair play team under a Chief Fair Play Officer, a scanning booth, random and post-game checks, shielded storage for devices and screening of every game score.[^s2] Increased protection covers norm events, national championships and prize funds from EUR 15,000, with a designated fair play specialist and controlled player–spectator contact; standard protection, for all other rated events, needs at least a person in charge of fair play and one security measure such as a metal detector.[^s2] The level also decides jurisdiction: cases from maximum- and increased-protection events go to the FPL, while standard-level cases usually stay with national federations unless titled players or title applications are involved.[^s1]

## Practical points for players

For a club player the rules boil down to a few habits: leave the phone outside or switched off where the event allows, expect scanning at stronger events, report a suspicion privately to the arbiter rather than accusing anyone publicly, and know that a rating gap alone is not grounds for a complaint.[^s1][^s3]

## Connections

The regulations are **developed by FIDE** and are part of the wider **FIDE Handbook**; they **depend on** Article 11.3 of the **FIDE Laws of Chess** for the over-the-board ban on devices, and sanctions are decided under the **FIDE Ethics and Disciplinary Code**.[^s1][^s3] The statistical test **uses** Regan's **intrinsic performance rating** approach, which ties move quality to the **Elo rating system** and relies on **computer chess** engines.[^s1][^s5] The **arbiter** enforces device rules and handles in-tournament complaints, and a fair-play finding can cost a player a title such as the **grandmaster title**.[^s1][^s3]

## Sources

[^s1]: FIDE Handbook, "Fair Play Regulations" (approved 10 November 2024, applied from 18 November 2024). https://handbook.fide.com/files/handbook/FPL_Regulations_2024.pdf (accessed 2026-11-10)
[^s2]: FIDE Handbook, "Fair Play Protection Measures" (approved 10 November 2024, applied from 18 November 2024). https://handbook.fide.com/files/handbook/FPL_Protection_Measures_2024.pdf (accessed 2026-11-10)
[^s3]: FIDE Rules Commission, "Article 11: The Conduct of the Players". https://rcc.fide.com/?p=872 (accessed 2026-11-10)
[^s4]: Takis Nikolopoulos, FIDE Arbiters' Commission, "Changes of the article 11.3.b. of the Laws of Chess" (17 September 2014). https://arbiters.fide.com/?p=1410 (accessed 2026-11-10)
[^s5]: Kenneth W. Regan and Guy Haworth, "Intrinsic Chess Ratings", Proceedings of the 25th AAAI Conference on Artificial Intelligence (2011), pp. 834-839; record at University at Buffalo Research Connect. https://researchconnect.buffalo.edu/en/publications/intrinsic-chess-ratings/ (accessed 2026-11-10)
