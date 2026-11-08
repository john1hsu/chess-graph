---
id: kt:horizon-effect
type: Concept
title: Horizon effect
aliases: [Horizon problem, Negative horizon effect, Positive horizon effect]
domain: computer-chess
summary: >-
  The class of misjudgements a depth-limited game-tree search makes because it cannot see past its
  maximum search depth: it may push an unavoidable loss just beyond that horizon and believe it
  avoided, or grab a gain too early because its consequences lie out of sight.
fen: "5r1k/4Qpq1/4p3/1p1p2P1/2p2P2/1p2P3/3P4/BK6 b - - 0 1"
status: current
volatile: false
verified: 2026-11-08
broader: [kt:game-tree-search]
related: [kt:quiescence-search, kt:minimax, kt:evaluation-function, kt:singular-extensions]
relations:
  - {predicate: counteredBy, object: kt:quiescence-search}
  - {predicate: counteredBy, object: kt:singular-extensions}
  - {predicate: developedBy, object: kt:hans-berliner}
  - {predicate: dependsOn, object: kt:evaluation-function}
sources:
  - id: s1
    title: "Chess as Problem Solving: The Development of a Tactics Analyzer (PhD dissertation, March 1974)"
    publisher: Hans J. Berliner, Carnegie-Mellon University, via DTIC
    url: https://apps.dtic.mil/sti/pdfs/AD0784881.pdf
    type: academic
    accessed: 2026-11-08
  - id: s2
    title: "Some Necessary Conditions for a Master Chess Program (IJCAI 1973, pp. 77–85)"
    publisher: Hans J. Berliner, ML Anthology record
    url: https://mlanthology.org/ijcai/1973/berliner1973ijcai-some
    type: academic
    accessed: 2026-11-08
  - id: s3
    title: "Computer Chess and Search (Encyclopedia of Artificial Intelligence, 2nd ed., report version 1991)"
    publisher: T. A. Marsland, University of Alberta
    url: https://webdocs.cs.ualberta.ca/~tony/RecentPapers/encyc.mac-1991.pdf
    type: academic
    accessed: 2026-11-08
  - id: s4
    title: "Computer Backgammon (Scientific American 242(6), 1980), reproduction"
    publisher: Hans J. Berliner, reproduced by bkgm.com
    url: https://bkgm.com/articles/Berliner/ComputerBackgammon/
    type: publication
    accessed: 2026-11-08
  - id: s5
    title: "Horizon Effect"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/Horizon_Effect
    type: community
    accessed: 2026-11-08
created: 2026-11-08
---

# Horizon effect

The horizon effect is the family of errors a chess program makes because its search stops at a fixed depth. Whatever lies beyond that maximum depth, the program's horizon, is invisible to it, and anything its static evaluation cannot detect at the last position searched effectively does not exist for the program.[^s1] Marsland's survey calls it an unresolved defect of chess programs and notes that every program exhibits it to some degree.[^s3] It is the reason a strong engine still needs more than raw depth: the evaluation at the edge of the tree must be trustworthy, and in tactical positions it often is not.[^s5]

## Origin

Hans Berliner examined the phenomenon under the name "Horizon Effect" in his 1973 IJCAI paper, describing it as a source of unpredictable evaluation errors arising from the interaction between the static evaluation and the rules that decide when the search stops.[^s2] He used it as part of his argument that the programs of the day could not simply be scaled up to master strength.[^s2] His 1974 Carnegie-Mellon dissertation analysed the problem in detail and built a tactics analyser designed to avoid it.[^s1]

## Negative and positive forms

Berliner distinguished two forms.[^s1] In the **negative horizon effect**, the program sees an unavoidable loss coming and uses the timing of moves to push it beyond the horizon, so that within the searched tree the problem appears solved.[^s1] Typical symptoms are delaying moves that give up further material or weaken the position merely to postpone a loss that will happen anyway.[^s3] Berliner's own example was a trapped bishop: because the program's quiescence procedure looked at captures but not at moves attacking trapped pieces, it kept making sacrifices to delay the bishop's capture.[^s1]

In the **positive horizon effect**, the program grabs a gain too soon, either because it appears achievable within the horizon when it is not, or because it could be had later in a better form.[^s1] Examples in the dissertation include a positional gain the opponent can simply undo, and promoting a pawn before extracting its full value.[^s1] Berliner argued that this form is often a matter of missing knowledge rather than insufficient search.[^s1]

## Example

In the position given (Black to move), White's bishop on a1 attacks Black's queen on g7, which is pinned against the king on h8. A program whose quiescence search covers only captures assumes that any interposition saves the queen, and so finds the line 1...b2 2.Bxb2 c3 3.Bxc3 d4 4.Bxd4 e5 5.Bxe5, throwing four pawns in front of the bishop one after another.[^s3][^s5] Marsland notes that even an eight-ply search of this line might not reveal that the queen is lost all the same, so the program "believes" it has saved it at the cost of four pawns.[^s3] The position comes from a study by Hermann Kaindl.[^s3] Berliner gives a king-and-pawn example in the same spirit, where a three-ply search thinks it has solved a problem it has only postponed.[^s4]

## Remedies and limits

The main remedy is **quiescence search**: Marsland describes the quality of the quiescence search as what controls the severity of the horizon effect, and programs with weak quiescence suffer more.[^s3] Berliner observed that the negative form disappears if the ordinary search obeys the same rules as the quiescence search, or if undesirable developments are explicitly flagged and investigated during quiescence; simply extending the principal variation by two plies only handles one-move threats.[^s1] Other approaches extend the search in non-quiescent positions automatically, including Harris's bandwidth search, check extensions and the **singular extensions** of Anantharaman, Campbell and Hsu, which Marsland calls a first step toward smarter extension.[^s3][^s5] None of these removes the effect completely; they only push the horizon further out or make it smarter.[^s5]

Berliner contrasted all this with human play: experts think in terms of events and keep analysing while an important one remains unresolved, rather than stopping at a fixed depth.[^s4]

## Connections

The horizon effect is a property of depth-limited **game-tree search** and of **minimax** applied with a cut-off, and it arises because the **evaluation function** is applied to positions that are not quiet.[^s1][^s3] It is countered chiefly by **quiescence search** and by search extensions such as **singular extensions**.[^s3] The concept was named and analysed by **Hans Berliner**.[^s1][^s2]

## Sources
[^s1]: H. J. Berliner, *Chess as Problem Solving: The Development of a Tactics Analyzer*, PhD dissertation, Carnegie-Mellon University (March 1974), via DTIC. https://apps.dtic.mil/sti/pdfs/AD0784881.pdf (accessed 2026-11-08)
[^s2]: H. J. Berliner, "Some Necessary Conditions for a Master Chess Program", *Proc. 3rd International Joint Conference on Artificial Intelligence* (1973), pp. 77–85; record at ML Anthology. https://mlanthology.org/ijcai/1973/berliner1973ijcai-some (accessed 2026-11-08)
[^s3]: T. A. Marsland, "Computer Chess and Search", *Encyclopedia of Artificial Intelligence*, 2nd ed. (report version, University of Alberta, 1991), sections 2.6 and 3.7. https://webdocs.cs.ualberta.ca/~tony/RecentPapers/encyc.mac-1991.pdf (accessed 2026-11-08)
[^s4]: H. J. Berliner, "Computer Backgammon", *Scientific American* 242(6), 64–72 (1980), reproduced by bkgm.com. https://bkgm.com/articles/Berliner/ComputerBackgammon/ (accessed 2026-11-08)
[^s5]: Chess Programming Wiki, "Horizon Effect". https://www.chessprogramming.org/Horizon_Effect (accessed 2026-11-08)
