---
id: kt:threefold-repetition
type: Rule
title: Threefold repetition
aliases: [Draw by repetition, Repetition of position, Triple occurrence of position, Three-fold repetition, Fivefold repetition, Article 9.2]
domain: rules-and-notation
summary: >-
  The FIDE rule that the player on the move may claim a draw when the same position, with the same
  side to move and the same possible moves, has occurred or is about to occur for at least the third
  time; a fifth occurrence ends the game automatically.
moves: "1.e4 Nf6 2.e5 d5 3.Bc4 Ng8 4.Bf1 Nf6 5.Bc4 Ng8 6.Bf1 Nf6"
status: current
volatile: true
verified: 2026-11-13
broader: [kt:fide-laws-of-chess, kt:draw]
related: [kt:fifty-move-rule, kt:en-passant, kt:castling, kt:touch-move, kt:arbiter, kt:us-chess, kt:perpetual-check]
relations:
  - {predicate: partOf, object: kt:fide-laws-of-chess}
  - {predicate: developedBy, object: kt:fide}
  - {predicate: exemplifiedBy, object: kt:spassky-versus-fischer-reykjavik-1972-game-17}
  - {predicate: contrastsWith, object: kt:dead-position}
sources:
  - id: s1
    title: "Article 9: The Drawn Game"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/article9/
    type: governing-body
    accessed: 2026-11-13
  - id: s2
    title: "Summary of differences between the FIDE Laws of Chess and the US Chess Official Rules of Chess, 7th edition (updated 1 January 2022)"
    publisher: US Chess
    url: https://new.uschess.org/sites/default/files/media/documents/uschess-fide-rules-comparison.pdf
    type: governing-body
    accessed: 2026-11-13
  - id: s3
    title: "Repetition of Position or Moves in Chess"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://www.chesshistory.com/winter/extra/repetition.html
    type: reference
    accessed: 2026-11-13
  - id: s4
    title: "Arbiter Case Studies"
    publisher: All India Chess Federation
    url: https://aicf.in/wp-content/uploads/2013/07/Arbiter-Case-studies.pdf
    type: publication
    accessed: 2026-11-13
  - id: s5
    title: "Bobby Fischer in Iceland — 45 years ago (11)"
    publisher: Frederic Friedel, ChessBase News, 25 August 2017
    url: https://en.chessbase.com/newsroom/post/bobby-fischer-in-iceland-45-years-ago-13
    type: publication
    accessed: 2026-11-13
created: 2026-11-13
---

# Threefold repetition

Threefold repetition is the rule that stops a game from cycling forever. Under Article 9.2 of the FIDE Laws of Chess, as published by the FIDE Rules Commission (checked November 2026), the player on the move may claim a draw when the same position has appeared at least three times; the occurrences need not come from the same sequence of moves, and they need not be consecutive.[^s1] The claim can be made in two ways: when the position has just arisen and the claimant is to move, or when the claimant's next move would create it, in which case that move must first be written on the scoresheet, cannot be changed, and is declared to the arbiter without being played.[^s1]

## What counts as "the same position"

The Laws define sameness strictly. Two positions are identical only if the same player has the move, pieces of the same kind and colour stand on the same squares, and every possible move is the same for both players.[^s1] It is the pieces' kind that matters, not their identity: an Indian federation's arbiter case book records a claim upheld where the two white rooks had swapped squares between occurrences.[^s4] Two details trip players up:

- **En passant.** A position in which a pawn could have been captured en passant is not the same as the otherwise identical position a move later, when that capture is no longer available.[^s1]
- **Castling rights.** If a king or rook that still had castling rights moves, the later positions differ from the earlier ones even if the pieces return; rights are lost only by the king or rook actually moving.[^s1] The same case book describes a claim rejected because the arbiter had dated the loss of castling rights to the wrong move.[^s4]

## How to claim, and what goes wrong

A claim is made by pausing the clock, and it cannot be withdrawn. If it is correct, the game ends in a draw at once; if not, the opponent receives two extra minutes and play continues, with any written move then played.[^s1] FIDE also treats a repetition claim as a draw offer.[^s1] A player who touches a piece with intent to move it loses the right to claim on that move, which is why the order "write, declare, pause the clock" matters.[^s1][^s4] Arbiters are advised to check claims by replaying the game rather than trusting two scoresheets, and the case book shows that even a mistaken rejection can be corrected later by the arbiter.[^s4]

US Chess, in its comparison document updated January 2022, keeps the claimant "on the move" until the clock is pressed, so a player there may make the repeating move on the board and still claim; under FIDE that move must be written but not played.[^s2]

## Fivefold repetition

Players may decline to claim, so FIDE adds an automatic backstop: Article 9.6.1 ends the game as a draw, with no claim required, once the same position has appeared at least five times.[^s1] US Chess has only a weaker version, under which the director may, but need not, declare the draw after five consecutive pairs of repeated moves; its rules still use that block-of-moves pattern, which FIDE has dropped.[^s2]

## From moves to positions: a short history

Edward Winter's research shows that early codes spoke of repeating *moves*, not positions. A German code of 1858 linked the draw to repeating the same series of moves, and the rules for the 1886 Steinitz–Zukertort match required a series of moves to be repeated six times.[^s3] The decisive change came at London 1883: the committee found "a series of moves repeated three times" ambiguous, and the wording published in the tournament book referred instead to the same position occurring three times, with no requirement that the occurrences be consecutive.[^s3] German codes continued to require three successive repetitions of moves into the 1900s, and Winter could not establish exactly when today's form was fixed everywhere.[^s3]

## Example

The opening sequence above illustrates the en passant detail. After 2...d5 White could capture en passant on d6, but after 4...Nf6 the pieces stand exactly as before with White to move and no en passant capture available, so this is a *new* position: 6...Nf6 produces only its second occurrence, not the third, and a claim at that moment would fail.[^s1] By contrast, 1.Nf3 Nf6 2.Ng1 Ng8 3.Nf3 Nf6 4.Ng1 Ng8 is claimable, because the initial position counts as the first occurrence.[^s1]

At the top level, Game 17 of the 1972 world championship match in Reykjavik was drawn when Bobby Fischer, playing Black, claimed a repetition that would arise with 45...Re1, and chief arbiter Lothar Schmid upheld the claim, according to Robert Byrne's contemporary report as quoted by ChessBase.[^s5]

## Connections

Threefold repetition is **part of** the **FIDE Laws of Chess** (Article 9), **developed by** **FIDE**, and is one of the main routes to a **draw**.[^s1] It shares its claim procedure and an automatic backstop with the **fifty-move rule**, and it **contrasts with** the **dead position**, which ends a game immediately without any claim.[^s1] Its definition of identical positions depends on the rules for **en passant** and **castling**, the **touch-move** rule can forfeit a claim, and the **arbiter** decides disputes.[^s1][^s4] It is the formal end of a **perpetual check** that neither side avoids, **US Chess** applies a variant procedure, and the rule is **exemplified by** Spassky–Fischer, Reykjavik 1972, game 17.[^s2][^s5]

## Sources

[^s1]: FIDE Rules Commission, "Article 9: The Drawn Game". https://rcc.fide.com/article9/ (accessed 2026-11-13)
[^s2]: US Chess, "Summary of differences between the FIDE Laws of Chess and the US Chess Official Rules of Chess, 7th edition" (updated 1 January 2022). https://new.uschess.org/sites/default/files/media/documents/uschess-fide-rules-comparison.pdf (accessed 2026-11-13)
[^s3]: Edward Winter, Chess Notes, "Repetition of Position or Moves in Chess". https://www.chesshistory.com/winter/extra/repetition.html (accessed 2026-11-13)
[^s4]: All India Chess Federation, "Arbiter Case Studies". https://aicf.in/wp-content/uploads/2013/07/Arbiter-Case-studies.pdf (accessed 2026-11-13)
[^s5]: Frederic Friedel, ChessBase News, "Bobby Fischer in Iceland — 45 years ago (11)" (25 August 2017). https://en.chessbase.com/newsroom/post/bobby-fischer-in-iceland-45-years-ago-13 (accessed 2026-11-13)
