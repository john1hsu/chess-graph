---
id: kt:rook-versus-pawn
type: EndgameType
title: Rook versus pawn
aliases: [Rook against pawn, Rook vs pawn, Rook vs. pawn, Rook versus one pawn, Rook against a lone pawn, Rook vs. one pawn]
domain: endgames
summary: >-
  The endgame of king and rook against king and a single pawn. The rook normally wins when its king
  can reach the pawn in time or the defending king can be cut off, but a far-advanced pawn supported by
  its king can draw, and occasionally win, so the result turns on counting tempi and a handful of
  special resources.
fen: "4R3/8/7K/8/1kp5/8/8/8 w - - 0 1"
status: current
volatile: false
verified: 2026-11-16
broader: [kt:chess-endgame, kt:rook-endgames]
related: [kt:passed-pawn, kt:stalemate, kt:saavedra-position, kt:endgame-tablebases]
relations:
  - {predicate: hasPart, object: kt:cutting-off-the-king}
  - {predicate: hasPart, object: kt:shouldering}
  - {predicate: usesTechnique, object: kt:underpromotion}
  - {predicate: usesTechnique, object: kt:outflanking}
sources:
  - id: s1
    title: "100 Endgames You Must Know, sixth improved edition (sample pages: chapter 5, Rook vs. Pawn)"
    publisher: Jesús de la Villa, New In Chess (2023); excerpt hosted by Chess Tigers
    url: https://shop.chess-tigers.de/cdn/shop/files/100endgames.pdf
    type: book
    accessed: 2026-11-16
  - id: s2
    title: "Dvoretsky's Endgame Manual, sixth edition (excerpt: contents and chapter 9 sample)"
    publisher: Mark Dvoretsky, revised by Karsten Müller and Alex Fishbein, Russell Enterprises (2025); excerpt hosted by De Beste Zet
    url: https://www.debestezet.nl/catalog/images/PDF/Dvoretskys%20Endgame%20Manual%206th%20Edition.pdf
    type: book
    accessed: 2026-11-16
  - id: s3
    title: "New series \"Fundamental Endgame Knowledge\" – Part 1: Rook vs. pawn"
    publisher: Karsten Müller, ChessBase News (7 January 2023)
    url: https://en.chessbase.com/post/new-series-fundamental-endgame-knowledge-part-1-rook-vs-pawn
    type: publication
    accessed: 2026-11-16
  - id: s4
    title: "Rook vs Pawn (Endgame Column)"
    publisher: Charlotte Chess Center
    url: https://www.charlottechesscenter.org/post/rook-vs-pawn
    type: community
    accessed: 2026-11-16
created: 2026-11-16
---

# Rook versus pawn

Rook versus pawn is the ending in which one side has king and rook and the other only king and one pawn. It rarely arises from nothing: it usually comes out of a rook ending in which one player has had to give up the rook for a dangerous passed pawn.[^s1] Mark Dvoretsky makes the same point from the other direction, advising that when a passed pawn is so strong that the opponent will have to give a rook for it, the player should already be steering by the methods of rook-against-pawns theory.[^s2] Jesús de la Villa calls it one of the most important chapters of his book and stresses that, unlike queen or knight against a pawn, where the difficulties are confined to a pawn on the seventh or sixth rank, rook against pawn can be hard wherever the pawn stands.[^s1]

## Counting tempi

The first tool is a count. For the rook's side, count the moves its king and rook need to control the promotion square; for the pawn's side, the moves its pawn needs to promote with the king's support. De la Villa warns that the bare count only works when nothing special interferes, typically when the two kings stand on opposite sides of the pawn and cannot get in each other's way.[^s1] He credits Max Euwe with mapping, in the 1930s, the zone of squares from which the attacking king arrives in time in one such position.[^s1]

## Example: a pure count

In the diagram position (FEN above: White Kh6, Re8; Black Kb4, Pc4) each side needs five tempi, so the side to move decides the game. With White to move, 1.Kg5! c3 2.Kf4 c2 3.Rc8 Kb3 4.Ke3 Kb2 5.Kd2 wins the pawn; with Black to move, 1...c3 2.Kg5 c2 3.Rc8 Kb3 4.Kf4 Kb2 is a draw.[^s1] Even here the order of moves matters: the natural 1.Rc8? lets Black reply 1...Kc3!, putting the king in front of the pawn's file and spoiling the count.[^s1]

## The special resources

Most practical cases are decided by the factors that upset the count. Karsten Müller's introduction to the ending names four motifs: stalemate defences, cutting off the king, the body check (shouldering) and the in-between check that gains a tempo.[^s3] Dvoretsky's chapter on rook against one pawn covers the same ground under headings for "moving downstairs", cutting off the king, promotion to a knight, stalemate, the intermediate check, shouldering and outflanking.[^s2]

- **Cutting off the king.** A rook that separates the defending king from its pawn often wins at once; de la Villa notes this is especially effective while the king and pawn have not yet crossed the middle of the board, and that it wins outright against a rook's pawn or when king and pawn are apart.[^s1] Müller's example cuts the king off along the fifth rank.[^s3] In one de la Villa position (White Kh8, Rg7; Black Kb6, Pa5) only 1.Rg5! wins, while 1.Rg8? Kc5 lets the black king escort the pawn and draw.[^s1]
- **Knight promotion and stalemate.** With the pawn on the seventh, the defender may have to promote to a knight to avoid mate; Müller notes that a knight next to its king can draw against a rook, and that a knight's pawn can also be saved by stalemate tricks.[^s3] The Charlotte Chess Center's column adds that this resource fails with a rook's pawn.[^s4]
- **The pawn wins.** If the rook can neither get behind the pawn nor reach its promotion square, a far-advanced pawn can even promote and win.[^s4]

## Pitfalls

The commonest error is trusting a quick count when the kings can interfere: a king that blocks its rival's route, or a rook check that gains a tempo, changes the arithmetic by a whole move.[^s1][^s3] The attacker should also look first for a cut-off before bringing the king, since a wasted rook move can let the defending king reach the pawn.[^s1]

## Connections

Rook versus pawn is a sub-ending of **rook endgames** and the **chess endgame**, and it is where many rook endings with a strong **passed pawn** finish.[^s2] **Cutting off the king** and **shouldering** are its two central techniques, the first for the rook's side and the second mostly for the pawn's side, and Dvoretsky pairs shouldering with **outflanking**.[^s2][^s3] Its drawing resources use **underpromotion** and **stalemate**,[^s3] ideas that also run through the **Saavedra position**, the famous study in which king and pawn beat a rook. Exact results for every position are known from **endgame tablebases**, but over the board players rely on counting and the motifs above.[^s1]

## Sources
[^s1]: J. de la Villa, *100 Endgames You Must Know*, 6th edition, New In Chess (2023), sample pages, chapter 5 "Rook vs. Pawn". https://shop.chess-tigers.de/cdn/shop/files/100endgames.pdf (accessed 2026-11-16)
[^s2]: M. Dvoretsky, *Dvoretsky's Endgame Manual*, 6th edition, rev. K. Müller and A. Fishbein, Russell Enterprises (2025), excerpt. https://www.debestezet.nl/catalog/images/PDF/Dvoretskys%20Endgame%20Manual%206th%20Edition.pdf (accessed 2026-11-16)
[^s3]: K. Müller, "New series 'Fundamental Endgame Knowledge' – Part 1: Rook vs. pawn", ChessBase News, 7 January 2023. https://en.chessbase.com/post/new-series-fundamental-endgame-knowledge-part-1-rook-vs-pawn (accessed 2026-11-16)
[^s4]: Charlotte Chess Center, "Rook vs Pawn", Endgame Column. https://www.charlottechesscenter.org/post/rook-vs-pawn (accessed 2026-11-16)
