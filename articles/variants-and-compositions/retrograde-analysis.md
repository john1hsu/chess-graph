---
id: kt:retrograde-analysis
type: ProblemGenre
title: Retrograde analysis
aliases: [Retroanalysis, Retro-analysis, Retro analysis, Retros, Retro problems, Retrograde analytical problems]
domain: variants-and-compositions
summary: >-
  The deduction of the play that must have led to a chess position (its legality, whose move it is, the
  last move played, castling and en passant rights), used both as a genre of composed problems and, by
  extension, as the backward algorithm that generates endgame tablebases.
status: current
volatile: false
verified: 2026-11-10
fen: "1nbqkbnr/p1p1pppp/3p4/8/8/8/1PPP1PPP/RNBQKBNR b KQk - 4 7"
broader: [kt:chess-composition, kt:chess-problems]
related: [kt:helpmate, kt:endgame-tablebases, kt:en-passant, kt:castling, kt:dead-position]
relations:
  - {predicate: governedBy, object: kt:codex-of-chess-composition}
  - {predicate: hasPart, object: kt:proof-game}
  - {predicate: hasPart, object: kt:retractor}
  - {predicate: enables, object: kt:endgame-tablebases}
sources:
  - id: s1
    title: "Codex of Chess Compositions (version Vilnius 2019)"
    publisher: World Federation for Chess Composition (WFCC)
    url: https://www.wfcc.ch/?p=198
    type: governing-body
    accessed: 2026-11-10
  - id: s2
    title: "Retrograde Analysis (beginners' guide)"
    publisher: British Chess Problem Society, The Problemist
    url: https://mail.theproblemist.org/beginner.pl?type=b_ret
    type: publication
    accessed: 2026-11-10
  - id: s3
    title: "Conventions in Retroanalysis: A Plea for Consistency and Completeness"
    publisher: Alexander George, Amherst College (first published in diagrammes, 1994)
    url: https://ageorge.people.amherst.edu/AG/Retroanalysis.pdf
    type: academic
    accessed: 2026-11-10
  - id: s4
    title: "Complexity of Retrograde and Helpmate Chess Problems: Even Cooperative Chess is Hard (arXiv:2010.09271)"
    publisher: Josh Brunner, Erik D. Demaine, Dylan Hendrickson and Julian Wellman, MIT CSAIL
    url: https://arxiv.org/abs/2010.09271
    type: academic
    accessed: 2026-11-10
  - id: s5
    title: "A Memory Efficient Retrograde Algorithm and Its Application To Chinese Chess Endgames"
    publisher: Ren Wu and Donald F. Beal, More Games of No Chance (MSRI Publications, Vol. 42, 2002)
    url: https://library.slmath.org/books/Book42/files/wu.pdf
    type: academic
    accessed: 2026-11-10
  - id: s6
    title: "Special conventions in retro-analytical problems"
    publisher: Peter Wong, OzProblems (Walkabout, 17 April 2020)
    url: https://www.ozproblems.com/walkabout/walkabout2020/apr17
    type: community
    accessed: 2026-11-10
created: 2026-11-10
---

# Retrograde analysis

Retrograde analysis (retroanalysis, or simply "retro") is the deduction of the imaginary game that led to a position. From the diagram alone, the solver works out facts the position does not show directly: whether it is legal, which side is to move, what the last move was, and whether castling or an en passant capture is still available.[^s2] The WFCC Codex, the rulebook of chess composition, lists retroanalytical compositions as a special type, classified apart from their stipulation, and notes that their solutions need not be simple move sequences.[^s1]

## How the reasoning works

The Codex calls a position legal if some sequence of moves reaches it from the initial array; the sequence that does so is a *proof game*.[^s1] Solvers test this with a set of standard tools. They count missing pieces against the captures that pawn structures show, remembering that promoted pawns account for extra pieces. They look for pieces captured on their home squares. They check whether the side not to move is in check, which would make the position impossible. And they list every candidate last move, discarding those that could not have been played.[^s2]

A classic case is T. R. Dawson's mate in two from the *Falkirk Herald*, 1914. Black's last move must have been a pawn double step. It cannot have been ...d7-d5, because that pawn had to move earlier to free the c8 bishop, so it was ...f7-f5, and the key is the en passant capture of that pawn.[^s2] Alexander George traces this style of puzzle back through Sam Loyd (1888), Dawson and W. Langstaff (1922), among others.[^s3]

## Conventions

Because history is often uncertain, problemists agree on conventions, set out in Article 16 of the Codex.[^s1]

- **Castling** is permitted unless it can be proved impossible.
- **En passant** on the first move is allowed only if it can be proved that the previous move was the double step.
- **Partial retrograde analysis (PRA):** when castling and en passant rights depend on each other, the solution splits into mutually exclusive parts, one per possible history.
- **Retro-strategy (RS):** if PRA cannot settle mutually exclusive castling rights, the side that castles first is deemed to have had the right.
- **A posteriori (AP):** any further convention must be stated; under AP, a castling move later in the solution can prove the history that legalises an earlier en passant capture.[^s1][^s6]

The fifty-move and dead-position rules do not normally apply in compositions, but they do in retro problems, and repetition can be proved by combining the proof game with the solution.[^s1] George argues that the castling convention can hide relevant histories, and he proposes treating every possible history as a separate case.[^s3]

## Forms

Retro problems ask questions such as "which side is to move?", "what was the last move?" or "can White castle?". *Retractors* have moves taken back from the diagram before forward play. *Shortest proof games* (SPGs) ask for the shortest legal game ending in the diagram.[^s2] Brunner, Demaine and colleagues proved that the general question (can this position be reached?) is PSPACE-complete on n×n boards, so retro reasoning is hard in principle as well as in practice.[^s4]

## Example: a shortest proof game

Richard Müller (*Rochade*, 1985) set a proof-game position (shown in the FEN above, after White's seventh move) that looks almost like the opening array. White's a- and e-pawns are missing, Black's b-pawn and a8 rook are gone, and Black's d-pawn stands on d6. The catch is that the queen on d1 is not White's original queen but a promoted pawn.[^s2] The solution is 1.a4 d6 2.a5 Bg4 3.a6 Bxe2 4.axb7 Bxd1 5.bxa8=Q Bg4 6.Qf3 Bc8 7.Qd1.[^s2] The black bishop goes out to take the original queen, then goes home; the new queen walks back to d1. A solver who assumes nothing happened on d1 never finds it.

## Retrograde analysis in computer chess

The same backward reasoning names the algorithm that builds endgame tablebases. It starts from positions with known results, such as checkmates, and works backwards one move at a time, marking the predecessor positions that can reach a known win or loss.[^s5] Wu and Beal credit Ströhlein (1970) with the first widely known description, and Clarke (1977) and Ken Thompson (1986) with independently reinventing it.[^s5]

## Connections

Retrograde analysis is a branch of **chess composition** within **chess problems**. Its conventions come from the WFCC **Codex of Chess Composition**, and its typical forms include the **proof game** and the **retractor**.[^s1][^s2] It decides the legality of **castling** and **en passant** in problems, and it is the only kind of composition where the **dead position** rule normally applies.[^s1] It shares a complexity analysis with the **helpmate**[^s4], and as an algorithm it generates **endgame tablebases**.[^s5]

## Sources
[^s1]: World Federation for Chess Composition, "Codex of Chess Compositions" (version Vilnius 2019), Arts. 3, 6, 14–18 and footnotes 17–21. https://www.wfcc.ch/?p=198 (accessed 2026-11-10)
[^s2]: British Chess Problem Society, "Retrograde Analysis" (beginners' guide), The Problemist. https://mail.theproblemist.org/beginner.pl?type=b_ret (accessed 2026-11-10)
[^s3]: Alexander George, "Conventions in Retroanalysis: A Plea for Consistency and Completeness" (Amherst, 2002; first published in *diagrammes*, 1994). https://ageorge.people.amherst.edu/AG/Retroanalysis.pdf (accessed 2026-11-10)
[^s4]: Josh Brunner, Erik D. Demaine, Dylan Hendrickson and Julian Wellman, "Complexity of Retrograde and Helpmate Chess Problems: Even Cooperative Chess is Hard", arXiv:2010.09271 (2020). https://arxiv.org/abs/2010.09271 (accessed 2026-11-10)
[^s5]: Ren Wu and Donald F. Beal, "A Memory Efficient Retrograde Algorithm and Its Application To Chinese Chess Endgames", in *More Games of No Chance*, MSRI Publications Vol. 42 (2002). https://library.slmath.org/books/Book42/files/wu.pdf (accessed 2026-11-10)
[^s6]: Peter Wong, "Special conventions in retro-analytical problems", OzProblems Walkabout, 17 April 2020. https://www.ozproblems.com/walkabout/walkabout2020/apr17 (accessed 2026-11-10)
