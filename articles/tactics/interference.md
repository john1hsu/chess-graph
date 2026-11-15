---
id: kt:interference
type: TacticalMotif
title: Interference
aliases: [Interference tactic, Line interference, Line interruption, Blocking the guard]
domain: tactics
summary: >-
  A tactic in which a piece is placed, often as a sacrifice or with check, on the line between an enemy
  long-range piece and the piece or square it defends, cutting the defence so that material or mate can be won.
fen: "k3q3/pp6/6R1/2np4/8/6K1/PPQ5/8 b - - 0 1"
status: current
volatile: false
verified: 2026-11-15
broader: [kt:chess-tactics, kt:removing-the-guard]
related: [kt:deflection, kt:overloading, kt:combination, kt:chess-problems, kt:pin]
relations:
  - {predicate: contrastsWith, object: kt:deflection}
  - {predicate: enables, object: kt:material-advantage}
  - {predicate: exemplifiedBy, object: kt:novotny-theme}
  - {predicate: exemplifiedBy, object: kt:grimshaw-theme}
sources:
  - id: s1
    title: "Blocking the Guard (Interference): Interference to Loosen a Piece"
    publisher: Ward Farnsworth, Predator at the Chessboard
    url: https://www.chesstactics.org/removing-the-guard/blocking-the-guard_interference/interference-to-loosen-a-piece/5_4_1_1.html
    type: book
    accessed: 2026-11-15
  - id: s2
    title: "Tactical Training (sample: contents and introduction)"
    publisher: Cyrus Lakdawala, Everyman Chess (via New In Chess)
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/8416.pdf
    type: book
    accessed: 2026-11-15
  - id: s3
    title: "Understanding Chess Tactics (excerpt)"
    publisher: Martin Weteschnik, Quality Chess
    url: https://qualitychess.co.uk/wp-content/uploads/2024/02/UnderstandingChessTactics-excerpt.pdf
    type: book
    accessed: 2026-11-15
  - id: s4
    title: "Interference (Chess Terms)"
    publisher: Chess.com
    url: https://www.chess.com/terms/interference-chess
    type: publication
    accessed: 2026-11-15
  - id: s5
    title: "Problem chess: Forgive me interfering, won't you?"
    publisher: Steve Giddins, ChessBase
    url: https://en.chessbase.com/post/problem-che-forgive-me-interfering-won-t-you-
    type: publication
    accessed: 2026-11-15
  - id: s6
    title: "Patterns of interference"
    publisher: Jon Speelman, ChessBase
    url: https://en.chessbase.com/post/speelman-agony-183
    type: publication
    accessed: 2026-11-15
created: 2026-11-15
---

# Interference

Interference is a tactic that cuts a line of defence. A piece is put on the square between an enemy long-range piece (a queen, rook or bishop) and the piece or square it protects, so that the protection stops working and the target can be captured or a mate delivered.[^s1][^s4] Chess.com also calls it obstruction, and Cyrus Lakdawala's *Tactical Training* gives it a chapter under the double name "Interference/Obstruction".[^s2][^s4] Because only line pieces defend at a distance, Ward Farnsworth sums the motif up as being entirely about lines.[^s1]

## How it works

Farnsworth files interference as one of the ways of **removing the guard**: next to capturing, distracting and attacking the guard, you can simply block it.[^s1] There are two ways to put a blocker on the line. You can play one of your own pieces there, or you can make a threat that forces your opponent to block the line with one of theirs.[^s1] Farnsworth notes that several conditions have to come together, which makes interference rarer than the other ways of removing a guard.[^s1] In practice the defender must be a line piece, a blocking square must be reachable, and the blocker must survive long enough for the follow-up.

The interfering move is nearly always forcing. Farnsworth's model example turns on a knight check. Without the check, the defender would get a free move to rescue the loose piece, and the tactic would fail.[^s1] Martin Weteschnik's *Understanding Chess Tactics* treats the same idea as part of the fight over lines. Its chapter on opening and closing lines urges the reader to cut enemy pieces off from their colleagues. In Witt–Hoellwarth (Germany 2004) it labels 1.Re7 as "line interruption": after 1...Bxe7 2.Qxf7+ Kh8 3.Rxe7 Qxe7 4.Qxe7, White wins.[^s3]

## Example position

The diagram position was constructed for this article on the pattern of Farnsworth's model example (Black to move).[^s1] Black's queen on e8 attacks the rook on g6, but White's queen on c2 guards it along the c2–g6 diagonal. 1...Ne4+! plants a knight on that diagonal with check. The d5-pawn protects the knight, so 2.Qxe4 dxe4 would just lose the queen for a knight. White has to move the king, for example 2.Kf4, and after 2...Qxg6 the rook is gone. This is the same three-part mechanism Farnsworth describes: a blocker on the line, protected and giving check.[^s1]

## Typical forms

- **Loosening a piece.** Interference cuts the guard of a piece that is already under attack, as in the example.[^s1]
- **Loosening a mating square.** Farnsworth gives separate sections to interference that cuts the guard of a mating square, interference on the penultimate rank, and interference that forms part of a double threat.[^s1]
- **Interference with a threat.** In Jakovenko–Nepomniachtchi (Russian Team Championship 2011), Chess.com notes that 1.Be6 both threatens mate on g8 and blocks the defence of the bishop on e7.[^s4]
- **Interference in problems.** Composers have built whole themes on it. A **Grimshaw** is a mutual interference between two black pieces, classically a rook and a bishop, that cross on one square. A **Novotny** sacrifices a piece on the crossing square, so that whichever of two defenders captures it blocks the other.[^s5] Jon Speelman notes that the Novotny also turns up over the board. He was prompted by a "super-Novotny" that Vasyl Ivanchuk played against Jorden van Foreest; Van Foreest recovered and went on to win.[^s6]

## Pitfalls and practical advice

- **Check the blocker's safety.** If the interfering piece can simply be captured, the line opens again and the tactic fails. Farnsworth's model works only because a pawn protects the knight.[^s1]
- **Use a forcing move.** A quiet interference gives the opponent time to move the attacked piece; a check or a bigger threat takes that time away.[^s1]
- **Look for it in defence too.** Lakdawala labels moves such as a king step that blocks a pin as interference, showing that the same geometry helps the defender.[^s2]
- **Don't confuse it with its neighbours.** Lakdawala groups interference with decoy and removal of the guard, calling them nearly synonymous in their geometry.[^s2] Speelman notes that some Novotny-like sacrifices are really deflections, which drag a defender off its square.[^s6]

## Connections

Interference is one of the **chess tactics** and one way of **removing the guard**, alongside **overloading** and **deflection**.[^s1][^s2] It **contrasts with** deflection: a deflection moves the defender away, while an interference leaves the defender where it is and blocks its line.[^s1][^s6] It is a common link in a **combination**, usually paying off in a **material advantage**.[^s1][^s3] It is related to the **pin**, since both depend on line pieces, and Lakdawala shows interference used against pins.[^s2] In **chess problems** it is **exemplified by** the **Novotny** and **Grimshaw** themes.[^s5][^s6]

## Sources

[^s1]: Ward Farnsworth, *Predator at the Chessboard*, section 5.4 "Blocking the Guard (Interference)". https://www.chesstactics.org/removing-the-guard/blocking-the-guard_interference/interference-to-loosen-a-piece/5_4_1_1.html (accessed 2026-11-15)
[^s2]: Cyrus Lakdawala, *Tactical Training*, Everyman Chess, sample pages. https://www.newinchess.com/media/wysiwyg/product_pdf/8416.pdf (accessed 2026-11-15)
[^s3]: Martin Weteschnik, *Understanding Chess Tactics*, Quality Chess, excerpt. https://qualitychess.co.uk/wp-content/uploads/2024/02/UnderstandingChessTactics-excerpt.pdf (accessed 2026-11-15)
[^s4]: Chess.com, "Interference" (Chess Terms). https://www.chess.com/terms/interference-chess (accessed 2026-11-15)
[^s5]: Steve Giddins, "Problem chess: Forgive me interfering, won't you?", ChessBase, 31 July 2011. https://en.chessbase.com/post/problem-che-forgive-me-interfering-won-t-you- (accessed 2026-11-15)
[^s6]: Jon Speelman, "Patterns of interference", ChessBase, 4 December 2022. https://en.chessbase.com/post/speelman-agony-183 (accessed 2026-11-15)
