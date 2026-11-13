---
id: kt:rule-of-the-square
type: Technique
title: Rule of the square
aliases: [Square of the pawn, Square rule, The square rule, Pawn square, Quadrant rule]
domain: endgames
summary: >-
  A visual shortcut for king-against-passed-pawn races: draw the square whose side runs from the
  pawn to its promotion rank; if the defending king can step into that square, it catches the
  unsupported pawn, otherwise the pawn queens.
fen: "8/8/8/6k1/1P6/8/8/7K w - - 0 1"
status: current
volatile: false
verified: 2026-11-13
broader: [kt:king-and-pawn-endgames, kt:passed-pawn]
related: [kt:key-squares, kt:opposition, kt:reti-endgame-study, kt:pawn-promotion]
relations:
  - {predicate: dependsOn, object: kt:tempo}
  - {predicate: contrastsWith, object: kt:counting-in-pawn-races}
sources:
  - id: s1
    title: "Dvoretsky's Endgame Manual, sixth edition (excerpt with table of contents)"
    publisher: Mark Dvoretsky, revised by Karsten Müller and Alex Fishbein, Russell Enterprises (2025); excerpt hosted by De Beste Zet
    url: https://www.debestezet.nl/catalog/images/PDF/Dvoretskys%20Endgame%20Manual%206th%20Edition.pdf
    type: book
    accessed: 2026-11-13
  - id: s2
    title: "100 Endgames You Must Know, fourth improved edition (sample pages and contents)"
    publisher: Jesús de la Villa, New In Chess (2015); excerpt hosted by Boekhuis
    url: https://download.boekhuis.nl/9789056916176_fragm-docb.pdf
    type: book
    accessed: 2026-11-13
  - id: s3
    title: "Chess Fundamentals (1921), Project Gutenberg eBook #33870"
    publisher: José Raúl Capablanca; Project Gutenberg
    url: https://gutenberg.org/cache/epub/33870/pg33870-images.html
    type: book
    accessed: 2026-11-13
  - id: s4
    title: "Rule of the Square"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/Rule_of_the_Square
    type: community
    accessed: 2026-11-13
  - id: s5
    title: "Kaleidoscope II (Study of the Month, July 2021)"
    publisher: Siegfried Hornecker, ChessBase News (2021-07-31)
    url: https://en.chessbase.com/post/study-of-the-month-2021-07
    type: publication
    accessed: 2026-11-13
created: 2026-11-13
---

# Rule of the square

The rule of the square answers one of the most frequent questions in a pawn ending: can the defending king catch a passed pawn that runs alone? Instead of counting moves, the player pictures a square on the board. One side of it runs from the pawn straight up to its promotion square, and the square extends sideways towards the defending king. If the king stands inside that square, or can step into it with the move, it catches the pawn; if not, the pawn promotes.[^s4] The rule is basic enough that standard endgame courses teach it at the very start: Dvoretsky's manual covers "The Rule of the Square" in its first chapter, under king against passed pawns, and de la Villa's collection makes it Ending 1.[^s1][^s2]

## How it works

The square works because a king moves one step in any direction, including diagonally, so its distance to a target is the larger of the file and rank differences rather than their sum. A king that can enter the square is therefore never more moves from the queening square than the pawn is.[^s4] Each pawn step shrinks the square by one file and one rank, so the side to move matters: the same placement can be a win with the pawn to move and a draw with the king to move.[^s4]

Two refinements come up constantly. A pawn still on its starting rank may advance two squares at once, so its square is drawn as if it already stood one rank further forward; this is why the largest possible square spans six ranks rather than seven.[^s4] And the rule assumes a clean race: the pawn has no support and nothing blocks the king's path. Once the attacking king can shoulder the defender away, other pawns take tempi, or the defender can create threats of his own, the shortcut no longer decides by itself.[^s4]

## Example

In the diagram position (White Kh1, Pb4; Black Kg5), the square of the b4-pawn covers the b- to f-files from the fourth rank to the eighth. The black king on g5 is one file outside it. With White to move, 1.b5 shrinks the square to the b- to e-files and the king is too late: 1...Kf6 2.b6 Ke7 3.b7 Kd7 4.b8=Q. With Black to move, 1...Kf5 steps inside, and the king then shadows the pawn: 2.b5 Ke6 3.b6 Kd7 4.b7 Kc7 5.b8=Q+ Kxb8 with a draw.[^s4]

## Limits and Réti's idea

The most famous exception is Richard Réti's study, published in the *Deutsch-Österreichische Tageszeitung* about a century before Hornecker's 2021 column. White's king on h8 stands far outside the square of Black's h5-pawn, yet it draws by heading down the long diagonal: 1.Kg7 h4 2.Kf6 Kb6 3.Ke5, threatening to support its own c6-pawn while approaching the h-pawn. After 3...h3 4.Kd6 White's pawn also queens, and after 3...Kxc6 4.Kf4 the white king is back inside the square.[^s5] Hornecker notes how sharply the geometry works: in a related setting a king on a3 can still save the game because the pawn square extends to b4, but a king on b2 loses although it reaches e5 just as quickly.[^s5] Dvoretsky's manual follows the rule of the square with "Réti's Idea" and "The Floating Square" in the same section.[^s1]

## Pitfalls

The rule is a shortcut for a calculation, not a substitute for it. Capablanca taught the underlying habit: before running a passed pawn, count whether the opposing king can get there in time, and when both sides have runners, count which pawn queens first, remembering that a pawn which promotes first may capture the other side's new queen.[^s3] Common errors are forgetting the double step from the starting rank, ignoring a piece or pawn that blocks the king's route, and overlooking that one's own king may obstruct the defender. Even computers have stumbled here: the Chess Programming Wiki records a 1984 ACM computer tournament game in which a program without the rule played a rook capture that turned a win into a loss.[^s4]

## Connections

The rule of the square is the first technique of king-and-pawn endings and the simplest question about a passed pawn: whether it can run alone.[^s1] When the king cannot catch the pawn by simple geometry, the methods that take over are counting tempi in pawn races, which Capablanca stressed, and Réti's idea of a king pursuing two goals at once.[^s3][^s5] It sits next to key squares and the opposition in the same opening chapter of the endgame manuals: the square tells whether the defender reaches the pawn at all, and the other two decide what happens once the kings meet.[^s1][^s2]

## Sources

[^s1]: Mark Dvoretsky, *Dvoretsky's Endgame Manual*, sixth edition, revised by Karsten Müller and Alex Fishbein (Russell Enterprises, 2025), excerpt with table of contents, chapter 1 "King vs. Passed Pawns". https://www.debestezet.nl/catalog/images/PDF/Dvoretskys%20Endgame%20Manual%206th%20Edition.pdf (accessed 2026-11-13)
[^s2]: Jesús de la Villa, *100 Endgames You Must Know*, fourth improved edition (New In Chess, 2015), sample pages and contents, Ending 1 "The rule of the square". https://download.boekhuis.nl/9789056916176_fragm-docb.pdf (accessed 2026-11-13)
[^s3]: José Raúl Capablanca, *Chess Fundamentals* (1921), section 12 "How to find out which Pawn will be the first to Queen", Project Gutenberg eBook #33870. https://gutenberg.org/cache/epub/33870/pg33870-images.html (accessed 2026-11-13)
[^s4]: Chess Programming Wiki, "Rule of the Square". https://www.chessprogramming.org/Rule_of_the_Square (accessed 2026-11-13)
[^s5]: Siegfried Hornecker, "Kaleidoscope II", Study of the Month, ChessBase News, 31 July 2021. https://en.chessbase.com/post/study-of-the-month-2021-07 (accessed 2026-11-13)
