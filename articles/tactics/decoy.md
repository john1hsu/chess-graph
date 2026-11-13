---
id: kt:decoy
type: TacticalMotif
title: Decoy
aliases: [Attraction, Decoy sacrifice, Luring, Magnet]
domain: tactics
summary: >-
  A tactic that lures an enemy piece onto a particular square, where it can then be
  exploited by a fork, pin, mating net or other follow-up; it is the mirror image of
  deflection, which drives a defender away from a square rather than drawing one onto it.
fen: "rn3rk1/pbppq1pp/1p2pb2/4N2Q/3PN3/3B4/PPP2PPP/R3K2R w KQ - 6 11"
status: current
volatile: false
verified: 2026-11-13
broader: [kt:chess-tactics]
related: [kt:deflection, kt:combination, kt:sacrifice, kt:fork, kt:back-rank-mate, kt:smothered-mate, kt:zwischenzug]
relations:
  - {predicate: contrastsWith, object: kt:deflection}
  - {predicate: enables, object: kt:fork}
  - {predicate: enables, object: kt:checkmate}
  - {predicate: usesTechnique, object: kt:sacrifice}
  - {predicate: exemplifiedBy, object: kt:lasker-thomas-1912}
sources:
  - id: s1
    title: "Decoy (Chess Terms)"
    publisher: Chess.com
    url: https://www.chess.com/terms/decoy-chess
    type: publication
    accessed: 2026-11-13
  - id: s2
    title: "Look! It's Elvis! (The Decoy Part 1)"
    publisher: Jessica Martin, ChessKid
    url: https://www.chesskid.com/learn/articles/look-its-elvis-the-decoy
    type: publication
    accessed: 2026-11-13
  - id: s3
    title: "Decoys on the Diagonal / Bishop Check Sacrifices, Figure 5.3.4.5 (Predator at the Chessboard)"
    publisher: Ward Farnsworth, chesstactics.org
    url: https://www.chesstactics.org/removing-the-guard/attacking-the-guard/decoys-on-the-diagonal_bishop-check-sacrifices/5_3_4_5.html
    type: publication
    accessed: 2026-11-13
  - id: s4
    title: "Flush Checks / The Decoy, Figure 5.3.3.1 (Predator at the Chessboard)"
    publisher: Ward Farnsworth, chesstactics.org
    url: https://www.chesstactics.org/removing-the-guard/attacking-the-guard/flush-checks_the-decoy/5_3_3_1.html
    type: publication
    accessed: 2026-11-13
  - id: s5
    title: "Chess Tactics for Kids (sample: contents and Tactic 7, Decoy Sacrifices)"
    publisher: Murray Chandler, Gambit Publications
    url: https://shop.chess-tigers.de/cdn/shop/files/Chess_Tactics_for_Kids.pdf
    type: book
    accessed: 2026-11-13
  - id: s6
    title: "Chaos in a Miniature (Edward Lasker v Sir George Thomas)"
    publisher: Edward Winter, Chess Notes
    url: https://www.chesshistory.com/winter/extra/laskerthomas.html
    type: reference
    accessed: 2026-11-13
created: 2026-11-13
---

# Decoy

A decoy, also called attraction or luring, is a tactic that forces an enemy piece onto a particular square, where it can then be attacked, forked, pinned or mated.[^s1][^s2] The square the piece is drawn to is the point: once the king, queen or another man is sitting there, a follow-up move that was not previously available becomes decisive.[^s1] Because the opponent will not usually step onto a bad square voluntarily, the decoying move is almost always forcing, a check or a capture the opponent must answer, and it is frequently a sacrifice offered precisely so that the capturing piece ends up where the attacker wants it.[^s1][^s3]

## Decoy versus deflection

Decoy is the mirror image of **deflection**. Both themes "distract" an enemy piece with a sacrifice, and online puzzle sets often group them together, but the geometry is opposite.[^s1] A deflection drives a defender *away* from a square or duty it is performing; a decoy draws a piece *onto* a square where it becomes a target.[^s1][^s2] Chess.com states the distinction plainly: deflection diverts a piece from its job, while a decoy is "drawing a piece onto a bad square," and treats the two as very closely related.[^s1] Coaching sources keep them as separate lessons for exactly this reason: in Murray Chandler's *Chess Tactics for Kids* the decoy sacrifice and the deflection are consecutive chapters.[^s5]

## Common uses

- **Setting up a fork.** The classic pattern draws the king (or queen) to a square where a knight then forks it together with another piece. A king lured onto a light square can run into a check-and-fork that wins the queen.[^s2]
- **Winning the queen with a flush check.** Farnsworth describes the "flush check" decoy: a rook check delivered right next to the king that the king must capture, after which the now-undefended enemy queen falls. In the simplest form Black plays a rook to h1, White must answer Kxh1, and Black then takes White's queen, which the king was guarding.[^s4]
- **Dragging the king into a mating net.** The decoy's most spectacular use is the king hunt: a queen sacrifice pulls the king up the board, where the remaining pieces drive it to its death (see the example below).[^s6]
- **Back-rank mates.** A piece can be lured onto the back rank or forced to block beside its own king so that a rook or queen mates.[^s2]

## Mechanics with checks

Farnsworth stresses that checks which put the enemy king and queen into a dependent relationship — forcing one of them to capture or block next to the other — are the natural engines of a decoy.[^s3] His bishop-check example runs 1.Bxf7+ (the king must take) 1...Qxf7 2.Rd8+ (a second sacrifice) 2...Kxd8 3.Qxf7: the first check decoys the queen, the second decoys the king off its guard of that queen, and White emerges a clear queen ahead.[^s3] The requirement that the opponent *must* take is what separates a sound decoy from a mere hopeful offer.[^s3][^s4]

## Example: Edward Lasker – Sir George Thomas, London 1912

The most famous decoy in chess literature is the queen sacrifice that opens Edward Lasker's miniature against Sir George Thomas at the City of London Chess Club, dated 29 October 1912 by Edward Winter's research.[^s6] In the diagram position (White to move) Lasker played **11.Qxh7+!!**, a pure attraction sacrifice: the queen is given up only to drag the Black king out of its shelter.[^s6] After **11...Kxh7 12.Nxf6+** the king is already stranded, and White's two knights, bishop and rook escort it from h7 all the way to g1, where a quiet king move delivers mate.[^s6]

```pgn
[Event "City of London Chess Club"]
[Site "London"]
[Date "1912.10.29"]
[White "Edward Lasker"]
[Black "George Alan Thomas"]
[Result "1-0"]

1. d4 e6 2. Nf3 f5 3. Nc3 Nf6 4. Bg5 Be7 5. Bxf6 Bxf6 6. e4 fxe4 7. Nxe4 b6
8. Ne5 O-O 9. Bd3 Bb7 10. Qh5 Qe7 11. Qxh7+ Kxh7 12. Nxf6+ Kh6 13. Neg4+ Kg5
14. h4+ Kf4 15. g3+ Kf3 16. Be2+ Kg2 17. Rh2+ Kg1 18. Kd2# 1-0
```

The finish is itself a hidden point: 18.Kd2 gives mate not by moving toward the king but by uncovering the rook on a1, which checks the Black king along the first rank while every flight square is covered.[^s6] Winter notes that sources disagree over whether Lasker ended with 18.Kd2 or with queenside castling (18.O-O-O), both of which mate; Lasker himself wrote that he chose the king move because it disturbed only one piece.[^s6]

## Pitfalls

- **The capture must be forced.** A decoy offer the opponent can decline is just a blunder; the sacrifice has to be a check or an otherwise unavoidable capture.[^s3][^s4]
- **Check the landing square.** The whole idea depends on what happens *after* the piece arrives; before sacrificing, confirm that the fork, pin or mate actually works with the enemy man on its new square.[^s2][^s4]
- **Mind the difference from deflection.** Luring a piece *onto* a square and driving one *off* a square call for different follow-ups; mixing them up is a common calculation error.[^s1][^s5]

## Connections

Decoy is one of the standard families of **chess tactics** and a frequent building block of a **combination**, almost always introduced by a **sacrifice**.[^s1][^s5] It **contrasts with** **deflection**, its mirror image, and the two are routinely taught as a pair.[^s1][^s5] Its typical payoff is to **enable** a **fork** — especially a knight fork of king and queen — or to **enable** **checkmate**, including the **back-rank mate** and the **smothered mate**, whose Philidor's-legacy form uses a queen sacrifice to lure a rook onto g8.[^s2][^s4] A **zwischenzug** can supply the forcing in-between move that makes a decoy work, and the Lasker–Thomas king hunt **exemplifies** the motif in its most dramatic form.[^s3][^s6]

## Sources

[^s1]: Chess.com, "Decoy" (Chess Terms). https://www.chess.com/terms/decoy-chess (accessed 2026-11-13)
[^s2]: Jessica Martin (BoundingOwl), "Look! It's Elvis! (The Decoy Part 1)", ChessKid. https://www.chesskid.com/learn/articles/look-its-elvis-the-decoy (accessed 2026-11-13)
[^s3]: Ward Farnsworth, "Decoys on the Diagonal / Bishop Check Sacrifices" (Figure 5.3.4.5), *Predator at the Chessboard*, chesstactics.org. https://www.chesstactics.org/removing-the-guard/attacking-the-guard/decoys-on-the-diagonal_bishop-check-sacrifices/5_3_4_5.html (accessed 2026-11-13)
[^s4]: Ward Farnsworth, "Flush Checks / The Decoy" (Figure 5.3.3.1), *Predator at the Chessboard*, chesstactics.org. https://www.chesstactics.org/removing-the-guard/attacking-the-guard/flush-checks_the-decoy/5_3_3_1.html (accessed 2026-11-13)
[^s5]: Murray Chandler, *Chess Tactics for Kids*, Gambit Publications (sample: contents and Tactic 7, "Decoy Sacrifices"). https://shop.chess-tigers.de/cdn/shop/files/Chess_Tactics_for_Kids.pdf (accessed 2026-11-13)
[^s6]: Edward Winter, "Chaos in a Miniature" (Edward Lasker v Sir George Thomas, 1912), Chess Notes. https://www.chesshistory.com/winter/extra/laskerthomas.html (accessed 2026-11-13)
