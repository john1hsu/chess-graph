---
id: kt:cutting-off-the-king
type: Technique
title: Cutting off the king
aliases: [Cut off the king, Cutting the king off, King cut off, Cut-off, Horizontal cut, Vertical cut, Cutting off along a rank, Cutting off along a file]
domain: endgames
summary: >-
  The endgame technique of using a rook (or another long-range piece) to control a whole file or rank so
  that the enemy king cannot cross it, keeping the defending king away from a passed pawn or confining it
  to the edge of the board.
fen: "6k1/R7/8/8/8/8/8/6K1 b - - 0 1"
status: current
volatile: false
verified: 2026-11-14
broader: [kt:rook-endgames, kt:chess-endgame]
related: [kt:lucena-position, kt:philidor-position, kt:king-and-pawn-endgames, kt:checkmate, kt:passed-pawn]
relations:
  - {predicate: enables, object: kt:lucena-position}
  - {predicate: alternativeTo, object: kt:shouldering}
  - {predicate: partOf, object: kt:rook-versus-pawn}
sources:
  - id: s1
    title: "Chess Fundamentals (1921), Project Gutenberg eBook #33870"
    publisher: José Raúl Capablanca; Project Gutenberg
    url: https://gutenberg.org/cache/epub/33870/pg33870-images.html
    type: book
    accessed: 2026-11-14
  - id: s2
    title: "Dvoretsky's Endgame Manual, 6th edition (sample pages)"
    publisher: Mark Dvoretsky, Russell Enterprises (excerpt hosted by De Beste Zet)
    url: https://www.debestezet.nl/catalog/images/PDF/Dvoretskys%20Endgame%20Manual%206th%20Edition.pdf
    type: book
    accessed: 2026-11-14
  - id: s3
    title: "100 Endgames You Must Know, sixth edition (sample pages)"
    publisher: Jesús de la Villa, New In Chess (excerpt hosted by Chess Tigers)
    url: https://shop.chess-tigers.de/cdn/shop/files/100endgames.pdf
    type: book
    accessed: 2026-11-14
  - id: s4
    title: "King, Rook and Pawn vs King and Rook – Part II"
    publisher: GM Matthew Sadler
    url: https://matthewsadler.me.uk/the-endgame/king-rook-pawn-vs-king-rook-part-ii/
    type: publication
    accessed: 2026-11-14
  - id: s5
    title: "Lone Pawn in Rook Endings: Number of Files Needed to Cut the King Off (Part 2)"
    publisher: Azel Chua (AdviceCabinet), Chess.com blog
    url: https://www.chess.com/blog/AdviceCabinet/lone-pawn-in-rook-endings-number-of-files-needed-to-cut-the-king-off-part-2
    type: community
    accessed: 2026-11-14
  - id: s6
    title: "Rook vs Pawn"
    publisher: Charlotte Chess Center, Endgame Column
    url: https://www.charlottechesscenter.org/post/rook-vs-pawn
    type: community
    accessed: 2026-11-14
  - id: s7
    title: "\"Simple\" Rook and Pawn vs Rook - Part 1: Cases Where the Pawn Wins"
    publisher: Charlotte Chess Center, Endgame Column
    url: https://www.charlottechesscenter.org/post/simple-rook-and-pawn-vs-rook-part-1-cases-where-the-pawn-wins
    type: community
    accessed: 2026-11-14
created: 2026-11-14
---

# Cutting off the king

Cutting off the king means placing a rook so that it controls an entire file or rank the enemy king would need to cross. Because a king cannot step onto an attacked square, the line becomes a wall: the defending king is held on one side of it, away from a passed pawn or pinned against the edge of the board. It is one of the most frequently used ideas in rook endings, and endgame manuals treat it as a technique in its own right: *Dvoretsky's Endgame Manual* has sections titled "Cutting the King Off" both in its chapter on rook against one pawn and among its general endgame ideas.[^s2]

## The first example: mating with king and rook

Most players meet the idea in the basic mate with king and rook against king. Capablanca's *Chess Fundamentals* opens its endgame examples with this mate and explains that the first rook move to the seventh rank immediately confines the black king to the last rank; the white king then walks up, and when the black king tries to slip out the rook shifts to keep the wall in place until the rook mates on the back rank.[^s1] In his next example the rook checks the king back towards the edge and stays close so that the king is confined to as few squares as possible.[^s1] The diagram position (FEN above) shows the same geometry: with the rook on a7, the black king on g8 has only the eighth rank to move along.

## Cutting along a file

In rook and pawn against rook, the attacker's rook usually cuts the defending king off from the pawn along a file. How many files of separation are needed depends on the pawn. Matthew Sadler, summarising rules he credits to Jesús de la Villa's terminology, gives the case of a bishop's pawn on the fourth rank: with the king cut off by only one file the defender can hold if the king stays active, but with a two-file cut White wins.[^s4] Azel Chua's Chess.com analysis extends the count: with a knight's pawn a two-file cut draws in his example while three files wins easily, and with a rook's pawn even three files draws while four files wins, after long variations.[^s5] The further the pawn is from the centre, the less room the attacking king has to escape checks, so a wider cut is needed. The Charlotte Chess Center's teaching sequence for the **Lucena position** makes the cut its first and most important step: keep the defending king off the pawn's file, advance the pawn to the seventh, drive the king further away with checks, then build the bridge.[^s7] For a rook's pawn on the seventh, where the bridge does not work, the same column says the king must be driven much further away, five files rather than three.[^s7]

## Cutting along a rank

The cut can also run horizontally. De la Villa calls cutting off the king "a very important resource" when the kings and pawn are still far from the promotion square, and notes that in rook against pawn it works most clearly against a rook's pawn or when king and pawn are already separated.[^s3] The Charlotte Chess Center's endgame column states a practical boundary for rook against pawn: the rook side wins if it can cut the king off on the fifth rank or further from its own point of view, while a cut on the fourth rank or closer tends to draw unless the defending king is out of play.[^s6] Sadler ranks a full "horizontal cut" as more powerful than a "half cut" and warns defenders not to let their king be cut off along a rank when facing a passed pawn.[^s4]

## Examples from practice

Dvoretsky's manual shows that the technique cuts both ways. In Yusupov–Tseshkovsky, Moscow 1981, Black won with rook and pawns by cutting the white king off along the fourth rank with a rook check, after which the passed pawn could not be stopped.[^s2] In Karjakin–Volokitin, Istanbul Olympiad 2012, White's rook move to the fourth rank both gained a tempo and cut off the king, and the black king ended on the wrong side of the pawn.[^s2] In the opposite direction, in Larsen–Torre, Leningrad Interzonal 1973, the defending rook cut the attacking king off from both of his pawns and the game was drawn.[^s2]

## Pitfalls

- **Cutting too late or too close.** A cut that leaves the king near the pawn's path can be undone; in rook against pawn the rank on which the cut happens often decides the result.[^s6]
- **Choosing the wrong rook move.** In de la Villa's rook-against-pawn example only the rook move that cuts the king off along a rank wins, while an alternative rook move lets the defending king approach and draw.[^s3]
- **Forgetting the defender's checks.** A one-file cut against an active defending king can be broken by checks and counterplay, which is why the number of files matters.[^s4]

## Connections

The technique belongs to **rook endgames** and the wider **chess endgame**. It **enables** the **Lucena position**, whose winning method starts with the cut,[^s7] and it is the thing a defender in the neighbouring **Philidor position** is trying to avoid. It is part of the theory of **rook versus pawn**, where Dvoretsky lists it beside outflanking and **shouldering**, the king-based alternative for holding the enemy king back.[^s2] Capablanca's rook mate links it to **checkmate**,[^s1] and a well-cut king often means a **passed pawn** that can be escorted home, or a rook trade into a won **king and pawn endgame**.[^s5]

## Sources
[^s1]: J. R. Capablanca, *Chess Fundamentals* (1921), Project Gutenberg eBook #33870. https://gutenberg.org/cache/epub/33870/pg33870-images.html (accessed 2026-11-14)
[^s2]: M. Dvoretsky, *Dvoretsky's Endgame Manual*, 6th edition, Russell Enterprises, sample pages. https://www.debestezet.nl/catalog/images/PDF/Dvoretskys%20Endgame%20Manual%206th%20Edition.pdf (accessed 2026-11-14)
[^s3]: J. de la Villa, *100 Endgames You Must Know*, 6th edition, New In Chess, sample pages. https://shop.chess-tigers.de/cdn/shop/files/100endgames.pdf (accessed 2026-11-14)
[^s4]: M. Sadler, "King, Rook and Pawn vs King and Rook – Part II". https://matthewsadler.me.uk/the-endgame/king-rook-pawn-vs-king-rook-part-ii/ (accessed 2026-11-14)
[^s5]: A. Chua, "Lone Pawn in Rook Endings: Number of Files Needed to Cut the King Off (Part 2)", Chess.com. https://www.chess.com/blog/AdviceCabinet/lone-pawn-in-rook-endings-number-of-files-needed-to-cut-the-king-off-part-2 (accessed 2026-11-14)
[^s6]: Charlotte Chess Center, "Rook vs Pawn", Endgame Column. https://www.charlottechesscenter.org/post/rook-vs-pawn (accessed 2026-11-14)
[^s7]: Charlotte Chess Center, "\"Simple\" Rook and Pawn vs Rook - Part 1: Cases Where the Pawn Wins". https://www.charlottechesscenter.org/post/simple-rook-and-pawn-vs-rook-part-1-cases-where-the-pawn-wins (accessed 2026-11-14)
