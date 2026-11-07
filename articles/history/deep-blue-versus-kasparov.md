---
id: kt:deep-blue-versus-kasparov
type: Event
title: Deep Blue versus Kasparov
aliases: [Kasparov versus Deep Blue, Deep Blue vs Kasparov, Kasparov vs Deep Blue, Deep Blue–Kasparov matches, Kasparov–Deep Blue rematch, Deep Blue versus Garry Kasparov]
domain: history
summary: >-
  The two six-game matches between world champion Garry Kasparov and IBM's chess computer Deep Blue:
  Kasparov won in Philadelphia in February 1996 by 4–2, and Deep Blue won the New York rematch in
  May 1997 by 3½–2½, the first match defeat of a reigning world champion by a computer under
  tournament conditions.
fen: "r1k4r/p2nb1p1/2b4p/1p1n1p2/2PP4/3Q1NB1/1P3PPP/R5K1 b - - 0 19"
status: historical
volatile: false
verified: 2026-11-07
broader: [kt:history-of-computer-chess]
related: [kt:evaluation-function, kt:alpha-beta-pruning, kt:caro-kann-defence]
relations:
  - {predicate: playedBy, object: kt:garry-kasparov}
  - {predicate: wonBy, object: kt:deep-blue}
  - {predicate: usesTechnique, object: kt:alpha-beta-pruning}
  - {predicate: usesTechnique, object: kt:quiescence-search}
sources:
  - id: s1
    title: "Deep Blue (Artificial Intelligence 134, 2002)"
    publisher: M. Campbell, A. J. Hoane Jr., F. Hsu (copy hosted by Northern Arizona University)
    url: https://www.cefns.nau.edu/~edo/Classes/CS470-570_WWW/Readings/Campbell2002.pdf
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s2
    title: "Garry Kasparov discusses game highlights after he wins the 1996 match against Deep Blue in Philadelphia, Pennsylvania"
    publisher: Computer History Museum (Mastering the Game exhibit, gift of Monroe Newborn)
    url: https://www.computerhistory.org/chess/stl-430b9bbc9c350/
    type: archive
    accessed: 2026-11-07
  - id: s3
    title: "Garry Kasparov, C.J. Tan, and Monroe Newborn at the 1997 Deep Blue vs Kasparov re-match press conference"
    publisher: Computer History Museum (Mastering the Game exhibit, gift of Monroe Newborn)
    url: https://www.computerhistory.org/chess/stl-430b9bbc88ad6/
    type: archive
    accessed: 2026-11-07
  - id: s4
    title: "Deep Blue"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/EBchecked/topic/155485/Deep-Blue
    type: reference
    accessed: 2026-11-07
  - id: s5
    title: "Simpson's In-the-Strand (chess column), The Spectator, 17 May 1997, p. 60"
    publisher: Raymond Keene, The Spectator Archive
    url: https://archive.spectator.co.uk/article/17th-may-1997/60/simpsons
    type: publication
    accessed: 2026-11-07
  - id: s6
    title: "Behind Deep Blue: Building the Computer that Defeated the World Chess Champion (Princeton University Press, 2002)"
    publisher: Feng-Hsiung Hsu; publisher's details via Lehmanns bookshop
    url: https://lehmanns.de/shop/geisteswissenschaften/4604324-9780691090658-behind-deep-blue
    type: book
    accessed: 2026-11-07
created: 2026-11-07
---

# Deep Blue versus Kasparov

"Deep Blue versus Kasparov" names the pair of six-game matches, played under standard tournament conditions, between world champion Garry Kasparov and IBM's purpose-built chess computer. In Philadelphia in 1996 Deep Blue won the opening game, the first time a computer had beaten a reigning world champion in a single game, but Kasparov recovered to take the match 4–2.[^s2] In the May 1997 rematch in New York the upgraded machine won 3½–2½, which the Computer History Museum describes as the first defeat of a reigning champion by a computer in a match at standard time controls.[^s3][^s4]

## Background

The machine grew out of a student project at Carnegie Mellon University in the mid-1980s, led by Feng-Hsiung Hsu, who later became Deep Blue's system architect and chip designer.[^s6] Its ancestors were ChipTest, a single-chip move generator, and Deep Thought, which in 1988 became the first chess machine to beat a grandmaster in tournament play. Part of the team then moved to IBM's T. J. Watson Research Center, where Deep Thought 2 won the ACM computer championships of 1991 and 1994 before work turned to Deep Blue.[^s1]

## The 1996 match

The February 1996 version, later called Deep Blue I, ran on a 36-node IBM RS/6000 SP with 216 custom chess chips, searching roughly 50 to 100 million positions per second.[^s1] After Deep Blue's first-game win the match stood level at 2–2 after four games, and Kasparov won the last two to finish 4–2.[^s1][^s2]

## Changes before the rematch

The team's own account says most of the year between matches went into the evaluation function rather than the parallel search, which stayed largely the same. A redesigned chip raised the number of evaluation features from about 6,400 to over 8,000, added repetition detection in hardware and ran at 2 to 2.5 million positions per second; Deep Blue II carried 480 of these chips across a 30-node SP.[^s1] It averaged about 126 million positions per second in searches longer than a minute during the 1997 match, peaking at 330 million.[^s1] Search was split between software on the host processors, using a selective alpha-beta search with forcing-line extensions and a transposition table, and the chips, which ran a fixed-depth null-window alpha-beta search with quiescence search for the last few plies.[^s1] Grandmaster Joel Benjamin prepared most of an opening book of about 4,000 positions, backed by an "extended book" that rewarded moves played in a 700,000-game grandmaster database.[^s1]

## The 1997 rematch

Kasparov won game 1, Deep Blue won game 2, games 3 to 5 were drawn, and Deep Blue won game 6 in 19 moves.[^s4][^s5] Writing in *The Spectator* the following week, grandmaster Raymond Keene argued that Kasparov had been psychologically overawed by the machine: he had resigned game 2 in a position where perpetual check was available, and in game 6 he chose a line Keene judged virtually hopeless for Black.[^s5] Keene also questioned whether six games were enough for IBM to declare victory and retire the machine.[^s5] Kasparov's later claim that human intervention shaped Deep Blue's decisive moves became a lasting controversy; Hsu disputes it in his book.[^s6]

## Example: game 6

The decisive game was a Caro-Kann Defence. After 7...h6, a move Keene marked as a blunder, Deep Blue sacrificed a knight on e6 for a lasting attack against Black's uncastled king, and Kasparov resigned after White's 19th move.[^s5] The score below follows the column, and the diagram position is the one after 19.c4 in which Black resigned, with his king still stranded in the centre-queenside and his queen already returned for a rook.

```pgn
[Event "Deep Blue v Kasparov rematch"]
[Site "New York"]
[Round "6"]
[White "Deep Blue"]
[Black "Garry Kasparov"]
[Result "1-0"]

1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nd7 5. Ng5 Ngf6 6. Bd3 e6 7. N1f3 h6
8. Nxe6 Qe7 9. O-O fxe6 10. Bg6+ Kd8 11. Bf4 b5 12. a4 Bb7 13. Re1 Nd5
14. Bg3 Kc8 15. axb5 cxb5 16. Qd3 Bc6 17. Bf5 exf5 18. Rxe7 Bxe7 19. c4 1-0
```

## Legacy and lessons

The designers attributed the win to a combination of large search capacity, deliberately non-uniform search and a complex evaluation function, helped by endgame databases, the extended book and tuning tools.[^s1] They were also candid about the shortcomings: parallel efficiency was only around 8 to 12 per cent, the hardware was inflexible and evaluation tuning was incomplete.[^s1] For players, the takeaway from the match commentary is less about engine internals than about practical play: Keene's view was that the champion lost to his own fear of the machine as much as to its moves.[^s5]

## Connections

The match is the best-known milestone in the **history of computer chess** and the event that defines **Garry Kasparov**'s encounter with **Deep Blue**.[^s3] Technically it showcased depth-limited **alpha-beta pruning** with **quiescence search** in hardware, and a very large handcrafted **evaluation function**.[^s1] Its final game is a cautionary example in the **Caro-Kann Defence**.[^s5]

## Sources
[^s1]: M. Campbell, A. J. Hoane Jr. and F. Hsu, "Deep Blue", *Artificial Intelligence* 134 (2002). https://www.cefns.nau.edu/~edo/Classes/CS470-570_WWW/Readings/Campbell2002.pdf (accessed 2026-11-07)
[^s2]: Computer History Museum, "Garry Kasparov discusses game highlights after he wins the 1996 match against Deep Blue in Philadelphia, Pennsylvania" (photo by Monroe Newborn). https://www.computerhistory.org/chess/stl-430b9bbc9c350/ (accessed 2026-11-07)
[^s3]: Computer History Museum, "Garry Kasparov, C.J. Tan, and Monroe Newborn at the 1997 Deep Blue vs Kasparov re-match press conference". https://www.computerhistory.org/chess/stl-430b9bbc88ad6/ (accessed 2026-11-07)
[^s4]: Encyclopaedia Britannica, "Deep Blue". https://www.britannica.com/EBchecked/topic/155485/Deep-Blue (accessed 2026-11-07)
[^s5]: R. Keene, "Simpson's In-the-Strand", *The Spectator*, 17 May 1997, p. 60. https://archive.spectator.co.uk/article/17th-may-1997/60/simpsons (accessed 2026-11-07)
[^s6]: F.-H. Hsu, *Behind Deep Blue: Building the Computer that Defeated the World Chess Champion*, Princeton University Press, 2002 (ISBN 978-0-691-09065-8). https://lehmanns.de/shop/geisteswissenschaften/4604324-9780691090658-behind-deep-blue (accessed 2026-11-07)
