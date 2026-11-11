---
id: kt:zwischenzug
type: TacticalMotif
title: Zwischenzug
aliases: [Intermezzo, In-between move, Intermediate move, Zwischenschach, In-between check]
domain: tactics
summary: >-
  A tactic in which a player, instead of making the expected move (usually a recapture), first
  inserts a forcing move such as a check or threat that the opponent must answer, and only then
  plays the expected move under better conditions.
fen: "6Rr/1k3p2/1pb1p2p/p1p1n2R/2P5/2P1B3/P1BK1PP1/8 b - - 0 27"
status: current
volatile: false
verified: 2026-11-11
broader: [kt:chess-tactics]
related: [kt:combination, kt:fork, kt:discovered-attack, kt:calculation, kt:deflection, kt:world-chess-championship]
relations:
  - {predicate: enables, object: kt:material-advantage}
  - {predicate: exemplifiedBy, object: kt:carlsen-versus-anand-sochi-2014-game-6}
sources:
  - id: s1
    title: "Zwischenzug! A Comprehensive Guide to Intermediate Moves (sample: contents, introduction and first chapters)"
    publisher: Natasha Regan and Matt Ball (via Boekhuis)
    url: https://download.boekhuis.nl/9789083413921_fragm-docb.pdf
    type: book
    accessed: 2026-11-11
  - id: s2
    title: "Zwischenzug! A Comprehensive Guide to Intermediate Moves"
    publisher: New In Chess
    url: https://www.newinchess.com/zwischenzug
    type: book
    accessed: 2026-11-11
  - id: s3
    title: "Zwischenzug – the intermediate move"
    publisher: Efstratios Grivas, ChessBase
    url: https://en.chessbase.com/post/zwischenzug-the-intermediate-move
    type: publication
    accessed: 2026-11-11
  - id: s4
    title: "Book of the Month: Zwischenzug! by Natasha Regan and Matt Ball"
    publisher: Ben Graff, English Chess Federation (Substack)
    url: https://englishchessfederation.substack.com/p/book-of-the-month-3af
    type: publication
    accessed: 2026-11-11
  - id: s5
    title: "World Chess Championship 2014 (6): massively relieved Carlsen takes the lead"
    publisher: The Week in Chess
    url: https://theweekinchess.com/chessnews/events/world-chess-championship-2014/massively-relieved-carlsen-takes-the-lead-in-dramatic-world-championship-game-6
    type: database
    accessed: 2026-11-11
created: 2026-11-11
---

# Zwischenzug

A zwischenzug (German *zwischen*, "between", and *Zug*, "move") is an intermediate move that breaks the expected sequence of play. The classic case is a recapture: instead of taking back at once, a player first makes a forcing move, typically a check or a threat, and recaptures only after the opponent has dealt with it.[^s1][^s3] English writers also call it an intermezzo or an in-between move; an in-between move that gives check is often called a *Zwischenschach*.[^s1][^s2]

## How it works

The motif exploits an assumption. Many calculations end with "he takes, I take back", and a zwischenzug points out that the recapture is not compulsory if something more forcing is available first.[^s3] The inserted move has to be forcing enough that the opponent cannot ignore it, otherwise it simply loses time; in return it lets the player seize the initiative, win material or dodge an unpleasant continuation.[^s3] Regan and Ball organise the forcing moves that can serve as in-between moves into five groups: checks, captures, mate threats, threats to capture and threats to promote.[^s1]

Grivas states that the term was first used by Fred Reinfeld and Irving Chernev in 1933, while noting that examples of the device predate the name and its exact origin is unknown.[^s3]

## Common patterns

Regan and Ball's survey of thousands of games groups recurring zwischenzugs into named patterns, among them back-rank checks, checks on the a2–g8 diagonal, knight checks on e7 and f6, "connected" queens that defend each other while both are attacked, mutual *en prise* positions, a pin played before recapturing, and a rook seizing an open file.[^s1] Typical outcomes include deflecting a defender, blocking or clearing a line, provoking a weakness, accelerating an attack, stopping counterplay and winning material.[^s1] They also name the *Zwischenantwort*, an in-between move played in answer to an in-between move.[^s1]

One of their examples shows the connected-queens pattern. In Van der Meer–Friberg (Chess.com, 2023), White did not recapture but played 15.Nxe4; after 15...Qxc2 the knight check 16.Nxf6+ came first, and only after 16...Bxf6 did White take back the queen with 17.Rxc2, finishing a piece up.[^s1]

## Example: Carlsen–Anand, 2014

In game 6 of the 2014 World Championship match in Sochi, Magnus Carlsen played 26.Kd2, a move he immediately recognised as an error.[^s5] Black could have replied 26...Nxe5, and after 27.Rxg8 the natural move is to recapture on g8. The diagram position shows the moment. Instead the in-between check **27...Nxc4+** comes first; after 28.Kd3 Nb2+ 29.Kd2 Black recaptures with 29...Rxg8, having picked up two pawns with very good winning chances.[^s5] Viswanathan Anand played 26...a4 after about a minute and lost the game.[^s5] Graff's review of the Regan–Ball book highlights this missed chance as an example of how even world-class players overlook intermediate moves.[^s4]

## Pitfalls and practical advice

- **Assuming the recapture.** The commonest error is to stop calculating at an "obvious" recapture; a strong reply can reverse a sequence that looked winning.[^s4]
- **Fast play.** Graff notes that quick time limits and online pre-moving make these moves easier to miss, for both sides.[^s4]
- **Weak in-between moves.** A non-forcing interpolation simply gives the opponent a free move, so the inserted move must demand an answer.[^s3]
- **Checking every forcing move.** The practical remedy, in Regan and Ball's framing, is to scan checks, captures and threats again before every routine recapture.[^s1]

## Connections

The zwischenzug is one of the **chess tactics** and a frequent link inside a **combination**, where it often sets up or refutes a **fork** or a **discovered attack**.[^s1][^s3] Among its outcomes Regan and Ball list **deflection**, and it usually **enables** a **material advantage**.[^s1] It is above all a test of **calculation**, since it lives in the step most players skip.[^s4] It is **exemplified by** the missed 27...Nxc4+ idea in Carlsen–Anand, game 6 of the 2014 **World Chess Championship** match.[^s5]

## Sources

[^s1]: Natasha Regan and Matt Ball, *Zwischenzug! A Comprehensive Guide to Intermediate Moves*, sample pages. https://download.boekhuis.nl/9789083413921_fragm-docb.pdf (accessed 2026-11-11)
[^s2]: New In Chess, *Zwischenzug! A Comprehensive Guide to Intermediate Moves* (product page). https://www.newinchess.com/zwischenzug (accessed 2026-11-11)
[^s3]: Efstratios Grivas, "Zwischenzug – the intermediate move", ChessBase, 2024. https://en.chessbase.com/post/zwischenzug-the-intermediate-move (accessed 2026-11-11)
[^s4]: Ben Graff, "Book of the Month", English Chess Federation, 2025. https://englishchessfederation.substack.com/p/book-of-the-month-3af (accessed 2026-11-11)
[^s5]: The Week in Chess, "World Chess Championship 2014 (6)". https://theweekinchess.com/chessnews/events/world-chess-championship-2014/massively-relieved-carlsen-takes-the-lead-in-dramatic-world-championship-game-6 (accessed 2026-11-11)
