---
id: kt:smothered-mate
type: MatingPattern
title: Smothered mate
aliases: [Smothered checkmate, Smother mate, Philidor's legacy, Philidor's Legacy]
domain: tactics
summary: >-
  A checkmate, almost always given by a knight, in which the mated king cannot move because every
  neighbouring square is occupied by its own pieces or pawns; its best-known form, Philidor's legacy,
  ends with a queen sacrifice that forces a rook to block the king's last escape square.
fen: "r4r1k/6pp/7N/3Q4/8/8/5PPP/6K1 w - - 0 1"
status: current
volatile: false
verified: 2026-11-13
broader: [kt:checkmate, kt:chess-tactics]
related: [kt:back-rank-mate, kt:sacrifice, kt:combination, kt:pin, kt:decoy]
relations:
  - {predicate: contrastsWith, object: kt:back-rank-mate}
  - {predicate: usesTechnique, object: kt:decoy}
  - {predicate: usesTechnique, object: kt:sacrifice}
  - {predicate: namedAfter, object: kt:francois-andre-danican-philidor}
  - {predicate: developedBy, object: kt:luis-ramirez-de-lucena}
sources:
  - id: s1
    title: "The Smothered Mate"
    publisher: Edward Winter, Chess Notes
    url: https://www.chesshistory.com/winter/extra/smothered.html
    type: reference
    accessed: 2026-11-13
  - id: s2
    title: "François-André Danican Philidor"
    publisher: Edward Winter, Chess Notes
    url: https://chesshistory.com/winter/extra/philidor1.html
    type: reference
    accessed: 2026-11-13
  - id: s3
    title: "Other Classic Mating Ideas: The Smothered Mate, Figures 6.2.14.1, 6.2.14.4 and 6.2.14.6 (Predator at the Chessboard)"
    publisher: Ward Farnsworth, chesstactics.org
    url: https://www.chesstactics.org/mating-patterns/other-classic-mating-ideas/the-smothered-mate/6_2_14_6.html
    type: publication
    accessed: 2026-11-13
  - id: s4
    title: "Smothered Mate (Chess Terms)"
    publisher: ChessKid (Chess.com)
    url: https://www.chesskid.com/learn/terms/smothered-mate
    type: publication
    accessed: 2026-11-13
  - id: s5
    title: "Study of the month: Don't bother me with smother mate"
    publisher: ChessBase News (Siegfried Hornecker)
    url: https://en.chessbase.com/post/study-of-the-month-don-t-bother-me-with-smother-mate
    type: publication
    accessed: 2026-11-13
  - id: s6
    title: "9. Smothered mate (tactics course)"
    publisher: ChessBase
    url: https://learn.chessbase.com/en/page/smothered-mate
    type: publication
    accessed: 2026-11-13
created: 2026-11-13
---

# Smothered mate

A smothered mate is a checkmate in which the king has no move because it is completely surrounded by its own men, so that a single check it cannot meet is enough to end the game.[^s4] The checking piece is nearly always a knight, for a simple reason: a knight's check jumps over the surrounding pieces and cannot be blocked, so the only defences are to capture the knight or move the king, and a smothered king can do neither.[^s4][^s5] ChessKid lists the usual ingredients: the king on or near the edge, its flight squares filled by its own pieces, potential defenders pinned or otherwise unable to help, and an enemy knight within reach.[^s4]

## Philidor's legacy

The most famous form is a forced sequence against a king castled short. A queen and knight drive the king into the corner with knight checks (often including a double check from h6), the queen is then sacrificed on g8 next to the king, the rook has to take it because the knight guards g8, and the knight returns to f7 to give mate against a king now walled in by rook and pawns.[^s3] Farnsworth's *Predator at the Chessboard* gives the complete sequence 1.Qe6+ Kh8 2.Nf7+ Kg8 3.Nh6++ Kh8 4.Qg8+ Rxg8 5.Nf7#, stresses the two motifs (the queen sacrifice that forces a self-block on g8, and the knight that both herds the king and covers g8), and credits the idea to Lucena's book of 1497.[^s3] The English name is much later: Edward Winter records that the term "Philidor's legacy" first appeared in print in Thomas Pruen's *An Introduction to the History and Study of Chess* (Cheltenham, 1804).[^s2] It therefore honours Philidor's reputation rather than recording him as the discoverer.

The mirror image against White's king is equally common. Farnsworth shows Black playing ...Qg1+, with the queen covered by a bishop on the a7–g1 diagonal so that the king cannot take it; after Rxg1 the knight mates on f2.[^s3] ChessBase's beginner course reduces the recognition cue to two items: a king without escape squares and a knight that can reach f7 (or f2).[^s6]

## How it arises and how to avoid it

Because the defender must cooperate by filling his own king's squares, the pattern usually needs force: a queen sacrifice that a rook must capture, or a pin that freezes the one piece able to take the knight.[^s4] It also occurs in opening traps when a player develops pieces next to an uncastled king without checking the enemy knight's jumps.[^s4] ChessKid's defensive advice is the same as for other mates on a cramped king: make luft (a pawn move such as ...h6 that gives the king air), keep the knight's landing square (typically f7 or f2) covered, and look at the opponent's threats before developing.[^s4]

Winter notes a refinement: smothering by pieces rather than pawns is rarer still, and away from the corner the attacker may need help from an advanced pawn to seal the last flight square.[^s1] He also queries an annotator's description of one club-game smothered mate as "unique", a reminder of how often the pattern recurs.[^s1]

## Example

In the diagram position (White to move), the knight on h6 guards g8, so **1.Qg8+** can only be met by **1...Rxg8**, and **2.Nf7#** is mate: the king on h8 is boxed in by its rook on g8 and pawns on g7 and h7, and nothing can capture the knight.[^s3] This is the closing stage of Philidor's legacy.

A full game ending in the same pattern, with Black mating on f2, is the Albin Counter-Gambit Müller v Crane, London, 22 October 1906, which Winter quotes from the *British Chess Magazine* of January 1907.[^s1] Black opened the h-file with ...h5–h4, sacrificed both rooks on h2 to remove the defenders and pull the queen to h2, and the knight on g4 dropped into f2.[^s1]

```pgn
[Event "London"]
[Date "1906.10.22"]
[White "Müller"]
[Black "Crane"]
[Result "0-1"]

1. d4 d5 2. c4 e5 3. dxe5 d4 4. a3 c5 5. f4 Nc6 6. Nf3 Bf5 7. g3 Be7 8. Bg2 h5
9. O-O h4 10. Qe1 hxg3 11. Qxg3 Rh6 12. Kh1 Rg6 13. Qe1 Qd7 14. Rg1 O-O-O
15. Nbd2 Nh6 16. Nf1 Rh8 17. Bd2 Ng4 18. e4 Bxe4 19. Ng5 Rgh6 20. Qg3 Rxh2+
21. Nxh2 Rxh2+ 22. Qxh2 Nf2# 0-1
```

Winter collects other cases, including an announced mate by Steinitz in a New York simultaneous of 27 November 1884 (16.Qe6+ Kb8 17.Nd7+ Kc8 18.Nxb6+ Kb8 19.Qc8+ Rxc8 20.Nd7#), which Steinitz himself called an ordinary version of the smothered mate.[^s1]

## In compositions

The theme is old enough to have attracted composers from the beginning. In a ChessBase "Study of the month" column, Siegfried Hornecker traces it back to the beginnings of modern chess, presents a 2016 study tourney whose set theme was a smothered mate by a promoted knight, and shows a Meyer–Bláthy problem from the *British Chess Magazine* of 1890 in which two knights chase the king around the board before mating it.[^s5]

## Connections

The smothered mate is a named pattern of **checkmate** and one of the standard families of **chess tactics**.[^s4] It **contrasts with** the **back-rank mate**: both exploit a king hemmed in by its own men, but the back-rank mate is given by a rook or queen along a line, the smothered mate by a knight jump.[^s4] Philidor's legacy **uses** a queen **sacrifice** as a **decoy**, forcing a rook onto the king's last free square, so it is a classic **combination**; the **pin** is the other common way to stop the knight being captured.[^s3][^s4] The name Philidor's legacy is **named after** **François-André Danican Philidor**, although it is first recorded in print only in 1804, while Farnsworth credits the idea to **Luis Ramírez de Lucena** in 1497.[^s2][^s3]

## Sources

[^s1]: Edward Winter, "The Smothered Mate", Chess Notes. https://www.chesshistory.com/winter/extra/smothered.html (accessed 2026-11-13)
[^s2]: Edward Winter, "François-André Danican Philidor", Chess Notes (C.N. 12189 on the term "Philidor's legacy"). https://chesshistory.com/winter/extra/philidor1.html (accessed 2026-11-13)
[^s3]: Ward Farnsworth, *Predator at the Chessboard*, "Other Classic Mating Ideas: The Smothered Mate", Figures 6.2.14.1, 6.2.14.4 and 6.2.14.6. https://www.chesstactics.org/mating-patterns/other-classic-mating-ideas/the-smothered-mate/6_2_14_6.html (accessed 2026-11-13)
[^s4]: ChessKid, "Smothered Mate" (Chess Terms). https://www.chesskid.com/learn/terms/smothered-mate (accessed 2026-11-13)
[^s5]: Siegfried Hornecker, "Study of the month: Don't bother me with smother mate", ChessBase News. https://en.chessbase.com/post/study-of-the-month-don-t-bother-me-with-smother-mate (accessed 2026-11-13)
[^s6]: ChessBase, tactics course, "9. Smothered mate". https://learn.chessbase.com/en/page/smothered-mate (accessed 2026-11-13)
