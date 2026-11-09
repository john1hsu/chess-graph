---
id: kt:chess-problems
type: ProblemGenre
title: Chess problem
aliases: [Chess problems, Composed problem, Directmate, Direct mate, Mate-in-n problem, Problem chess]
domain: variants-and-compositions
summary: >-
  A composed chess position with a stated task—most often White to move and force checkmate in a
  fixed number of moves—whose solution must be unique and whose value lies in the artistic idea it shows.
status: current
volatile: false
verified: 2026-11-09
fen: "n1rb4/1p3p1p/1p6/1R5K/8/p3p1PN/1PP1R3/N6k w - - 0 1"
broader: [kt:chess-composition]
related: [kt:endgame-study, kt:helpmate, kt:retrograde-analysis, kt:zugzwang, kt:pawn-promotion]
relations:
  - {predicate: governedBy, object: kt:codex-of-chess-composition}
  - {predicate: contrastsWith, object: kt:endgame-study}
  - {predicate: exemplifiedBy, object: kt:excelsior}
sources:
  - id: s1
    title: "Chess: Chess composition"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/chess/Chess-composition
    type: reference
    accessed: 2026-11-09
  - id: s2
    title: "Codex of Chess Compositions (version Vilnius 2019)"
    publisher: World Federation for Chess Composition (WFCC)
    url: https://www.wfcc.ch/?p=198
    type: governing-body
    accessed: 2026-11-09
  - id: s3
    title: "Chess glossary (Freshman Seminar 23j: Chess and Mathematics)"
    publisher: Harvard University, Department of Mathematics
    url: https://people.math.harvard.edu/~elkies/FS23j.05/glossary_chess.html
    type: academic
    accessed: 2026-11-09
  - id: s4
    title: "What is a chess problem? (Problem World No. 1)"
    publisher: Peter Wong, OzProblems
    url: https://www.ozproblems.com/problem-world/chess-problem
    type: community
    accessed: 2026-11-09
  - id: s5
    title: "Start Solving Now: Part I"
    publisher: Gary Kevin Ware, Chess Life Online (US Chess), 22 August 2008
    url: https://www.uschess.org/content/view/8672/471
    type: publication
    accessed: 2026-11-09
  - id: s6
    title: "ChessBase puzzles: Loyd's Excelsior"
    publisher: Frederic Friedel, ChessBase News, 26 October 2013
    url: https://en.chessbase.com/post/chebase-puzzles-loyds-excelsior-261013
    type: publication
    accessed: 2026-11-09
created: 2026-11-09
---

# Chess problem

A chess problem is a composed position with a stated task, the *stipulation*. In the classic orthodox form, the directmate, White moves first and must force checkmate within a set number of moves—usually two, three or four—against any defence.[^s1][^s3] The puzzle is only half the point: a problem is built to display an idea, its *theme*, and is judged as a work of art for subtlety, economy, paradox and unity of play.[^s4]

## Problem versus study

Problems and endgame studies are the two main branches of composition. A study asks White to win or draw with no move limit and usually resembles a game ending; a problem fixes the number of moves and its first move need not resemble anything a practical player would choose.[^s1] The WFCC Codex, the rulebook of the world composition body, groups compositions historically into studies, direct mates, selfmates and helpmates, and defines a direct mate as White moving first and mating within a specified maximum number of moves.[^s2]

## Key, threat and block

The first move of the solution is the *key*.[^s3] In modern problems it is rarely a check or capture; good keys are quiet, often give up something, and may even hand Black new freedom.[^s1][^s4] Two broad types follow. In a *threat* problem the key threatens mate next move, and each black defence that stops it allows a different mate. In a *block* problem the key is a waiting move: no mate is threatened, but Black is in zugzwang and every move he makes walks into a mate.[^s4][^s5] Solvers can attack a problem constructively—looking for flaws in the diagram such as an unguarded flight square or an unanswered check—or thematically, by recognising a pattern such as the cross-check or half-pin and looking for the key that sets it up.[^s5]

## Soundness: legality, cooks and duals

Orthodox problems must be legal positions, reachable from the initial array; illegal positions are not accepted in composition tournaments unless the conditions allow them.[^s2] The Codex adds conventions for hidden information: castling is allowed unless it can be proved impossible, while an en passant capture on the first move is allowed only if the double step can be proved.[^s2] A composition must be solvable only by the author's solution. A *cook* is a second solution with a different first move and makes the problem unsound; a *dual* is an alternative way of completing the stipulation later on, treated as a lesser defect whose gravity the judge weighs.[^s2][^s1] Economy also matters: every unit should serve the idea or the soundness.[^s4] Computer testing has made cooks much rarer, but the Codex keeps responsibility for soundness with the author.[^s4][^s2]

## Other genres

Beyond the directmate, a *helpmate* has Black move first and cooperate with White to be mated; a *selfmate* has White force an unwilling Black to give mate, a form thought to be at least 400 years old.[^s1][^s2] *Fairy* problems use new stipulations, pieces such as the grasshopper or nightrider, or other boards, and *retro* problems ask how the position arose; retrograde problems are usually classed with fairies.[^s1][^s3]

## History in brief

Positions with practical lessons go back to the ninth century, but the modern problem took shape by the mid-19th century, with English, German and Bohemian schools emerging later that century and classic themes such as the Nowotny, Grimshaw and Indian coming into use. Very long stipulations went out of fashion, and the 20th century explored heterodox forms. Adolf Anderssen is the only recognised world champion who was also an accomplished problemist, and FIDE awards International Master and Grandmaster of Chess Composition titles for works published in its albums.[^s1]

## Example: Loyd's Excelsior (mate in five)

Sam Loyd composed this problem in 1858 for a friend, Denis Julien, who claimed he could always spot the mating piece; ChessBase gives it as published in the *London Era* in 1861.[^s6] White: Kh5, Rb5, Re2, Na1, Nh3, pawns b2, c2, g3. Black: Kh1, Na8, Rc8, Bd8, pawns a3, b6, b7, e3, f7, h7 (FEN above). Quiet tries like 1.Rf5 or 1.Rd5 fail to ...Rc5, so White starts with the pawn: 1.b4! Rc5+ 2.bxc5 a2 3.c6 Bc7 4.cxb7 Bxg3 5.bxa8=Q#.[^s6] The humble b-pawn advances five times to deliver mate, the originality Britannica singles out.[^s1][^s6]

```pgn
[Event "Loyd, London Era 1861 — mate in 5 (main line)"]
[SetUp "1"]
[FEN "n1rb4/1p3p1p/1p6/1R5K/8/p3p1PN/1PP1R3/N6k w - - 0 1"]
[Result "1-0"]

1. b4 Rc5+ 2. bxc5 a2 3. c6 Bc7 4. cxb7 Bxg3 5. bxa8=Q# 1-0
```

## Connections

A chess problem is a genre of **chess composition**, set against the **endgame study**, which has no move limit.[^s1] Its soundness rules come from the WFCC **Codex of Chess Composition**.[^s2] Block problems depend on **zugzwang**, the **helpmate** and **retrograde analysis** are its main unorthodox branches, and Loyd's **Excelsior** turns on a run of **pawn promotion**.[^s4][^s3][^s6]

## Sources
[^s1]: Encyclopaedia Britannica, "Chess: Chess composition". https://www.britannica.com/topic/chess/Chess-composition (accessed 2026-11-09)
[^s2]: World Federation for Chess Composition, "Codex of Chess Compositions" (version Vilnius 2019), Arts. 5, 8–10, 13, 14, 16 and footnotes 9, 28. https://www.wfcc.ch/?p=198 (accessed 2026-11-09)
[^s3]: Harvard University, Freshman Seminar 23j "Chess and Mathematics", chess glossary, entries "Key", "Stipulation", "Helpmate", "Selfmate", "Fairy". https://people.math.harvard.edu/~elkies/FS23j.05/glossary_chess.html (accessed 2026-11-09)
[^s4]: Peter Wong, "What is a chess problem?", OzProblems, Problem World No. 1. https://www.ozproblems.com/problem-world/chess-problem (accessed 2026-11-09)
[^s5]: Gary Kevin Ware, "Start Solving Now: Part I", Chess Life Online (US Chess), 22 August 2008. https://www.uschess.org/content/view/8672/471 (accessed 2026-11-09)
[^s6]: Frederic Friedel, "ChessBase puzzles: Loyd's Excelsior", ChessBase News, 26 October 2013. https://en.chessbase.com/post/chebase-puzzles-loyds-excelsior-261013 (accessed 2026-11-09)
