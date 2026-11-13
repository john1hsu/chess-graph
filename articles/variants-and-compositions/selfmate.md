---
id: kt:selfmate
type: ProblemGenre
title: Selfmate
aliases: [Selfmates, Self-mate, Sui-mate, Suimate, "s#"]
domain: variants-and-compositions
summary: >-
  A chess problem genre in which White moves first and must force an unwilling Black to deliver checkmate
  within a stated number of moves; Black defends by trying to avoid giving mate.
status: current
volatile: false
verified: 2026-11-13
fen: "7k/8/8/5Q2/8/2p5/p1p1p3/2KbN3 w - - 0 1"
broader: [kt:chess-problems, kt:chess-composition]
related: [kt:checkmate, kt:zugzwang, kt:pawn-promotion, kt:reflexmate]
relations:
  - {predicate: governedBy, object: kt:codex-of-chess-composition}
  - {predicate: contrastsWith, object: kt:helpmate}
  - {predicate: usesTechnique, object: kt:battery}
sources:
  - id: s1
    title: "Chess: Chess composition"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/chess/Chess-composition
    type: reference
    accessed: 2026-11-13
  - id: s2
    title: "Codex of Chess Compositions (version Vilnius 2019)"
    publisher: World Federation for Chess Composition (WFCC)
    url: https://www.wfcc.ch/?p=198
    type: governing-body
    accessed: 2026-11-13
  - id: s3
    title: "Chess glossary (Freshman Seminar 23j: Chess and Mathematics)"
    publisher: Noam Elkies, Harvard University, Department of Mathematics
    url: https://people.math.harvard.edu/~elkies/FS23j.05/glossary_chess.html
    type: academic
    accessed: 2026-11-13
  - id: s4
    title: "Selfmates & Reflexmates (beginners' guide)"
    publisher: British Chess Problem Society, The Problemist
    url: https://theproblemist.org/beginner.pl?type=b_sr
    type: publication
    accessed: 2026-11-13
  - id: s5
    title: "Glossary of chess problem terms"
    publisher: British Chess Problem Society
    url: https://www.theproblemist.org/dloads/Glossary.pdf
    type: publication
    accessed: 2026-11-13
  - id: s6
    title: "Selfmates (Problem World)"
    publisher: Peter Wong, OzProblems
    url: https://www.ozproblems.com/problem-world/selfmates
    type: community
    accessed: 2026-11-13
  - id: s7
    title: "Problem World introduction to selfmates"
    publisher: Peter Wong, OzProblems Walkabout, 8 August 2019
    url: https://www.ozproblems.com/walkabout/walkabout2019/aug8
    type: community
    accessed: 2026-11-13
  - id: s8
    title: "Christmas puzzles: I'll force you to mate!"
    publisher: Frederic Friedel, ChessBase News, 29 December 2020
    url: https://en.chessbase.com/post/christmas-puzzles-i-ll-force-you-to-mate
    type: publication
    accessed: 2026-11-13
created: 2026-11-13
---

# Selfmate

A selfmate is a composed chess problem with an inverted goal: White moves first and must force Black, who resists, to give checkmate to the white king within a stated number of moves.[^s1][^s3] The WFCC Codex, the rulebook of world chess composition, gives exactly this as an example stipulation and lists selfmates among the four historically developed groups of compositions, beside studies, direct mates and helpmates.[^s2] The British Chess Problem Society writes it S#n and notes that selfmates have long been recognised as an orthodox genre.[^s4][^s5] It is sometimes called a sui-mate.[^s8]

## How it differs from other problems

In a direct mate White attacks and Black defends against being mated. In a selfmate Black still defends, but its defence is to avoid delivering mate, while White must arrange matters so that every black reply eventually leaves only mating moves.[^s3][^s6] This is the key difference from the helpmate, where the two sides cooperate.[^s1] Elkies remarks that forcing an opponent to mate you is usually much harder than giving mate by force.[^s3] Because the black king must be kept boxed in as well as the white king exposed, selfmates are often heavy with material; solvers like them anyway for their clear-cut solutions.[^s4]

Since White is the side meeting the stipulation, the BCPS notes that dual mates, which mar a directmate, are acceptable in a selfmate.[^s4] In solving contests the Codex asks solvers of selfmates to write every move except the mating move in each full-length variation, and selfmates form one round of the World Chess Solving Championship.[^s2]

## Typical mechanisms

Two engines drive most short selfmates. One is zugzwang: White plays a quiet move after which every legal black move gives mate. The other is a forcing check that Black can only answer with a mating move, often by opening a line from a black battery (two pieces lined up so that one unmasks the other).[^s6] Pins, especially white self-pins, restrict both sides so that Black's mating replies are forced.[^s6] Composers prize *changed play*, where the key alters White's replies to Black's defences, and *tries*, plausible keys that fail to one precise defence.[^s6]

A related family keeps the inverted goal but changes the compulsion. In a reflexmate either side must mate on the move if it can; in a semi-reflexmate the rule binds only Black.[^s4][^s5] Series and help forms (series selfmate, helpselfmate) also exist.[^s5]

## History

The genre is old. Britannica says the selfmate is believed to be at least 400 years old, and OzProblems traces it to medieval times, long before the 20th-century boom in other unorthodox stipulations.[^s1][^s7] Twentieth-century composers such as T. R. Dawson and Luigi Ceriani produced selfmates-in-two that are still used to teach the genre.[^s6][^s7]

## Example: a selfmate in two with promotions

Elkies gives this position (White Kc1, Qf5, Se1; Black Kh8, Bd1, pawns a2, c2, c3, e2; White to move) as a selfmate in two.[^s3] The black king, bishop and remaining pawns are frozen, so Black's only moves are promotions on a1, and the white king is already hemmed in by Black's own pawns.

The key is 1.Qf7!, which takes all the black king's squares. Now 1...a1=Q or 1...a1=R is mate at once. If Black underpromotes, 1...a1=B or 1...a1=N, White plays 2.Qg6!, again leaving Black nothing but mating moves: 2...Bb2# or 2...Nb3#.[^s3] The tempting 1.Qg6 fails to 1...a1=N!, because after 2.Qf7 the check 2...Nb3+ can be answered by 3.Qxb3, so Black escapes having to mate in time.[^s3] The problem shows how the selfmate turns promotion and zugzwang into weapons against the defender.

```pgn
[Event "Selfmate in 2 (Elkies glossary), main line"]
[SetUp "1"]
[FEN "7k/8/8/5Q2/8/2p5/p1p1p3/2KbN3 w - - 0 1"]
[Result "0-1"]

1. Qf7 a1=B 2. Qg6 Bb2# 0-1
```

```pgn
[Event "Selfmate in 2 (Elkies glossary), knight promotion"]
[SetUp "1"]
[FEN "7k/8/8/5Q2/8/2p5/p1p1p3/2KbN3 w - - 0 1"]
[Result "0-1"]

1. Qf7 a1=N 2. Qg6 Nb3# 0-1
```

## Connections

The selfmate is a genre of the **chess problem** within **chess composition**, and its stipulation and solving conventions are set by the WFCC **Codex of Chess Composition**.[^s2] It **contrasts with** the **helpmate**: in both the goal is an unusual mate, but there Black cooperates in being mated while here Black resists mating White.[^s1][^s3] Its goal is **checkmate** of White, typically forced through **zugzwang** or a black **battery** unmasked by check, and **pawn promotion** often supplies the mating force.[^s3][^s6] The **reflexmate** is its close variant with compulsory mates.[^s4]

## Sources
[^s1]: Encyclopaedia Britannica, "Chess: Chess composition". https://www.britannica.com/topic/chess/Chess-composition (accessed 2026-11-13)
[^s2]: World Federation for Chess Composition, "Codex of Chess Compositions" (version Vilnius 2019), Art. 5 and footnote 9(c); Annex II, Part II, Rules 1 and 7(c). https://www.wfcc.ch/?p=198 (accessed 2026-11-13)
[^s3]: Noam Elkies, Harvard University, Freshman Seminar 23j "Chess and Mathematics", chess glossary, entries "Selfmate", "Helpmate". https://people.math.harvard.edu/~elkies/FS23j.05/glossary_chess.html (accessed 2026-11-13)
[^s4]: British Chess Problem Society, "Selfmates & Reflexmates" (beginners' guide), The Problemist. https://theproblemist.org/beginner.pl?type=b_sr (accessed 2026-11-13)
[^s5]: British Chess Problem Society, "Glossary", entries "Selfmate", "Reflexmate", "Semi-Reflexmate", "Series selfmate", "Helpselfmate". https://www.theproblemist.org/dloads/Glossary.pdf (accessed 2026-11-13)
[^s6]: Peter Wong, "Selfmates", OzProblems, Problem World. https://www.ozproblems.com/problem-world/selfmates (accessed 2026-11-13)
[^s7]: Peter Wong, "Problem World introduction to selfmates", OzProblems Walkabout, 8 August 2019. https://www.ozproblems.com/walkabout/walkabout2019/aug8 (accessed 2026-11-13)
[^s8]: Frederic Friedel, "Christmas puzzles: I'll force you to mate!", ChessBase News, 29 December 2020. https://en.chessbase.com/post/christmas-puzzles-i-ll-force-you-to-mate (accessed 2026-11-13)
