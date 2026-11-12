---
id: kt:deflection
type: TacticalMotif
title: Deflection
aliases: [Deflection sacrifice, Deflecting the defender]
domain: tactics
summary: >-
  A tactic that forces an enemy piece away from an important duty, such as guarding a piece,
  a square or a line, so that a follow-up move that the piece was preventing becomes possible.
fen: "8/k7/P2b2P1/KP1Pn2P/8/8/7p/4n3 w - - 0 1"
status: current
volatile: false
verified: 2026-11-12
broader: [kt:chess-tactics]
related: [kt:combination, kt:sacrifice, kt:back-rank-mate, kt:zwischenzug, kt:overloading, kt:endgame-study]
relations:
  - {predicate: contrastsWith, object: kt:decoy}
  - {predicate: enables, object: kt:material-advantage}
  - {predicate: enables, object: kt:pawn-promotion}
  - {predicate: exemplifiedBy, object: kt:mitrofanov-study-1967}
sources:
  - id: s1
    title: "Removing the Guard (Chess Skills leaflet)"
    publisher: English Chess Federation
    url: https://www.englishchess.org.uk/wp-content/uploads/2010/01/guard.pdf
    type: governing-body
    accessed: 2026-11-12
  - id: s2
    title: "Deflection (Chess Terms)"
    publisher: Chess.com
    url: https://www.chess.com/terms/deflection-chess
    type: publication
    accessed: 2026-11-12
  - id: s3
    title: "Joys of Chess – the mother of all moves"
    publisher: Christian Hesse, ChessBase
    url: https://en.chessbase.com/newsroom/post/joys-of-chess-the-mother-of-all-moves?page=0
    type: publication
    accessed: 2026-11-12
  - id: s4
    title: "Winning Chess Tactics (sample: contents and chapter 10)"
    publisher: Yasser Seirawan (via New In Chess)
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/82202.pdf
    type: book
    accessed: 2026-11-12
  - id: s5
    title: "Tactical Training (sample: contents and introduction)"
    publisher: Cyrus Lakdawala, Everyman Chess (via New In Chess)
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/8416.pdf
    type: book
    accessed: 2026-11-12
  - id: s6
    title: "Deflection, Deflection on the Wall (The Decoy Part 2)"
    publisher: Jessica Martin, ChessKid
    url: https://www.chesskid.com/learn/articles/deflection-deflection-on-the-wall
    type: publication
    accessed: 2026-11-12
created: 2026-11-12
---

# Deflection

A deflection is a tactic that forces an enemy piece away from a square or a duty that matters, so that a move it was preventing becomes playable.[^s2] The duty can be guarding another piece, covering a mating square, watching a line or stopping a passed pawn; once the defender has been pulled away, the attacker cashes in by winning material, promoting a pawn or giving mate.[^s2][^s6] It is one of the standard families of combinational themes: Yasser Seirawan's *Winning Chess Tactics* gives it a chapter of its own, as does Cyrus Lakdawala's *Tactical Training*.[^s4][^s5]

## How it works

The English Chess Federation's teaching leaflet treats deflection as one of three ways of "removing the guard": a piece that is defended by another can be won if that defender is captured, overloaded or deflected.[^s1] The deflecting move is almost always forcing, typically a check or a capture the opponent must answer, and it is often a sacrifice, since the bait has to be something the defender cannot afford to ignore.[^s1][^s6] Two leaflet examples show the basic pattern: a rook capture with check on e7 removes the knight that guarded the queen, and a bishop check on c7 drags the king off its watch over a7, so that the queen falls or a pawn is won with a gain of material.[^s1] Chess.com's simplest model is Bxf7+ against a king on e8 that is the only guard of a queen on d8: the king must take, and the queen is lost.[^s2]

## Typical targets

- **Guards of the back rank.** A rook check on the eighth rank that the defending rook or queen must capture, after which the piece it was protecting, or the mating square, is undefended.[^s1][^s2] This is the usual mechanism of the **back-rank mate**.
- **Defenders of a mating square.** A knight on f6 that covers h7 is a classic target: once it is deflected, h7 is open to attack.[^s6]
- **Blockers of a passed pawn.** In endings a rook check or sacrifice can deflect the piece that stops a pawn; in one ECF exercise 1.Rg2+ Rxg2 lets the h-pawn promote.[^s1]
- **The king itself.** A king that has to guard a pawn and also stop a passed pawn can be deflected by the passed pawn's advance.[^s1][^s2]

## Distinguishing related themes

Coaching sources separate deflection, where a piece is driven *away* from a job, from the **decoy** (also called attraction), where a piece is lured *onto* a particular square where it can then be exploited.[^s6] Overloading describes the defender's situation, a piece with more jobs than it can do, which deflection then exploits.[^s1][^s2] The boundaries are loose in practice: Lakdawala groups decoy, attraction and removal of the guard in one chapter, calling decoy and removal of the guard nearly synonymous geometrically, and gives deflection and overloaded defenders chapters of their own.[^s5]

## Example: Mitrofanov's study (1967)

The most famous deflection in composition is Leopold Mitrofanov's study from the 1967 Rustaveli memorial tourney (White to play and win), shown in the diagram position.[^s3] After 1.b6+ Ka8 2.g7 h1=Q 3.g8=Q+ Bb8 4.a7 Nc6+ 5.dxc6 Qxh5+ White plays the astonishing 6.Qg5!!, offering the queen for nothing.[^s3] The point, as Christian Hesse explains it, is to deflect Black's queen onto the dark square g5, from where it can no longer stop the pawns: 6...Qxg5+ 7.Ka6 Qa5+ 8.Kxa5 Bxa7 9.c7 Kb7 10.bxa7 and a pawn promotes.[^s3]

```pgn
[Event "Rustaveli Memorial, Vecherni Tbilisi"]
[White "Leopold Mitrofanov (study)"]
[Black "?"]
[Date "1967"]
[Result "1-0"]
[SetUp "1"]
[FEN "8/k7/P2b2P1/KP1Pn2P/8/8/7p/4n3 w - - 0 1"]

1. b6+ Ka8 2. g7 h1=Q 3. g8=Q+ Bb8 4. a7 Nc6+ 5. dxc6 Qxh5+ 6. Qg5 Qxg5+ 7. Ka6 Qa5+ 8. Kxa5 Bxa7 9. c7 Kb7 10. bxa7 1-0
```

## Pitfalls and practical advice

- **"Free" material.** A piece offered for nothing is often a deflection; ChessKid's advice is to ask whether an apparently free capture is a trick.[^s6]
- **Move order.** Deflections usually work only in the right order; in one ECF exercise 1...Rxe1+ 2.Nxe1 Bxc5 wins a piece, while the reverse order lets White save it with a check.[^s1]
- **Count a defender's jobs.** Before relying on a piece as a guard, check what else it defends; a piece with two duties is the natural target.[^s1][^s2]

## Connections

Deflection is one of the **chess tactics** and a common link in a **combination**, usually introduced by a **sacrifice**.[^s1][^s4] It exploits **overloading** and **contrasts with** the **decoy**, which attracts a piece to a square rather than driving it off one.[^s5][^s6] It is a standard route to the **back-rank mate**, and a **zwischenzug** can serve as the forcing move that deflects a defender.[^s1] Its usual payoffs are a **material advantage** or **pawn promotion**, and it is **exemplified by** Mitrofanov's 1967 **endgame study**.[^s2][^s3]

## Sources

[^s1]: English Chess Federation, "Removing the Guard" (Chess Skills leaflet, after J. E. Littlewood and R. A. Furness). https://www.englishchess.org.uk/wp-content/uploads/2010/01/guard.pdf (accessed 2026-11-12)
[^s2]: Chess.com, "Deflection" (Chess Terms). https://www.chess.com/terms/deflection-chess (accessed 2026-11-12)
[^s3]: Christian Hesse, "Joys of Chess – the mother of all moves", ChessBase, 30 October 2013. https://en.chessbase.com/newsroom/post/joys-of-chess-the-mother-of-all-moves?page=0 (accessed 2026-11-12)
[^s4]: Yasser Seirawan, *Winning Chess Tactics*, sample pages. https://www.newinchess.com/media/wysiwyg/product_pdf/82202.pdf (accessed 2026-11-12)
[^s5]: Cyrus Lakdawala, *Tactical Training*, Everyman Chess, sample pages. https://www.newinchess.com/media/wysiwyg/product_pdf/8416.pdf (accessed 2026-11-12)
[^s6]: Jessica Martin, "Deflection, Deflection on the Wall (The Decoy Part 2)", ChessKid. https://www.chesskid.com/learn/articles/deflection-deflection-on-the-wall (accessed 2026-11-12)
