---
id: kt:development
type: StrategicConcept
title: Development
aliases: [Piece development, Developing the pieces, Lead in development, Development advantage, Mobilisation, Mobilization]
domain: openings
summary: >-
  The opening task of moving the pieces off their starting squares to active posts, usually minor
  pieces first and castling soon after; the side that mobilises faster can often seize the initiative.
fen: "rn2kb1r/p3qppp/2p2n2/1p2p1B1/2B1P3/1QN5/PPP2PPP/R3K2R w KQkq - 0 10"
status: current
volatile: false
verified: 2026-11-17
broader: [kt:chess-openings, kt:chess-strategy]
related: [kt:castling, kt:king-safety, kt:gambit, kt:tempo, kt:hypermodernism, kt:siegbert-tarrasch]
relations:
  - {predicate: enables, object: kt:initiative}
  - {predicate: championedBy, object: kt:paul-morphy}
  - {predicate: exemplifiedBy, object: kt:opera-game}
sources:
  - id: s1
    title: "Chess: Development of theory"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/chess/Development-of-theory
    type: reference
    accessed: 2026-11-17
  - id: s2
    title: "Development (chess)"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/development-chess
    type: reference
    accessed: 2026-11-17
  - id: s3
    title: "Chess Strategy (trans. J. du Mont), Project Gutenberg eBook #5614"
    publisher: Edward Lasker, G. Bell & Sons; Project Gutenberg edition
    url: https://www.gutenberg.org/ebooks/5614.epub.images
    type: book
    accessed: 2026-11-17
  - id: s4
    title: "The Principles of the Opening"
    publisher: IM Danny Rensch, Chess.com (updated 30 May 2018)
    url: https://www.chess.com/article/the-principles-of-the-opening
    type: publication
    accessed: 2026-11-17
  - id: s5
    title: "Development"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/Development
    type: community
    accessed: 2026-11-17
created: 2026-11-17
---

# Development

Development is the work of bringing the pieces from their home squares into play. Britannica names it, together with control of the centre, as the main business of the opening phase.[^s1] Edward Lasker's *Chess Strategy* states the aim bluntly: develop the pieces rapidly and avoid losing a move in any form, because the side that first gets all its pieces onto effective squares has the better chances.[^s3]

## The working rules

Most opening advice is development advice in disguise. The familiar guidelines are to bring out the knights and bishops before the rooks and queen, to point them at the centre, to castle early (Danny Rensch suggests before move 10, ideally around move 7) so that the king is safe and a rook joins the game, and not to move the same piece twice without good reason.[^s4] Siegbert Tarrasch compressed this into short rules such as developing knights before bishops and not moving the queen early.[^s1] An early queen sortie is costly because minor pieces can attack it and gain time as they develop.[^s4]

Pawn moves deserve particular care. Lasker counts a pawn move as useful only if it opens a line for a piece, which is why the advances of the king's and queen's pawns are so valuable: they free a bishop and the queen at once. Pawn moves that release nothing simply waste time.[^s3]

## Counting time

Development is measured in tempi, or moves. Lasker defines a lost move as bringing a piece to its square in more moves than necessary, and argues that a player who loses one hands the initiative to the opponent.[^s3] Engine programmers formalise the same idea: the Chess Programming Wiki describes a "tempo balance" in which each developed minor piece and castling count as a tempo while pawn moves do not, and it reports Tarrasch's estimate that three tempi are worth roughly one pawn, the arithmetic behind many gambits.[^s5]

## When development matters most

A lead in development is not a permanent asset. Britannica notes that Paul Morphy, who prized what he called superior development, recognised that it counted for less in blocked positions and for much more once the centre or the kingside opened.[^s2][^s1] Morphy gave up pawns to get his queen, rooks and bishops into action quickly, while Wilhelm Steinitz later observed that such a lead may be transient and turned instead to small, lasting advantages.[^s1] José Raúl Capablanca added a further caution: each opening move should serve a plan, not develop a piece merely for the sake of it.[^s1] The Hypermoderns showed that the classical recipe was not the only one, developing bishops by fianchetto and inviting the opponent to occupy the centre with pawns.[^s1]

## Example: the cost of lost moves

Lasker uses Morphy's 1858 game against the Duke of Brunswick and Count Isouard to illustrate lost time. After 1.e4 e5 2.Nf3 d6 3.d4 Bg4 4.dxe5 Bxf3 5.Qxf3 dxe5 6.Bc4 Nf6 7.Qb3 Qe7 8.Nc3 c6 9.Bg5 b5 (see `fen`), White has a knight and both bishops in play and is ready to castle queenside, while Black's bishop on f8 is blocked by the queen and the b8-knight has not moved.[^s3] Lasker traces this back to 2...d6, which shut in the king's bishop, and 3...Bg4, after which the bishop moved twice only to be exchanged for a knight that had moved once, a net gift of time.[^s3] The forced 7...Qe7 then hemmed in the f8-bishop and the king's rook, and Black's remaining moves went on protecting pawns instead of developing; Lasker describes Black as effectively playing several pieces down, and Morphy's sacrifices that followed exploited exactly that.[^s3]

## Connections

Development sits under **chess openings** and the wider **chess strategy**, and it **enables** the **initiative**: Britannica describes Morphy using faster mobilisation to gain the ability to force matters.[^s1] It is **championed by Paul Morphy** and **exemplified by** the **Opera Game**, Lasker's model of lost tempi.[^s2][^s3] It is closely tied to **castling** and **king safety**, since castling both shelters the king and develops a rook.[^s4] The idea of a **tempo** as its unit, and of the **gambit** as a trade of material for time, follow from Tarrasch's tempo-for-pawn estimate.[^s5] **Siegbert Tarrasch** codified its rules, and **hypermodernism** challenged them.[^s1]

## Sources
[^s1]: Encyclopaedia Britannica, "Chess: Development of theory". https://www.britannica.com/topic/chess/Development-of-theory (accessed 2026-11-17)
[^s2]: Encyclopaedia Britannica, "Development (chess)". https://www.britannica.com/topic/development-chess (accessed 2026-11-17)
[^s3]: E. Lasker, *Chess Strategy*, trans. J. du Mont, G. Bell & Sons; Project Gutenberg eBook #5614. https://www.gutenberg.org/ebooks/5614.epub.images (accessed 2026-11-17)
[^s4]: D. Rensch, "The Principles of the Opening", Chess.com, updated 30 May 2018. https://www.chess.com/article/the-principles-of-the-opening (accessed 2026-11-17)
[^s5]: Chess Programming Wiki, "Development". https://www.chessprogramming.org/Development (accessed 2026-11-17)
