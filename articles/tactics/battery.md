---
id: kt:battery
type: TacticalMotif
title: Battery
aliases: [Battery play, Chess battery]
domain: tactics
summary: >-
  Two or more pieces of the same colour lined up on one rank, file or diagonal so that they act
  together along it: either a line piece backing up the piece in front of it, or a rear line piece
  waiting to be unmasked when the front piece moves away.
fen: "5rk1/ppp2ppp/8/8/8/3Q4/PP3PPP/1B4K1 w - - 0 1"
status: current
volatile: false
verified: 2026-11-16
broader: [kt:chess-tactics]
related: [kt:discovered-attack, kt:double-check, kt:alekhines-gun, kt:open-file, kt:chess-problems, kt:windmill]
relations:
  - {predicate: enables, object: kt:discovered-attack}
  - {predicate: enables, object: kt:double-check}
  - {predicate: enables, object: kt:checkmate}
sources:
  - id: s1
    title: "Extreme Chess Tactics, chapter 2: Battery Play (sample pages)"
    publisher: Yochanan Afek, Gambit Publications 2017 (excerpt hosted by Chess Tigers)
    url: https://chess-tigers.de/cdn/shop/files/Extreme_Chess_Tactics.pdf
    type: book
    accessed: 2026-11-16
  - id: s2
    title: "The Chess Seesaw/Windmill"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://www.chesshistory.com/winter/extra/seesaw.html
    type: reference
    accessed: 2026-11-16
  - id: s3
    title: "Grivas: Underdeveloped Battery"
    publisher: GM Efstratios Grivas, ChessBase
    url: https://en.chessbase.com/post/grivas-underdeveloped-battery
    type: publication
    accessed: 2026-11-16
  - id: s4
    title: "Grivas: Underdeveloped Battery (2)"
    publisher: GM Efstratios Grivas, ChessBase
    url: https://en.chessbase.com/post/grivas-underdeveloped-battery-2
    type: publication
    accessed: 2026-11-16
  - id: s5
    title: "Battery (Chess Terms)"
    publisher: Chess.com
    url: https://www.chess.com/terms/battery-chess
    type: publication
    accessed: 2026-11-16
  - id: s6
    title: "Battery Play (Problem World, No. 8)"
    publisher: Peter Wong, OzProblems
    url: https://www.ozproblems.com/problem-world/battery-play
    type: community
    accessed: 2026-11-16
created: 2026-11-16
---

# Battery

A **battery** is a formation of two or more pieces of the same colour on one rank, file or diagonal, so that their power along that line adds up.[^s3][^s4] In practical play the word usually means heavy pieces (rooks and queen) stacked on a file, or a queen and bishop sharing a diagonal.[^s3][^s5] Problemists and study composers use it in a narrower sense: two pieces aimed at a target, where the front piece can step off the line and unleash the rear one.[^s1][^s6] Both senses describe the same geometry and are worth knowing, because a stacked battery often becomes a firing battery a few moves later.

## Two kinds of battery

**Supporting batteries.** Here every piece on the line backs up the one in front. Chess.com applies the term to rooks or queens on an open or half-open file and to a queen and bishop on a diagonal.[^s5] Grivas notes that the most common queen-and-bishop form has the bishop on an open diagonal supporting its queen, and that batteries serve defence as well as attack and usually form part of a larger combination.[^s3][^s4] The strongest file version, two rooks with the queen behind them, is known as **Alekhine's gun**, completed on the c-file with 26.Qc1 in Alekhine–Nimzowitsch, San Remo 1930.[^s5]

**Firing batteries.** In Afek's definition the rear piece must be a line mover (queen, rook or bishop), while the front piece may be anything except the queen.[^s1] When the front piece moves, the rear piece's line opens: this is a **discovered attack**, or a discovered check when the target is the king.[^s1][^s6] Afek distinguishes three types.[^s1]

- **Direct battery:** the rear piece is unleashed straight at the king or another target.[^s1]
- **Indirect battery:** the line points at a square next to the king, so that firing it takes away a flight square.[^s1]
- **Masked battery:** a piece of either colour still stands between the front piece and the target, and the battery becomes live only once that blocker leaves.[^s1]

Problem literature adds the **half-battery**, with two pieces standing between a line piece and the enemy king; whichever of them moves off the line leaves a battery made of the other.[^s6]

## Why batteries work

A firing battery gives two threats in one move: the unmasked piece attacks along the line while the front piece is free to threaten something of its own. If the line leads to the king, the defender must answer the check first, so the front piece can often roam freely or capture what it attacks; if both pieces give check, it is a **double check** and only a king move helps.[^s1] Afek stresses patience as well: a battery is a loaded weapon, and firing it too early can throw away its value, while combining it with zugzwang often decides.[^s1]

A battery that fires again and again is the **windmill** (or seesaw), in which a rook and a supporting line piece alternate discovered checks and the moving piece collects material on every cycle. Edward Winter traces the "see-saw" back to a Bird–Williams game of 1849 and later cases by Zukertort and Steinitz, who wrote of a "so-called seesaw of checks".[^s2]

## Example

In the diagram (White to move), the bishop on b1 stands behind the queen on d3, forming a battery on the b1–h7 diagonal. **1.Qxh7#** is mate: the queen is protected along the diagonal, the rook on f8 blocks the king's escape and h8 is covered by the queen. The set-up is the bishop-on-b1, queen-on-d3 diagonal battery that Chess.com uses to illustrate the idea.[^s5] For the defender, the lesson is to keep h7 covered (or the diagonal blocked) whenever such a battery can form.

## Pitfalls

- **Lining up on a closed line.** A battery is only as good as the line it occupies; Chess.com's file examples use open or semi-open files, and doubling on a blocked line usually just wastes tempi.[^s5]
- **Ignoring the defender's counter-battery.** Afek's Euwe–Denker, Groningen 1946 example shows the defender breaking free with a counter-strike (35...f3!) that turns the tables.[^s1]
- **Moving the front piece carelessly.** The firing move must itself do something; the front piece should check, capture or threaten, otherwise the defender simply blocks the line.[^s1][^s6]

## Connections

The battery belongs to **chess tactics** as the set-up behind several motifs: it **enables** the **discovered attack** and the **double check**, and in queen-and-bishop or heavy-piece form it frequently **enables** **checkmate**.[^s1][^s3][^s5] On a file it is the tactical side of the strategy of the **open file**, and its strongest file form is **Alekhine's gun**.[^s5] Repeated firing produces the **windmill**.[^s2] In **chess problems**, batteries are a core building block, classified as direct, indirect, masked or half-batteries.[^s1][^s6]

## Sources

[^s1]: Yochanan Afek, *Extreme Chess Tactics* (Gambit Publications, 2017), chapter 2 "Battery Play", sample pages. https://chess-tigers.de/cdn/shop/files/Extreme_Chess_Tactics.pdf (accessed 2026-11-16)
[^s2]: Edward Winter, "The Chess Seesaw/Windmill", Chess Notes. https://www.chesshistory.com/winter/extra/seesaw.html (accessed 2026-11-16)
[^s3]: Efstratios Grivas, "Grivas: Underdeveloped Battery", ChessBase. https://en.chessbase.com/post/grivas-underdeveloped-battery (accessed 2026-11-16)
[^s4]: Efstratios Grivas, "Grivas: Underdeveloped Battery (2)", ChessBase. https://en.chessbase.com/post/grivas-underdeveloped-battery-2 (accessed 2026-11-16)
[^s5]: Chess.com, "Battery" (Chess Terms). https://www.chess.com/terms/battery-chess (accessed 2026-11-16)
[^s6]: Peter Wong, "Battery Play", OzProblems Problem World. https://www.ozproblems.com/problem-world/battery-play (accessed 2026-11-16)
