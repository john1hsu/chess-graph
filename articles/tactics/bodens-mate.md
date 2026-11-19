---
id: kt:bodens-mate
type: MatingPattern
title: Boden's mate
aliases: [Bodens mate, Boden's Mate, Criss-cross mate, Crisscross mate, Boden mate]
domain: tactics
summary: >-
  A checkmate by two bishops on crossing diagonals against a king, usually castled queenside, whose
  escape squares are blocked by its own pieces; it is named after Samuel Boden's 15-move win against
  Schulder, published in 1853, which ended with a queen sacrifice on c3 and ...Ba3 mate.
fen: "2k1r2r/ppp3pp/2n5/3B1b2/5P2/b1P1BQ2/P2N1P1P/2KR3R w - - 1 16"
status: current
volatile: false
verified: 2026-11-19
broader: [kt:checkmate, kt:chess-tactics]
related: [kt:bishop-pair, kt:sacrifice, kt:removing-the-guard, kt:smothered-mate, kt:back-rank-mate, kt:castling]
relations:
  - {predicate: namedAfter, object: kt:samuel-boden}
  - {predicate: exemplifiedBy, object: kt:schulder-versus-boden-1853}
  - {predicate: usesTechnique, object: kt:sacrifice}
  - {predicate: usesTechnique, object: kt:removing-the-guard}
  - {predicate: contrastsWith, object: kt:blackburnes-mate}
sources:
  - id: s1
    title: "Boden's Mate"
    publisher: Edward Winter, Chess Notes
    url: https://chesshistory.com/winter/extra/boden.html
    type: reference
    accessed: 2026-11-19
  - id: s2
    title: "Other Classic Mating Ideas: Boden's Mate, Figure 6.2.11.1 (Predator at the Chessboard)"
    publisher: Ward Farnsworth, chesstactics.org
    url: https://www.chesstactics.org/mating-patterns/other-classic-mating-ideas/bodens-mate/6_2_11_1.html
    type: book
    accessed: 2026-11-19
  - id: s3
    title: "Other Classic Mating Ideas: Boden's Mate, Figure 6.2.11.4 (Predator at the Chessboard)"
    publisher: Ward Farnsworth, chesstactics.org
    url: https://www.chesstactics.org/mating-patterns/other-classic-mating-ideas/bodens-mate/6_2_11_4.html
    type: book
    accessed: 2026-11-19
  - id: s4
    title: "Other Classic Mating Ideas: Boden's Mate, Figure 6.2.11.5 (Predator at the Chessboard)"
    publisher: Ward Farnsworth, chesstactics.org
    url: https://www.chesstactics.org/mating-patterns/other-classic-mating-ideas/bodens-mate/6_2_11_5.html
    type: book
    accessed: 2026-11-19
  - id: s5
    title: "Boden's Mate (Chess Terms)"
    publisher: Chess.com
    url: https://www.chess.com/terms/bodens-mate-chess
    type: publication
    accessed: 2026-11-19
  - id: s8
    title: "Other Classic Mating Ideas: Boden's Mate, Figure 6.2.11.8 (Predator at the Chessboard)"
    publisher: Ward Farnsworth, chesstactics.org
    url: https://www.chesstactics.org/mating-patterns/other-classic-mating-ideas/bodens-mate/6_2_11_8.html
    type: book
    accessed: 2026-11-19
  - id: s6
    title: "Edward Winter's Chess Explorations (72)"
    publisher: ChessBase News (Edward Winter)
    url: https://en.chessbase.com/post/edward-winter-s-che-explorations-72-
    type: publication
    accessed: 2026-11-19
  - id: s7
    title: "Boden's Crisscross Mate"
    publisher: ChessKid (Jessica E. Prescott)
    url: https://www.chesskid.com/learn/articles/bodens-criss-cross-mate
    type: publication
    accessed: 2026-11-19
created: 2026-11-19
---

# Boden's mate

Boden's mate is a checkmate given by two bishops working on diagonals that cross at, or next to, the enemy king, while the king's remaining flight squares are filled by its own men.[^s5] It is most often seen against a king that has castled queenside, though the geometry can appear anywhere on the board.[^s5] Because the two bishops form an X around the king, the pattern is also taught as the "criss-cross" mate: one bishop holds the king in place and the other gives the check along the second diagonal.[^s7]

## How it works

Ward Farnsworth's *Predator at the Chessboard* describes the division of labour: one bishop cuts off the king's escape squares while the other attacks along the crossing diagonal.[^s2] He compares it with the two-bishop mate associated with Blackburne, where the edge of the board stops a king on h8 from retreating; in Boden's mate the same job falls to the defender's own pieces, or to an enemy rook, for example one on e1 that keeps a king on c8 from stepping onto the e-file.[^s2] The typical target is a king on c1 or c8 with pawns on the a- and b-files and pieces on d1/d8 or d2/d7: one bishop on the f4–b8 (or f5–b1) diagonal covers b8 and c7, and the other arrives on a6 (or a3) to give mate.[^s3][^s4]

The mating bishop rarely has a free diagonal to begin with. The usual way to open it is a **sacrifice** that forces a pawn off the b-file: a queen or rook captures or checks on c3 or c6, the b-pawn recaptures, and the a3–f8 or a6–f1 diagonal is suddenly open to the king.[^s3][^s4]

## The name-giving game

The pattern takes its name from a miniature won by the Englishman Samuel Standidge Boden (1826–82), a landscape painter whose *Chess Monthly* obituary ranked him among England's best players.[^s1] The game, against an opponent known only as Schulder, opened with Philidor's Defence (2...d6). Edward Winter records that it was published in 1853 in both the *Chess Player* and the *British Chess Review*, neither of which gave a date or venue; London is usually assumed, and later books variously date it 1844, 1851, 1853, 1860 or 1865.[^s1][^s6] Winter also notes that nothing is reliably known about Schulder beyond the surname.[^s1]

```pgn
[Event "Casual game"]
[White "Schulder"]
[Black "Samuel Boden"]
[Result "0-1"]

1. e4 e5 2. Nf3 d6 3. c3 f5 4. Bc4 Nf6 5. d4 fxe4 6. dxe5 exf3 7. exf6 Qxf6
8. gxf3 Nc6 9. f4 Bd7 10. Be3 O-O-O 11. Nd2 Re8 12. Qf3 Bf5 13. O-O-O d5
14. Bxd5 Qxc3+ 15. bxc3 Ba3# 0-1
```

Farnsworth uses the finish as a teaching position.[^s3] White's king on c1 has no flight squares: d1 and d2 are occupied by its own rook and knight, b1 and c2 are covered by the bishop on f5, and b2, vacated by the recapture, lies on the bishop's line of check.[^s3] Boden's 13...d5 attacks the bishop on c4 and sets up the combination; after 14.Bxd5 the sacrifice 14...Qxc3+ forces 15.bxc3, which opens the a3–c1 diagonal, and 15...Ba3 is mate.[^s3] Farnsworth points out that White's best defence after 13...d5 was to move the rook from d1 to e1, freeing a square for the king, at the cost of a bishop.[^s3] The diagram above is the final position.

## Earlier examples and the term

Boden's game was not the first occurrence. Winter cites Horwitz v Popert, Hamburg 1844, described as purportedly the first instance, and Kieseritzky v Dumoncheau, published in the *Deutsche Schachzeitung* in 1850, both ending with a bishop mate on a6 after sacrifices on c6.[^s1] He also leaves open when the name "Boden's mate" first appeared in print, asking whether it predates Renaud and Kahn's *L'art de faire mat* (1947).[^s1]

## Recognising and preventing it

Farnsworth's exercises show the two defenders that most often stand in the way: a pawn on b7 (or b2) and a piece guarding a6 (or a3).[^s4] In one position White sacrifices a rook and then the queen on c6, a square both defenders also cover, so that each capture drags a guard away and Ba6 mates; he adds that a check on a pawn-guarded square can work as well as a capture there.[^s4] In another, the bishop is the least obvious attacker: a queen sacrifice on the g7–h6 diagonal clears the way for Bh6 mate against a king hemmed in by its own pieces and a rook on e1.[^s8]

For the defender the lesson follows from the mechanism. A king castled queenside with pieces on d1/d8 and d2/d7 has no flight squares, so any open diagonal to it from the a-file is dangerous; keeping the b-pawn on its square, giving the king an escape square (for instance by moving the d-file rook), and noticing when an opposing bishop already controls b8/b1 or c7/c2 all reduce the risk.[^s3][^s5]

## Connections

Boden's mate is a named pattern of **checkmate** and one of the standard families of **chess tactics**.[^s5] It is **named after** **Samuel Boden** and **exemplified by** his game against Schulder (1853).[^s1] It shows the attacking power of the **bishop pair** and nearly always **uses** a **sacrifice** to **remove the guard**, typically the b-pawn shielding the king.[^s3][^s4] It **contrasts with** **Blackburne's mate**, where the board edge rather than the king's own pieces confines the king.[^s2] Like the **smothered mate** and the **back-rank mate**, it punishes a king boxed in by its own men, a recurring risk after queenside **castling**.[^s2][^s5]

## Sources

[^s1]: Edward Winter, "Boden's Mate", Chess Notes. https://chesshistory.com/winter/extra/boden.html (accessed 2026-11-19)
[^s2]: Ward Farnsworth, *Predator at the Chessboard*, "Other Classic Mating Ideas: Boden's Mate", Figure 6.2.11.1. https://www.chesstactics.org/mating-patterns/other-classic-mating-ideas/bodens-mate/6_2_11_1.html (accessed 2026-11-19)
[^s3]: Ward Farnsworth, *Predator at the Chessboard*, "Other Classic Mating Ideas: Boden's Mate", Figure 6.2.11.4. https://www.chesstactics.org/mating-patterns/other-classic-mating-ideas/bodens-mate/6_2_11_4.html (accessed 2026-11-19)
[^s4]: Ward Farnsworth, *Predator at the Chessboard*, "Other Classic Mating Ideas: Boden's Mate", Figure 6.2.11.5. https://www.chesstactics.org/mating-patterns/other-classic-mating-ideas/bodens-mate/6_2_11_5.html (accessed 2026-11-19)
[^s5]: Chess.com, "Boden's Mate" (Chess Terms). https://www.chess.com/terms/bodens-mate-chess (accessed 2026-11-19)
[^s6]: Edward Winter, "Edward Winter's Chess Explorations (72)", ChessBase News. https://en.chessbase.com/post/edward-winter-s-che-explorations-72- (accessed 2026-11-19)
[^s8]: Ward Farnsworth, *Predator at the Chessboard*, "Other Classic Mating Ideas: Boden's Mate", Figure 6.2.11.8. https://www.chesstactics.org/mating-patterns/other-classic-mating-ideas/bodens-mate/6_2_11_8.html (accessed 2026-11-19)
[^s7]: Jessica E. Prescott, "Boden's Crisscross Mate", ChessKid. https://www.chesskid.com/learn/articles/bodens-criss-cross-mate (accessed 2026-11-19)
