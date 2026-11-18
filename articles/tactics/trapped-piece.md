---
id: kt:trapped-piece
type: TacticalMotif
title: Trapped piece
aliases: [Trapping a piece, Trapped pieces, Piece trap]
domain: tactics
summary: >-
  A piece that has no safe square to go to: every move it can make loses it, so the opponent can
  win it by attacking it, or leave it imprisoned as a long-term liability.
fen: "8/B1k2ppp/1p6/8/8/8/5PPP/6K1 w - - 0 1"
status: current
volatile: false
verified: 2026-11-18
broader: [kt:chess-tactics]
related: [kt:desperado, kt:domination, kt:good-and-bad-bishops, kt:poisoned-pawn]
relations:
  - {predicate: enables, object: kt:material-advantage}
  - {predicate: exemplifiedBy, object: kt:fischer-spassky-1972}
sources:
  - id: s1
    title: "Spassky v Fischer, Reykjavik, 1972"
    publisher: Edward Winter, Chess Notes
    url: https://chesshistory.com/winter/extra/spasskyfischer.html
    type: reference
    accessed: 2026-11-18
  - id: s2
    title: "Fischer: Move by Move (sample pages: introduction)"
    publisher: Cyrus Lakdawala, Everyman Chess (sample hosted by New In Chess)
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/7548.pdf
    type: book
    accessed: 2026-11-18
  - id: s3
    title: "Learn Chess the Right Way, Book 2: Winning Material (sample pages)"
    publisher: Susan Polgar, Russell Enterprises (sample hosted by New In Chess)
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/3713.pdf
    type: book
    accessed: 2026-11-18
  - id: s4
    title: "Grivas on Trapping a Piece"
    publisher: GM Efstratios Grivas, ChessBase News
    url: https://en.chessbase.com/post/grivas-on-trapping-a-piece
    type: publication
    accessed: 2026-11-18
  - id: s5
    title: "Trapped Piece"
    publisher: Chess.com, Chess Terms
    url: https://www.chess.com/terms/trapped-piece-chess
    type: publication
    accessed: 2026-11-18
  - id: s6
    title: "Bobby Fischer Opens Match With Incredible Blunder"
    publisher: Peter Doggers, Chess.com
    url: https://www.chess.com/article/view/50-year-anniversary-fischer-spassky-game-1
    type: publication
    accessed: 2026-11-18
created: 2026-11-18
---

# Trapped piece

A **trapped piece** is one that has no escape: every square it can move to is covered, so it cannot get away from an attack without being captured.[^s4][^s5] Knights and bishops are the usual victims, but rooks and queens can be caught too. Pawns are not normally described as trapped, since their movement is so limited anyway, and the king cannot be captured at all; a checkmated king is, in effect, the ultimate trapped piece.[^s4][^s5] Teaching books treat trapping a piece as one of the standard ways of winning material, alongside forks, pins and the intermediate move; Susan Polgar's *Learn Chess the Right Way, Book 2: Winning Material* lists it among the patterns the solver must recognise in its mixed-exercise chapter.[^s3]

## How a piece gets trapped

The motif has two halves. First the piece's **mobility** is taken away, usually by pawns, which control squares cheaply and cannot be chased off by a minor piece; then the piece is **attacked**, or simply left out of play.[^s4] GM Efstratios Grivas describes three typical routes: restricting the piece with pawns and pieces and then attacking it, driving it to a bad square or a corner where it has little room, and simply capturing it once it has nowhere to go.[^s4]

The classic victims are:

- **A minor piece that grabs a rook's pawn.** A bishop that takes on a7 or h2 (or a2/h7) can be shut in by a pawn advance next to it, such as ...b6 or g3, and then picked up by the king.[^s1][^s2]
- **A knight on the rim.** A knight on h5 or a4 has few squares, and a single pawn move can leave it with none.[^s5]
- **An early queen raid.** Grivas singles out the queen that wanders off in the opening to chase pawns, including so-called poisoned pawns, as a frequent trapping target.[^s4]
- **A rook boxed in on the back rank** by enemy bishops that control its exit squares.[^s5]

Not every trapped piece can be won at once. A bishop entombed behind its own pawns, or a rook shut in a corner, may survive for many moves, but it is effectively out of the game and the opponent is playing with an extra piece in practice.[^s4][^s5]

## Example

In the diagram position (FEN `8/B1k2ppp/1p6/8/8/8/5PPP/6K1 w - - 0 1`), White's bishop has just taken a pawn on a7 and Black has replied ...b6. The bishop's only squares are b8, covered by the black king on c7, and b6, a pawn defended by the king. Black threatens ...Kb7 and ...Kxa7, and White's king is far too far away to help. The best White can do is give the bishop up for a pawn with Bxb6+ or Bb8+, a desperado that limits the damage. This is a constructed teaching position, not a game, built on the same rook's-pawn pattern the sources describe.[^s1][^s2][^s5]

## The most famous case

The best-known trapped piece in championship history is Bobby Fischer's bishop in the first game of his 1972 world-title match with Boris Spassky in Reykjavik, played on 11 July 1972.[^s6] In a level ending Fischer played 29...Bxh2, taking a poisoned pawn; after 30.g3 the bishop was hemmed in on h2.[^s1][^s2] Cyrus Lakdawala, in *Fischer: Move by Move*, calls the capture an inexplicable blunder and notes that the natural move was 29...Ke7.[^s2] Edward Winter's survey shows that annotators disagreed on how bad it was: Reuben Fine gave it two question marks, while other writers called it no gross blunder.[^s1] Chess.com's anniversary account adds that the capture did not lose at once: it is widely believed Fischer missed White's later resource 35.Bd2, after which the bishop was trapped for good. He got two pawns for it but still lost, resigning on move 56.[^s6] Winter also records that Fischer later told Guðmundur Thórarinsson he had overlooked that the bishop would be shut in.[^s1]

## Pitfalls and practical advice

Before taking a loose pawn with a piece, check where the piece will go next; the edge of the board and a pawn move by the opponent are the warning signs.[^s1][^s4] When your piece is already caught, look for the best desperado capture or check before it is taken, rather than shuffling it.[^s5] From the attacking side, train yourself to notice pieces with few or no safe squares, because those are often a tactic waiting to happen.[^s4][^s5]

## Connections

The trapped piece is a branch of **chess tactics** whose usual pay-off is a **material advantage**.[^s3][^s4] It is the most common reason a piece becomes a **desperado**, and it shades into strategic ideas: a piece permanently cut off is a case of **domination**, and a bishop blocked in by its own pawns is the extreme of a **bad bishop**.[^s4][^s5] Many traps begin with a **poisoned pawn**, as in the first game of **Fischer–Spassky 1972**, which is the standard illustration of the motif.[^s1][^s2][^s6]

## Sources

[^s1]: Edward Winter, "Spassky v Fischer, Reykjavik, 1972", Chess Notes. https://chesshistory.com/winter/extra/spasskyfischer.html (accessed 2026-11-18)
[^s2]: Cyrus Lakdawala, *Fischer: Move by Move*, Everyman Chess, sample pages (introduction). https://www.newinchess.com/media/wysiwyg/product_pdf/7548.pdf (accessed 2026-11-18)
[^s3]: Susan Polgar, *Learn Chess the Right Way, Book 2: Winning Material*, Russell Enterprises, sample pages. https://www.newinchess.com/media/wysiwyg/product_pdf/3713.pdf (accessed 2026-11-18)
[^s4]: Efstratios Grivas, "Grivas on Trapping a Piece", ChessBase News. https://en.chessbase.com/post/grivas-on-trapping-a-piece (accessed 2026-11-18)
[^s5]: Chess.com, "Trapped Piece", Chess Terms. https://www.chess.com/terms/trapped-piece-chess (accessed 2026-11-18)
[^s6]: Peter Doggers, "Bobby Fischer Opens Match With Incredible Blunder", Chess.com. https://www.chess.com/article/view/50-year-anniversary-fischer-spassky-game-1 (accessed 2026-11-18)
