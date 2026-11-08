---
id: kt:pawn-promotion
type: Rule
title: Pawn promotion
aliases: [Promotion, Queening, Promotion (chess)]
domain: rules-and-notation
summary: >-
  The rule that a pawn reaching the last rank must, as part of the same move, be exchanged for a
  new queen, rook, bishop or knight of its own colour, regardless of which pieces have already been
  captured.
moves: "1.e4 e5 2.f4 exf4 3.b3 Qh4+ 4.g3 fxg3 5.h3 g2+ 6.Ke2 Qxe4+ 7.Kf2 gxh1=N#"
fen: "rnb1kbnr/pppp1ppp/8/8/4q3/1P5P/P1PP1Kp1/RNBQ1BNR b kq - 1 7"
status: current
volatile: true
verified: 2026-11-08
broader: [kt:fide-laws-of-chess, kt:pawn]
related: [kt:en-passant, kt:lucena-position, kt:philidor-position, kt:saavedra-position, kt:passed-pawn]
relations:
  - {predicate: leadsTo, object: kt:underpromotion}
sources:
  - id: s1
    title: "FIDE Laws of Chess (applied from 1 January 2023), full text: Articles 3.7, 4.4, 4.6, 7.5 and Appendix A"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/
    type: governing-body
    accessed: 2026-11-08
  - id: s2
    title: "The Evolution of Modern Chess Rules: Pawn Promotion"
    publisher: John McCrary, US Chess
    url: https://new.uschess.org/news/evolution-modern-chess-rules-pawn-promotion
    type: publication
    accessed: 2026-11-08
  - id: s3
    title: "Underpromotion in Chess"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/underpromotion.html
    type: reference
    accessed: 2026-11-08
  - id: s4
    title: "pawn promotion"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/pawn-promotion
    type: reference
    accessed: 2026-11-08
created: 2026-11-08
---

# Pawn promotion

Pawn promotion is the rule that turns a pawn reaching the far rank into a new piece. Britannica describes it as the exchange of the pawn, on arriving at the eighth rank, for a queen, rook, bishop or knight; promoting to a queen is commonly called queening, and choosing any of the other three is called underpromotion.[^s4] It is the reason passed pawns matter so much: almost every endgame plan either aims at a promotion or tries to stop one.

## The rule as of November 2026

The FIDE Laws of Chess applied from 1 January 2023, still the text in force as of November 2026, deal with promotion inside the article on pawn moves (Article 3.7.3). When a pawn reaches the rank furthest from its starting position, the player must exchange it, as part of the same move, for a new queen, rook, bishop or knight of the same colour on the square of arrival. The choice is not restricted to pieces that have already been captured, so a player may have two or more queens.[^s1] Several procedural articles support this. Under Article 4.4.4, the choice of piece is final once the new piece has touched the promotion square, and Article 4.6.3 adds that if an enemy piece stands on the promotion square it must be captured. A player who reaches the last rank and presses the clock without replacing the pawn has made an illegal move, and the pawn is replaced by a queen of the same colour (Article 7.5.2); using two hands to promote also counts as an illegal move (Article 7.5.4). In rapid play, Appendix A has its own procedure for a pawn left standing on the furthest rank.[^s1]

Because the new piece only appears at the end of the move, it cannot move again before the opponent replies.[^s2]

## How the rule evolved

Promotion is old, but its weight on the game changed. In medieval chess the pawn could become only a queen, then a weak piece moving one square diagonally; Britannica notes that before the rule reforms of around 1475 promotion was a relatively minor factor, and that the newly powerful queen made the prospect of promotion a dynamic element of play.[^s4][^s2] Older regional customs varied: John McCrary, a former US Chess president, records an Indian practice where a pawn became the piece that originally stood on its file.[^s2]

The main modern dispute was the "lost-piece" rule, under which a pawn could become only a piece already captured; if none had been lost, it waited on the last rank until a capture freed one. Ercole del Rio favoured this rule, while George Walker in 1841 and especially Howard Staunton argued for the freedom to promote to any piece, including a second queen.[^s2] The British Chess Association's 1862 code even allowed a "dummy" pawn to stay on the last rank. McCrary dates the modern rule's general acceptance to the end of the nineteenth century, with the lost-piece rule lingering in parts of Italy and Germany until then.[^s2]

## Underpromotion and practical points

- **Queen by default, but not always.** A queen is almost always best, yet a knight can win by giving check or a fork, and a rook or bishop can avoid stalemating the opponent. The best-known case is the Saavedra study, where the winning move promotes to a rook; Winter notes that the version first published by Barbier in 1895 had a queen promotion that only drew.[^s3]
- **Mate by a new knight.** Winter's collection includes several short games ending in a knight promotion with mate, such as N.N. v A. Goetz, Strasbourg c.1880 (moves above), where 7...gxh1=N# exploits the white king on f2.[^s3] In the key position before Black's seventh move, a queen on h1 would give no check, whereas the knight checks and the king has no escape.
- **Do it properly over the board.** Have the new piece ready, place it with the same hand that moved the pawn, and remember that touching the square with your chosen piece fixes the choice.[^s1]
- **No upside-down rooks in the Laws.** The inverted rook as a stand-in for a second queen goes back at least to an 1897 suggestion recorded by McCrary, but under current FIDE Laws the pawn must be replaced by an actual queen, rook, bishop or knight.[^s2][^s1]

## Connections

Promotion is part of the **FIDE Laws of Chess** and one of the special moves of the **pawn**, sharing Article 3.7 with **en passant**.[^s1] It is the goal behind every **passed pawn** and the decisive threat in rook endings such as the **Lucena position** and the **Philidor position**, and its most famous **underpromotion** occurs in the **Saavedra position**.[^s3][^s4]

## Sources

[^s1]: FIDE Rules Commission, "FIDE Laws of Chess" (approved 7 August 2022, applied from 1 January 2023), Articles 3.7.3, 4.4.4, 4.6.3, 7.5.2, 7.5.4 and Appendix A. https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/ (accessed 2026-11-08)
[^s2]: John McCrary, US Chess, "The Evolution of Modern Chess Rules: Pawn Promotion" (2021). https://new.uschess.org/news/evolution-modern-chess-rules-pawn-promotion (accessed 2026-11-08)
[^s3]: Edward Winter, Chess Notes, "Underpromotion in Chess". https://chesshistory.com/winter/extra/underpromotion.html (accessed 2026-11-08)
[^s4]: Encyclopaedia Britannica, "pawn promotion". https://www.britannica.com/topic/pawn-promotion (accessed 2026-11-08)
