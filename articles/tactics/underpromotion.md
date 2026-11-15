---
id: kt:underpromotion
type: TacticalMotif
title: Underpromotion
aliases: [Under-promotion, Minor promotion, Knighting, Knight promotion, Rook promotion, Bishop promotion]
domain: tactics
summary: >-
  Promoting a pawn to a rook, bishop or knight instead of a queen, chosen either to avoid giving
  stalemate or to exploit the knight's move, which a queen cannot make.
fen: "2K5/1P5r/2k5/8/8/8/8/8 w - - 0 3"
status: current
volatile: false
verified: 2026-11-15
broader: [kt:chess-tactics]
related: [kt:saavedra-position, kt:albin-countergambit, kt:fork, kt:endgame-study, kt:excelsior]
relations:
  - {predicate: governedBy, object: kt:pawn-promotion}
  - {predicate: counters, object: kt:stalemate}
sources:
  - id: s1
    title: "FIDE Laws of Chess (applied from 1 January 2023), full text: Articles 3.7.3.3–3.7.3.5, 4.4.4, 4.6 and 7.5.2"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/
    type: governing-body
    accessed: 2026-11-15
  - id: s2
    title: "Endgame Explorations 6: Underpromotion (Part 1)"
    publisher: Noam D. Elkies (originally in Chess Horizons), via chabris.com
    url: https://www.chabris.com/pub/acj/extra/Elkies/Elkies06.html
    type: publication
    accessed: 2026-11-15
  - id: s3
    title: "Underpromotion in Chess"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/underpromotion.html
    type: reference
    accessed: 2026-11-15
  - id: s4
    title: "Pawn Promotion to Bishop or Rook in the Endgame Study (Interchess, 1996)"
    publisher: Harold van der Heijden (book listing, biblio.co.uk)
    url: https://biblio.co.uk/book/pawn-promotion-bishop-rook-endgame-study/d/1588419801
    type: book
    accessed: 2026-11-15
  - id: s5
    title: "A Guide To Underpromotion"
    publisher: GM Daniel Naroditsky, Chess.com
    url: https://www.chess.com/article/view/a-guide-to-underpromotion
    type: publication
    accessed: 2026-11-15
  - id: s6
    title: "The Rarest Chess Move: Underpromoting To A Bishop"
    publisher: NM Sam Copeland, Chess.com
    url: https://www.chess.com/blog/SamCopeland/the-rarest-chess-move-underpromoting-to-a-bishop
    type: publication
    accessed: 2026-11-15
created: 2026-11-15
---

# Underpromotion

Underpromotion is the choice, when a pawn reaches the last rank, of a rook, bishop or knight rather than a queen. The FIDE Laws allow any of the four pieces of the player's own colour, and the choice is not limited to pieces that have already been captured, so a player may have three knights or two light-squared bishops on the board.[^s1] The choice is final once the new piece has touched the promotion square, and a pawn left on the last rank after the clock is pressed is an illegal move that the arbiter corrects by putting a queen there.[^s1]

## Why promote to less than a queen

A queen can make every move a rook or a bishop can, so a lesser piece is only ever better because of what it *cannot* do or because of the one move the queen lacks. Naroditsky reduces the practical cases to two: avoiding a stalemate, and using the knight's unique jump.[^s5] Elkies draws the same line, calling knight promotions "positive" (they add knight moves the queen does not have) and rook or bishop promotions "negative" (they remove queen moves that would stalemate the opponent or allow a stalemate trick).[^s2]

- **Knight promotions** are the common kind. They usually come with check or a fork, or keep a mating net going. Copeland notes that knight underpromotions occur all the time in practical play.[^s6]
- **Rook promotions** are almost always about stalemate: the rook does the queen's job on the files and ranks without also covering the enemy king's last free diagonal squares.[^s2][^s5]
- **Bishop promotions** are the rarest. Copeland calls them nearly unheard of in practical play, citing Reshko–Kaminsky (1972) and Kholmov–Ehlvest (1983) as games where only the bishop won.[^s6] Van der Heijden devoted a whole study collection to bishop and rook promotions, with a history of the device and a classification of its themes.[^s4]

## Example: the knight saves the draw

Elkies gives a basic rook-against-pawn ending with White Kc7, pawn b6 against Black Kc5, rook h6, where White draws only by 1.b7 Rh7 2.Kc8 Kc6! 3.b8=N+!.[^s2] The diagram shows the moment before White's third move. Queening fails at once: after 3.b8=Q? Rh8 the queen blocks its own king's escape square, the black king covers b7, c7 and d7, and the rook check along the eighth rank is mate. The knight promotion comes with check and leaves the king room, so Black cannot keep both the attack and the material.[^s2]

## Example: the Lasker Trap

The best-known underpromotion in opening play ends the Lasker Trap of the Albin Countergambit: 1.d4 d5 2.c4 e5 3.dxe5 d4 4.e3? Bb4+ 5.Bd2 dxe3! 6.Bxb4 exf2+ 7.Ke2 fxg1=N+!.[^s2] Promoting to a queen on g1 would let White capture it with the rook, but the knight arrives with check, so White has no time to take it and Black wins material. Elkies points out that Black thereby gets a third knight as early as move seven.[^s2]

## In the historical record

Edward Winter has collected many practical instances, from Showalter–Robbins (St Louis, 1890), which ended with a knight promotion giving mate, to modern grandmaster games such as Adams–Miles (Tilburg, 1993) and Xiu Jun–Ivanchuk (Lucerne, 1993).[^s3] He also quotes Tim Krabbé's description of Babushkin–Postnikov (1969–70) as the only knighting on record that was not a check, while noting that René Olthof later published many more examples of non-checking knight promotions.[^s3]

## Pitfalls

- **Queening on autopilot.** The commonest error is promoting to a queen without checking whether the opponent has no legal moves left; Naroditsky advises looking at the enemy king's remaining squares before every promotion.[^s5]
- **Touching the wrong piece.** Over the board the choice is fixed as soon as the new piece touches the promotion square, so decide before reaching for a piece.[^s1]
- **Showing off.** A lesser piece is only justified when it achieves something the queen cannot; Copeland distinguishes forced bishop promotions from merely stylish ones.[^s6]

## Connections

Underpromotion is one of the **chess tactics** and exists only because the **pawn promotion** rule lets the player choose the new piece.[^s1] Its rook and bishop forms **counter** a **stalemate** defence, the theme of the **Saavedra position** and of many an **endgame study**, while the knight form usually works as a check or **fork**, as in the Lasker Trap of the **Albin Countergambit**.[^s2][^s5] Composers have made rook and bishop promotions a theme of their own in the endgame study, with van der Heijden's collection classifying the variants.[^s4] The **Excelsior**, a pawn-walk problem theme, is linked as a composition that often finishes with one; its own article gives the examples.

## Sources

[^s1]: FIDE Rules Commission, *FIDE Laws of Chess* (applied from 1 January 2023), Articles 3.7.3.3–3.7.3.5, 4.4.4, 4.6, 7.5.2. https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/ (accessed 2026-11-15)
[^s2]: Noam D. Elkies, "Endgame Explorations 6: Underpromotion (Part 1)", originally in *Chess Horizons*. https://www.chabris.com/pub/acj/extra/Elkies/Elkies06.html (accessed 2026-11-15)
[^s3]: Edward Winter, Chess Notes, "Underpromotion in Chess". https://chesshistory.com/winter/extra/underpromotion.html (accessed 2026-11-15)
[^s4]: Harold van der Heijden, *Pawn Promotion to Bishop or Rook in the Endgame Study* (Interchess, 1996), book listing. https://biblio.co.uk/book/pawn-promotion-bishop-rook-endgame-study/d/1588419801 (accessed 2026-11-15)
[^s5]: Daniel Naroditsky, "A Guide To Underpromotion", Chess.com. https://www.chess.com/article/view/a-guide-to-underpromotion (accessed 2026-11-15)
[^s6]: Sam Copeland, "The Rarest Chess Move: Underpromoting To A Bishop", Chess.com. https://www.chess.com/blog/SamCopeland/the-rarest-chess-move-underpromoting-to-a-bishop (accessed 2026-11-15)
