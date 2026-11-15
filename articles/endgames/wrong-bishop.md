---
id: kt:wrong-bishop
type: EndgameType
title: Wrong bishop
aliases: [Wrong-coloured bishop, Wrong-colored bishop, Bishop of the wrong colour, Bishop of the wrong color, Wrong rook pawn, Wrong rook's pawn, Bishop and wrong rook pawn]
domain: endgames
summary: >-
  An ending with bishop and rook's pawn against a lone king in which the bishop does not control the
  pawn's promotion square; if the defending king reaches that corner the position is a draw, despite
  the extra piece and pawn.
fen: "6k1/8/6KP/5B2/8/8/8/8 w - - 0 1"
status: current
volatile: false
verified: 2026-11-15
broader: [kt:chess-endgame]
related: [kt:fortress, kt:stalemate, kt:opposite-coloured-bishops, kt:good-and-bad-bishops, kt:shouldering]
relations:
  - {predicate: usesTechnique, object: kt:fortress}
  - {predicate: dependsOn, object: kt:stalemate}
  - {predicate: exemplifiedBy, object: kt:vancura-position}
sources:
  - id: s1
    title: "Chess Fundamentals (1921), Project Gutenberg eBook #33870"
    publisher: José Raúl Capablanca; Project Gutenberg
    url: https://gutenberg.org/cache/epub/33870/pg33870-images.html
    type: book
    accessed: 2026-11-15
  - id: s2
    title: "Dvoretsky's Endgame Manual, fifth edition (excerpt with table of contents)"
    publisher: Mark Dvoretsky, Russell Enterprises; excerpt hosted by Chess Tigers
    url: https://shop.chess-tigers.de/cdn/shop/files/dem5_excerpt.pdf
    type: book
    accessed: 2026-11-15
  - id: s3
    title: "The wrong bishop"
    publisher: Frederic Friedel, ChessBase News (16 May 2016)
    url: https://en.chessbase.com/post/the-wrong-bishop
    type: publication
    accessed: 2026-11-15
  - id: s4
    title: "The wrong bishop – part two"
    publisher: Frederic Friedel, ChessBase News (22 May 2016)
    url: https://en.chessbase.com/newsroom/post/the-wrong-bishop-part-two
    type: publication
    accessed: 2026-11-15
  - id: s5
    title: "The Wrong-Coloured Bishop: Fortresses - Save A Lost Position"
    publisher: BigBrainChess_08, Lichess blog
    url: https://lichess.org/@/BigBrainChess_08/blog/the-wrong-coloured-bishop-fortresses-save-a-lost-position/nlOuSTzJ
    type: community
    accessed: 2026-11-15
created: 2026-11-15
---

# Wrong bishop

A bishop and a pawn normally beat a lone king without difficulty. The great exception is the **wrong bishop**: the pawn is a rook's pawn (on the a- or h-file) and the bishop runs on the opposite colour to the pawn's promotion square. A light-squared bishop with an h-pawn (h8 is dark) or a dark-squared bishop with an a-pawn (a8 is light) is "wrong" for White. If the defending king gets into the corner in front of the pawn, the stronger side cannot drive it out and the game is drawn.[^s1][^s3] Capablanca singled this out as the bishop's greatest weakness, a case in which the extra piece is worth nothing at all.[^s1] Dvoretsky files "Bishop and Rook Pawn" among the elementary fortresses in his chapter on bishop versus pawns.[^s2]

## How the draw works

The defender's king simply shuttles between the corner square and its neighbours, for instance h8 and g8 against an h-pawn. The bishop can never attack the corner square, the pawn cannot evict a king standing in front of it, and the attacking king cannot approach without taking the defender's last flight squares away. Every attempt to force progress ends either in a repetition or in stalemate.[^s3][^s5] Friedel notes that the ending has been understood for more than five hundred years, yet early chess programs routinely misjudged it.[^s3]

The diagram position (White Kg6, Bf5, h6; Black Kg8; White to move) shows the stalemate defence. After 1.Kh5 Kh8 2.h7 Kg7 3.Bc2 Kh8 4.Kh6 Black is stalemated, and 1.Be6+ Kh8 2.h7 is also stalemate.[^s3] Black can still lose by leaving the corner: 1.Kh5 Kf8? allows 2.Bh7! Kf7 3.Kg5 Ke7 4.Kg6 Kf8 5.Kf6, when the bishop covers g8 and the pawn queens.[^s3] The lesson for the defender is that the king belongs on the corner squares, not merely near them.

Extra rook's pawns on the same file do not change the verdict, because they all queen on the same square that the bishop cannot control.[^s5]

## The attacker's task: keep the king out

Since the corner is a fortress once occupied, the stronger side must win the race to it. The winning method is to use the bishop and pawn together to build a barrier so that the defending king never reaches the critical squares, while the attacking king may be too far away to help, especially when the defender uses its own king to shoulder it off.[^s4] Vancura's study from *Ceske Slovo*, 1922 (White Kc3, Bh3, h2; Black Kf2) is the classic illustration: only 1.Bd7!! wins, aiming the bishop at e8 so that, together with the pawn on h6, it seals off f7 and g7. Natural alternatives such as 1.Bg4, 1.Be6, 1.Bf5 and 1.Bc8 all let the black king reach the corner.[^s4] Friedel reports that even strong solvers needed many minutes to find the key move.[^s4]

```pgn
[Event "Ceske Slovo (study)"]
[White "J. Vancura"]
[Black "Study"]
[Result "1-0"]
[SetUp "1"]
[FEN "8/8/8/8/8/2K4B/5k1P/8 w - - 0 1"]

1. Bd7 Ke3 2. h4 Ke4 3. h5 Ke5 4. h6 Kf6 5. Be8 1-0
```

## Using it as a resource

The wrong bishop is above all a saving device for the weaker side. In a position from Greco's *Le Iev des Eschets* (1621) Black, facing two connected passed pawns, draws with 1...Ra1+ 2.Rf1 Rxf1+! 3.Kxf1 Bh3!: after 4.gxh3 White is left with a light-squared bishop and h-pawns, the wrong combination for h8.[^s3] A Lichess lesson shows the same trick from the other side, sacrificing a bishop so that the opponent's capture leaves only a rook's pawn the remaining bishop cannot support.[^s5]

## Pitfalls

- **For the attacker:** trading into bishop and rook's pawn without checking the colour of the queening square. Friedel describes 1980s programs giving up a won ending by capturing the "more valuable" bishop instead of the knight, leaving a drawn wrong-bishop ending.[^s3]
- **For the defender, as a swindle:** offering a pawn so that its capture leaves a wrong-bishop ending. In a 1982 game a human player tried this against Cray Blitz with 4.a5, but the program declined 4...bxa5, which would have drawn, and won instead.[^s3]
- **For both:** forgetting that the fortress exists only for rook's pawns; with any other pawn the bishop's colour matters far less.[^s5]

## Connections

The wrong bishop is the most elementary fortress, the drawing set-up in which a material advantage cannot be converted, and it depends on stalemate as the defender's ultimate resource.[^s2][^s3] It is a close relative of opposite-coloured bishop endings, where a bishop that cannot fight for the critical squares likewise leaves the stronger side unable to win, and it shows the general weakness of a bishop confined to one colour that good-and-bad-bishop theory discusses.[^s1][^s5] The Vancura study exemplifies the winning technique against it, and shouldering is the king manoeuvre the defender uses to keep the attacking king away.[^s4]

## Sources
[^s1]: José Raúl Capablanca, *Chess Fundamentals* (1921), Chapter II, section on the relative value of knight and bishop; Project Gutenberg. https://gutenberg.org/cache/epub/33870/pg33870-images.html (accessed 2026-11-15)
[^s2]: Mark Dvoretsky, *Dvoretsky's Endgame Manual*, fifth edition, Russell Enterprises (excerpt with table of contents). https://shop.chess-tigers.de/cdn/shop/files/dem5_excerpt.pdf (accessed 2026-11-15)
[^s3]: Frederic Friedel, "The wrong bishop", ChessBase News, 16 May 2016. https://en.chessbase.com/post/the-wrong-bishop (accessed 2026-11-15)
[^s4]: Frederic Friedel, "The wrong bishop – part two", ChessBase News, 22 May 2016. https://en.chessbase.com/newsroom/post/the-wrong-bishop-part-two (accessed 2026-11-15)
[^s5]: BigBrainChess_08, "The Wrong-Coloured Bishop: Fortresses - Save A Lost Position", Lichess blog. https://lichess.org/@/BigBrainChess_08/blog/the-wrong-coloured-bishop-fortresses-save-a-lost-position/nlOuSTzJ (accessed 2026-11-15)
