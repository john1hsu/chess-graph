---
id: kt:zugzwang
type: StrategicConcept
title: Zugzwang
aliases: [Compulsion to move, Mutual zugzwang, Reciprocal zugzwang, Full-point zugzwang, Zugzwang position, Zug]
domain: endgames
summary: >-
  A position in which the obligation to make a move is a disadvantage: the side to move would get a
  better result if it could pass. When this holds for both sides at once it is a mutual zugzwang, and
  the result depends only on whose turn it is.
fen: "8/8/8/8/8/p7/k2N4/2K5 b - - 0 1"
status: current
volatile: false
verified: 2026-11-09
broader: [kt:chess-strategy]
related: [kt:opposition, kt:triangulation, kt:key-squares, kt:endgame-tablebases, kt:endgame-study, kt:chess-problems]
relations:
  - {predicate: exemplifiedBy, object: kt:saemisch-nimzowitsch-copenhagen-1923}
  - {predicate: championedBy, object: kt:aron-nimzowitsch}
  - {predicate: contrastsWith, object: kt:stalemate}
sources:
  - id: s1
    title: "Zugzwang (Chess Notes feature article)"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://www.chesshistory.com/winter/extra/zugzwang.html
    type: reference
    accessed: 2026-11-09
  - id: s2
    title: "3-5 Man Mutual Zugzwangs in Chess"
    publisher: G.McC. Haworth, University of Reading; Computer Olympiad Workshop 6, Maastricht (ICGA, 2001)
    url: https://reading-clone.eprints-hosting.org/5950/1/2001g_CoW6_H_3-5-Man_Mutual_Zugzwangs_in_Chess.pdf
    type: academic
    accessed: 2026-11-09
  - id: s3
    title: "6-man Chess and Zugzwangs"
    publisher: Eiko Bleicher and Guy Haworth, University of Reading (CORE repository)
    url: https://core.ac.uk/download/12729.pdf
    type: academic
    accessed: 2026-11-09
  - id: s4
    title: "Mutual zugzwang in a pawn ending"
    publisher: Satanick Mukhuty, ChessBase India (3 September 2019)
    url: https://www.chessbase.in/news/Mutual-zugzwang-in-a-pawn-ending
    type: publication
    accessed: 2026-11-09
created: 2026-11-09
---

# Zugzwang

Zugzwang, German for "compulsion to move", describes a position in which having to move is a burden: the player on move would be better off if the rules allowed a pass.[^s1] Chess has no pass, so a player in zugzwang must make some move that weakens the position, gives up a key square or lets the opponent through.[^s4] The idea is most common in endgames, especially those with pawns, but it can also decide a middlegame, as in Nimzowitsch's best-known win, and it is a favourite theme of composed studies.[^s1][^s3]

## Definitions and types

Chess writers have never fully agreed on how narrow the term should be. Edward Winter's survey records Wolfgang Heidenfeld's strict view that zugzwang is the compulsion, as opposed to the right, to move; the *Oxford Companion to Chess* (1984) instead defined it as a position where each side would do worse if it were its turn; David Hooper separated true zugzwang from a "squeeze", in which the obligation to move is only the means of converting an advantage, while Hugh Myers argued for the broader reading.[^s1] Nimzowitsch, in *My System*, described it as a configuration in which any change can only harm the side that has to make it.[^s1]

Endgame tablebases made the idea precise. Guy Haworth's 2001 survey defines a *mutual zugzwang* as a position in which each side would get a better theoretical result if the other side were to move, and splits them into three kinds: a draw with White to move but a White win with Black to move; the mirror case for Black; and the "full-point" kind, in which whoever moves loses.[^s2] Scanning all endgames with up to five men, it found 21,677 White-win, 3,395 Black-win and only 33 full-point mutual zugzwangs, spread over 59 of 146 endgames; full-point cases appeared in just six, all of which contain pawns, among them king and pawn against king and pawn.[^s2] A later study by Eiko Bleicher and Haworth tested zugzwang with a "null move" (asking whether passing would improve the result), counted roughly 900,000 such positions in six-man endings, and found that pawns raise their density about fourfold.[^s3]

## Key position

In the `fen` above (White Kc1, Nd2; Black Ka2, pawn a3), taken from Haworth's tables, the knight-against-pawn ending is a mutual zugzwang of the White-win type: with White to move it is a draw, but with Black to move White wins.[^s2] The reason is visible on the board. Black's only legal move is 1...Ka1, because b1, b2 and b3 are covered and the pawn is blocked, so the black king is pushed into the corner where the knight and king can work against it; if White has to move instead, any knight or king move releases the bind.[^s2]

## How players use it

The practical skill is to reach the critical position with the opponent on move. In pawn endings that usually means *losing a tempo*: a spare pawn move, a triangle of king moves or a choice between a one-square and two-square pawn advance. ChessBase India's examples show both sides of this. In a study after Becker, the natural 1.b4 races to a queen ending that is a mutual zugzwang with White to move and only draws, while 1.b3, a deliberately slower move, reaches the same position with Black to move and wins.[^s4] In a pawn ending from André Chéron's treatise, one careless king step lets White fall into zugzwang himself, after which any White move drops the e-pawn.[^s4] The common mistake is therefore to count moves only for speed and forget to count whose turn it will be.[^s4]

## History of the term

Winter traces the word to German chess writing: an unsigned article on zugzwang appeared in the *Deutsche Schachzeitung* in September 1858, and in December 1896 the same magazine reported that White had "died of Zugzwang" in a Steinitz–Lasker match game.[^s1] The term was rare in English until Nimzowitsch's *My System* (1929) and became established in English sources in the 1930s, after translations such as "movebound" failed to catch on.[^s1] Nimzowitsch also made Sämisch v Nimzowitsch, Copenhagen 1923, famous as the "Immortal Zugzwang Game", ending with 25...h6, though Heidenfeld disputed whether it met the strict definition.[^s1]

## Connections

In **king-and-pawn endgames**, zugzwang is what the **opposition**, **key squares** and **triangulation** are for: they are ways of arranging for the opponent, rather than oneself, to be on move in the critical position, the same tempo-counting shown by the Becker and Chéron examples.[^s4] It should not be confused with **stalemate**: in a zugzwang the side to move still has legal moves, as Black does with 1...Ka1 in the key position, but every one of them makes things worse.[^s2] **Endgame tablebases** allowed every mutual zugzwang with few pieces to be catalogued, and Bleicher and Haworth note that such positions undermine the null-move heuristic, the engine assumption that having the move is always an advantage.[^s2][^s3] Zugzwang is also a recurring theme of the **endgame study**, where it often appears both in the main line and as the refutation of a plausible try.[^s3] Composers of block **chess problems** use the same compulsion. **Aron Nimzowitsch** popularised the word in English, and his Copenhagen 1923 win is its best-known illustration.[^s1]

## Sources

[^s1]: Edward Winter, "Zugzwang", Chess Notes feature article. https://www.chesshistory.com/winter/extra/zugzwang.html (accessed 2026-11-09)
[^s2]: G.McC. Haworth, "3-5 Man Mutual Zugzwangs in Chess", Computer Olympiad Workshop 6, Maastricht, 2001. https://reading-clone.eprints-hosting.org/5950/1/2001g_CoW6_H_3-5-Man_Mutual_Zugzwangs_in_Chess.pdf (accessed 2026-11-09)
[^s3]: Eiko Bleicher and Guy Haworth, "6-man Chess and Zugzwangs". https://core.ac.uk/download/12729.pdf (accessed 2026-11-09)
[^s4]: Satanick Mukhuty, "Mutual zugzwang in a pawn ending", ChessBase India, 3 September 2019. https://www.chessbase.in/news/Mutual-zugzwang-in-a-pawn-ending (accessed 2026-11-09)
