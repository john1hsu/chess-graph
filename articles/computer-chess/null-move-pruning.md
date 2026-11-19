---
id: kt:null-move-pruning
type: Algorithm
title: Null-move pruning
aliases: [Null move pruning, Null-move heuristic, Null move heuristic, Null-move search, NMP, Null-move forward pruning]
domain: computer-chess
summary: >-
  A forward-pruning technique in chess engines that lets the side to move "pass" and searches the
  resulting position to reduced depth; if the opponent still cannot bring the score below beta, the
  node is cut off without searching any real moves, on the assumption that passing is almost never
  the best move.
fen: "8/8/8/3pK3/2kP4/8/8/8 w - - 0 1"
status: current
volatile: false
verified: 2026-11-19
broader: [kt:game-tree-search, kt:alpha-beta-pruning]
related: [kt:zugzwang, kt:horizon-effect, kt:quiescence-search, kt:king-and-pawn-endgames]
relations:
  - {predicate: dependsOn, object: kt:alpha-beta-pruning}
  - {predicate: counteredBy, object: kt:zugzwang}
  - {predicate: developedBy, object: kt:donald-beal}
  - {predicate: contrastsWith, object: kt:quiescence-search}
sources:
  - id: s1
    title: "Verified Null-Move Pruning (ICGA Journal 25(3), 2002), author preprint"
    publisher: Omid David-Tabibi and Nathan S. Netanyahu, Bar-Ilan University (arXiv)
    url: https://arxiv.org/pdf/0808.1125
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s2
    title: "Verified null-move pruning, ICGA Journal vol. 25 no. 3, pp. 153-161 (abstract)"
    publisher: IOS Press
    url: https://content.iospress.com/articles/icga-journal/icg25305
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s3
    title: "Adaptive null-move pruning, ICGA Journal vol. 22 no. 3, pp. 123-132 (abstract)"
    publisher: E. A. Heinz, IOS Press
    url: https://content.iospress.com/articles/icga-journal/icg22302
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s4
    title: "The Nature of Minimax Search (PhD thesis, Dissertation Series 99-3)"
    publisher: Donald F. Beal, University of Maastricht
    url: https://project.dke.maastrichtuniversity.nl/games/files/phd/Beal_thesis.pdf
    type: academic
    accessed: 2026-11-19
  - id: s5
    title: "Extended futility pruning and limited razoring: Introduction"
    publisher: Ernst A. Heinz, MIT CSAIL web pages
    url: https://people.csail.mit.edu/heinz/dt/node20.html
    type: academic
    accessed: 2026-11-19
  - id: s6
    title: "ICCA Journal, Volume 16, Number 3 (September 1993), contents and abstracts"
    publisher: E. A. Heinz's ICCA Journal database, MIT CSAIL
    url: https://people.csail.mit.edu/heinz/iccaj_db/node4.html
    type: archive
    accessed: 2026-11-19
created: 2026-11-19
---

# Null-move pruning

Null-move pruning is one of the standard ways a modern alpha-beta engine avoids searching hopeless lines in full. At a node where the engine already seems to be doing well, it lets the side to move skip its turn, searches the opponent's replies to a reduced depth, and if the score still stays at or above beta it prunes the node immediately.[^s1] The idea works because in nearly every chess position having the move is an advantage, so the value of "passing" is a reasonable lower bound on what the best real move would achieve.[^s1][^s4]

## The idea of the null move

A null move changes who is to move and nothing else. It is illegal in chess, but inside a search it is a useful thought experiment: the side to move can usually do better than doing nothing, so a score obtained after a pass is a bound that real moves are expected to beat.[^s4] Donald Beal developed this into a "null-move quiescence" search, first published in *Artificial Intelligence* in 1990, arguing that bounds set by null moves are more reliable than the static evaluations they come from and that they give a domain-independent form of selective search.[^s4] Beal's own experiments reported that a material-only version solved 276 of 300 tactical test positions from Reinfeld's collection.[^s4]

## How engines use it

In the form engines adopted, the search makes the null move, then searches the reply with depth reduced by an extra amount R; a fail-high (score at least beta) cuts the node off.[^s1] Standard safeguards are that the null move is not tried when the side to move is in check, and two null moves are never played in succession.[^s1] Ernst Heinz credited the 1989–1990 experiments of Beal and of Goetsch and Campbell with reviving interest in selective search, and described null-move pruning as among the most popular alpha-beta enhancements, with only minor tactical weaknesses and good scaling with depth.[^s5] Christian Donninger's 1993 paper in the *ICCA Journal* proposed applying the null move recursively as a heuristic for controlling the whole search, backed by results against strong human players.[^s6]

## Choosing the reduction

The size of R is a trade-off. Early programs used R = 1, which is safe but saves little; R = 3 searches much faster but risks missing tactics just beyond the shortened horizon, and R = 2 was long regarded as the best fixed compromise.[^s1] Heinz's adaptive null-move pruning varies R with the remaining depth, using R = 3 far from the leaves and R = 2 nearer them; in tests with his program DarkThought it kept tactical strength while cutting search effort by roughly 10 to 30 per cent at depths of 8 to 12 plies.[^s3][^s1] Heinz also argued that brute-force searchers had lost their dominance around 1990, when null-move pruning spread, and that leading programs had become selective forward-pruners.[^s3]

## The zugzwang problem

The whole method rests on one assumption: that passing is never better than the best real move. In zugzwang that assumption is false, because every move worsens the position, and standard null-move pruning can then return badly wrong results.[^s1] Beal noted that such positions are rare and occur mostly late in the game, when pieces are blocked or tied down.[^s4] Zugzwang is especially common in king and pawn endgames, which is why engines typically switch the null move off in such positions.[^s1]

The diagram position is a simple mutual zugzwang. Each king guards its own pawn and attacks the enemy pawn. With White to move, every legal king move abandons d4, and Black's king would face the same problem if it were Black's turn. A null-move search from this position would let White "pass", see Black forced to give up d5, and wrongly conclude that White stands well, exactly the failure the verification method below is designed to catch.[^s1]

## Verified null-move pruning

Omid David-Tabibi and Nathan Netanyahu proposed a fix published in the *ICGA Journal* in 2002. Instead of cutting off at once after a fail-high with R = 3, the search continues at one ply less depth to verify the result; if that verification finds that no real move reaches beta, the node is treated as a zugzwang and re-searched at full depth.[^s1][^s2] In their experiments with the engine Genesis, verified R = 3 produced trees smaller than standard R = 2 while solving more tactical test positions, and it scored 68.5 out of 100 in self-play against standard R = 2.[^s1] They stress that it needs only a few lines of change in an existing null-move search.[^s2]

## Connections

Null-move pruning is a forward-pruning refinement of **alpha-beta pruning** within **game-tree search**, and it grew out of Donald Beal's null-move **quiescence search**.[^s4][^s5] Its blind spot is **zugzwang**, most of all in **king and pawn endgames**, and its depth reduction trades speed against a greater risk of the **horizon effect**.[^s1]

## Sources
[^s1]: O. David-Tabibi and N. S. Netanyahu, "Verified Null-Move Pruning", author preprint of *ICGA Journal* 25(3), 2002. https://arxiv.org/pdf/0808.1125 (accessed 2026-11-19)
[^s2]: IOS Press, *ICGA Journal* vol. 25 no. 3, pp. 153–161, "Verified null-move pruning" (abstract). https://content.iospress.com/articles/icga-journal/icg25305 (accessed 2026-11-19)
[^s3]: E. A. Heinz, "Adaptive null-move pruning", *ICGA Journal* vol. 22 no. 3, pp. 123–132, 1999 (abstract). https://content.iospress.com/articles/icga-journal/icg22302 (accessed 2026-11-19)
[^s4]: D. F. Beal, *The Nature of Minimax Search*, PhD thesis, University of Maastricht, 1999 (chapter 10 is an edited version of "A Generalised Quiescence Search Algorithm", *Artificial Intelligence* 43, 1990). https://project.dke.maastrichtuniversity.nl/games/files/phd/Beal_thesis.pdf (accessed 2026-11-19)
[^s5]: E. A. Heinz, "Introduction" (extended futility pruning and limited razoring). https://people.csail.mit.edu/heinz/dt/node20.html (accessed 2026-11-19)
[^s6]: ICCA Journal database, Volume 16, Number 3 (September 1993), including C. Donninger, "Null Move and Deep Search", pp. 137–143. https://people.csail.mit.edu/heinz/iccaj_db/node4.html (accessed 2026-11-19)
