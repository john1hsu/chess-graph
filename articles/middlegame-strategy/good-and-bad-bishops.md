---
id: kt:good-and-bad-bishops
type: StrategicConcept
title: Good and bad bishops
aliases: [Bad bishop, Good bishop, Good bishop versus bad bishop, Bad bishops, Good bishops]
domain: middlegame-strategy
summary: >-
  The distinction between a bishop whose scope is free of its own pawns (a "good" bishop) and one
  hemmed in by its own pawns fixed on squares of its colour (a "bad" bishop); because pawn chains
  change slowly, the difference is semi-permanent and shapes plans, exchanges and endgames.
fen: "2b5/4k3/4p1p1/1pNpP2p/1P1P1K1P/6P1/8/8 b - - 0 1"
status: current
volatile: false
verified: 2026-11-11
broader: [kt:chess-strategy, kt:pawn-structure]
related: [kt:bishop-pair, kt:french-defence, kt:outpost, kt:blockade, kt:opposite-coloured-bishops]
relations:
  - {predicate: championedBy, object: kt:jose-raul-capablanca}
  - {predicate: contrastsWith, object: kt:knight-versus-bishop}
sources:
  - id: s1
    title: "Chess Fundamentals (section 14, 'The Relative Value of Knight and Bishop')"
    publisher: José Raúl Capablanca, 1921; Project Gutenberg edition
    url: https://gutenberg.org/cache/epub/33870/pg33870-images.html
    type: book
    accessed: 2026-11-11
  - id: s2
    title: "The Secret Life of Bad Bishops (sample pages)"
    publisher: Esben Lund, Quality Chess, 2014; excerpt hosted by New In Chess
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/7438.pdf
    type: book
    accessed: 2026-11-11
  - id: s3
    title: "Bishop (chess)"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/bishop-chess
    type: reference
    accessed: 2026-11-11
  - id: s4
    title: "Understanding before Moving 43: Good bishops, bad bishops"
    publisher: Herman Grooten, ChessBase News (16 September 2021)
    url: https://en.chessbase.com/newsroom/post/understanding-before-moving-43-good-bishops-bad-bishops
    type: publication
    accessed: 2026-11-11
  - id: s5
    title: "Understanding before Moving 18: The bad bishop"
    publisher: Herman Grooten, ChessBase News (14 March 2021)
    url: https://en.chessbase.com/post/understanding-before-moving-18-the-bad-bishop
    type: publication
    accessed: 2026-11-11
  - id: s6
    title: "How Bad is a Bad Bishop?"
    publisher: WIM Iryna Zenyuk, Chess.com (updated 26 May 2009)
    url: https://www.chess.com/article/view/how-bad-is-a-bad-bishop?page=2
    type: publication
    accessed: 2026-11-11
  - id: s7
    title: "Bad Bishop"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/Bad_Bishop
    type: community
    accessed: 2026-11-11
created: 2026-11-11
---

# Good and bad bishops

A bishop is confined to squares of one colour, so its strength depends heavily on where the pawns stand, above all its own.[^s3][^s1] When a side's pawns are fixed on squares of its bishop's colour, they block the bishop's diagonals; such a piece is called a **bad bishop**. A bishop whose own pawns sit on the other colour, leaving its diagonals open, is a **good bishop**.[^s4] Herman Grooten's rule of thumb is that the bishop suffers most when those pawns are also blocked, because then they cannot move out of its way.[^s4] Britannica uses the same sense, describing the good bishop as the one less encumbered by pawns.[^s3]

## Why it matters

Capablanca argued that a piece's value can often be judged by the number of squares it commands, so pawns on the bishop's colour reduce its worth directly.[^s1] From that he drew two working rules: with a bishop of your own, keep your pawns on the opposite colour; against an enemy bishop, keep them on its colour, especially passed pawns that your king can support. He added that the rules must sometimes bend to the position.[^s1] The Chess Programming Wiki notes why engines treat the bad bishop as a separate evaluation term rather than ordinary low mobility: the restriction is semi-permanent, more so when the position is blocked.[^s7]

The worst case combines two kinds of wall. Grooten describes a bishop shut out by enemy pawns and also obstructed by its own as effectively a dead piece and a spectator, which lets the opponent concentrate pieces of the other colour where the bishop can never contest them.[^s5] Zenyuk's image is a bishop with no operational space that resembles a rather big pawn.[^s6]

## Nuances and exceptions

- **Outside or inside the chain.** A bishop that has been developed in front of its pawn chain is much less of a liability than one stuck behind it; the Chess Programming Wiki cites the Slav bishop on f5, and notes that some programs, such as Crafty, only score a bishop as bad when its forward mobility is impaired.[^s7]
- **Bad but useful.** A bishop that looks bad can still defend key squares or pawns, or bear on enemy pieces, and may be worth keeping; Zenyuk warns against trading it automatically.[^s6]
- **Good or bad depends on the other pieces.** Esben Lund argues that the usual good/bad labels are simplified and misleading. He prefers to speak of a double-edged bishop whose worth turns on which pieces remain, and he points out that pawns on the bishop's colour are at least protected by it, which can suit a side that attacks on one wing and only needs to hold the other.[^s2]

## Typical plans

For the side with the bad bishop, the main remedies are to exchange it, to bring it outside the pawn chain, or to change the structure with pawn breaks that open its diagonals.[^s6][^s7] Zenyuk's examples turn on pawn breaks such as c5 for a bishop on b7 buried behind pawns on a6, b5 and c6, or f4–f5 to open the other side's position.[^s6] For the opponent, the aim is the reverse: keep the structure fixed, avoid letting the bad bishop be exchanged or freed, and steer towards simplification so that a good knight or good bishop faces a bad bishop in the ending.[^s5][^s4] Grooten notes that these imbalances are especially telling in endgames, citing a study by Yuri Averbakh in which a bishop blocked by its own pawns loses against a free one.[^s4]

## Illustrative position

The diagram position (constructed for this article, Black to move) shows the pattern in pure form. All of Black's pawns (b5, d5, e6, g6, h5) stand on light squares and are fixed by White pawns on dark squares, so the c8-bishop can only shuffle between c8, b7, a6 and d7. White's knight on c5 sits on a dark square that the bishop can never attack, and White's king and pawns also live on dark squares, out of the bishop's reach. This is Capablanca's colour rule applied by both sides: White's pawns are on the colour opposite the bishop's, Black's on the same.[^s1][^s4]

## Connections

Good and bad bishops are a core theme of **chess strategy** and follow directly from **pawn structure**, since the structure decides which bishop is restricted.[^s1][^s4] The **French Defence** is a standard opening case, since Black's e6–d5 chain stands on light squares in front of the c8-bishop. The theme is also linked to the **bishop pair**, whose value drops when one of the bishops is bad, and to **opposite-coloured bishops**, where the colour of the fixed pawns often decides the result.[^s2][^s3] A bad bishop's opponent often posts a knight on an **outpost** of the other colour, the classic **knight versus bishop** contrast, and a fixed pawn chain acts as a **blockade** of the bishop's diagonals.[^s5][^s6] **José Raúl Capablanca** (championed by) gave the best-known statement of the colour rules.[^s1]

## Sources
[^s1]: J. R. Capablanca, *Chess Fundamentals* (1921), section 14, "The Relative Value of Knight and Bishop", Project Gutenberg. https://gutenberg.org/cache/epub/33870/pg33870-images.html (accessed 2026-11-11)
[^s2]: E. Lund, *The Secret Life of Bad Bishops*, Quality Chess, 2014, sample pages. https://www.newinchess.com/media/wysiwyg/product_pdf/7438.pdf (accessed 2026-11-11)
[^s3]: Encyclopaedia Britannica, "Bishop (chess)". https://www.britannica.com/topic/bishop-chess (accessed 2026-11-11)
[^s4]: H. Grooten, "Understanding before Moving 43: Good bishops, bad bishops", ChessBase News, 16 September 2021. https://en.chessbase.com/newsroom/post/understanding-before-moving-43-good-bishops-bad-bishops (accessed 2026-11-11)
[^s5]: H. Grooten, "Understanding before Moving 18: The bad bishop", ChessBase News, 14 March 2021. https://en.chessbase.com/post/understanding-before-moving-18-the-bad-bishop (accessed 2026-11-11)
[^s6]: I. Zenyuk, "How Bad is a Bad Bishop?", Chess.com (updated 26 May 2009). https://www.chess.com/article/view/how-bad-is-a-bad-bishop?page=2 (accessed 2026-11-11)
[^s7]: Chess Programming Wiki, "Bad Bishop". https://www.chessprogramming.org/Bad_Bishop (accessed 2026-11-11)
