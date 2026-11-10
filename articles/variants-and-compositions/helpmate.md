---
id: kt:helpmate
type: ProblemGenre
title: Helpmate
aliases: [Helpmates, Help-mate, Cooperative mate, Co-operative mate, h#]
domain: variants-and-compositions
summary: >-
  A chess problem genre in which Black moves first and cooperates with White so that the black king is
  checkmated in a stated number of moves; the solution is a single cooperative line, and composers usually
  give several thematically linked solutions or twins.
status: current
volatile: false
verified: 2026-11-10
fen: "4R3/8/Q7/1B1p4/2bpR3/P2kr3/6K1/6b1 b - - 0 1"
broader: [kt:chess-problems, kt:chess-composition]
related: [kt:checkmate, kt:dead-position, kt:retrograde-analysis, kt:endgame-study]
relations:
  - {predicate: governedBy, object: kt:codex-of-chess-composition}
  - {predicate: contrastsWith, object: kt:selfmate}
  - {predicate: developedBy, object: kt:max-lange}
sources:
  - id: s1
    title: "Chess: Chess composition"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/chess/Chess-composition
    type: reference
    accessed: 2026-11-10
  - id: s2
    title: "Codex of Chess Compositions (version Vilnius 2019)"
    publisher: World Federation for Chess Composition (WFCC)
    url: https://www.wfcc.ch/?p=198
    type: governing-body
    accessed: 2026-11-10
  - id: s3
    title: "Chess glossary (Freshman Seminar 23j: Chess and Mathematics)"
    publisher: Harvard University, Department of Mathematics
    url: https://people.math.harvard.edu/~elkies/FS23j.05/glossary_chess.html
    type: academic
    accessed: 2026-11-10
  - id: s4
    title: "Complexity of Retrograde and Helpmate Chess Problems: Even Cooperative Chess is Hard (arXiv:2010.09271)"
    publisher: Josh Brunner, Erik D. Demaine, Dylan Hendrickson and Julian Wellman, MIT CSAIL
    url: https://ar5iv.labs.arxiv.org/html/2010.09271
    type: academic
    accessed: 2026-11-10
  - id: s5
    title: "Helpmates (Problem World)"
    publisher: Peter Wong, OzProblems
    url: https://www.ozproblems.com/problem-world/helpmates
    type: community
    accessed: 2026-11-10
  - id: s6
    title: "Helpmates of the 'distant' future – Part 1"
    publisher: Peter Wong, OzProblems (Walkabout, 29 November 2014)
    url: https://www.ozproblems.com/walkabout/walkabout2014/nov29
    type: community
    accessed: 2026-11-10
  - id: s7
    title: "Helpmates (beginners' guide)"
    publisher: British Chess Problem Society, The Problemist
    url: https://mail.theproblemist.org/beginner.pl?type=b_hm
    type: publication
    accessed: 2026-11-10
  - id: s8
    title: "Helpmate in Two (T. Garai, Probleemblad 1989)"
    publisher: Hans Bodlaender, The Chess Variant Pages
    url: https://www.chessvariants.com/problems.dir/helpmates.html
    type: community
    accessed: 2026-11-10
created: 2026-11-10
---

# Helpmate

A helpmate is a composed chess problem in which the two sides work together: Black moves first and cooperates with White so that the black king is checkmated in a stated number of moves.[^s1][^s3] The WFCC Codex, the rulebook of the world composition body, defines it in these terms and counts helpmates among the four historically developed groups of compositions, alongside studies, direct mates and selfmates.[^s2] Only the players' motives change; every rule of chess still applies, so a check must still be answered.[^s5] The British Chess Problem Society calls it the most popular kind of chess problem, and notes that some countries call it the cooperative mate.[^s7]

## Conventions

Because Black starts, a helpmate in two (written h#2) has four single moves: Black, White, Black, and White's mate. Problemists write the black move first after each move number, so a solution reads "1.Black White 2.Black White#".[^s5][^s7] Where the first move does not lie with the conventional side, the Codex requires the stipulation to say so.[^s2]

A helpmate solution is one exact sequence with no defensive variations, which changes how soundness is judged. An unwanted extra solution is a *cook*, a flaw in any problem.[^s7] In help-play the Codex treats any dual as making the problem unsound (it tolerates only a final-move promotion to pieces of partly the same power), and the intended line must also come without transposed move orders.[^s2][^s7]

## Multiple solutions, twins and set play

Since one line gives little room for content, composers create variety with phases of play. A problem may be stipulated with two or more solutions; it may be *twinned*, with small changes to the diagram making new positions; or it may have *set play*, a line that would work if White moved first.[^s5] The Codex requires the stipulation to state the number of solutions, the changes for each twin, and any set play, which then counts as part of the author's solution.[^s2] Twinning is far more common in helpmates than in directmates.[^s5]

The art lies in unity. Good helpmates show the same strategy in each solution: pieces swapping roles, two knights exchanging places, or all four promotions spread across the phases.[^s5][^s7] A useful solving hint is that if a piece has several routes to a square, you are probably on the wrong track.[^s7]

## History and development

The helpmate was invented in the mid-19th century, and early examples usually had a single line with modest thematic content.[^s6] The British Chess Problem Society credits Max Lange, the namesake of the Max Lange Attack, with inventing it.[^s7] Helpmates were long classed as fairy chess but are now treated as orthodox by problemists.[^s8] Modern two- and three-movers usually have two closely linked solutions. Around 2000, as computer testing became common, "helpmates of the future" appeared, with two pairs of matching solutions; later work pushed this to three pairs.[^s6]

The helpmate question also matters outside composition. Brunner, Demaine and colleagues point out that, under FIDE rules, whether any series of legal moves can still mate decides whether a position is dead and whether a player who runs out of time loses. They prove the generalised helpmate problem on an n×n board is PSPACE-complete: cooperative play is still computationally hard.[^s4]

## Example: Garai, h#2 with two solutions

This helpmate in two by T. Garai won second prize in *Probleemblad* in 1989 and appears in the FIDE Album 1989–91.[^s8] White: Kg2, Qa6, Re8, Re4, Bb5, Pa3. Black: Kd3, Re3, Bc4, Bg1, Pd4, Pd5 (FEN above, Black to move). The two solutions are 1.Bxb5 Rxe3+ 2.Kc4 Rc8# and 1.Rxe4 Bxc4+ 2.Ke3 Qh6#.[^s8]

The pair shows the reciprocity that judges reward. In one line the black bishop captures the white bishop and the white rook recaptures with check; in the other, the black rook takes the white rook and the white bishop recaptures with check. Each time the black king steps onto the square its own captured piece left, and a distant white piece mates.[^s8]

```pgn
[Event "Probleemblad 1989, 2nd Prize — h#2, solution 1"]
[SetUp "1"]
[FEN "4R3/8/Q7/1B1p4/2bpR3/P2kr3/6K1/6b1 b - - 0 1"]
[Result "1-0"]

1... Bxb5 2. Rxe3+ Kc4 3. Rc8# 1-0
```

```pgn
[Event "Probleemblad 1989, 2nd Prize — h#2, solution 2"]
[SetUp "1"]
[FEN "4R3/8/Q7/1B1p4/2bpR3/P2kr3/6K1/6b1 b - - 0 1"]
[Result "1-0"]

1... Rxe4 2. Bxc4+ Ke3 3. Qh6# 1-0
```

(The PGN blocks use game notation, where Black's first move is written 1...; problemists number the same line 1.Bxb5 Rxe3+ 2.Kc4 Rc8#.[^s5][^s8])

## Connections

The helpmate is a genre of the **chess problem** within **chess composition**, and its soundness rules come from the WFCC **Codex of Chess Composition**.[^s1][^s2] It **contrasts with** the **selfmate**, where White forces an unwilling Black to give mate.[^s1][^s3] Its goal is **checkmate**. Because it asks whether mate can be reached at all, it underlies the **dead position** rule, and it shares its complexity analysis with **retrograde analysis**.[^s4] Its invention is credited to **Max Lange**.[^s7]

## Sources
[^s1]: Encyclopaedia Britannica, "Chess: Chess composition". https://www.britannica.com/topic/chess/Chess-composition (accessed 2026-11-10)
[^s2]: World Federation for Chess Composition, "Codex of Chess Compositions" (version Vilnius 2019), Arts. 5, 8, 13, 15, 21 and footnotes 2, 6, 9. https://www.wfcc.ch/?p=198 (accessed 2026-11-10)
[^s3]: Harvard University, Freshman Seminar 23j "Chess and Mathematics", chess glossary, entries "Helpmate", "Selfmate". https://people.math.harvard.edu/~elkies/FS23j.05/glossary_chess.html (accessed 2026-11-10)
[^s4]: Josh Brunner, Erik D. Demaine, Dylan Hendrickson and Julian Wellman, "Complexity of Retrograde and Helpmate Chess Problems: Even Cooperative Chess is Hard", arXiv:2010.09271 (2020). https://ar5iv.labs.arxiv.org/html/2010.09271 (accessed 2026-11-10)
[^s5]: Peter Wong, "Helpmates", OzProblems, Problem World. https://www.ozproblems.com/problem-world/helpmates (accessed 2026-11-10)
[^s6]: Peter Wong, "Helpmates of the 'distant' future – Part 1", OzProblems Walkabout, 29 November 2014. https://www.ozproblems.com/walkabout/walkabout2014/nov29 (accessed 2026-11-10)
[^s7]: British Chess Problem Society, "Helpmates" (beginners' guide), The Problemist. https://mail.theproblemist.org/beginner.pl?type=b_hm (accessed 2026-11-10)
[^s8]: Hans Bodlaender, "Helpmate in Two" (T. Garai, *Probleemblad* 1989, 2nd Prize; FIDE Album 1989–91), The Chess Variant Pages. https://www.chessvariants.com/problems.dir/helpmates.html (accessed 2026-11-10)
