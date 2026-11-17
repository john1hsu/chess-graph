---
id: kt:windmill
type: TacticalMotif
title: Windmill
aliases: [Seesaw, See-saw, Zwickmühle, Windmill attack]
domain: tactics
summary: >-
  A repeating combination in which a rook (or other piece) shuttles between two squares next to the
  enemy king, alternately giving check and uncovering a discovered check from a supporting piece,
  so that it can capture material on every cycle while the king is unable to escape.
fen: "r3rnk1/pb3pp1/3pp2p/1q4BQ/1P1P4/4N1R1/P4PPP/4R1K1 w - - 4 25"
status: current
volatile: false
verified: 2026-11-17
broader: [kt:chess-tactics]
related: [kt:discovered-attack, kt:battery, kt:double-check, kt:combination, kt:sacrifice, kt:rook-on-the-seventh-rank]
relations:
  - {predicate: usesTechnique, object: kt:discovered-attack}
  - {predicate: dependsOn, object: kt:battery}
  - {predicate: exemplifiedBy, object: kt:torre-versus-lasker-moscow-1925}
  - {predicate: enables, object: kt:material-advantage}
sources:
  - id: s1
    title: "The Chess Seesaw/Windmill"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://www.chesshistory.com/winter/extra/seesaw.html
    type: reference
    accessed: 2026-11-17
  - id: s2
    title: "Carlos Torre"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/torre.html
    type: reference
    accessed: 2026-11-17
  - id: s3
    title: "The windmill (Predator at the Chessboard: Rook discoveries)"
    publisher: Ward Farnsworth, chesstactics.org
    url: https://www.chesstactics.org/the-discovered-attack/rook-discoveries/the-windmill/3_2_6_4.html
    type: publication
    accessed: 2026-11-17
  - id: s4
    title: "Torre's Windmill Attack"
    publisher: ChessKid.com
    url: https://www.chesskid.com/learn/articles/torres-windmill-attack
    type: publication
    accessed: 2026-11-17
  - id: s5
    title: "Torre Plays the Torre at Moscow 1925"
    publisher: Michael Goeller, The Kenilworthian
    url: https://kenilworthian.blogspot.com/2005/09/torre-plays-torre-at-moscow-1925.html
    type: community
    accessed: 2026-11-17
  - id: s6
    title: "Carlos Torre Repetto (player page)"
    publisher: chessgames.com
    url: https://chessgames.com/player/carlos_torre-repetto.html?kpage=2
    type: database
    accessed: 2026-11-17
created: 2026-11-17
---

# Windmill

The windmill, older English name **seesaw**, is a combination of repeated checks in which one piece swings back and forth beside the enemy king. On one move it gives check itself; on the next it steps away and uncovers a check from a second piece standing behind it, usually a bishop. Because every step is check, the defender never gets a free move, and the swinging piece can pick off a new target each time it leaves the checking square.[^s3][^s4] Ward Farnsworth describes the typical case as a rook backed by a bishop against a king that has only a couple of squares to shuttle between.[^s3]

## Names and history

Edward Winter's survey shows that "see-saw" is the older chess term: the *Chess Player's Chronicle* used it in a note to a Bird–Williams game in 1849, and Steinitz later wrote of a so-called seesaw of checks when annotating his 1886 loss to James McConnell.[^s1] Nimzowitsch used the German *Zwickmühle*, which the English translation of *My System* rendered as "seesaw"; Winter notes that the German word refers to the double mill of Nine Men's Morris rather than to a windmill, and that the date at which "windmill" entered chess writing is still an open question.[^s1] His collection of examples runs from Zukertort–N.N., London 1879, through a 1902 telegraph game between Singapore and Hong Kong and Chaurang–Moore, The Hague 1957, to games played in the 21st century.[^s1]

## How it works

Three ingredients are needed:

- **A battery aimed at the king.** A bishop (sometimes a rook or queen) sits behind the moving piece on the line to the king, so each step off that line is a discovered check.[^s3]
- **A king with almost no room.** The king must have only one or two squares, typically h8 and g8 behind its own pawns, so it cannot break the rhythm by walking out of the net.[^s3][^s4]
- **Loose targets along the swinging piece's path.** On a rank such as the seventh, the rook can take a pawn or piece on each discovered check and then return to the checking square.[^s3]

Two practical points follow. First, repetition of position is no danger to the attacker, because the material on the board changes every cycle.[^s4] Second, the attacker should choose the order of captures carefully and stop the mill when the job is done: in the classic example below, White did not bother with the a7-pawn, because removing it would have opened a file for Black's rook.[^s4]

## Example: Torre–Lasker, Moscow 1925

The best-known windmill came in Carlos Torre's win over Emanuel Lasker at the Moscow international tournament of 1925.[^s2][^s6] In the diagram position, White's bishop on g5 is pinned against the queen on h5 by Black's queen on b5, and a rook stands ready on g3.[^s4] Torre played **25.Bf6!**, leaving his queen to be taken while uncovering an attack on Black's queen and lining up rook and bishop against g7.[^s3][^s4] After **25...Qxh5 26.Rxg7+ Kh8** the mill turned: **27.Rxf7+** (discovered check) **Kg8 28.Rg7+ Kh8 29.Rxb7+ Kg8 30.Rg7+ Kh8 31.Rg5+ Kh7 32.Rxh5**, regaining the queen with two pawns and the b7-bishop already gone.[^s3][^s5] White later converted the extra pawns, and Lasker resigned four pawns down at move 43.[^s4][^s5] Winter records that W. Ritson Morry later argued that Chaurang–Moore had produced an even finer seesaw, which shows how far the Torre game became the benchmark.[^s1][^s2]

```pgn
[Event "Moscow"]
[Site "Moscow"]
[Date "1925.??.??"]
[Round "12"]
[White "Torre, Carlos"]
[Black "Lasker, Emanuel"]
[Result "1-0"]

1. d4 Nf6 2. Nf3 e6 3. Bg5 c5 4. e3 cxd4 5. exd4 Be7 6. Nbd2 d6 7. c3 Nbd7
8. Bd3 b6 9. Nc4 Bb7 10. Qe2 Qc7 11. O-O O-O 12. Rfe1 Rfe8 13. Rad1 Nf8
14. Bc1 Nd5 15. Ng5 b5 16. Na3 b4 17. cxb4 Nxb4 18. Qh5 Bxg5 19. Bxg5 Nxd3
20. Rxd3 Qa5 21. b4 Qf5 22. Rg3 h6 23. Nc4 Qd5 24. Ne3 Qb5 25. Bf6 Qxh5
26. Rxg7+ Kh8 27. Rxf7+ Kg8 28. Rg7+ Kh8 29. Rxb7+ Kg8 30. Rg7+ Kh8 31. Rg5+ Kh7
32. Rxh5 Kg6 33. Rh3 Kxf6 34. Rxh6+ Kg5 35. Rh3 Reb8 36. Rg3+ Kf6 37. Rf3+ Kg6
38. a3 a5 39. bxa5 Rxa5 40. Nc4 Rd5 41. Rf4 Nd7 42. Rxe6+ Kg5 43. g3 1-0
```

## Pitfalls

- **For the defender:** a fianchetto or castled king with a bishop or rook bearing down on g7 and an enemy rook able to reach the seventh rank is the warning sign; breaking the battery, or giving the king a flight square, comes before grabbing material.[^s3][^s4]
- **For the attacker:** each check must really be forced. If the king can step off the shuttle squares, or if the defender can interpose with tempo, the mill stops and the attacker may be left with a sacrificed queen and nothing to show for it.[^s3]

## Connections

The windmill is a pattern within **chess tactics** that **uses** the **discovered attack** over and over, and it **depends on** a **battery** of two line pieces against the king.[^s1][^s3] The swinging rook usually works along the seventh rank, so it is a sharp tactical cousin of the strategic **rook on the seventh rank**. It is almost always launched by a **sacrifice**, as Torre's queen offer shows, and is a classic finish of a **combination**; when the moving piece checks at the same moment as the unmasked one, it overlaps with **double check**.[^s3][^s4] Each turn of the mill wins something, so the motif **enables** a decisive **material advantage**, and it is **exemplified by** **Torre versus Lasker, Moscow 1925**.[^s2][^s5][^s6]

## Sources

[^s1]: Edward Winter, "The Chess Seesaw/Windmill", Chess Notes. https://www.chesshistory.com/winter/extra/seesaw.html (accessed 2026-11-17)
[^s2]: Edward Winter, "Carlos Torre", Chess Notes. https://chesshistory.com/winter/extra/torre.html (accessed 2026-11-17)
[^s3]: Ward Farnsworth, "The windmill", Predator at the Chessboard (chesstactics.org). https://www.chesstactics.org/the-discovered-attack/rook-discoveries/the-windmill/3_2_6_4.html (accessed 2026-11-17)
[^s4]: ChessKid.com, "Torre's Windmill Attack". https://www.chesskid.com/learn/articles/torres-windmill-attack (accessed 2026-11-17)
[^s5]: Michael Goeller, "Torre Plays the Torre at Moscow 1925", The Kenilworthian. https://kenilworthian.blogspot.com/2005/09/torre-plays-torre-at-moscow-1925.html (accessed 2026-11-17)
[^s6]: chessgames.com, "Carlos Torre Repetto". https://chessgames.com/player/carlos_torre-repetto.html?kpage=2 (accessed 2026-11-17)
