---
id: kt:double-check
type: TacticalMotif
title: Double check
aliases: [Double-check]
domain: tactics
summary: >-
  A check given by two pieces at once, normally when a piece moves off a line with check and
  uncovers a second check behind it; since neither check can be blocked or captured away with one
  move, the king itself must move.
fen: "rnbk1b1r/pp3ppp/2p5/4q1B1/4n3/8/PPP2PPP/2KR1BNR b - - 1 10"
status: current
volatile: false
verified: 2026-11-11
broader: [kt:chess-tactics]
related: [kt:discovered-attack, kt:checkmate, kt:sacrifice, kt:combination, kt:fork]
relations:
  - {predicate: dependsOn, object: kt:discovered-attack}
  - {predicate: leadsTo, object: kt:checkmate}
  - {predicate: governedBy, object: kt:fide-laws-of-chess}
  - {predicate: exemplifiedBy, object: kt:reti-versus-tartakower-vienna-1910}
sources:
  - id: s1
    title: "FIDE Laws of Chess (full text, applied from 1 January 2023)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/
    type: governing-body
    accessed: 2026-11-11
  - id: s2
    title: "Double Check in Chess"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://www.chesshistory.com/winter/extra/doublecheck.html
    type: reference
    accessed: 2026-11-11
  - id: s3
    title: "Réti v Tartakower"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://www.chesshistory.com/winter/extra/retitartakower.html
    type: reference
    accessed: 2026-11-11
  - id: s4
    title: "The ultimate weapon (Jon Speelman's Agony Column)"
    publisher: ChessBase News
    url: https://en.chessbase.com/post/speelman-agony-197
    type: publication
    accessed: 2026-11-11
  - id: s5
    title: "Double Check (Chess Terms)"
    publisher: Chess.com
    url: https://www.chess.com/fr/terms/double-check-chess
    type: publication
    accessed: 2026-11-11
created: 2026-11-11
---

# Double check

A double check is a position in which the king is attacked by two enemy pieces at the same moment. The FIDE Laws already allow for it in their definition of check: a king is in check when it is attacked by "one or more" of the opponent's pieces, and no move may leave it in check.[^s1] In practice a double check almost always arises from a discovery: one piece steps off a line and gives check itself, and in doing so unmasks a queen, rook or bishop that checks along the line it has just cleared.[^s2][^s5]

## Why the king must move

Against a single check the defender has three resources: capture the checking piece, put something in the way, or move the king. Against two checks arriving on two different lines, a single capture or interposition can remove at most one of them, so the only legal replies are king moves.[^s4][^s5] That is the whole source of the motif's power. Jon Speelman notes that when the king has no safe flight square the result is sudden mate, and that even when it can step aside the follow-up is often decisive.[^s4] Nimzowitsch's famous remark in *My System*, rendered in English as saying that even the laziest king flees wildly in the face of a double check, makes the same point.[^s2]

## Unusual forms

Winter's survey shows that a tidy definition is harder than it looks. Positions published in the *British Chess Magazine* (1957) and *CHESS* (1960) produce a double check through an en passant capture, where the capturing pawn removes a blocker from one line and the vacated square opens another; in one of them the pawn itself gives no check at all.[^s2] Speelman adds that in rare cases the forced king move can itself deliver mate, and that with fairy pieces such as the nightrider even treble checks become possible.[^s4]

## Key example: Réti v Tartakower, Vienna 1910

The best-known double check in practical play finished a short game in Vienna in 1910. Winter's research shows it was not a lightning game, as later books claimed: Georg Marco reported that it was played for a stake at fifteen moves an hour, and the first publication in Marco's *Neues Wiener Tagblatt* column (1 April 1910) simply ended with 10.Bg5+ and resignation.[^s3]

```pgn
[Event "Vienna"]
[Date "1910.??.??"]
[White "Richard Reti"]
[Black "Savielly Tartakower"]
[Result "1-0"]

1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nf6 5. Qd3 e5 6. dxe5 Qa5+ 7. Bd2 Qxe5
8. O-O-O Nxe4 9. Qd8+ Kxd8 10. Bg5+ Kc7 11. Bd8# 1-0
```

The diagram position is the one after **10.Bg5+**. The bishop checks from g5 and, by leaving d2, opens the d-file for the rook on d1. Black's queen could capture the bishop and the knight could block on d2 or d6, but none of those deals with both checks, so only **10...Ke8** and **10...Kc7** are legal. Chess.com points out that the first runs into 11.Rd8# and the second into 11.Bd8#, which is how the game is usually given.[^s3][^s5]

## Typical patterns and pitfalls

- **Queen sacrifice first.** The Réti game shows the commonest pattern: a queen sacrifice drags the king onto a line, then a double check leaves it no time to escape. Chess.com's practice position repeats the idea with a queen sacrifice on a8 and a knight double check from b6.[^s5]
- **King hunts.** Several of Winter's historical games use a chain of double and discovered checks to march the king out of its shelter until a quiet mate follows: in Vane–Miles, Sydney 1897, the king is driven to h4 and mated by 8.Rh5, and in the Leonard brothers' odds game a knight double check is followed at once by 10.Nf5 mate.[^s2]
- **Defending.** Because only king moves are legal, the defender should look early at which flight squares are covered. Winter cites a 1988 game in which an annotator recommended a defence that allowed an immediate mate on the back rank after a double check, a reminder that the motif is easy to overlook.[^s2]
- **Not automatically winning.** If the king has a safe square and the attacker has sacrificed material to set up the check, the defender may survive; Speelman stresses that the threat comes from the forced king move, not from the check itself.[^s4]

## Connections

Double check is a **chess tactic** and the most forceful form of the **discovered attack**, on which it **depends**: without a piece unmasking a line there is almost never a second simultaneous check.[^s2][^s5] It **leads to** **checkmate** whenever the king's flight squares are covered, and it often follows a **sacrifice** within a longer **combination**, as in **Réti v Tartakower, Vienna 1910**, which **exemplifies** the motif.[^s3][^s5] Its legal basis is the definition of check in the **FIDE Laws of Chess**.[^s1] Like a **fork**, it creates two threats at once, but both threats are checks and they come from two different pieces.[^s4]

## Sources

[^s1]: FIDE, "FIDE Laws of Chess" (approved 2022, applied from 1 January 2023), Article 3.9. https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/ (accessed 2026-11-11)
[^s2]: Edward Winter, "Double Check in Chess", Chess Notes. https://www.chesshistory.com/winter/extra/doublecheck.html (accessed 2026-11-11)
[^s3]: Edward Winter, "Réti v Tartakower", Chess Notes. https://www.chesshistory.com/winter/extra/retitartakower.html (accessed 2026-11-11)
[^s4]: Jon Speelman, "The ultimate weapon", ChessBase News, 2 July 2023. https://en.chessbase.com/post/speelman-agony-197 (accessed 2026-11-11)
[^s5]: Chess.com, "Double Check" (Chess Terms). https://www.chess.com/fr/terms/double-check-chess (accessed 2026-11-11)
