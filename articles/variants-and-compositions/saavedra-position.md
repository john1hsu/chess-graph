---
id: kt:saavedra-position
type: Game
title: Saavedra position
aliases: [Saavedra study, Saavedra's study, Barbier–Saavedra study, Saavedra rook promotion]
domain: variants-and-compositions
summary: >-
  The most famous endgame study, published in Glasgow in 1895: White (Kb6, Pc6) beats a lone rook
  (Black Ka1, Rd5) only by escaping the checks and then promoting to a rook instead of a queen, which
  avoids a stalemate trap. The win is credited to Fernando Saavedra, though its origin is disputed.
fen: "8/8/1KP5/3r4/8/8/8/k7 w - - 0 1"
status: current
volatile: false
verified: 2026-11-14
broader: [kt:endgame-study]
related: [kt:pawn-promotion, kt:stalemate, kt:rook-endgames, kt:chess-composition]
relations:
  - {predicate: namedAfter, object: kt:fernando-saavedra}
  - {predicate: usesTechnique, object: kt:underpromotion}
  - {predicate: developedBy, object: kt:georges-barbier}
sources:
  - id: s1
    title: "The discovery of the Saavedra (with the 1895 Weekly Citizen columns)"
    publisher: Tim Krabbé, Chess Curiosities
    url: https://timkr.home.xs4all.nl/chess/saavedra.htm
    type: primary-record
    accessed: 2026-11-14
  - id: s2
    title: "The Messenger – the Saavedra myth exposed"
    publisher: Tim Krabbé, Chess Curiosities
    url: https://timkr.home.xs4all.nl/chess2/prynd.htm
    type: publication
    accessed: 2026-11-14
  - id: s3
    title: "Fernando Saavedra"
    publisher: Chess Scotland, history biographies (Alan McGowan)
    url: https://www.chessscotland.com/documents/history/biographies/saavedra.htm
    type: publication
    accessed: 2026-11-14
  - id: s4
    title: "Endgame Explorations 6: Underpromotion (Part 1)"
    publisher: Noam D. Elkies (Harvard), originally in Chess Horizons; ACJ Extra
    url: https://chabris.com/pub/acj/extra/Elkies/Elkies06.html
    type: publication
    accessed: 2026-11-14
  - id: s5
    title: "Chess: Chess composition"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/chess/Chess-composition
    type: reference
    accessed: 2026-11-14
created: 2026-11-14
---

# Saavedra position

The Saavedra position is a four-piece ending (White king b6 and pawn c6; Black king a1 and rook d5; White to play and win) whose solution ends with the pawn promoting to a rook rather than a queen. A. J. Roycroft called it "unquestionably the most famous of all endgame studies", and the Oxford Companion to Chess credits it with inspiring later composers such as Liburkin and Lommer.[^s3] It is the standard textbook example of an underpromotion forced by the need to avoid stalemate.[^s4]

## The solution

White's first move is obvious, 1.c7, and Black can only answer with rook checks along the d-file. The point of White's king walk is to approach the rook while staying out of reach of the alternatives: Elkies shows that 2.Kb5! is necessary, because the tempting 2.Kb7? Rd7 or 2.Kc5? Rd1 lets Black hold.[^s4] Play then runs 2...Rd5+ 3.Kb4 Rd4+ 4.Kb3 Rd3+ (or 4.Kc3 Rd1) 5.Kc2, and the checks are exhausted.[^s4]

Black's last resource is 5...Rd4!, setting a trap. If White queens with 6.c8=Q?, then 6...Rc4+! 7.Qxc4 leaves Black's king on a1 with no legal move, and the game is a stalemate draw.[^s3][^s4] The winning move is 6.c8=R!!. The rook cannot be lured into the same stalemate, but it threatens Ra8 mate, so Black must play 6...Ra4; then 7.Kb3 attacks the rook and threatens Rc1 mate at the same time, and Black can only delay the end by giving up the rook.[^s3][^s4]

```pgn
[Event "Saavedra position (Glasgow Weekly Citizen, 1895)"]
[SetUp "1"]
[FEN "8/8/1KP5/3r4/8/8/8/k7 w - - 0 1"]
[Result "1-0"]

1. c7 Rd6+ 2. Kb5 Rd5+ 3. Kb4 Rd4+ 4. Kc3 Rd1 5. Kc2 Rd4 6. c8=R Ra4 7. Kb3 1-0
```

## How the study appeared in 1895

The position grew out of a newspaper column. In the *Glasgow Weekly Citizen* of 27 April 1895, Georges Barbier recalled an ending from a game between W. N. Potter and Fenton in which the players had agreed a draw, believing the pawn could only be traded for the rook.[^s1][^s3] On 4 May Barbier gave a stalemating drawing line and printed his own version of the position as "Black moves and draws"; the solution followed on 11 May.[^s1] On 18 May he reversed himself: a member of the Glasgow club, the Reverend Fernando Saavedra, had found that White wins, and the corrected solution with the rook promotion appeared on 25 May, Barbier calling it one of the most remarkable endings he had seen in years.[^s1][^s3] Barbier's columns contained slips of their own, including a mix-up of White and Black, and John Selman showed in 1940 that Barbier had recalled the Potter game wrongly.[^s1]

Saavedra (1847–1922) was a Spanish-born member of a religious order who played for the West of Scotland in inter-district matches in the 1890s; Krabbé describes him as a modest player made famous by a single move.[^s3][^s2] Later historians, among them Roycroft, Ian Mullen, Edward Winter and Tim Krabbé, have reconstructed the story from the original columns.[^s3]

## The attribution dispute

In August 2001 the Irish historian David McAlister found that on 25 May 1895, the same day as Barbier's solution, J. A. Porterfield Rynd's column in the Dublin *Saturday Herald* published a simultaneous game Rynd had played at the Clontarf club against W. Lynam, ending in the same rook promotion.[^s2] Saavedra had been a Clontarf member, and Krabbé concludes that the idea was first found in that game and that Saavedra most likely carried it to Glasgow as a messenger rather than as its discoverer, while finding no clear evidence of deliberate dishonesty.[^s2] The position had earlier been misattributed in other ways too, including to Emanuel Lasker and as a game rather than a study.[^s2] The name "Saavedra position" has nevertheless stuck.

## Lessons for practical play

Composers use underpromotion, stalemate and sacrifice as recurring study themes, and this study combines the first two in their purest form.[^s5] Elkies stresses that a rook promotion is a purely negative choice: a queen can make every move a rook can, so promoting to a rook only makes sense when the queen's extra power would hand the opponent a stalemate.[^s4] For a club player the practical habit is to check, before queening against a cornered king, whether the defender has a forcing check or capture that leaves him without moves. The king walk also teaches how to approach a checking rook diagonally so that the final check can be met.

## Connections

The Saavedra position is the best-known **endgame study** and a classic piece of **chess composition**.[^s5] It is **named after** Fernando Saavedra, who found or relayed the win, and was **developed by** **Georges Barbier**, who composed the setting from a half-remembered game.[^s1][^s3] Its key move is an **underpromotion**, a special case of **pawn promotion**, chosen to avoid **stalemate**.[^s4] The material, rook against an advanced pawn, makes it a cousin of practical **rook endgames**.[^s4]

## Sources
[^s1]: Tim Krabbé, "The discovery of the Saavedra", Chess Curiosities, reproducing Georges Barbier's *Glasgow Weekly Citizen* columns of 27 April to 25 May 1895. https://timkr.home.xs4all.nl/chess/saavedra.htm (accessed 2026-11-14)
[^s2]: Tim Krabbé, "The Messenger – the Saavedra myth exposed", Chess Curiosities. https://timkr.home.xs4all.nl/chess2/prynd.htm (accessed 2026-11-14)
[^s3]: Alan McGowan, "Fernando Saavedra", Chess Scotland history biographies. https://www.chessscotland.com/documents/history/biographies/saavedra.htm (accessed 2026-11-14)
[^s4]: Noam D. Elkies, "Endgame Explorations 6: Underpromotion (Part 1)", originally in *Chess Horizons*; ACJ Extra. https://chabris.com/pub/acj/extra/Elkies/Elkies06.html (accessed 2026-11-14)
[^s5]: Encyclopaedia Britannica, "Chess: Chess composition". https://www.britannica.com/topic/chess/Chess-composition (accessed 2026-11-14)
