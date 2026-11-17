---
id: kt:knight-versus-bishop
type: EndgameType
title: Knight versus bishop
aliases: [Bishop versus knight, Bishop vs knight, Knight vs bishop, Bishop against knight, Knight against bishop, Bishop versus knight endgame, Knight versus bishop endgame]
domain: endgames
summary: >-
  Endings in which one side has a bishop and the other a knight, usually with pawns; the bishop is
  generally favoured in open positions with pawns on both wings, while the knight does best in
  closed or one-wing positions, against a bad bishop, or where it can dominate and fork.
fen: "8/8/1pnk2p1/pBp2p1p/P4P1P/2P3P1/1P2K3/8 w - - 0 45"
status: current
volatile: false
verified: 2026-11-17
broader: [kt:chess-endgame]
related: [kt:good-and-bad-bishops, kt:bishop-pair, kt:passed-pawn, kt:zugzwang, kt:fork]
relations:
  - {predicate: contrastsWith, object: kt:good-and-bad-bishops}
  - {predicate: exemplifiedBy, object: kt:fischer-versus-taimanov-vancouver-1971-game-4}
  - {predicate: championedBy, object: kt:bobby-fischer}
  - {predicate: usesTechnique, object: kt:domination}
sources:
  - id: s1
    title: "Chess Fundamentals (1921), Chapter II, 'The Relative Value of Knight and Bishop'"
    publisher: José Raúl Capablanca; Project Gutenberg eBook #33870
    url: https://gutenberg.org/cache/epub/33870/pg33870-images.html
    type: book
    accessed: 2026-11-17
  - id: s2
    title: "Dvoretsky's Endgame Manual, fourth edition (excerpt with table of contents)"
    publisher: Mark Dvoretsky, Russell Enterprises, 2014; excerpt hosted by New In Chess
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/2703.pdf
    type: book
    accessed: 2026-11-17
  - id: s3
    title: "The old riddle of Fischer vs Taimanov"
    publisher: Karsten Müller, ChessBase News (13 May 2020)
    url: https://en.chessbase.com/newsroom/post/the-old-riddle-of-fischer-vs-taimanov
    type: publication
    accessed: 2026-11-17
  - id: s4
    title: "The Eternal Struggle (Endings column)"
    publisher: Alex Fishbein, American Chess Magazine no. 30 (2022)
    url: https://chessjournalism.org/wp-content/uploads/2023/06/acm-030-the-eternal-struggle-alex-fishbein.pdf
    type: publication
    accessed: 2026-11-17
  - id: s5
    title: "The Fischer ending"
    publisher: ChessBase News (12 May 2010)
    url: https://en.chessbase.com/post/the-fischer-ending
    type: publication
    accessed: 2026-11-17
created: 2026-11-17
---

# Knight versus bishop

**Knight versus bishop** endings are those in which the only pieces left, apart from kings and pawns, are one bishop on one side and one knight on the other, often with the rooks just exchanged or still on the board. The two minor pieces are roughly equal in value, so the question is never "which is worth more?" but "which is better *in this pawn structure*?"[^s1][^s2] Dvoretsky devotes a whole chapter of his endgame manual to the subject, split into the cases where the bishop is superior and those where the knight is, plus the elementary endings of a single pawn against the other minor piece.[^s2]

## When the bishop is better

Capablanca argued that the bishop is in most cases the stronger piece. The knight can reach squares of both colours, which leads beginners to prefer it, but it acts on only one colour at a time and needs several moves to cross from one wing to the other; a bishop can also stalemate a knight by taking away all its squares, which a knight can never do to a bishop.[^s1] He observed that the stronger the player, the more the bishop is valued, and that masters of his era had moved away from the knight preference of players such as Pillsbury and Chigorin.[^s1]

The bishop's advantage grows with the openness of the position and the spread of the pawns. In Capablanca's graded examples, pawns on one side only give a draw; three pawns on each wing make the bishop preferable because it can watch both flanks from a central square; and pawns on both wings together with a passed rook's pawn give the bishop side a decisive edge.[^s1] Dvoretsky's headings name the bishop's typical weapons: cutting the knight off from the action, fixing the enemy pawns on squares of the bishop's colour, supporting a passed pawn, and exploiting an open position with a more active king.[^s2]

## When the knight is better

The knight's best case, according to Capablanca, is a blocked position with all the pawns on one side of the board, where it can attack pawns the bishop cannot defend.[^s1] Dvoretsky lists the knight's assets as domination and forks, fixing pawns, and closed positions with a bad bishop.[^s2] Fishbein, examining modern examples, found that the knight usually comes out on top when the bishop is hemmed in by its own pawns, but that it can also hold or win against a free bishop by cooperating with an active central king, by building a barrier the enemy king cannot cross, or by creating forks.[^s4] One of his examples is the ninth game of the 1984 world championship match, in which Karpov's knight beat Kasparov's bad bishop.[^s4]

## Pawn placement

Capablanca's rule for the side with the bishop is to put pawns on the opposite colour to it, so they do not block it; against an enemy bishop, keep your pawns on its colour, especially a passed pawn escorted by the king, so that the bishop must attack them rather than merely blockade.[^s1] He gave no fixed winning plan, recommending instead that the king march towards the centre or the weak and passed pawns, and that passed pawns be advanced as far as is safe, with each case calculated concretely.[^s1]

## Example: Fischer–Taimanov, Vancouver 1971

The diagram shows the position after the rook exchange in the fourth game of Fischer's 1971 Candidates quarter-final against Taimanov (White Ke2, Bb5, pawns a4, b2, c3, f4, g3, h4; Black Kd6, Nc6, pawns a5, b6, c5, f5, g6, h5). Müller reports that the sources agree the position was lost after Taimanov's 42...Kd8?!, which let Fischer trade rooks with 43.Rd3 and 44.Rxd6; without rooks he regards the ending as a clear win, though the adjourned position with rooks is a borderline case even for engines.[^s3]

```pgn
[Event "Candidates quarter-final, game 4"]
[Site "Vancouver"]
[Date "1971.05.25"]
[White "Robert James Fischer"]
[Black "Mark Taimanov"]
[Result "1-0"]
[SetUp "1"]
[FEN "8/8/1pnk2p1/pBp2p1p/P4P1P/2P3P1/1P2K3/8 w - - 0 45"]

45. Kd3 Ne7 46. Be8 Kd5 47. Bf7+ Kd6 48. Kc4 Kc6 49. Be8+ Kb7 50. Kb5 Nc8
51. Bc6+ Kc7 52. Bd5 Ne7 53. Bf7 Kb7 54. Bb3 Ka7 55. Bd1 Kb7 56. Bf3+ Kc7
57. Ka6 Nc8 58. Bd5 Ne7 59. Bc4 Nc6 60. Bf7 Ne7 61. Be8 Kd8 62. Bxg6 Nxg6
63. Kxb6 Kd7 64. Kxc5 Ne7 65. b4 axb4 66. cxb4 Nc8 67. a5 Nd6 68. b5 Ne4+
69. Kb6 Kc8 70. Kc6 Kb8 71. b6 1-0
```

The game score shows the bishop's typical method: the white king walks into the queenside while the bishop keeps the knight and the black king tied to the defence of b6 and g6; finally the bishop is given up for the g-pawn so the king can win the queenside pawns and create unstoppable passed pawns.[^s3] Fischer scored so well with bishop against knight, often with rooks still on, that rook and bishop against rook and knight became known as the "Fischer ending".[^s5]

## Pitfalls

- **Trusting the rule of thumb.** Fishbein shows strong players misjudging these endings in both directions; activity, king position and tactics often outweigh the general preference for the bishop.[^s4]
- **Exchanging rooks too eagerly or too reluctantly.** In Fischer–Taimanov the defender's choice of whether to allow the rook trade decided the game.[^s3]
- **Putting pawns on the bishop's colour.** A bishop blocked by its own pawns hands the knight its best scenario.[^s1][^s4]

## Connections

This ending is a chapter of endgame theory in its own right, and it contrasts with the middlegame question of good and bad bishops, which concerns the quality of one bishop rather than the balance of two different minor pieces.[^s2][^s4] Passed pawns and zugzwang are the bishop side's usual winning tools, while forks and domination are the knight's.[^s1][^s2] Fischer's games, above all his 1971 win against Taimanov, are the standard illustrations of the bishop's superiority.[^s3][^s5]

## Sources
[^s1]: José Raúl Capablanca, *Chess Fundamentals* (1921), Chapter II, "The Relative Value of Knight and Bishop"; Project Gutenberg. https://gutenberg.org/cache/epub/33870/pg33870-images.html (accessed 2026-11-17)
[^s2]: Mark Dvoretsky, *Dvoretsky's Endgame Manual*, fourth edition, Russell Enterprises, 2014 (excerpt with table of contents, Chapter 7 "Bishop versus Knight"). https://www.newinchess.com/media/wysiwyg/product_pdf/2703.pdf (accessed 2026-11-17)
[^s3]: Karsten Müller, "The old riddle of Fischer vs Taimanov", ChessBase News, 13 May 2020. https://en.chessbase.com/newsroom/post/the-old-riddle-of-fischer-vs-taimanov (accessed 2026-11-17)
[^s4]: Alex Fishbein, "The Eternal Struggle", *American Chess Magazine* no. 30 (2022). https://chessjournalism.org/wp-content/uploads/2023/06/acm-030-the-eternal-struggle-alex-fishbein.pdf (accessed 2026-11-17)
[^s5]: "The Fischer ending", ChessBase News, 12 May 2010. https://en.chessbase.com/post/the-fischer-ending (accessed 2026-11-17)
