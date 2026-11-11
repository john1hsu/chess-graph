---
id: kt:checkmate
type: Rule
title: Checkmate
aliases: [Mate, Check mate, Shah mat, Checkmating the king]
domain: rules-and-notation
summary: >-
  The position in which a player's king is in check and that player has no legal move to escape
  it; delivering it is the object of the game and wins immediately under the FIDE Laws of Chess.
fen: "7k/6Q1/6K1/8/8/8/8/8 b - - 0 1"
status: current
volatile: true
verified: 2026-11-11
broader: [kt:fide-laws-of-chess]
related: [kt:double-check, kt:back-rank-mate, kt:helpmate, kt:shatranj, kt:chess-tactics]
relations:
  - {predicate: partOf, object: kt:fide-laws-of-chess}
  - {predicate: contrastsWith, object: kt:stalemate}
  - {predicate: contrastsWith, object: kt:dead-position}
sources:
  - id: s1
    title: "FIDE Laws of Chess (full text, applied from 1 January 2023)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/
    type: governing-body
    accessed: 2026-11-11
  - id: s2
    title: "When does a game of chess end?"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/question/When-does-a-game-of-chess-end
    type: reference
    accessed: 2026-11-11
  - id: s3
    title: "Fool's Mate"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/foolsmate.html
    type: reference
    accessed: 2026-11-11
  - id: s4
    title: "mate / checkmate"
    publisher: David Wilton, Wordorigins.org
    url: https://www.wordorigins.org/big-list-entries/mate
    type: publication
    accessed: 2026-11-11
  - id: s5
    title: "Shatranj"
    publisher: Hans Bodlaender and John William Brown, The Chess Variant Pages
    url: https://chessvariants.com/historic.dir/shatranj.html
    type: community
    accessed: 2026-11-11
created: 2026-11-11
---

# Checkmate

Checkmate is the end point that the whole game is built around. Article 1.4 of the FIDE Laws of Chess, in the edition applied from 1 January 2023 and still the current text as of November 2026, states each player's objective as attacking the opponent's king so that the opponent has no legal move.[^s1] Article 5.1.1 adds that the player who checkmates the opponent's king wins, and that the game ends at once, provided the mating move was itself legal.[^s1] Britannica puts the same idea in everyday terms: the game is decided when a king is attacked and cannot avoid capture.[^s2]

## How the rule works

Checkmate depends on the definition of **check**. Under Article 3.9.1 a king is in check when one or more enemy pieces attack it, and this holds even if the attacker is pinned against its own king and could not legally move to the king's square.[^s1] Article 3.9.2 forbids any move that exposes one's own king to check or leaves it in check.[^s1] It follows that a player in check may only make moves that end the check: moving the king to a safe square, capturing the checking piece, or putting a piece between a long-range checker and the king. When none of these exists, the king is mated. The king is never actually captured; the game stops one move earlier.[^s1][^s2]

The key position above shows the simplest pattern (Black to move: Black king h8; White king g6, queen g7). The queen gives check from g7, the black king cannot take it because the white king guards g7, and every other square next to the king is covered, so it is checkmate. Move the white king away from g6 and the same queen move would only be check, because Black could capture on g7.[^s1]

## How checkmate interacts with other rules

- **Priority over draws.** Article 9.6 makes a game drawn automatically after a fivefold repetition or 75 moves without a capture or pawn move, but adds that a checkmate on the last move takes precedence.[^s1]
- **Time and resignation.** A player who runs out of time loses under Article 6.9, except that the game is drawn if the opponent could not checkmate by any series of legal moves; Article 5.1.2 applies the same test to a resignation.[^s1] So whether mate is still possible decides results even when no mate is played.
- **Not stalemate, not a dead position.** If the side to move has no legal move but is not in check, the game is a stalemate and a draw (Article 5.2.1); if neither side can ever mate, it is a dead position and also a draw (Article 5.2.2).[^s1] Britannica lists these alongside agreement as ways a game can be drawn instead of decided.[^s2]

## Shortest mates and common pitfalls

The fastest possible mate is the two-move **Fool's Mate**, in which White weakens the e1–h4 diagonal with both the f- and g-pawns and Black's queen mates on h4. Edward Winter traces the pattern to Arthur Saul's English manual of 1614, which described a "mate at two draughts", and notes that the term itself appears in the 1618 edition cited by the *Oxford English Dictionary*.[^s3] It has occurred in serious play: Winter records Boruchowitz v Koltanowski, Belgian Championship, Antwerp 1922, which ended 1 f3 e5 2 g4 Qh4 mate, and a three-move version, Higuera v Solana, Hollywood 1945.[^s3]

```pgn
[Event "Belgian Championship"]
[Site "Antwerp"]
[Date "1922.??.??"]
[White "Boruchowitz"]
[Black "Koltanowski"]
[Result "0-1"]

1. f3 e5 2. g4 Qh4# 0-1
```

The practical lesson for club players is that early pawn moves in front of the king can be fatal: in the games Winter collects, a moved or missing f-pawn (usually together with an advanced g-pawn) opened a diagonal to the king before the queen arrived.[^s3] Before playing for mate, check all three escapes the Laws allow the defender (a king move, a capture of the checker, an interposition); overlooking one of them turns an intended mate into a mere check.[^s1]

## Origin of the word

The term came into European languages from Persian *shah mat*, usually glossed "the king is dead" (or from a verb meaning "to die"), by way of Arabic.[^s4] David Wilton notes that an Anglo-Latin poem of the late eleventh century already uses it, and that the earliest English record is in *Of Arthour and Merlin*, a manuscript copied around 1330.[^s4] Checkmate was not always the only way to win in the older game: in shatranj, a player also won by stripping the opponent's king of all its other pieces (the bare king), and stalemate counted as a win as well.[^s5]

## Connections

Checkmate is defined in the **FIDE Laws of Chess** (Articles 1, 3 and 5) and is the outcome that **stalemate** and the **dead position** are measured against: all three turn on whether the side to move has legal moves and whether mate remains possible.[^s1] Because no move may leave the king in check, a **double check** can only be met by a king move, which is why it so often ends in mate.[^s1] Standard patterns such as the **back-rank mate** are core material in **chess tactics**, and the **helpmate** problem genre turns the goal around, with both sides cooperating to mate one king. Its history runs back through **shatranj**, where it shared the winning role with the bare king.[^s5]

## Sources

[^s1]: FIDE Rules Commission, "FIDE Laws of Chess" (approved 7 August 2022, applied from 1 January 2023). https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/ (accessed 2026-11-11)
[^s2]: Encyclopaedia Britannica, "When does a game of chess end?". https://www.britannica.com/question/When-does-a-game-of-chess-end (accessed 2026-11-11)
[^s3]: Edward Winter, Chess Notes, "Fool's Mate". https://chesshistory.com/winter/extra/foolsmate.html (accessed 2026-11-11)
[^s4]: David Wilton, Wordorigins.org, "mate / checkmate" (2022). https://www.wordorigins.org/big-list-entries/mate (accessed 2026-11-11)
[^s5]: Hans Bodlaender and John William Brown, The Chess Variant Pages, "Shatranj". https://chessvariants.com/historic.dir/shatranj.html (accessed 2026-11-11)
