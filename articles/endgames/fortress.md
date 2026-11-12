---
id: kt:fortress
type: Technique
title: Fortress
aliases: [Fortress (chess), Chess fortress, Impregnable fortress, Fortress draw, Building a fortress, Erecting a fortress]
domain: endgames
summary: >-
  A defensive set-up in which the side that is behind in material arranges its king, pieces and pawns
  so that the stronger side cannot break through with correct defence, so the position is a draw
  despite the material deficit.
fen: "7k/8/6KP/8/8/3B4/8/8 w - - 0 1"
status: current
volatile: false
verified: 2026-11-12
broader: [kt:chess-endgame]
related: [kt:opposite-coloured-bishops, kt:zugzwang, kt:stalemate, kt:endgame-tablebases, kt:wrong-bishop]
relations:
  - {predicate: usesTechnique, object: kt:blockade}
  - {predicate: counters, object: kt:material-advantage}
  - {predicate: contrastsWith, object: kt:horizon-effect}
sources:
  - id: s1
    title: "Detecting Fortresses in Chess"
    publisher: Matej Guid and Ivan Bratko, Elektrotehniški vestnik (English edition) 79(1-2), 35-40 (2012)
    url: https://ev.fe.uni-lj.si/1-2-2012/Guid.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Dvoretsky's Endgame Manual, sixth edition (excerpt with table of contents)"
    publisher: Mark Dvoretsky, revised by Karsten Müller and Alex Fishbein, Russell Enterprises (2025); excerpt hosted by De Beste Zet
    url: https://www.debestezet.nl/catalog/images/PDF/Dvoretskys%20Endgame%20Manual%206th%20Edition.pdf
    type: book
    accessed: 2026-11-12
  - id: s3
    title: "100 Endgame Patterns You Must Know (excerpt with table of contents)"
    publisher: Jesús de la Villa, New In Chess (2021)
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/9112.pdf
    type: book
    accessed: 2026-11-12
  - id: s4
    title: "Simply impregnable (ChessBase Magazine #226 sample: Dorian Rogozenco on the rook-versus-queen fortress)"
    publisher: ChessBase News (2025)
    url: https://en.chessbase.com/post/new-chessbase-magazine-36
    type: publication
    accessed: 2026-11-12
  - id: s5
    title: "When the rook is as powerful as the queen!"
    publisher: GM Sundararajan Kidambi, ChessBase India (2017)
    url: https://chessbase.in/news/Queen_versus_rook_by_Kidambi
    type: publication
    accessed: 2026-11-12
  - id: s6
    title: "The Wrong-Coloured Bishop: Fortresses - Save A Lost Position"
    publisher: Lichess blog (BigBrainChess_08)
    url: https://lichess.org/@/BigBrainChess_08/blog/the-wrong-coloured-bishop-fortresses-save-a-lost-position/nlOuSTzJ
    type: community
    accessed: 2026-11-12
created: 2026-11-12
---

# Fortress

A **fortress** is a position in which the side with more material cannot win against accurate defence, because the defender has built a barrier that the attacker's extra force cannot penetrate.[^s1] The term covers a family of drawing set-ups rather than a single position: Dvoretsky's standard endgame manual treats "elementary fortresses" such as bishop plus rook's pawn as basic theory, returns to fortresses in knight-versus-bishop and queen-versus-rook endings, and closes with a general chapter on fortresses as a defensive principle alongside king activity and zugzwang.[^s2] De la Villa's pattern book likewise lists fortress patterns in opposite-coloured bishop endings, rook versus minor piece, and queen versus two minor pieces.[^s3]

## How a fortress works

A fortress usually rests on two things: squares the attacker cannot enter, and a defender who can shuffle without spoiling the set-up. Dvoretsky's final chapter distinguishes a "fortified camp", where the defending king shelters behind its pieces, from a "pawn barrier", where a pawn chain seals the board.[^s2] Because the defender only needs waiting moves, zugzwang is the attacker's main weapon against a fortress; a sound fortress is one in which the defender always has a harmless move available.[^s2]

The attacker's other weapon is the breakthrough. Guid and Bratko analyse a Dvoretsky example in which a materially winning side cannot make progress by quiet manoeuvring, and wins only with a pawn sacrifice that opens a path for the king; in the same paper an apparently natural capture turns a won position into a fortress.[^s1] For the defender this is the practical lesson: a fortress is often reached by deliberately giving back material so the remaining position is drawn, and for the attacker it means checking, before simplifying, whether the resulting position can be held.

## Typical fortresses

**Bishop and rook's pawn.** If the attacker's bishop does not control the promotion square of a rook's pawn, the defending king in that corner cannot be driven out, and attempts to dislodge it tend to end in stalemate.[^s6] In the diagram position (White: Kg6, Bd3, pawn h6; Black: Kh8) White is a bishop and pawn up but h8 is a dark square that the light-squared bishop can never cover, so the game is drawn; Dvoretsky files this case first among the elementary fortresses.[^s2] [^s6] The same idea is sometimes reached by sacrificing a piece to create the rook's-pawn ending on purpose.[^s6]

**Rook against queen.** With pawns on the board a rook can hold against a queen when the rook sits on a protected square in front of the defender's pawn and cuts off the enemy king. Rogozenco's ChessBase series classifies such fortresses by where the queen side's pawn stands, and stresses that holding them requires only a handful of rules, such as keeping the king in front of the pawn and the rook on the correct rank.[^s4] Kidambi's analysis of a rook-versus-queen ending from the 2017 European Club Cup gives similar practical pointers (safe squares for king and rook, stopping the pawn from advancing too far) and notes that the queen side can still have tactical tries before the rook reaches its post.[^s5]

**Opposite-coloured bishops and rook against minor piece** are other common homes for fortresses; de la Villa gives each its own fortress pattern, and a third for a queen against two minor pieces.[^s3]

## Fortresses and computers

Fortresses are a classic weakness of engines. Heuristic search gives high scores to positions with extra material, so a program may keep manoeuvring without a winning plan; the decisive breakthrough often requires a sacrifice whose payoff lies beyond the search horizon.[^s1] Guid and Bratko propose detecting fortresses by watching the evaluation across increasing search depths: if the backed-up score stays practically flat for all moves, the position is probably a fortress, whereas a move whose score keeps rising with depth suggests a breakthrough.[^s1] In pawnless or few-piece positions, endgame tablebases settle the question exactly.[^s1]

## Pitfalls

- For the defender: building the barrier one tempo too late. Several fortresses only work once a piece reaches a specific square, and the stronger side may have tactics before that.[^s5]
- For the attacker: assuming that extra material wins. Before trading into an ending, check whether the defender can reach a known fortress, especially a wrong-coloured rook's-pawn ending.[^s6] [^s1]

## Connections

A fortress is a technique within the endgame that neutralises a material advantage, usually by a blockade of key squares. It is closely tied to zugzwang, the main way to break a fortress, and to stalemate, which underlies the rook's-pawn draw.[^s2] [^s6] Opposite-coloured bishop endings are the best-known setting for fortresses, and the wrong-bishop case is the elementary example.[^s3] [^s2] The fortress contrasts with the horizon effect, since an engine's inability to see a distant breakthrough is what makes fortresses hard to evaluate, and endgame tablebases provide exact answers where they apply.[^s1]

## Sources
[^s1]: Matej Guid and Ivan Bratko, "Detecting Fortresses in Chess", Elektrotehniški vestnik 79(1-2), 2012. https://ev.fe.uni-lj.si/1-2-2012/Guid.pdf (accessed 2026-11-12)
[^s2]: Mark Dvoretsky, *Dvoretsky's Endgame Manual*, 6th ed., Russell Enterprises 2025 (excerpt). https://www.debestezet.nl/catalog/images/PDF/Dvoretskys%20Endgame%20Manual%206th%20Edition.pdf (accessed 2026-11-12)
[^s3]: Jesús de la Villa, *100 Endgame Patterns You Must Know*, New In Chess 2021 (excerpt). https://www.newinchess.com/media/wysiwyg/product_pdf/9112.pdf (accessed 2026-11-12)
[^s4]: ChessBase News, "Simply impregnable" (Dorian Rogozenco, ChessBase Magazine #226). https://en.chessbase.com/post/new-chessbase-magazine-36 (accessed 2026-11-12)
[^s5]: Sundararajan Kidambi, "When the rook is as powerful as the queen!", ChessBase India, 2017. https://chessbase.in/news/Queen_versus_rook_by_Kidambi (accessed 2026-11-12)
[^s6]: Lichess blog, "The Wrong-Coloured Bishop: Fortresses - Save A Lost Position". https://lichess.org/@/BigBrainChess_08/blog/the-wrong-coloured-bishop-fortresses-save-a-lost-position/nlOuSTzJ (accessed 2026-11-12)
