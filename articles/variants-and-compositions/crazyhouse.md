---
id: kt:crazyhouse
type: Variant
title: Crazyhouse
aliases: [Drop chess, Crazy house, Crazyhouse chess]
domain: variants-and-compositions
summary: >-
  A two-player chess variant in which every captured piece changes colour and goes into the
  capturer's pocket, from which it may later be dropped onto any empty square instead of making
  a normal move.
fen: "6k1/5ppp/8/8/8/8/5PPP/6K1 w - - 0 1"
status: current
volatile: true
verified: 2026-11-14
broader: [kt:chess-variants]
related: [kt:bughouse, kt:shogi, kt:checkmate, kt:pawn-promotion, kt:monte-carlo-tree-search, kt:stockfish]
relations:
  - {predicate: usesTechnique, object: kt:sacrifice}
  - {predicate: contrastsWith, object: kt:chess960}
sources:
  - id: s1
    title: "Learning to play the Chess Variant Crazyhouse above World Champion Level with Deep Neural Networks and Human Data"
    publisher: "Czech, Willig, Beyer, Kersting & Fürnkranz, arXiv:1908.06660 (2019; later in Frontiers in Artificial Intelligence)"
    url: https://arxiv.org/pdf/1908.06660
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s2
    title: "Exploring the Performance of Deep Residual Networks in Crazyhouse Chess"
    publisher: "Gordon Chi, Stanford University (arXiv:1908.09296)"
    url: https://arxiv.org/pdf/1908.09296
    type: academic
    accessed: 2026-11-14
  - id: s3
    title: "Crazyhouse"
    publisher: Lichess (variant rules page)
    url: https://lichess.org/variant/crazyhouse
    type: publication
    accessed: 2026-11-14
  - id: s4
    title: "What is Crazyhouse?"
    publisher: Chess.com Help Center
    url: https://support.chess.com/en/articles/8614995-what-is-crazyhouse
    type: publication
    accessed: 2026-11-14
created: 2026-11-14
---

# Crazyhouse

Crazyhouse, also called drop chess, keeps every rule of ordinary chess and adds one more: the drop.[^s1][^s3] When a player captures a piece, it switches colour and goes into that player's pocket (Chess.com calls it the bank). On any later turn, instead of moving a piece on the board, the player may place a piece from the pocket on an empty square.[^s3][^s4] Researchers describe it as the single-player version of bughouse and note that its drop element resembles the one in shogi.[^s1]

## Rules in detail

Only three restrictions shape drops. A pawn may not be dropped on the first or eighth rank, a drop may never capture, and a drop is a full move.[^s2][^s3][^s4] Drops may give check and even immediate checkmate, and a player in check may answer by dropping a piece in between.[^s3][^s4] Promotion is temporary in material terms: a promoted piece that is later captured goes into the pocket as a pawn, not as the queen or knight it had become.[^s1][^s3][^s4] Otherwise the classical rules apply, including castling, en passant and threefold repetition, and games end by checkmate, stalemate or time-out as usual.[^s1][^s4] On Lichess a drop is written with the piece letter, an `@` sign and the target square, for example `N@f7`, with the letter left out for pawns.[^s3]

## How the game feels

Because nothing ever leaves the game, crazyhouse is far more tactical than standard chess. Long forced mating sequences are common, and the opening advantage of the first player is larger than in chess.[^s1] Draws are very rare: in one data set of strong Lichess games they made up only 0.40% of results, and nearly every game ended in checkmate.[^s1] The number of legal moves is much larger as well, up to roughly three times that of standard chess by one estimate, and with so few draws one mistake often decides the game.[^s1][^s2] Most play happens online at short time controls; in the Lichess data used by Czech and colleagues, nearly half the games were one-minute games.[^s1]

## Typical ideas and pitfalls

The guiding principle is that material in the pocket is as real as material on the board. Strong human players often sacrifice pieces for activity and an attack on the king, knowing that every captured piece can come back as a drop near the enemy king.[^s1] Since a drop can land next to the king in one move, king safety matters more than in standard chess, and players under attack or short of time make many more errors.[^s1]

Two pitfalls follow directly from the rules. First, a check along a line is not automatically mate: if the defender holds any piece in hand, it can usually be dropped between king and checker.[^s3][^s4] Second, chasing promotion is less rewarding, because a captured promoted piece only returns to the opponent's pocket as a pawn.[^s3]

## Example

In the key position above (white king g1, pawns f2, g2, h2; black king g8, pawns f7, g7, h7), suppose White holds a rook in the pocket. `R@e8+` would be a back-rank mate in ordinary chess, since the king's pawns block its escape. In crazyhouse it is mate only if Black has nothing in hand; with even a pawn or knight in the pocket, Black can drop it on f8 to block, because blocking drops are always allowed.[^s3][^s4] This is why experienced players count the opponent's pocket before every attacking check, and prefer contact checks or knight checks that no drop can interrupt.

## Computers and competition

Crazyhouse is a long-standing test bed for game-playing programs. Early engines included Sjeng (1999) and Sunsetter (2001), and Stockfish was later adapted to the variant with its own tuned piece and pocket values.[^s1] In 2018, a deep residual network trained on Lichess games reached a peak Lichess rating of 2278 over 294 rated games.[^s2] The CrazyAra engine, trained with supervised learning on human games and searching with Monte-Carlo tree search, won four of five informal games against Justin Tan (LM JannLee), described as the 2017 crazyhouse world champion, on 21 December 2018 at 5 minutes plus 15 seconds. A later version, CrazyAraFish, scored three wins and one draw in ten games against Stockfish 10 at 30 minutes plus 30 seconds.[^s1] As of November 2026 the variant is offered on major servers including Lichess and Chess.com.[^s3][^s4]

## Connections

Crazyhouse is one of the chess variants, and bughouse is its four-player team form, in which a captured piece goes to the partner rather than to one's own pocket.[^s1] Its drop rule links it to shogi, while its handling of checkmate and pawn promotion modifies the standard rules.[^s1][^s3] Its heavy reliance on sacrifices for the initiative comes from the recycling of material, and its large branching factor made it a natural target for Monte-Carlo tree search and for variant versions of Stockfish.[^s1][^s2] It contrasts with Chess960 in where it departs from the standard game: crazyhouse keeps the usual starting position and piece moves and changes only what happens to captured material.[^s1][^s3]

## Sources
[^s1]: J. Czech, M. Willig, A. Beyer, K. Kersting, J. Fürnkranz, "Learning to play the Chess Variant Crazyhouse above World Champion Level with Deep Neural Networks and Human Data", arXiv:1908.06660 (2019). https://arxiv.org/pdf/1908.06660 (accessed 2026-11-14)
[^s2]: G. Chi, "Exploring the Performance of Deep Residual Networks in Crazyhouse Chess", Stanford University, arXiv:1908.09296. https://arxiv.org/pdf/1908.09296 (accessed 2026-11-14)
[^s3]: Lichess, "Crazyhouse" variant page. https://lichess.org/variant/crazyhouse (accessed 2026-11-14)
[^s4]: Chess.com Help Center, "What is Crazyhouse?". https://support.chess.com/en/articles/8614995-what-is-crazyhouse (accessed 2026-11-14)
