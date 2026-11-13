---
id: kt:draw
type: Rule
title: Draw
aliases: [Drawn game, Draw (chess), Remis, Draw by agreement, Agreed draw, Draw offer]
domain: rules-and-notation
summary: >-
  A game of chess that ends with neither player winning, scored as half a point each; under
  the FIDE Laws it arises from stalemate, a dead position, mutual agreement, a correct
  repetition or fifty-move claim, the automatic fivefold/75-move rules, or a flag fall when
  the opponent could not checkmate.
fen: "8/8/8/4k3/3q4/2r5/8/7K b - - 0 70"
status: current
volatile: true
verified: 2026-11-13
broader: [kt:fide-laws-of-chess]
related: [kt:arbiter, kt:chess-tournament, kt:fortress, kt:perpetual-check, kt:emanuel-lasker]
relations:
  - {predicate: partOf, object: kt:fide-laws-of-chess}
  - {predicate: hasPart, object: kt:stalemate}
  - {predicate: hasPart, object: kt:dead-position}
  - {predicate: hasPart, object: kt:threefold-repetition}
  - {predicate: hasPart, object: kt:fifty-move-rule}
  - {predicate: contrastsWith, object: kt:checkmate}
sources:
  - id: s1
    title: "Article 9: The Drawn Game"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/article9/
    type: governing-body
    accessed: 2026-11-13
  - id: s2
    title: "Article 5: The Completion of the Game"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/article5/
    type: governing-body
    accessed: 2026-11-13
  - id: s3
    title: "Questions & Answers, November 2021"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/2021/11/08/questions-answers-november-2021/
    type: governing-body
    accessed: 2026-11-13
  - id: s4
    title: "Chess Draws"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://www.chesshistory.com/winter/extra/draws.html
    type: reference
    accessed: 2026-11-13
  - id: s5
    title: "Unfought draws – reader feedback"
    publisher: ChessBase News, 20 March 2008
    url: https://en.chessbase.com/post/unfought-draws-reader-feedback
    type: publication
    accessed: 2026-11-13
created: 2026-11-13
---

# Draw

A draw is the third possible result of a chess game, alongside a win for White and a win for Black. Under the FIDE Laws of Chess, as published by the FIDE Rules Commission (checked November 2026), a game can be drawn in two quite different ways. Some draws end the game at once, with no claim needed, because the position itself leaves no winner: stalemate, a dead position, and agreement between the players.[^s2] Others depend on the history of the game and must normally be claimed by a player: threefold repetition and the fifty-move rule, with fivefold repetition and the 75-move rule as automatic backstops.[^s1] A third family belongs to the clock: when one player's time runs out, the game is still drawn if the opponent could not have checkmated by any series of legal moves.[^s3]

## The ways a game is drawn

**Immediate draws (Article 5.2).** The game ends in a draw when the player to move has no legal move and is not in check (stalemate), or when neither side can checkmate with any series of legal moves (a dead position); in both cases the move that created the position must itself have been legal.[^s2] The players may also simply agree a draw, which ends the game at once, provided each has made at least one move.[^s2]

**Claimed draws (Articles 9.2 and 9.3).** A player on the move may claim when the same position has appeared three times, or when fifty moves by each side have passed without a pawn move or capture.[^s1] For repetition, the positions count as the same only if the same side is to move, the same pieces stand on the same squares and the same moves are available, so a lost castling right or an en passant chance makes positions different.[^s1]

**Automatic backstops (Article 9.6).** Without any claim, the game is drawn when a position occurs for at least the fifth time, or after 75 moves by each player with no pawn move or capture; a checkmate on that final move still counts.[^s1]

**Time and material (Article 6.9).** A flag fall normally loses, but FIDE's Rules Commission confirms that the game is instead drawn when the opponent could not checkmate by any legal sequence.[^s3] The test is whether mate is possible at all, even with the loser's cooperation, not whether it is likely.[^s3]

## Draw offers and agreed draws

Article 9.1 regulates how an agreed draw happens. A player should offer a draw only after making a move on the board and before pressing the clock; an offer made at another moment still stands but may be penalised as a distraction.[^s1] An offer cannot carry conditions or be withdrawn, and it remains open until the opponent accepts it, rejects it in words, touches a piece with the intention of moving it, or the game ends some other way.[^s1] Both players mark the offer on the scoresheet with "(=)", and a claim of repetition or of fifty moves also counts as a draw offer.[^s1] Event regulations may forbid draw offers before a stated number of moves, or entirely, unless the arbiter agrees.[^s1]

That last clause exists because short, agreed "grandmaster draws" have long annoyed organisers and spectators. A 2008 ChessBase reader survey gathered the main remedies proposed: the Sofia rule, which bars agreed draws so that only the arbiter can let a game stop; three points for a win and one for a draw; and draw offers that remain open for the rest of the game.[^s5]

## History

Early tournaments did not always accept draws as final. Edward Winter's collection notes that at Paris 1900 a drawn game was replayed once with colours reversed, and that at Monte Carlo 1901, following a suggestion by Emanuel Lasker, a first draw was worth a quarter-point to each player before a replay.[^s4] The earliest half-point scoring Winter has found is the Dundee tournament, whose organisers decided in September 1867 that a draw would count as half a game each.[^s4] Proposals to devalue draws are just as old: in 1892 James Mason suggested scoring a win as 1, a draw as 0 and a loss as minus a half, and C.J.S. Purdy later showed this to be equivalent to the three-one-zero system proposed in 1955.[^s4] Lasker defended draws as the natural outcome of good play between masters, though he also warned that chess might one day "die the death of the draw".[^s4]

## Example and practical points

In the key position above, Black has king, queen and rook against a bare white king, and it is Black's turn. If Black's flag falls here, Black does not lose: White has only a king and cannot mate by any sequence of legal moves, so the game is drawn.[^s3] The same test cuts the other way: if any legal sequence, however cooperative, could end in mate by the side with time left, the flag fall still loses.[^s3]

- **Offer correctly.** Move, offer, then press the clock; an offer on the opponent's time is not void but may be penalised.[^s1]
- **Know which draws need a claim.** Repetition and fifty-move draws are claimed (or arise automatically only at five repetitions or 75 moves); stalemate and dead positions end the game without anyone saying a word.[^s1][^s2]
- **Check the event rules.** A no-draw-offer regulation overrides the usual freedom to agree.[^s1][^s5]

## Connections

The draw is **part of** the **FIDE Laws of Chess**, which describe its routes in Articles 5, 6 and 9.[^s1][^s2] It **has parts** in **stalemate**, the **dead position**, **threefold repetition** and the **fifty-move rule**, each with its own node, and it **contrasts with** **checkmate**, the decisive way a game ends.[^s2] Claims and no-draw regulations are handled by the **arbiter** and by **chess tournament** rules; over the board, a **fortress** or **perpetual check** is how a worse position is steered towards a draw. **Emanuel Lasker** appears in its history as both defender of the draw and author of a scoring reform.[^s4]

## Sources

[^s1]: FIDE Rules Commission, "Article 9: The Drawn Game". https://rcc.fide.com/article9/ (accessed 2026-11-13)
[^s2]: FIDE Rules Commission, "Article 5: The Completion of the Game". https://rcc.fide.com/article5/ (accessed 2026-11-13)
[^s3]: FIDE Rules Commission, "Questions & Answers, November 2021". https://rcc.fide.com/2021/11/08/questions-answers-november-2021/ (accessed 2026-11-13)
[^s4]: Edward Winter, Chess Notes, "Chess Draws". https://www.chesshistory.com/winter/extra/draws.html (accessed 2026-11-13)
[^s5]: ChessBase News, "Unfought draws – reader feedback" (20 March 2008). https://en.chessbase.com/post/unfought-draws-reader-feedback (accessed 2026-11-13)
