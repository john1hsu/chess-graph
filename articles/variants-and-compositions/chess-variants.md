---
id: kt:chess-variants
type: Concept
title: Chess variants
aliases: [Chess variant, Variant chess, Chess variations (games), Unorthodox chess]
domain: variants-and-compositions
summary: >-
  Games derived from, related to or modelled on chess that change its board, pieces, starting
  position, move rules or winning condition; they range from regional sister games such as xiangqi
  and shogi to modern rule tweaks such as Chess960, crazyhouse and antichess.
status: current
volatile: true
verified: 2026-11-11
broader: [kt:chess]
related: [kt:chess960, kt:chess-problems, kt:fide-laws-of-chess, kt:alphazero, kt:shatranj]
relations:
  - {predicate: hasPart, object: kt:xiangqi}
  - {predicate: hasPart, object: kt:shogi}
  - {predicate: exemplifiedBy, object: kt:chess960}
  - {predicate: influencedBy, object: kt:chaturanga}
  - {predicate: contrastsWith, object: kt:fide-laws-of-chess}
sources:
  - id: s1
    title: "FIDE Laws of Chess, Guidelines II. Chess960 Rules"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/guidelinesii/
    type: governing-body
    accessed: 2026-11-11
  - id: s2
    title: "Chinese chess"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/sports/Chinese-chess
    type: reference
    accessed: 2026-11-11
  - id: s3
    title: "Shogi"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/shogi
    type: reference
    accessed: 2026-11-11
  - id: s4
    title: "Assessing Game Balance with AlphaZero: Exploring Alternative Rule Sets in Chess (arXiv:2009.04374)"
    publisher: N. Tomašev, U. Paquet, D. Hassabis, V. Kramnik (arXiv)
    url: https://arxiv.org/abs/2009.04374v2
    type: academic
    accessed: 2026-11-11
  - id: s5
    title: "Chess variants"
    publisher: Lichess
    url: https://lichess.org/variant
    type: publication
    accessed: 2026-11-11
  - id: s6
    title: "The Encyclopedia of Chess Variants (Book Info)"
    publisher: The Chess Variant Pages
    url: https://chessvariants.org/books.dir/ecv.html
    type: community
    accessed: 2026-11-11
created: 2026-11-11
---

# Chess variants

A chess variant is any game that keeps the recognisable core of chess (two armies, a royal piece to be checkmated or captured) while changing something else: the board, the pieces, the starting array, how pieces move, or how the game is won. The family is large enough that David Pritchard's *Encyclopedia of Chess Variants* (1994), the first book to attempt a comprehensive survey, needed 384 pages, and roughly half of the games it describes can be played with an ordinary set.[^s6] After Pritchard's death in 2005 John Beasley completed an expanded edition, *The Classified Encyclopedia of Chess Variants*, which arranges the material by type.[^s6]

## Sister games and historical forerunners

The oldest "variants" are not modifications of modern chess at all but parallel descendants of the same ancestor. Chinese chess (xiangqi) is believed, like Western chess, to derive from the Indian game chaturanga; it is played on the 90 points of a 9 × 10 grid divided by a "river", and each general and its two advisers are confined to a nine-point palace.[^s2] Japanese shogi uses a 9 × 9 board and twenty pieces per side, and its defining feature is the drop: a captured piece changes sides and may later be placed back on the board as a move, subject to restrictions such as no pawn drop that gives checkmate.[^s3] Shogi also widens promotion, since every piece except the king and gold general may promote on entering, moving within or leaving the last three ranks.[^s3] Britannica groups Western chess, xiangqi and shogi as one family of two-player games aimed at mating the opposing king.[^s3]

## Main kinds of modern variant

A useful working classification follows what is changed:

- **Starting position.** Chess960 shuffles the back rank under fixed constraints, keeps every other law, and only adapts castling; FIDE publishes its rules as Guidelines II accompanying the Laws of Chess.[^s1]
- **Pieces and captures.** In crazyhouse, as in shogi, captured pieces may be dropped back into play in place of a normal move.[^s3][^s5]
- **Winning condition.** As of November 2026 the Lichess server lists variants that win by giving three checks, by bringing the king to the centre, or by racing the king to the far rank; in antichess (losing chess) the goal is to lose all one's pieces, and being stalemated also wins.[^s5]
- **Army or material.** Horde pits one side's mass of pawns against a normal army.[^s5]
- **Single rule changes.** Tomašev, Paquet, Hassabis and Kramnik used AlphaZero to study nine "atomic" changes, including no castling, pawns moving only one square, stalemate counting as a win, "torpedo" pawns that may advance two squares from any rank, and self-capture.[^s4]

## Why variants matter to chess players

Variants are a laboratory for the rules of chess itself. The AlphaZero study was motivated by the size of opening theory and the high draw rate in elite classical chess.[^s4] Its self-play games found torpedo, semi-torpedo, no-castling and stalemate-as-win to be the most decisive of the nine variants, and pawn-one-square and pawn-back the most drawish; piece values also shifted between variants.[^s4] Draw rates rose with longer thinking time in every variant, which the authors took as a hint that the standard starting position may be a theoretical draw.[^s4]

For a club player, variants also train specific skills. Drop games such as crazyhouse, where any captured piece can reappear next to the king, sharpen tactical alertness, while Chess960 removes memorised openings and leaves only general principles.[^s1][^s5] The trap is transfer: habits that are correct in a variant (sacrificing material freely in antichess, ignoring castling in no-castling chess) can be harmful in standard games, so it helps to keep the rule differences explicit.

## Variants and compositions

Problem composers have their own tradition of altered rules: fairy chess problems use new pieces, boards or conditions. Such works are judged as compositions rather than played as games, whereas Pritchard's encyclopedia concentrates on playable games of all periods, from ancient times to the present, including in-depth treatment of popular forms such as Kriegspiel, losing chess and progressive chess, and about 160 commercial variants.[^s6]

## Connections

Chess variants sit under the broad node **chess**. **Xiangqi** and **shogi** are parts of the wider family, descended like Western chess from **chaturanga**, as was **shatranj**.[^s2] **Chess960** is the best-known modern example and the only one FIDE regulates through guidelines attached to the **FIDE Laws of Chess**, which define the orthodox game that variants depart from.[^s1] **AlphaZero** has been used to compare variant rule sets.[^s4] **Chess problems** in fairy genres are the compositional counterpart of variant play.

## Sources

[^s1]: FIDE Rules Commission, "FIDE Laws of Chess, Guidelines II. Chess960 Rules". https://rcc.fide.com/guidelinesii/ (accessed 2026-11-11)
[^s2]: Encyclopaedia Britannica, "Chinese chess". https://www.britannica.com/sports/Chinese-chess (accessed 2026-11-11)
[^s3]: Encyclopaedia Britannica, "Shogi". https://www.britannica.com/topic/shogi (accessed 2026-11-11)
[^s4]: N. Tomašev, U. Paquet, D. Hassabis and V. Kramnik, "Assessing Game Balance with AlphaZero: Exploring Alternative Rule Sets in Chess", arXiv:2009.04374 (2020). https://arxiv.org/abs/2009.04374v2 (accessed 2026-11-11)
[^s5]: Lichess, "Chess variants" (variant list as of November 2026). https://lichess.org/variant (accessed 2026-11-11)
[^s6]: The Chess Variant Pages, "The Encyclopedia of Chess Variants (Book Info)", on David Pritchard's encyclopedia (1994) and its classified edition. https://chessvariants.org/books.dir/ecv.html (accessed 2026-11-11)
