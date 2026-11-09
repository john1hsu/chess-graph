---
id: kt:stalemate
type: Rule
title: Stalemate
aliases: [Stale mate, Stale, Draw by stalemate, Mate ahogado]
domain: rules-and-notation
summary: >-
  The rule that a game is drawn when the player to move has no legal move and their king is not in
  check; once a win or a loss depending on time and place, it has been a draw everywhere since the
  mid-nineteenth century.
fen: "k7/2Q5/1K6/8/8/8/8/8 b - - 0 1"
status: current
volatile: true
verified: 2026-11-09
broader: [kt:fide-laws-of-chess, kt:draw]
related: [kt:zugzwang, kt:king-and-pawn-endgames, kt:endgame-study, kt:chaturanga, kt:en-passant]
relations:
  - {predicate: partOf, object: kt:fide-laws-of-chess}
  - {predicate: contrastsWith, object: kt:checkmate}
  - {predicate: contrastsWith, object: kt:zugzwang}
  - {predicate: contrastsWith, object: kt:dead-position}
sources:
  - id: s1
    title: "Laws of Chess, Article 5: The Completion of the Game"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/article5/
    type: governing-body
    accessed: 2026-11-09
  - id: s2
    title: "Stalemate"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://www.chesshistory.com/winter/extra/stalemate.html
    type: reference
    accessed: 2026-11-09
  - id: s3
    title: "The Evolution of Modern Chess Rules: Stalemate"
    publisher: John McCrary, US Chess
    url: https://new.uschess.org/news/evolution-modern-chess-rules-stalemate
    type: publication
    accessed: 2026-11-09
  - id: s4
    title: "Chess: Object of the game (stalemate)"
    publisher: Encyclopaedia Britannica
    url: https://britannica.com/EBchecked/topic/562613/stalemate
    type: reference
    accessed: 2026-11-09
  - id: s5
    title: "Who needs stalemate? Let's abolish it!"
    publisher: Matt Bishop, ChessBase News
    url: https://en.chessbase.com/post/who-needs-stalemate-let-s-abolish-it-
    type: publication
    accessed: 2026-11-09
created: 2026-11-09
---

# Stalemate

Stalemate is the position in which the player whose turn it is has no legal move but is not in check. In the FIDE Laws of Chess, as published by the FIDE Rules Commission as of November 2026, Article 5.2.1 declares the game drawn in that case, and the result is immediate provided the move that produced the position was itself legal.[^s1] Britannica lists stalemate among the standard ways a game ends in a draw, alongside threefold repetition and the fifty-move rule.[^s4] The same article of the Laws treats the neighbouring **dead position**, where neither side can checkmate by any series of legal moves, as a separate drawing rule.[^s1]

## How the rule works

Two conditions must both hold: no piece or pawn of the side to move has a legal move, and that side's king is not attacked. If the king is attacked and there is no legal move, it is checkmate instead.[^s1] The rule follows from the principle that a player may never move into check: a king with only attacked squares around it cannot move at all, and if nothing else can move either, play simply stops.[^s5]

A textbook illustration is the key position above (Black to move: Black king a8; White king b6, queen c7). The black king is not in check, but a7, b7 and b8 are all covered, so Black has no legal move and the game is drawn on the spot under Article 5.2.1.[^s1] The stronger side has hemmed the lone king in one move too early; a queen move that left a flight square, or a check, would have kept the win alive.

## History: win, loss or draw

The rule has not always been a draw. John McCrary, a former US Chess president, notes that before the nineteenth century stalemate was variously treated as illegal, as a win or half-win for the side delivering it, as a loss for that side, or as a draw.[^s3] Edward Winter cites Lucena (1497) recording that in Spain the stalemated player lost half the stake, while the Italian school counted it a draw.[^s2] England went the other way: Arthur Saul's *The Famous Game of Chesse-play* (1614) called stalemate a lost game for the player who gives it, a rule repeated in English books into the eighteenth century and still defended by Peter Pratt in the early 1800s.[^s2][^s3] Winter quotes Murray crediting J.H. Sarratt and the London Chess Club with adopting the Continental draw in the early nineteenth century, and McCrary dates the draw as universal by the mid-1800s.[^s2][^s3]

The debate never fully stopped. Winter records Capablanca arguing in 1919 that the old rule was more logical and proposing at Nottingham in 1936 that the materially superior side receive a fraction of a point, and T.H. Tylor's 1940 *BCM* essay "The Stalemate Fallacy".[^s2] A 2012 ChessBase reader article revived the case, listing Capablanca, Réti, Lasker and Nimzowitsch among players who had favoured a change.[^s5]

## Practical consequences

- Stalemate is a key defensive resource in the endgame. The ChessBase piece points out that if stalemate were a win, king and pawn against king would become far easier, and a fair share of rook-and-pawn against rook positions would become winnable, because many standard draws rest on it.[^s5]
- The defender can also seek stalemate actively by offering the last mobile pieces. Winter collects games such as Walbrodt v von Scheve, Berlin 1891, which ended 81...Qd6+ 82 Kxd6 stalemate, and Maliutin v Gregory, Breslau 1912, ended by 47 Kxh1 stalemate.[^s2]
- Under the old English rule the stalemated side won, so a player could play deliberately for self-stalemate; McCrary shows a position in which one capture stalemates the opponent and another forces the opponent to stalemate oneself, the two moves swapping value as the rule changes.[^s3]

## Connections

Stalemate is part of the **FIDE Laws of Chess** (Article 5) and one of the ways a game ends in a **draw**, distinct from **checkmate**, which requires the king to be in check, and from a **dead position**, where moves remain but mate is impossible.[^s1] It contrasts with **zugzwang**, where the side to move still has legal moves but all of them hurt, and it underpins many drawing methods in **king-and-pawn endgames**.[^s5] Stalemate traps are a staple of the **endgame study**, and the shifting rule traced back through Lucena and Saul links it to the older games descended from **chaturanga**.[^s2][^s3]

## Sources

[^s1]: FIDE Rules Commission, "Laws of Chess, Article 5: The Completion of the Game". https://rcc.fide.com/article5/ (accessed 2026-11-09)
[^s2]: Edward Winter, Chess Notes, "Stalemate". https://www.chesshistory.com/winter/extra/stalemate.html (accessed 2026-11-09)
[^s3]: John McCrary, US Chess, "The Evolution of Modern Chess Rules: Stalemate" (2021). https://new.uschess.org/news/evolution-modern-chess-rules-stalemate (accessed 2026-11-09)
[^s4]: Encyclopaedia Britannica, "Chess: Object of the game" (stalemate). https://britannica.com/EBchecked/topic/562613/stalemate (accessed 2026-11-09)
[^s5]: Matt Bishop, ChessBase News, "Who needs stalemate? Let's abolish it!" (2012). https://en.chessbase.com/post/who-needs-stalemate-let-s-abolish-it- (accessed 2026-11-09)
