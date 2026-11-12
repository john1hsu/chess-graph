---
id: kt:back-rank-mate
type: MatingPattern
title: Back-rank mate
aliases: [Back rank mate, Back-rank checkmate, Corridor mate, Back-rank weakness, Weak back rank]
domain: tactics
summary: >-
  A checkmate delivered by a rook or queen along the opponent's first rank, where the king cannot
  escape because the squares in front of it are blocked by its own pawns or covered by enemy pieces.
fen: "6k1/5ppp/8/8/8/8/5PPP/3R2K1 w - - 0 1"
status: current
volatile: false
verified: 2026-11-12
broader: [kt:checkmate, kt:chess-tactics]
related: [kt:combination, kt:castling, kt:deflection, kt:smothered-mate, kt:prophylaxis]
relations:
  - {predicate: usesTechnique, object: kt:deflection}
  - {predicate: contrastsWith, object: kt:smothered-mate}
  - {predicate: exemplifiedBy, object: kt:adams-versus-torre-new-orleans-1920}
sources:
  - id: s1
    title: "Glossary of chess terms (FIDE education archive)"
    publisher: FIDE
    url: https://eduarchive.fide.com/wp-content/uploads/2020/05/glossary_en.pdf
    type: governing-body
    accessed: 2026-11-12
  - id: s2
    title: "The Back-Rank Mate"
    publisher: Edward Winter, Chess Notes
    url: https://www.chesshistory.com/winter/extra/backrank.html
    type: reference
    accessed: 2026-11-12
  - id: s3
    title: "Adams v Torre – A Sham?"
    publisher: Edward Winter, Chess Notes
    url: https://www.chesshistory.com/winter/extra/adamstorre.html
    type: reference
    accessed: 2026-11-12
  - id: s4
    title: "Back-Rank Mate (Chess Terms)"
    publisher: Chess.com
    url: https://www.chess.com/terms/back-rank-mate-chess
    type: publication
    accessed: 2026-11-12
  - id: s5
    title: "Back Rank Checkmate (Chess Terms)"
    publisher: ChessKid (Chess.com)
    url: https://www.chesskid.com/learn/terms/back-rank-checkmate
    type: publication
    accessed: 2026-11-12
  - id: s6
    title: "The Back Rank Mate: Sealing off the King's Flight Squares, Figure 6.1.3.5 (Predator at the Chessboard)"
    publisher: Ward Farnsworth, chesstactics.org
    url: https://www.chesstactics.org/mating-patterns/the-back-rank-mate/sealing-off-the-kings-flight-squares/6_1_3_5.html
    type: publication
    accessed: 2026-11-12
created: 2026-11-12
---

# Back-rank mate

A back-rank mate is a checkmate given by a rook or a queen along the opponent's first rank: the eighth rank against Black, the first against White. The king cannot step forward because the squares on the next rank are occupied by its own pawns or controlled by the attacker, and it cannot run sideways along the rank it is being checked on.[^s4][^s5] FIDE's educational glossary defines the back rank as the rank on which the pieces start the game and notes that it is often the scene of a dramatic "corridor" mate, in which a rook or queen checks along it while the flight squares on the next rank are blocked or attacked.[^s1]

## Why it happens

The pattern grows out of sound habits. Castling and leaving the three pawns in front of the king unmoved is normally a safe arrangement, but it also builds the wall that later traps the king; ChessKid's teaching page calls this pawn cover a "blanket" for the king.[^s4][^s5] The danger appears when the heavy pieces leave the first rank (to attack, to occupy an open file, or simply because they have been exchanged) and nothing is left to cover it. The mate need not depend only on the king's own pawns: an enemy bishop or advanced pawn covering one of the flight squares does the same job.[^s4][^s6] Farnsworth gives an example in which a pawn that has reached the third rank in front of the king takes away its escape squares as effectively as the king's own pawns would.[^s6]

## Exploiting a weak back rank

Against a careful defender the mate is rarely available at once, so the attacker works on the pieces that guard the rank.[^s5]

- **Overloading and deflection.** A rook or queen that guards both the back rank and something else can be asked to do too much. ChessKid's examples include capturing a piece that a rook was defending, when that rook cannot recapture without abandoning the back rank.[^s5] Chess.com cites a Gligorić v Fischer game in which a knight fork won the exchange because White's rook on d1 could not leave the first rank without allowing mate on a1.[^s4]
- **Decoy sacrifices.** Giving up material to pull the last defender off the rank, then mating on the square it left, is the classic form of the combination.[^s4][^s5]
- **Doubling and batteries.** Two rooks, or a queen and rook, lined up on an open file add force when one defender holds the rank.[^s5]

Edward Winter's collection of historical finishes shows how old and how varied the theme is, from a Tarrasch game of the early 1880s to Capablanca v Grommer, New York, 2 July 1913, which ended 39.Re8 Rf4 40.Qb8 Kg8 41.Qb3+ Kh8 42.Rxf8+ Rxf8 43.Qf7 Qc8 44.Qxf8+ and Black resigned.[^s2]

## Defending

The standard remedy is *luft* ("air"): moving one of the pawns in front of the castled king, typically h3 or g3 for White and ...h6 or ...g6 for Black, so the king has a flight square.[^s5] The other is to keep a rook or the queen guarding the first rank while the king is boxed in, and to check before every move whether an enemy heavy piece can reach the rank.[^s5] Both are forms of **prophylaxis**: anticipating the opponent's idea rather than reacting to it.

## Example

In the diagram position (White to move), **1.Rd8#** is mate. The king on g8 is attacked along the eighth rank, the pawns on f7, g7 and h7 take away every square on the seventh, and nothing can capture the rook or block the check. Had Black played ...h6 earlier, the king would simply step to h7.[^s4][^s5]

A celebrated (but doubtful) illustration is the game published as Adams v Torre, New Orleans 1920, in which White's queen repeatedly offered itself to exploit the overloaded defenders of e8.[^s3] Winter shows that the game first appeared only in the *American Chess Bulletin* of November 1925, with notes by the loser, and gathers testimony that Torre built it from analysis of a casual game, so it should be treated as a composition-like example rather than a verified tournament result.[^s3] In the score below, 18...Qxg4 would allow 19.Rxe8+ Rxe8 20.Rxe8#, and at the end 23...Qxb7 runs into the same mate on e8.

```pgn
[Event "New Orleans (authenticity disputed)"]
[Date "1920.??.??"]
[White "Adams"]
[Black "Torre"]
[Result "1-0"]

1. e4 e5 2. Nf3 d6 3. d4 exd4 4. Qxd4 Nc6 5. Bb5 Bd7 6. Bxc6 Bxc6 7. Nc3 Nf6
8. O-O Be7 9. Nd5 Bxd5 10. exd5 O-O 11. Bg5 c6 12. c4 cxd5 13. cxd5 Re8
14. Rfe1 a5 15. Re2 Rc8 16. Rae1 Qd7 17. Bxf6 Bxf6 18. Qg4 Qb5 19. Qc4 Qd7
20. Qc7 Qb5 21. a4 Qxa4 22. Re4 Qb5 23. Qxb7 1-0
```

## Names

Many reference works use "corridor mate" as a synonym, but Winter notes that definitions differ. The earliest use he cites is the French *mat du couloir* in a 1947 book; Horton's 1959 dictionary restricts it to a king trapped on an edge rank behind its pawns, while Pandolfini treats the back-rank mate as one case of a more general corridor mate along any line.[^s2] This graph treats the names as one subject.

## Connections

The back-rank mate is a named pattern of **checkmate** and one of the basic families of **chess tactics**.[^s1][^s4] It is a frequent finish of a **combination**, and it **uses** **deflection** and decoy sacrifices to remove the defenders of the rank.[^s4][^s5] The pawn shelter created by **castling** is what makes it possible, and making luft or keeping a guard on the rank is the **prophylaxis** that prevents it.[^s5] It **contrasts with** the **smothered mate**, where a knight mates a king hemmed in by its own pieces rather than a heavy piece along a line. It is **exemplified by** the disputed **Adams v Torre, New Orleans 1920**.[^s3]

## Sources

[^s1]: FIDE, Glossary of chess terms (education archive), entries "Back rank" and "Corridor mate". https://eduarchive.fide.com/wp-content/uploads/2020/05/glossary_en.pdf (accessed 2026-11-12)
[^s2]: Edward Winter, "The Back-Rank Mate", Chess Notes. https://www.chesshistory.com/winter/extra/backrank.html (accessed 2026-11-12)
[^s3]: Edward Winter, "Adams v Torre – A Sham?", Chess Notes. https://www.chesshistory.com/winter/extra/adamstorre.html (accessed 2026-11-12)
[^s4]: Chess.com, "Back-Rank Mate" (Chess Terms). https://www.chess.com/terms/back-rank-mate-chess (accessed 2026-11-12)
[^s5]: ChessKid, "Back Rank Checkmate" (Chess Terms). https://www.chesskid.com/learn/terms/back-rank-checkmate (accessed 2026-11-12)
[^s6]: Ward Farnsworth, *Predator at the Chessboard*, "The Back Rank Mate: Sealing off the King's Flight Squares", Figure 6.1.3.5. https://www.chesstactics.org/mating-patterns/the-back-rank-mate/sealing-off-the-kings-flight-squares/6_1_3_5.html (accessed 2026-11-12)
