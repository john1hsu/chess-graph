---
id: kt:illegal-move
type: Rule
title: Illegal move
aliases: [Illegal moves, Illegal move rule, Illegal move penalty, Article 7.5]
domain: rules-and-notation
summary: >-
  A move that breaks the piece-movement rules of the Laws of Chess; under FIDE rules it is
  complete once the clock is pressed, the prior position is restored, the opponent gains two
  minutes for a first offence and a second offence loses the game.
fen: "4k3/8/8/8/2b5/8/8/4K2R w K - 0 1"
status: current
volatile: true
verified: 2026-11-17
broader: [kt:fide-laws-of-chess]
related: [kt:touch-move, kt:arbiter, kt:rapid-chess, kt:blitz-chess, kt:us-chess, kt:pawn-promotion]
relations:
  - {predicate: partOf, object: kt:fide-laws-of-chess}
  - {predicate: developedBy, object: kt:fide}
  - {predicate: contrastsWith, object: kt:touch-move}
sources:
  - id: s1
    title: "Article 7: Irregularities"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/article7/
    type: governing-body
    accessed: 2026-11-17
  - id: s2
    title: "FIDE Laws of Chess (full text, applied from 1 January 2023)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/
    type: governing-body
    accessed: 2026-11-17
  - id: s3
    title: "Appendix A. Rapid Chess"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/?p=876
    type: governing-body
    accessed: 2026-11-17
  - id: s4
    title: "Arbiters' Manual 2024 (Article 7.5 with commentary)"
    publisher: FIDE Arbiters' Commission
    url: https://arbiters.fide.com/wp-content/uploads/Publications/Manual/Arbiters_Manual_2024.pdf
    type: governing-body
    accessed: 2026-11-17
  - id: s5
    title: "Summary of differences between the FIDE Laws of Chess and the US Chess Official Rules of Chess, 7th edition (updated 1 January 2022)"
    publisher: US Chess
    url: https://new.uschess.org/sites/default/files/media/documents/uschess-fide-rules-comparison.pdf
    type: governing-body
    accessed: 2026-11-17
  - id: s6
    title: "Illegal moves and irregularities (by IA Tamas Gyomber, from ECU Magazine, January 2024)"
    publisher: ChessBase News
    url: https://en.chessbase.com/post/illegal-moves-and-irregularities
    type: publication
    accessed: 2026-11-17
created: 2026-11-17
---

# Illegal move

The FIDE Laws of Chess define a legal move as one that meets all the relevant requirements of Articles 3.1 to 3.9, which describe how each piece moves, including castling, en passant and promotion; any move that fails one of them is illegal.[^s2] Moving into check, castling through an attacked square or moving a pinned piece so that one's own king is exposed are all typical examples. As of November 2026 the Rules Commission publishes the text applied from 1 January 2023, in which the handling of illegal moves sits in Article 7.5, among the "irregularities".[^s1][^s2]

## When a move becomes illegal

The key idea is completion. Under Article 7.5.1 an illegal move is only completed when the player presses the clock; until then it can be corrected, subject to the touch-move rules of Article 4.[^s1] The Arbiters' Manual stresses the same point: before the clock is pressed, a player may replace an illegal move without penalty.[^s4] Once it is completed, the position immediately before the irregularity is reinstated (or the last identifiable position if that cannot be determined), and the touch-move obligations apply to the replacement move.[^s1]

Three further actions are treated and penalised as illegal moves even though no piece moves wrongly: pressing the clock after moving a pawn to the last rank without promoting it (the pawn becomes a queen), pressing the clock without making a move at all, and making a single move with two hands, for example castling or capturing with both hands.[^s1] Capturing the opponent's king is also illegal and is penalised in the same way.[^s4]

## Penalties

For a first completed illegal move the arbiter gives the opponent two extra minutes; for a second by the same player, the arbiter declares the game lost.[^s1] There is one exception: if the opponent could not checkmate the offender's king by any legal series of moves, the game is drawn instead.[^s1] The manual adds that the arbiter must intervene whenever he or she sees an illegal move, without waiting for a claim, and that any increment the offender gained by pressing the clock should be taken off.[^s4] The Manual notes that the illegal-move rules changed significantly in 2017 and had to be changed again from 1 January 2018.[^s4]

In rapid and blitz the time penalty is one minute instead of two.[^s2] Where the rapid default rules (Appendix A.5) apply, the arbiter acts only if he or she sees the illegal move before the opponent moves; otherwise the opponent must claim before making their own next move. If neither happens, the illegal move stands and play continues, and after the opponent's move it can only be corrected if the players agree without the arbiter.[^s3] Blitz follows the same rapid provisions.[^s2]

## US Chess differs

US Chess treats illegal moves more leniently. Each illegal move gives the opponent two minutes, with no loss for repeated offences; a director corrects observed illegal moves unless either player has under five minutes, and under a widely used variation only on a claim. An illegal move not corrected within ten moves (two in time pressure) stands, whereas FIDE sets no such limit.[^s5]

## Example and pitfalls

In the diagram position, White has kingside castling rights, but the black bishop on c4 attacks f1, the square the king must cross, so 1.O-O would be illegal; if White pressed the clock after castling, the position would be restored, Black would receive two extra minutes, and the touch-move rules would govern White's replacement move.[^s1][^s2]

Practical points: keep moving and pressing with the same hand, since a two-handed move counts as an illegal move; do not assume a second illegal move will be forgiven in a FIDE event; and in rapid or blitz under the default rules, claim at once, because an illegal move you overlook stands after your reply.[^s1][^s3][^s6] An arbiter writing for the European Chess Union also separates true illegal moves from other irregularities: knocking pieces over is handled under Article 7.4, and touching one piece but moving another is a touch-move infringement penalised under Article 12.9.[^s6]

## Connections

The illegal-move rule is **part of** the **FIDE Laws of Chess**, maintained by **FIDE**, and is enforced by the **arbiter** under Article 7.5.[^s1][^s4] It **contrasts with** **touch-move**: touch-move governs a move still in progress, while the illegal-move rule takes over once the clock is pressed.[^s1][^s4] Its rapid and blitz versions appear in the appendices on **rapid chess** and **blitz chess**, an unpromoted pawn ties it to **pawn promotion**, and **US Chess** applies its own, more lenient version.[^s1][^s3][^s5]

## Sources
[^s1]: FIDE Rules Commission, "Article 7: Irregularities". https://rcc.fide.com/article7/ (accessed 2026-11-17)
[^s2]: FIDE Rules Commission, "FIDE Laws of Chess" (full text, applied from 1 January 2023). https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/ (accessed 2026-11-17)
[^s3]: FIDE Rules Commission, "Appendix A. Rapid Chess". https://rcc.fide.com/?p=876 (accessed 2026-11-17)
[^s4]: FIDE Arbiters' Commission, Arbiters' Manual 2024. https://arbiters.fide.com/wp-content/uploads/Publications/Manual/Arbiters_Manual_2024.pdf (accessed 2026-11-17)
[^s5]: US Chess, "Summary of differences between the FIDE Laws of Chess and the US Chess Official Rules of Chess" (updated 1 January 2022). https://new.uschess.org/sites/default/files/media/documents/uschess-fide-rules-comparison.pdf (accessed 2026-11-17)
[^s6]: Tamas Gyomber, "Illegal moves and irregularities", ChessBase News (from ECU Magazine, January 2024). https://en.chessbase.com/post/illegal-moves-and-irregularities (accessed 2026-11-17)
