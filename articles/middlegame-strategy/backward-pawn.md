---
id: kt:backward-pawn
type: PawnStructure
title: Backward pawn
aliases: [Backward pawns, Backwards pawn, Straggler pawn]
domain: middlegame-strategy
summary: >-
  A pawn that has fallen behind its neighbours on the adjacent files, so that no friendly pawn can
  protect it and it cannot advance safely because an enemy pawn controls the square in front of it;
  it is especially weak on a half-open file, and the square in front of it becomes an outpost.
fen: "2r2rk1/4bppp/p2p4/1p1Np3/4P3/8/PPP2PPP/3R1RK1 w - - 0 20"
status: current
volatile: false
verified: 2026-11-14
broader: [kt:pawn-structure]
related: [kt:weak-squares, kt:isolated-queens-pawn, kt:minority-attack, kt:sicilian-defence, kt:najdorf-variation, kt:dragon-variation, kt:wilhelm-steinitz, kt:francois-andre-danican-philidor]
relations:
  - {predicate: leadsTo, object: kt:outpost}
  - {predicate: contrastsWith, object: kt:isolated-queens-pawn}
  - {predicate: exemplifiedBy, object: kt:sveshnikov-variation}
sources:
  - id: s1
    title: "Chess: Development of theory"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/chess/Development-of-theory
    type: reference
    accessed: 2026-11-14
  - id: s2
    title: "Britannica: The Evolution of Chess Theory (Part 2)"
    publisher: Andrew Soltis, ChessBase News (republished from Encyclopaedia Britannica)
    url: https://en.chessbase.com/post/britannica-the-development-of-chess-theory-2
    type: publication
    accessed: 2026-11-14
  - id: s3
    title: "Backward Pawn"
    publisher: Chess.com (Chess Terms)
    url: https://www.chess.com/terms/backward-pawn-chess
    type: publication
    accessed: 2026-11-14
  - id: s4
    title: "The Winning Academy 32: The Hole"
    publisher: Jan Markos, ChessBase News
    url: https://en.chessbase.com/post/the-winning-academy-32-the-hole
    type: publication
    accessed: 2026-11-14
  - id: s5
    title: "The pawn outpost on d5 in the Dragon (ChessBase Magazine 231)"
    publisher: Mihail Marin, ChessBase
    url: https://en.chessbase.com/post/neu-chessbase-magazin-4
    type: publication
    accessed: 2026-11-14
  - id: s6
    title: "Elements of Positional Evaluation, 4th edition (excerpt)"
    publisher: Dan Heisman, Russell Enterprises
    url: https://shop.chess-tigers.de/cdn/shop/files/elements_excerpt.pdf
    type: book
    accessed: 2026-11-14
  - id: s7
    title: "Backward Pawn"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/Backward_Pawn
    type: community
    accessed: 2026-11-14
created: 2026-11-14
---

# Backward pawn

A backward pawn is a pawn that has been left behind by the pawns on the neighbouring files. Because those pawns have advanced past it or disappeared, no friendly pawn can ever defend it, and it cannot step forward without being captured by an enemy pawn that watches its next square.[^s3][^s1] Britannica gives the classical formulation attributed to Steinitz: a pawn on an open file, held back by an enemy pawn on an adjoining file and unable to be guarded by any other pawn.[^s1][^s2] Engine programmers use essentially the same test: the pawn has no pawn support and its stop square is controlled by an enemy "sentry" pawn.[^s7]

## History of the idea

Philidor already warned in the eighteenth century against pawns that are unprotected by another pawn and cannot safely advance.[^s1] Steinitz made such pawns part of a general theory of structural weaknesses: weaknesses are pawns that are hard to defend or squares that enemy pieces can occupy, and they become more serious as pieces are exchanged, so a better pawn structure is an advantage that survives into the endgame.[^s2][^s1] He also coined the term "hole" for a square that has lost its pawn protection, which is exactly what the square in front of a backward pawn becomes.[^s2]

## Why it is weak

- **A fixed target.** Since only pieces can defend it, the opponent can pile up attackers while the defender must tie pieces to its protection.[^s3]
- **The half-open file.** A backward pawn on a file with no enemy pawn is exposed to rooks and the queen along that file; Britannica's definition and engine heuristics both treat this as the aggravating case.[^s1][^s7]
- **The hole in front.** The square ahead of it can never be challenged by a pawn, so it is a natural outpost for an enemy piece, often a knight.[^s3][^s1]

## Compensation and the modern view

A backward pawn is not automatically bad. Boleslavsky's treatment of the Sicilian, in which Black plays ...d6 and ...e5, deliberately accepts a backward d-pawn and a hole on d5 in exchange for play on the c-file and pressure on White's e-pawn; this structure became standard in lines such as the Najdorf and Sveshnikov.[^s1][^s4] Markos argues that the hole only matters if the opponent has a piece that can actually reach and use it: in Shirov–Kramnik, Linares 2000, Black's pawns kept White's pieces away from d5, and Kramnik freed his game with the break ...d5.[^s4] Marin's survey of the reversed situation in the Dragon, where White's exd5 recapture leaves Black with a backward e7-pawn, likewise weighs that weakness against counterplay on the queenside and against White's own d5-pawn.[^s5]

## Plans and pitfalls

For the side playing against it, the recipe is to fix the pawn, occupy the square in front of it, and then attack it with heavy pieces on the file; exchanging the defender's active pieces makes the target easier to win.[^s3][^s2] For the owner, the standard remedies are to achieve the advance after all (the ...d5 break in the Sicilian structure), to exchange off the enemy piece that wants the hole, or to generate enough activity elsewhere that the pawn never becomes the focus.[^s4] A common club-level error is to overrate the weakness: Heisman notes that players often refuse to win material because the capture would leave them with a backward, isolated or doubled pawn, whereas an extra pawn is usually worth more than such a static flaw.[^s6]

## Example position

In the illustrative diagram, Black's d6-pawn is backward: the c-pawn has gone, the e-pawn has advanced to e5, and the d-file is half-open. White's knight sits unchallengeable on d5 and the rook on d1 already presses on d6, which must be defended by the bishop on e7. White's natural plan is to add pressure on the d-file while the knight blocks the pawn; Black, in Markos's terms, needs a "key" of his own, such as a piece that can challenge d5 or the chance to prepare ...d5.[^s3][^s4]

## Connections

The backward pawn is a type of **pawn structure** and a special case of **weak squares**, since the square in front of it is the classic **outpost**.[^s1][^s3] It **contrasts with the isolated queen's pawn**, which has no neighbours at all, whereas a backward pawn still has a neighbour that has run ahead of it.[^s2] A **minority attack** is one way of creating one, and the ...d6/...e5 structures of the **Sicilian Defence**, including the **Najdorf** and the **Sveshnikov**, accept one deliberately; the **Dragon** can saddle Black with a backward e-pawn.[^s1][^s4][^s5] The idea goes back to **Philidor** and was systematised by **Steinitz**.[^s1][^s2]

## Sources
[^s1]: Encyclopaedia Britannica, "Chess: Development of theory". https://www.britannica.com/topic/chess/Development-of-theory (accessed 2026-11-14)
[^s2]: A. Soltis, "Britannica: The Evolution of Chess Theory (Part 2)", ChessBase News. https://en.chessbase.com/post/britannica-the-development-of-chess-theory-2 (accessed 2026-11-14)
[^s3]: Chess.com, "Backward Pawn", Chess Terms. https://www.chess.com/terms/backward-pawn-chess (accessed 2026-11-14)
[^s4]: J. Markos, "The Winning Academy 32: The Hole", ChessBase News. https://en.chessbase.com/post/the-winning-academy-32-the-hole (accessed 2026-11-14)
[^s5]: M. Marin, "The pawn outpost on d5 in the Dragon", ChessBase Magazine 231. https://en.chessbase.com/post/neu-chessbase-magazin-4 (accessed 2026-11-14)
[^s6]: D. Heisman, *Elements of Positional Evaluation*, 4th ed., Russell Enterprises, excerpt (section 5.2). https://shop.chess-tigers.de/cdn/shop/files/elements_excerpt.pdf (accessed 2026-11-14)
[^s7]: Chess Programming Wiki, "Backward Pawn". https://www.chessprogramming.org/Backward_Pawn (accessed 2026-11-14)
