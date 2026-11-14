---
id: kt:corresponding-squares
type: Technique
title: Corresponding squares
aliases: [Co-ordinate squares, Coordinate squares, Sister squares, Conjugate squares, Cases conjuguées, Related squares, Theory of corresponding squares]
domain: endgames
summary: >-
  An endgame analysis method that pairs each square of the attacking king with the square or squares
  the defending king must occupy in reply; the defender holds only by keeping to these matching
  squares, so the attacker wins by manoeuvring until no corresponding square is available.
fen: "6k1/3p4/3p4/3P4/4P1p1/6P1/8/K7 w - - 0 1"
status: current
volatile: false
verified: 2026-11-14
broader: [kt:king-and-pawn-endgames]
related: [kt:key-squares, kt:opposition, kt:zugzwang, kt:computer-chess]
relations:
  - {predicate: dependsOn, object: kt:zugzwang}
  - {predicate: hasPart, object: kt:opposition}
  - {predicate: hasPart, object: kt:triangulation}
  - {predicate: developedBy, object: kt:marcel-duchamp}
sources:
  - id: s1
    title: "Co-ordinate Square: Solution to Many Chess Pawn Endgames"
    publisher: Kenneth Ward Church, Proceedings of the Sixth International Joint Conference on Artificial Intelligence (IJCAI 1979)
    url: https://ijcai.org/proceedings/1979/37
    type: academic
    accessed: 2026-11-14
  - id: s2
    title: "Co-ordinate squares: a solution to many chess pawn endgames (B.S. thesis, advisor Richard Greenblatt)"
    publisher: Kenneth Ward Church, Massachusetts Institute of Technology, DSpace@MIT (1978)
    url: https://dspace.mit.edu/handle/1721.1/154966
    type: academic
    accessed: 2026-11-14
  - id: s3
    title: "Opposition et cases conjuguées sont réconciliées (catalogue record)"
    publisher: Philadelphia Museum of Art Library and Archives; Marcel Duchamp and Vitaly Halberstadt, L'Echiquier, Paris (1932)
    url: https://library.philamuseum.org/Record/000075230
    type: archive
    accessed: 2026-11-14
  - id: s4
    title: "Dvoretsky's Endgame Manual, fifth edition (excerpt with table of contents)"
    publisher: Mark Dvoretsky, revised by Karsten Müller, Russell Enterprises (2020)
    url: https://shop.chess-tigers.de/cdn/shop/files/dem5_excerpt.pdf
    type: book
    accessed: 2026-11-14
  - id: s5
    title: "Theory of corresponding squares"
    publisher: Sundararajan Kidambi (GM), ChessBase News, 16 June 2023
    url: https://en.chessbase.com/post/theory-of-corresponding-squares-kidambi
    type: publication
    accessed: 2026-11-14
  - id: s6
    title: "Corresponding Squares"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/Corresponding_Squares
    type: community
    accessed: 2026-11-14
created: 2026-11-14
---

# Corresponding squares

Corresponding squares are pairs of squares that belong together in a mutual-zugzwang fight between the two kings. For each square the attacking king can stand on, only a few squares are available to the defending king that do not lead to a known lost position; as the attacker moves, the defender must step to a square that corresponds to the attacker's new square.[^s1] If at some moment no such square can be reached, the defence collapses. The same idea goes by several names: co-ordinate squares in the computer-science literature,[^s1] "sister squares" among some Russian authors,[^s5] and *cases conjuguées* in the French title of the first book devoted to it.[^s3]

## How the method works

The analysis starts from the end. First one identifies the critical squares: squares from which the attacking king wins outright, for instance by breaking through or by capturing a pawn. Then one asks, for each square next to them, where the defending king must stand to meet that threat, and works outward square by square.[^s6] The result is a map: each attacking-king square is paired with its defensive reply. The side whose king can follow the map keeps the balance; the side that can reach a square whose partner the opponent cannot reach in time wins.[^s6]

The opposition is the simplest case of this map, with the kings separated by one square on a file or rank. Dvoretsky's manual accordingly treats corresponding squares directly after key squares in its pawn-endgame chapter, before the opposition, "mined squares", triangulation and "other cases of correspondence".[^s4] Triangulation is the attacker's way of reaching a corresponding pair with the defender to move, when the defender has no matching triangle of his own.[^s4]

## Key example

The diagram FEN shows a position the Chess Programming Wiki attributes to C. D. Lockock (1892), White to move: White has king a1 and pawns d5, e4, g3; Black has king g8 and pawns d6, d7, g4.[^s6] White has two critical squares. From d4 the king threatens e4-e5 followed by Kxe5, so whenever White's king reaches d4 Black's king must be able to answer on f6. From e3 the king threatens Kf4 and Kxg4, so the answer to Ke3 is Kg5.[^s6] Working back from those two pairs gives the correspondences for the rest of the board. Averbakh described the case in which two corresponding squares touch diagonally and leave room for a 3x3 block as an "eight-square system", which lets the remaining squares be numbered quickly.[^s6]

## Beyond pawn endings

The method is not limited to kings. Dvoretsky shows a bishop ending in which White wins by handing Black the move, noting that the f3- and f7-squares obviously correspond; in another of his examples the c7-square corresponds both to c3 and to g3, so one piece can have more than one partner.[^s4] Kidambi charts a bishop-against-knight ending in which each knight square has a bishop square from which Black still covers the knight's entry points; he notes that he worked the chart out in reverse, and that the pairings create mutual zugzwang because the defender has no spare moves.[^s5]

## Pitfalls

The commonest error is to treat correspondence as a matter of distance alone. What matters is whose turn it is when the attacker arrives: the defender must already be on the partner square with the attacker to move, so a defender who is one tempo late loses even if his king is close.[^s1] A second error is to stop after finding one pair. A single missed correspondence lets the attacker reach a square with no reply, and a square can have more than one partner, so the map has to be built for every square the attacking king can use.[^s4][^s6]

## History and computers

Marcel Duchamp and Vitaly Halberstadt published *Opposition et cases conjuguées sont réconciliées* in Paris in 1932, through L'Echiquier, with text in French, English and German; a copy is held by the Philadelphia Museum of Art.[^s3] Kenneth Church turned the theory into a program in his 1978 MIT bachelor's thesis, supervised by Richard Greenblatt.[^s2] His IJCAI 1979 paper presents co-ordinate squares as a knowledge representation solved by constraint propagation, likened to Waltz's scene-analysis algorithm, and reports that endgames needing twenty to thirty plies of conventional tree search can be solved efficiently this way.[^s1] Later work included Mike Clarke's 1980 "Theory of Coordinate Squares"; the wiki notes that modern engines now solve such endings easily by search, while judging whether to enter a pawn ending remains the harder practical problem.[^s6]

## Connections

Corresponding squares belong to the theory of king-and-pawn endgames and rest on zugzwang. The opposition is their simplest special case, and triangulation is the standard way to gain the decisive tempo within such a system; Dvoretsky's manual groups all of them with key squares at the start of its pawn-endgame chapter.[^s4] The method's critical squares play the role that key squares play in simpler endings: they are the attacker's goal, and the correspondences describe the fight for access to them.[^s6] Duchamp and Halberstadt's 1932 book is an early full treatment,[^s3][^s6] and Church's thesis and IJCAI paper connect the topic to computer chess.[^s1][^s2]

## Sources
[^s1]: Kenneth Ward Church, "Co-ordinate Square: Solution to Many Chess Pawn Endgames", IJCAI 1979. https://ijcai.org/proceedings/1979/37 (accessed 2026-11-14)
[^s2]: Kenneth Ward Church, "Co-ordinate squares: a solution to many chess pawn endgames", B.S. thesis, MIT, 1978. https://dspace.mit.edu/handle/1721.1/154966 (accessed 2026-11-14)
[^s3]: Philadelphia Museum of Art Library and Archives, catalogue record for Duchamp and Halberstadt, *Opposition et cases conjuguées sont réconciliées* (1932). https://library.philamuseum.org/Record/000075230 (accessed 2026-11-14)
[^s4]: Mark Dvoretsky, *Dvoretsky's Endgame Manual*, 5th ed., Russell Enterprises, excerpt. https://shop.chess-tigers.de/cdn/shop/files/dem5_excerpt.pdf (accessed 2026-11-14)
[^s5]: Sundararajan Kidambi, "Theory of corresponding squares", ChessBase News, 2023. https://en.chessbase.com/post/theory-of-corresponding-squares-kidambi (accessed 2026-11-14)
[^s6]: Chess Programming Wiki, "Corresponding Squares". https://www.chessprogramming.org/Corresponding_Squares (accessed 2026-11-14)
