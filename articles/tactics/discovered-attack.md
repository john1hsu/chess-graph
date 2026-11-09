---
id: kt:discovered-attack
type: TacticalMotif
title: Discovered attack
aliases: [Discovery, Discovered check]
domain: tactics
summary: >-
  A tactic in which one piece moves off a line and uncovers an attack by a queen, rook or bishop
  standing behind it, so that the moving piece and the unmasked piece can create two threats at once.
fen: "4k3/q4ppp/8/8/8/4B3/5PPP/4R1K1 w - - 0 1"
status: current
volatile: false
verified: 2026-11-09
broader: [kt:chess-tactics]
related: [kt:double-check, kt:pin, kt:skewer, kt:fork, kt:combination, kt:zwischenzug]
relations:
  - {predicate: contrastsWith, object: kt:fork}
  - {predicate: enables, object: kt:material-advantage}
  - {predicate: leadsTo, object: kt:double-check}
sources:
  - id: s1
    title: "Discovered Attacks (Chess Skills leaflet)"
    publisher: English Chess Federation
    url: https://www.englishchess.org.uk/wp-content/uploads/2010/01/discoveredattacks.pdf
    type: governing-body
    accessed: 2026-11-09
  - id: s2
    title: "Double Check in Chess"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/doublecheck.html
    type: reference
    accessed: 2026-11-09
  - id: s3
    title: "Tactics: 6. Discovered attack"
    publisher: ChessBase (learn.chessbase.com)
    url: https://learn.chessbase.com/en/page/tactics-the-discovered-attack
    type: publication
    accessed: 2026-11-09
  - id: s4
    title: "Discovered Attack (Chess Terms)"
    publisher: Chess.com
    url: https://www.chess.com/terms/discovered-attack-chess
    type: publication
    accessed: 2026-11-09
created: 2026-11-09
---

# Discovered attack

A discovered attack happens when a piece moves away from a line and thereby uncovers an attack by another piece standing behind it on that rank, file or diagonal.[^s1][^s4] The piece in the back must be a line piece (queen, rook or bishop), while the piece that moves can be anything, including a pawn or the king. What makes the motif dangerous is that the moving piece is free to make a threat of its own on the same move, so the opponent faces two threats and can usually answer only one.[^s1][^s3] ChessBase therefore treats it as a special form of the double attack and calls it one of the most frequent tactics in practice.[^s3]

## How it works

The defender's problem is one of tempo. After the discovery, the unmasked piece and the moved piece each demand a reply, and a single move rarely deals with both.[^s3] Chess.com stresses a consequence that club players often miss: a discovered attack can let the moving piece capture something that is *protected*, because the opponent has no time to recapture while a bigger piece is under attack.[^s4] ChessBase adds that even a discovery against a piece of equal value can work if the moving piece then escapes the line, for instance by giving check or recapturing on a protected square.[^s3]

## Discovered check and double check

The strongest form is the **discovered check**, in which the uncovered piece attacks the king. The opponent must deal with the check first, so the moving piece can usually take whatever it attacked on the next move.[^s1][^s4] Reuben Fine was fond of this point, calling discovered check "the dive-bomber of the chess board" in 1942.[^s2]

If the moving piece also gives check, the result is a **double check**. No single capture or interposition can meet two checks, so the king must move.[^s1] Edward Winter's survey of the term shows how often double check finishes games: in Vane–Miles, Sydney 1897, a sequence of double and discovered checks drives the king up the board until **8.Rh5** is mate.[^s2] Winter also points out that a double check can arise without the checking pawn itself giving check, through an en passant capture that opens a line.[^s2]

## Example

In the diagram position (White to move), the bishop on e3 stands between White's rook on e1 and the black king on e8. **1.Bc5+** uncovers a check from the rook and at the same time attacks the queen on a7. Black's only legal replies are a king move or the interposition ...Qe7, and after either one White collects the queen, for example **1...Kd7 2.Bxa7**. This is the pattern of the ECF leaflet's opening illustration, in which a bishop move to c5 uncovers a rook check from e1 and wins the queen.[^s1]

## Common patterns

- **Knight discoveries.** A knight jumps away from a bishop's or rook's line with check or a fork; several ECF exercises win the queen for a knight this way.[^s1]
- **Queen facing a rook on an open file.** ChessBase describes a queen opposite an enemy rook with only one piece between them as careless placement that invites a discovery.[^s3]
- **The poisoned pawn.** A pawn that looks undefended because a piece stands in front of its protector may be defended after all, since that piece can move away with check; ChessBase illustrates the trap in the French Defence.[^s3][^s4]
- **The windmill.** A rook and bishop alternate discovered checks, and every cycle the rook takes a piece; ECF exercise 10 shows a rook shuttling between g7 and the seventh rank in this way.[^s1]

## Pitfalls

- **Ignoring the second threat.** The defender usually loses material by meeting only the obvious threat; always look at what the moving piece attacks.[^s4]
- **A loose moving piece.** If the moving piece lands where it can be taken with check, or the opponent has a stronger counter-check, the discovery may fail. ECF exercise 5 notes that one tempting discovery is weaker because of a recapture.[^s1]
- **Defensive lesson.** Before grabbing material, check whether a blocking piece can move with tempo and unmask an attack on your king or queen.[^s3]

## Connections

The discovered attack belongs to the family of **chess tactics**, and ChessBase files it under double attacks.[^s3] It **contrasts with** the **fork**, where one piece attacks two targets from one square, whereas here the two threats come from two different pieces.[^s4] It **leads to** **double check** when the moving piece also gives check.[^s1][^s2] It is the active counterpart of the **pin**: a piece pinned against the king is, in effect, a discovery waiting to happen for the side that owns the line, and the motif is close in geometry to the **skewer**. Discoveries are common building blocks of a **combination**, often with an in-between check (a **zwischenzug**) that lets the moving piece escape, as in the blitz pattern ChessBase cites from Barden–Lenton, 1961.[^s3] Like other double attacks, a successful discovery **enables** a **material advantage**.[^s1][^s4]

## Sources

[^s1]: English Chess Federation, "Discovered Attacks" (Chess Skills leaflet). https://www.englishchess.org.uk/wp-content/uploads/2010/01/discoveredattacks.pdf (accessed 2026-11-09)
[^s2]: Edward Winter, "Double Check in Chess", Chess Notes. https://chesshistory.com/winter/extra/doublecheck.html (accessed 2026-11-09)
[^s3]: ChessBase, "Tactics: 6. Discovered attack". https://learn.chessbase.com/en/page/tactics-the-discovered-attack (accessed 2026-11-09)
[^s4]: Chess.com, "Discovered Attack" (Chess Terms). https://www.chess.com/terms/discovered-attack-chess (accessed 2026-11-09)
