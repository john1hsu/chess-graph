---
id: kt:calculation
type: Technique
title: Calculation
aliases: [Calculating variations, Chess calculation, Analysis of variations, Tree of analysis]
domain: training-and-improvement
summary: >-
  The skill of working out concrete sequences of moves and replies in one's head before moving;
  Kotov taught it as choosing candidate moves and examining each branch of a "tree of analysis",
  and research since de Groot shows that stronger players search faster, deeper and more selectively.
status: current
volatile: false
verified: 2026-11-09
broader: [kt:chess-expertise, kt:cognitive-psychology-of-chess]
related: [kt:chess-tactics, kt:combination, kt:einstellung-effect, kt:game-tree-search, kt:visualization]
relations:
  - {predicate: hasPart, object: kt:candidate-moves}
  - {predicate: hasPart, object: kt:progressive-deepening}
  - {predicate: championedBy, object: kt:alexander-kotov}
  - {predicate: influencedBy, object: kt:adriaan-de-groot}
sources:
  - id: s1
    title: "Think Like a Grandmaster (A. A. Kotov)"
    publisher: Batsford Books
    url: https://www.batsfordbooks.com/1136192
    type: book
    accessed: 2026-11-09
  - id: s2
    title: "Adriaan Dingeman de Groot (1914–2006) — obituary, Psychologische Rundschau"
    publisher: Fernand Gobet and Jochen Musch, Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/2617/1/De%20Groot%20Obituary%20-%20%20Psychologische%20Rundschau.pdf
    type: academic
    accessed: 2026-11-09
  - id: s3
    title: "Chess players' thinking revisited (Swiss Journal of Psychology 57, 1998)"
    publisher: Fernand Gobet, Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/822/4/1791.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "Adaptive expert decision making: Skilled chessplayers search more and deeper (ICGA Journal 27(4), 2004)"
    publisher: Guillermo Campitelli and Fernand Gobet, Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/825/1/Gobet_Search_ICGA.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s5
    title: "The Winning Academy 15: How to avoid blunders (part 1)"
    publisher: Jan Markos (GM), ChessBase News
    url: https://en.chessbase.com/post/the-winning-academy-15-how-to-avoid-blunders-part-1
    type: publication
    accessed: 2026-11-09
  - id: s6
    title: "Christiansen v Karpov, Hoogovens, Wijk aan Zee 1993 (game score)"
    publisher: Lichess study
    url: https://lichess.org/study/embed/nkXYPOHc/SSa6JLCz
    type: database
    accessed: 2026-11-09
created: 2026-11-09
---

# Calculation

Calculation is the work of seeing concrete variations in your head: choosing moves to consider, imagining the opponent's best replies, following the resulting lines to a position you can judge, and comparing the outcomes before touching a piece. It is the engine behind tactics and combinations, but it also decides quiet positions, where a plan has to survive the opponent's concrete answers. The classic training text is Alexander Kotov's *Think Like a Grandmaster*, which presents itself as a manual on when and how to analyse, built around candidate moves and the "tree of analysis".[^s1]

## Kotov's method

Kotov's advice, as summarised by Campitelli and Gobet, is to begin by listing the candidate moves, then analyse each one in turn down to an evaluation, without jumping back and forth between branches.[^s4] The tree image is the point: a disciplined calculator knows which branch he is on, finishes it, and only then moves to the next, so that the final choice compares finished assessments rather than half-seen impressions.[^s1][^s4]

## What research says about search

Adriaan de Groot's think-aloud studies, first published in Dutch in 1946 and in English as *Thought and Choice in Chess* in 1965, found that strong players chose better moves but did not search clearly more moves or deeper lines than weaker ones; most players examined only three or four of the often thirty legal moves.[^s2] He also described progressive deepening, the habit of returning to the same line again and again, each time looking a little further.[^s2]

Fernand Gobet's replication with 48 Swiss players on de Groot's own test position found modest skill effects: average search depth rose from about 2.9 plies in Class B players to 5.0 in masters, but the number of positions visited was similar for all groups above Class B.[^s3] Campitelli and Gobet then argued that these positions were too easy to require deep search. With positions chosen to demand it, a grandmaster and an international master generated roughly 370–400 positions in 30 minutes, with mean depths of 10–14 plies, against about 88 positions and under 3 plies for a Class B player; depth and speed rose steadily with rating.[^s4] Their conclusion is that experts combine fast pattern recognition with real, deep search and adapt the mix to the position.[^s4] They also noticed that the two weaker players made no candidate lists and hopped between moves, while the international master followed Kotov's textbook pattern almost exactly.[^s4]

## Practical habits and pitfalls

Most calculation errors are not deep. Grandmaster Jan Markos recommends a short safety routine before calculating at all: count the unprotected pieces on both sides, then list every forcing move (checks, captures, threats), including ugly-looking ones, and check each briefly; exchanges deserve the same scrutiny.[^s5] He suggests spending about ten extra seconds per move on this rather than playing natural moves instantly.[^s5] Other useful habits follow from the research: name your candidates before diving in, finish a line to a position you can evaluate, and keep candidate lists open to new ideas, as the grandmaster in the study did when he expanded his list mid-analysis.[^s4]

## Example: two loose pieces

Markos's first example is Christiansen v Karpov, Wijk aan Zee 1993. After 11...Bd6, both the bishop on d6 and the knight on h5 were unprotected, and White's quiet retreat 12.Qd1 attacked both at once; Karpov resigned.[^s5][^s6] A blunder check of unprotected pieces would have flagged the danger before any deep calculation was needed.[^s5]

```pgn
[Event "Hoogovens"]
[Site "Wijk aan Zee NED"]
[Date "1993.01.18"]
[Round "2"]
[White "Larry Christiansen"]
[Black "Anatoly Karpov"]
[Result "1-0"]

1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. a3 Ba6 5. Qc2 Bb7 6. Nc3 c5 7. e4 cxd4 8. Nxd4 Nc6 9. Nxc6 Bxc6 10. Bf4 Nh5 11. Be3 Bd6 12. Qd1 1-0
```

## Connections

Calculation is a core topic in chess expertise and the cognitive psychology of chess, where it is studied alongside pattern recognition.[^s3][^s4] It **has parts** in candidate moves and progressive deepening,[^s2][^s4] was **championed by** Alexander Kotov as a teachable method,[^s1] and was **influenced by** Adriaan de Groot's research on how players think.[^s2] It drives chess tactics and the combination, is distorted by the Einstellung effect, and has a mechanical counterpart in computer game-tree search, the subject of the ICGA Journal where Campitelli and Gobet published.[^s4] It relates to visualization, the ability to hold the changing board in mind while the lines are worked out.

## Sources

[^s1]: A. A. Kotov, *Think Like a Grandmaster*, Batsford. https://www.batsfordbooks.com/1136192 (accessed 2026-11-09)
[^s2]: Gobet, F. & Musch, J., obituary of Adriaan de Groot, *Psychologische Rundschau*. https://bura.brunel.ac.uk/bitstream/2438/2617/1/De%20Groot%20Obituary%20-%20%20Psychologische%20Rundschau.pdf (accessed 2026-11-09)
[^s3]: Gobet, F. (1998), "Chess players' thinking revisited", *Swiss Journal of Psychology* 57, 18–32. https://bura.brunel.ac.uk/bitstream/2438/822/4/1791.pdf (accessed 2026-11-09)
[^s4]: Campitelli, G. & Gobet, F. (2004), "Adaptive expert decision making: Skilled chessplayers search more and deeper", *ICGA Journal* 27(4), 209–216. https://bura.brunel.ac.uk/bitstream/2438/825/1/Gobet_Search_ICGA.pdf (accessed 2026-11-09)
[^s5]: Jan Markos, "The Winning Academy 15: How to avoid blunders (part 1)", ChessBase News, 11 November 2022. https://en.chessbase.com/post/the-winning-academy-15-how-to-avoid-blunders-part-1 (accessed 2026-11-09)
[^s6]: Lichess study, Christiansen v Karpov, Hoogovens 1993. https://lichess.org/study/embed/nkXYPOHc/SSa6JLCz (accessed 2026-11-09)
