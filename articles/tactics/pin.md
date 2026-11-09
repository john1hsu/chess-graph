---
id: kt:pin
type: TacticalMotif
title: Pin
aliases: [Absolute pin, Relative pin, Pinned piece, Cross pin, Half-pin]
domain: tactics
summary: >-
  A tactic in which a bishop, rook or queen attacks an enemy piece that cannot move off the line
  without exposing a more valuable piece, usually the king or queen, standing behind it.
fen: "4k3/pp3ppp/2n5/1B6/3P4/8/PPP2PPP/4K3 w - - 0 1"
status: current
volatile: false
verified: 2026-11-09
broader: [kt:chess-tactics]
related: [kt:skewer, kt:fork, kt:discovered-attack, kt:combination, kt:aron-nimzowitsch]
relations:
  - {predicate: contrastsWith, object: kt:skewer}
  - {predicate: enables, object: kt:material-advantage}
  - {predicate: influencedBy, object: kt:aron-nimzowitsch}
sources:
  - id: s1
    title: "The Pin (Chess Skills leaflet)"
    publisher: English Chess Federation
    url: https://www.englishchess.org.uk/wp-content/uploads/2010/01/pin.pdf
    type: governing-body
    accessed: 2026-11-09
  - id: s2
    title: "The Chess Pin"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://www.chesshistory.com/winter/extra/pin.html
    type: reference
    accessed: 2026-11-09
  - id: s3
    title: "Simple Relative Pins (Predator at the Chessboard)"
    publisher: Ward Farnsworth, chesstactics.org
    url: https://www.chesstactics.org/the-pin-and-the-skewer/the-relative-pin/simple-relative-pins/4_4_1_1.html
    type: publication
    accessed: 2026-11-09
  - id: s4
    title: "Tactics by Paul Littlewood – The Pin"
    publisher: English Chess Federation (ChessMoves, via Chess.com)
    url: https://www.chess.com/blog/EnglishChessFederati/tactics-by-paul-littlewood-the-pin
    type: publication
    accessed: 2026-11-09
  - id: s5
    title: "Pin (Chess Terms)"
    publisher: Chess.com
    url: https://www.chess.com/terms/pin-chess
    type: publication
    accessed: 2026-11-09
created: 2026-11-09
---

# Pin

A pin is an attack along a line on an enemy piece that cannot move without exposing a second, usually more valuable piece behind it.[^s1] Only the line pieces can pin: a bishop along a diagonal, a rook along a rank or file, and a queen along either; a knight jumps rather than slides, so it can never pin.[^s3][^s4] The pinned piece is not lost at once, but it is frozen, and the side that pinned it can then attack it again or exploit the fact that it no longer really defends anything.[^s1][^s5]

## Absolute and relative pins

The key distinction is what stands behind the pinned piece. In an **absolute pin** that piece is the king, so moving the pinned piece would expose the king to check and is illegal under the rules; the piece literally cannot move.[^s5][^s4] In a **relative pin** the piece behind is something else of value, typically the queen or a rook. Moving the pinned piece is legal but costs material.[^s5][^s3] Farnsworth notes that relative pins are harder to spot than absolute ones, because there is no simple scan comparable to checking the lines leading to the king; he suggests looking for enemy pieces that share a line and asking what lies behind each.[^s3] Because a relative pin is not binding, the pinned piece can sometimes move anyway with a bigger threat. Littlewood gives a position in which a knight pinned to the queen captures on e5, the opponent takes the queen, and the knight's side mates with Bxf7+ and Nd5.[^s4]

## How pins win material

The ECF leaflet sorts pin tactics into a few recurring patterns.[^s1]

- **Pin and win.** A rook or bishop pins a queen to the king, and the queen is lost for the pinning piece.[^s1]
- **Attack the pinned piece.** Once a piece is pinned, a cheaper attacker, often a pawn, hits it again and it cannot step away.[^s1]
- **Capture because of a pin.** A piece that is pinned cannot recapture, so a capture on a square it appears to guard simply wins material, or even mates, as when a pinned g-pawn cannot take on h3.[^s1]

Littlewood adds the **cross pin**, in which a piece already pinned on one line is pinned again on a second line, often with decisive effect, and cites Shirov–Bareev (Novgorod 1994), where a queen caught between two pins was lost.[^s4]

## Example

In the diagram position (White to move), the bishop on b5 pins the black knight on c6 to the king on e8. **1.d5** attacks the knight with a pawn. The knight cannot move, and even if the black king steps off the diagonal, **2.dxc6** wins a piece for a pawn. This is the second ECF pattern: a pinned piece attacked by a pawn.[^s1]

## Breaking a pin

Chess.com lists four standard remedies: capture the pinning piece, interpose another piece on the line, move the valuable piece behind so the pin becomes harmless, or set up a stronger pin of your own against the pinner.[^s5] The writer C. J. S. Purdy summed up the defender's attitude with the slogan "always unpin", which Winter dates to his 1967 notes on Fischer–Stein.[^s2] The pitfalls run both ways: a player who pins must check that the pinned piece cannot break free with a stronger threat, as in Littlewood's relative-pin example, while a defender should avoid lining up the king or queen behind a piece on a line the opponent controls.[^s4][^s3]

## Name and theory

The term is old. Winter's earliest examples come from George Walker, who wrote "pin Kt." in an 1833 treatise and by 1844 used the word as a conventional term for a bishop pinning a knight.[^s2] Related terms followed: the problem composer Comins Mansfield is credited with "half-pin" around 1915, and Fred Reinfeld's quip that the pin is mightier than the sword appears from 1948.[^s2] Aron Nimzowitsch treated the pin as a positional weapon rather than a trick; in *My System* he wrote that "the defensive power of a pinned piece is only imaginary".[^s2][^s4]

## Connections

The pin belongs to the family of **chess tactics** and is a common ingredient of a **combination**.[^s4] It **contrasts with** the **skewer**, its mirror image: in a skewer the more valuable piece stands in front and must move, exposing the one behind.[^s5][^s3] Like the **fork** and the **discovered attack**, a successful pin usually **enables** a **material advantage**.[^s1] Its treatment as a strategic restraining device was **influenced by** **Aron Nimzowitsch**.[^s2][^s4]

## Sources

[^s1]: English Chess Federation, "The Pin" (Chess Skills leaflet). https://www.englishchess.org.uk/wp-content/uploads/2010/01/pin.pdf (accessed 2026-11-09)
[^s2]: Edward Winter, "The Chess Pin", Chess Notes. https://www.chesshistory.com/winter/extra/pin.html (accessed 2026-11-09)
[^s3]: Ward Farnsworth, *Predator at the Chessboard*, "Simple Relative Pins". https://www.chesstactics.org/the-pin-and-the-skewer/the-relative-pin/simple-relative-pins/4_4_1_1.html (accessed 2026-11-09)
[^s4]: Paul Littlewood, "Tactics by Paul Littlewood – The Pin", English Chess Federation *ChessMoves* (January 2022), via Chess.com. https://www.chess.com/blog/EnglishChessFederati/tactics-by-paul-littlewood-the-pin (accessed 2026-11-09)
[^s5]: Chess.com, "Pin" (Chess Terms). https://www.chess.com/terms/pin-chess (accessed 2026-11-09)
