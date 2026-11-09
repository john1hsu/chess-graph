---
id: kt:material-advantage
type: StrategicConcept
title: Material advantage
aliases: [Material, Material balance, Material superiority, Being ahead in material, Relative value of the pieces, Piece values, Point count]
domain: middlegame-strategy
summary: >-
  Having more or more valuable pieces and pawns than the opponent, measured with conventional
  piece values (pawn 1, knight and bishop about 3, rook about 5, queen about 9) that guide
  decisions about exchanges, sacrifices and simplification.
fen: "6k1/ppp2ppp/4b3/8/8/8/P4PPP/3R2K1 w - - 0 1"
status: current
volatile: false
verified: 2026-11-09
broader: [kt:chess-strategy]
related: [kt:evaluation-function, kt:combination, kt:sacrifice, kt:bishop-pair, kt:the-exchange, kt:simplification]
relations:
  - {predicate: dependsOn, object: kt:piece-values}
  - {predicate: leadsTo, object: kt:simplification}
  - {predicate: contrastsWith, object: kt:sacrifice}
sources:
  - id: s1
    title: "Assessing Game Balance with AlphaZero: Exploring Alternative Rule Sets in Chess"
    publisher: Nenad Tomašev, Ulrich Paquet, Demis Hassabis and Vladimir Kramnik, arXiv:2009.04374 (2020)
    url: https://arxiv.org/pdf/2009.04374
    type: academic
    accessed: 2026-11-09
  - id: s2
    title: "The Value of the Chess Pieces"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/value.html
    type: reference
    accessed: 2026-11-09
  - id: s3
    title: "Chess Fundamentals (Chapter I, section 5: Relative Value of the Pieces)"
    publisher: José Raúl Capablanca, Project Gutenberg edition
    url: https://gutenberg.org/files/33870/33870-h/33870-h.htm
    type: book
    accessed: 2026-11-09
  - id: s4
    title: "The Evaluation of Material Imbalances (reprint of the 1999 Chess Life article, with 2012 update)"
    publisher: Larry Kaufman, reprinted on danheisman.com
    url: https://www.danheisman.com/evaluation-of-material-imbalances.html
    type: publication
    accessed: 2026-11-09
  - id: s5
    title: "When You're Way Ahead"
    publisher: Dan Heisman, Chess.com blog
    url: https://www.chess.com/blog/danheisman/when-youre-way-ahead
    type: publication
    accessed: 2026-11-09
  - id: s6
    title: "Exchanging to Win"
    publisher: Exeter Chess Club (2010)
    url: https://exeterchessclub.org.uk/node/808
    type: community
    accessed: 2026-11-09
created: 2026-11-09
---

# Material advantage

A player has a material advantage when the pieces and pawns they still have on the board are worth more than the opponent's. Since every unit has a different power, "material" is counted with a scale of values rather than by number of pieces; the familiar club scale gives the pawn 1, knight and bishop 3, rook 5 and queen 9.[^s2] Winning material is the usual aim of tactics, and a material count is the first thing most players and engines look at when judging a position.[^s1]

## How material is counted

Piece scales are older than modern chess literature. Edward Winter's survey of historical tables shows early 19th-century authors giving decimal values such as knight 3.05, bishop 3.5, rook 5.48 and queen 9.94, mid-century writers treating bishop and knight as equal, and Emanuel Lasker in 1905 publishing a scale he said came from experience rather than calculation. The now-standard 1–3–3–5–9 table appears in Reuben Fine's *Chess The Easy Way* (1942).[^s2] Several of these authors warned that the true value depends on the position; one 1882 manual says so in almost exactly those words.[^s2]

Two modern attempts measured the values from games. Larry Kaufman, using a database of roughly 300,000 games between players rated 2300 and above, arrived at knight and bishop about 3¼, rook 5 and queen 9¾ (revised in 2012 to 3.5, 3.5, 5.25 and 10), with the bishop pair worth about an extra half pawn.[^s4] In 2020 a DeepMind team fitted a simple model to AlphaZero self-play games and obtained knight 3.05, bishop 3.33, rook 5.63 and queen 9.5, close to the conventional scale; the authors present these as approximations, not a gold standard.[^s1]

## Imbalances and context

The values matter most when the two sides have *different* material of roughly equal total, an imbalance. Capablanca held that two bishops are almost always better than two knights, that a rook is worth a minor piece and two pawns, that two rooks are slightly stronger than a queen, and that the knight loses power and the rook gains it as pieces are exchanged.[^s3] Kaufman's statistics add detail: the exchange (rook for a minor piece) is worth about 1¾ pawns on average but less when the side giving it up keeps the bishop pair; each pawn beyond five on a side slightly helps knights and hurts rooks; and queen against two rooks depends on how many minor pieces remain.[^s4]

The diagram is a simple example. White has a rook and four pawns, Black a bishop and six pawns, so the 1–3–3–5–9 count is level (9 against 9). Capablanca's rule of rook for minor piece and two pawns says the same, but he also notes that a bishop with pawns fights a rook better than a knight does, so the count alone does not settle the evaluation.[^s3][^s2]

## Converting an advantage

Being ahead is only useful if it is converted. Dan Heisman's advice for a large advantage is to think about defence first, keep the position simple, make fair trades of pieces but not necessarily of pawns, and keep every piece active; complications, he argues, mostly help the side that is behind.[^s5] The classic club form of the rule is to exchange pieces but keep pawns, because simplification magnifies the extra material while remaining pawns give the stronger side something to promote.[^s6]

## Pitfalls

- **Counting instead of evaluating.** Values are averages; Kaufman's adjustments for the bishop pair and pawn count, and Capablanca's notes on rooks and knights in the ending, show how far a position can depart from the table.[^s4][^s3]
- **Grabbing at the cost of safety.** Heisman's first principle is defence: an extra piece is worth little if the opponent gets a mating attack or other counterplay.[^s5]
- **Unnecessary pawn trades.** Trading pawns while ahead can remove the winning chances, since the stronger side may need pawns to promote.[^s6][^s5]

## Connections

Material advantage sits under general **chess strategy** and **depends on** a scale of **piece values**, which Winter traces through two centuries of chess books.[^s2] It is the usual goal of a **combination** and is what tactics such as the fork and pin **enable**; a **sacrifice** deliberately **contrasts with** it, giving up material for other gains. The **bishop pair** and **the exchange** are the best-studied material imbalances.[^s4][^s3] For computers, material is the first term of an **evaluation function**, and the AlphaZero study shows that a model using only piece counts reproduces the traditional scale.[^s1] Once ahead, the standard technique of **simplification** **leads** from a material plus to a won ending.[^s5][^s6]

## Sources

[^s1]: Nenad Tomašev, Ulrich Paquet, Demis Hassabis and Vladimir Kramnik, "Assessing Game Balance with AlphaZero: Exploring Alternative Rule Sets in Chess", arXiv:2009.04374 (2020), section 3.8. https://arxiv.org/pdf/2009.04374 (accessed 2026-11-09)
[^s2]: Edward Winter, Chess Notes, "The Value of the Chess Pieces". https://chesshistory.com/winter/extra/value.html (accessed 2026-11-09)
[^s3]: José Raúl Capablanca, *Chess Fundamentals*, Chapter I, section 5, "Relative Value of the Pieces" (Project Gutenberg). https://gutenberg.org/files/33870/33870-h/33870-h.htm (accessed 2026-11-09)
[^s4]: Larry Kaufman, "The Evaluation of Material Imbalances" (Chess Life, March 1999, with 2012 update), reprinted on danheisman.com. https://www.danheisman.com/evaluation-of-material-imbalances.html (accessed 2026-11-09)
[^s5]: Dan Heisman, "When You're Way Ahead", Chess.com blog. https://www.chess.com/blog/danheisman/when-youre-way-ahead (accessed 2026-11-09)
[^s6]: Exeter Chess Club, "Exchanging to Win" (2010). https://exeterchessclub.org.uk/node/808 (accessed 2026-11-09)
