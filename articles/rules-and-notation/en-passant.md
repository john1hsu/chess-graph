---
id: kt:en-passant
type: Rule
title: En passant
aliases: [En passant capture, Capture en passant, e.p., Prise en passant, In passing]
domain: rules-and-notation
summary: >-
  The special pawn capture in which a pawn that has just advanced two squares from its starting
  square, landing beside an enemy pawn, may be taken by that pawn as though it had moved only one
  square; the capture is legal only on the very next move.
moves: "1.e4 e6 2.e5 d5 3.exd6"
fen: "rnbqkbnr/ppp2ppp/4p3/3pP3/8/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 3"
status: current
volatile: true
verified: 2026-11-08
broader: [kt:fide-laws-of-chess, kt:pawn]
related: [kt:pawn-promotion, kt:threefold-repetition, kt:forsyth-edwards-notation, kt:stalemate, kt:wilhelm-steinitz]
sources:
  - id: s1
    title: "FIDE Laws of Chess (effective 1 January 2023), Articles 3.7 and 9.2"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/E012023
    type: governing-body
    accessed: 2026-11-08
  - id: s2
    title: "Laws of Chess (2018–2023 texts; 2023 Laws in force)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/laws-of-chess/
    type: governing-body
    accessed: 2026-11-08
  - id: s3
    title: "En passant (Chess)"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/enpassant.html
    type: reference
    accessed: 2026-11-08
  - id: s4
    title: "The Evolution of Modern Chess Rules: En Passant"
    publisher: John McCrary, US Chess
    url: https://new.uschess.org/news/evolution-modern-chess-rules-en-passant
    type: publication
    accessed: 2026-11-08
  - id: s5
    title: "en passant"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/en-passant
    type: reference
    accessed: 2026-11-08
  - id: s6
    title: "Forsyth-Edwards Notation"
    publisher: Chess Programming Wiki
    url: https://chessprogramming.org/Forsyth-Edwards_Notation
    type: community
    accessed: 2026-11-08
created: 2026-11-08
---

# En passant

En passant ("in passing") is the one capture in chess where the capturing piece does not land on the square of the piece it takes. When a pawn uses its optional two-square first move and finishes beside an enemy pawn on an adjacent file, that enemy pawn may capture it as if it had advanced only one square.[^s5] The FIDE Laws of Chess in force as of November 2026 (the text applying from 1 January 2023) set this out in Article 3.7.3: the capturing pawn moves diagonally to the square the advancing pawn passed over, and the captured pawn is removed.[^s1][^s2]

## How the rule works

Three conditions must all hold. The capturing pawn must stand on its fifth rank (the fourth for Black); the enemy pawn must have just made a two-square advance from its starting square; and the two pawns must end up side by side. FIDE adds the timing restriction in Article 3.7.3.2: the capture is legal only on the move immediately after the advance.[^s1] If the opportunity is not taken at once, it is gone for good, even if the pawns remain next to each other. Like other captures it is optional, though it becomes compulsory when it is the only legal move, and it is subject to the usual rule that no move may leave one's own king in check.[^s1][^s3]

In the position after 1.e4 e6 2.e5 d5, Black's d-pawn has jumped past d6, a square the e5-pawn attacks, so White may reply 3.exd6, placing the pawn on d6 and removing the pawn from d5. Edward Winter uses exactly this sequence, from Steinitz v Elson, Philadelphia 1882, to illustrate the rule.[^s3]

## Why it exists

The two-square first move is old: John McCrary, a former US Chess president, dates it to around 1200, and notes that it raised an obvious problem, since it let a pawn slip past an enemy pawn that would otherwise have controlled its path.[^s4] Local customs differed for centuries. Into the early nineteenth century England allowed the en passant capture, while Italy and Germany did not; the modern rule became universal in the mid-1800s.[^s4] J.H. Sarratt's 1808 treatise already gave the English rule and recorded the Italian practice of letting the pawn pass unchallenged, known as *passar battaglia*.[^s3] McCrary points out how this changed opening play: under the Italian rule, after 1.e4 e6 2.d4 d5 3.e5, Black could play ...f5 with no fear of an immediate capture.[^s4]

A long nineteenth-century debate concerned whether the capture could be refused when it was a player's only legal move, which would have produced stalemate. Winter traces the argument from Saint-Amant in *Le Palamède* in 1846, with Anderssen joining in, to a revision of the law; the capture is now compulsory in that situation like any other only move.[^s3][^s4]

## Practical points and pitfalls

- Use it or lose it: the most common error is noticing the capture a move too late. Winter records a single known case of an "en passant deferred", made two moves late and unnoticed until after the game, at the 1976 Haifa Olympiad.[^s3]
- The capture can open lines in unexpected ways, giving discovered checks or even mate. Winter collects a composed game that ends 6.gxf6 mate (1.e4 e5 2.Qh5 Nc6 3.g4 d6 4.Bh3 Kd7 5.g5+ f5 6.gxf6#), credited to Pal Benko, and notes the widely publicised Hammer v Carlsen game of January 2023 that ended with an en passant mate.[^s3]
- Repetition: under Article 9.2.3.1 two positions are not the same if, at the start of the sequence, an en passant capture was possible, because the available moves differ.[^s1] McCrary notes that this clarification was added only in recent decades.[^s4]
- In problems, an en passant key is allowed only when retrograde reasoning proves the opponent's last move was the double step.[^s4]

## Connections

En passant is part of the **FIDE Laws of Chess** and a special move of the **pawn**, alongside **pawn promotion**, which shares Article 3.7.[^s1] It interacts with **threefold repetition** through Article 9.2 and historically with **stalemate** through the only-legal-move debate.[^s1][^s3] It also shapes notation: **Forsyth–Edwards Notation** records an en passant target square after every double pawn push, whether or not a capture is actually possible, while the X-FEN variant records it only when a capture might be legal.[^s6] The standard illustration of the rule comes from a game of **Wilhelm Steinitz**.[^s3]

## Sources

[^s1]: FIDE Handbook, "FIDE Laws of Chess (effective 1 January 2023)", Articles 3.7 and 9.2. https://handbook.fide.com/chapter/E012023 (accessed 2026-11-08)
[^s2]: FIDE Rules Commission, "Laws of Chess". https://rcc.fide.com/laws-of-chess/ (accessed 2026-11-08)
[^s3]: Edward Winter, Chess Notes, "En passant (Chess)". https://chesshistory.com/winter/extra/enpassant.html (accessed 2026-11-08)
[^s4]: John McCrary, US Chess, "The Evolution of Modern Chess Rules: En Passant" (2021). https://new.uschess.org/news/evolution-modern-chess-rules-en-passant (accessed 2026-11-08)
[^s5]: Encyclopaedia Britannica, "en passant". https://www.britannica.com/topic/en-passant (accessed 2026-11-08)
[^s6]: Chess Programming Wiki, "Forsyth-Edwards Notation". https://chessprogramming.org/Forsyth-Edwards_Notation (accessed 2026-11-08)
