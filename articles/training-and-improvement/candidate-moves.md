---
id: kt:candidate-moves
type: Technique
title: Candidate moves
aliases: [Candidate move, Kotov's candidate moves]
domain: training-and-improvement
summary: >-
  The short list of moves a player decides are worth examining before calculating any of them;
  popularised by Alexander Kotov as the first step of a disciplined search, and studied by
  psychologists who found that strong players examine few first moves but choose them well.
status: current
volatile: false
verified: 2026-11-12
broader: [kt:calculation]
related: [kt:chess-tactics, kt:prophylaxis, kt:adriaan-de-groot, kt:progressive-deepening]
relations:
  - {predicate: partOf, object: kt:calculation}
  - {predicate: developedBy, object: kt:alexander-kotov}
  - {predicate: counters, object: kt:einstellung-effect}
sources:
  - id: s1
    title: "Adaptive expert decision making: Skilled chessplayers search more and deeper (ICGA Journal 27(4), 2004)"
    publisher: Guillermo Campitelli and Fernand Gobet, Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/825/1/Gobet_Search_ICGA.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Chess players' thinking revisited (Swiss Journal of Psychology 57, 1998)"
    publisher: Fernand Gobet, Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/822/4/1791.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s3
    title: "The mechanism of the Einstellung (set) effect: A pervasive source of cognitive bias (Current Directions in Psychological Science 19(2), 2010)"
    publisher: Merim Bilalić, Peter McLeod and Fernand Gobet, University of Klagenfurt
    url: https://cognition.aau.at/download/Publikationen/Bilalic/Bilalic_etal_2010b.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "\"Think Like a Grandmaster\" by Alexander Kotov (review)"
    publisher: GM Bryan Smith, Chess.com
    url: https://www.chess.com/article/view/quotthink-like-a-grandmasterquot-by-alexander-kotov
    type: publication
    accessed: 2026-11-12
  - id: s5
    title: "The Candidate Moves Technique"
    publisher: Rafael Leitão (GM) website
    url: https://rafaelleitao.com/candidate-moves-technique
    type: publication
    accessed: 2026-11-12
  - id: s6
    title: "How To Find The Best Chess Move"
    publisher: GM Gregory Serper, Chess.com
    url: https://www.chess.com/article/view/how-to-find-the-best-chess-move
    type: publication
    accessed: 2026-11-12
  - id: s7
    title: "Scholar's Mate"
    publisher: Chess.com Terms
    url: https://www.chess.com/terms/scholars-mate-chess
    type: database
    accessed: 2026-11-12
created: 2026-11-12
---

# Candidate moves

Candidate moves are the handful of moves a player consciously selects as worth examining before any detailed calculation begins. The term comes from Alexander Kotov's *Think Like a Grandmaster*, whose method is to identify the candidates, count them, and then analyse each one separately.[^s4][^s6] The idea is simple, but it answers a real problem: in a typical position there are dozens of legal moves, and a player who starts calculating the first idea that appears may never notice a better one. Grandmaster Gregory Serper credits the book with helping players systematise their thinking.[^s6]

## Kotov's rule and its purpose

As Campitelli and Gobet summarise it, Kotov asked players to decide which moves deserve attention first, then examine each candidate until the resulting position can be evaluated, finishing one branch before starting the next and never jumping back and forth between branches.[^s1] Kotov also described the opposite failure: after long, disorderly thought in a complicated position, a player short of time suddenly plays a move he has barely looked at, and it turns out to be a blunder. Smith's review discusses this pattern under the name "Kotov syndrome".[^s4] The candidate list is the defence against it: by naming the options first, the player knows what he is comparing and when the comparison is finished.[^s1][^s4]

## What research found

Psychological studies of real thinking show that strong players are selective. In Fernand Gobet's replication of Adriaan de Groot's think-aloud experiment, 48 Swiss players spent up to 30 minutes on de Groot's position A. Masters examined on average only 3.2 different first moves, fewer than Class A players at 6.5; most masters looked at one to three, while about two-fifths of the Class A players considered nine to eleven.[^s2] The rate at which new first moves appeared did not depend on skill, and de Groot's own grandmasters had averaged about four.[^s2] Strength therefore shows less in the length of the list than in its quality: good candidates come from recognised patterns.

Campitelli and Gobet's protocols add detail on how candidates are used. The two intermediate players never formed a candidate list and hopped from move to move. The international master, who had read Kotov, followed the textbook almost exactly, building a list he rarely changed and analysing each move to an evaluation. The grandmaster also made a list but added to it whenever a new idea demanded a new candidate.[^s1] The authors conclude that search can be placed under strategic control rather than being purely the "progressive deepening" de Groot observed.[^s1]

## Criticism and refinements

Kotov's procedure is often called too mechanical. GM Bryan Smith doubts that strong players think this way, arguing that pattern recognition chooses the candidates, that in complex positions some candidates only appear after examining variations, and that real analysis involves testing ideas and backtracking.[^s4] The website of GM Rafael Leitão notes that no grandmaster calculates exactly as Kotov prescribes and points out that Kotov's own model analysis misses candidate moves; it describes John Nunn's looser approach of first scanning tempting and forcing moves, returning to build a careful list only in complicated positions, and mentions later revisions by Dvoretsky and Aagaard.[^s5] Serper similarly shows Kotov overlooking a candidate in his own book example that his students found.[^s6]

## Why list alternatives at all

The strongest argument for deliberately naming candidates comes from research on the Einstellung effect. Bilalić, McLeod and Gobet gave experts a position with a familiar five-move smothered mate and a shorter, less familiar three-move mate. No candidate master found the shorter mate when the familiar one was available, though all found it when the familiar idea was disabled. Eye tracking showed players still looking at the familiar solution's squares while saying they were searching for something better.[^s3] The familiar idea cost experts roughly three standard deviations of performance, so a first idea, however good, deserves to be treated as one candidate among several.[^s3]

## Example: include the opponent's forcing replies

After 1.e4 e5 2.Bc4 Nc6 3.Qh5, Black's natural candidates include 3...g6, which attacks the queen and prepares development, 3...Qe7 and 3...Qf6, which guard f7 at some cost, and the attractive 3...Nf6, which attacks the queen.[^s7] Testing each candidate against White's checks and captures eliminates 3...Nf6 at once, because f7 is attacked twice and 4.Qxf7# follows.[^s7]

## Connections

Candidate moves are **part of** calculation, the first step of Kotov's "tree of analysis".[^s1] The technique was **developed by** Alexander Kotov as a teachable method,[^s4] and research descending from Adriaan de Groot measures how many first moves players of each level actually consider, alongside the progressive deepening he described.[^s1][^s2] Listing alternatives **counters** the Einstellung effect, in which a familiar idea hides a better one.[^s3] In tactical positions the scan usually begins with forcing moves,[^s5] and the example above shows why the opponent's forcing replies belong in the check too, which links the technique to prophylaxis.[^s7]

## Sources

[^s1]: Campitelli, G. & Gobet, F. (2004), "Adaptive expert decision making: Skilled chessplayers search more and deeper", *ICGA Journal* 27(4), 209–216. https://bura.brunel.ac.uk/bitstream/2438/825/1/Gobet_Search_ICGA.pdf (accessed 2026-11-12)
[^s2]: Gobet, F. (1998), "Chess players' thinking revisited", *Swiss Journal of Psychology* 57, 18–32. https://bura.brunel.ac.uk/bitstream/2438/822/4/1791.pdf (accessed 2026-11-12)
[^s3]: Bilalić, M., McLeod, P. & Gobet, F. (2010), "The mechanism of the Einstellung (set) effect: A pervasive source of cognitive bias", *Current Directions in Psychological Science* 19(2), 111–115. https://cognition.aau.at/download/Publikationen/Bilalic/Bilalic_etal_2010b.pdf (accessed 2026-11-12)
[^s4]: Bryan Smith (GM), "'Think Like a Grandmaster' by Alexander Kotov", Chess.com. https://www.chess.com/article/view/quotthink-like-a-grandmasterquot-by-alexander-kotov (accessed 2026-11-12)
[^s5]: "The Candidate Moves Technique", Rafael Leitão website. https://rafaelleitao.com/candidate-moves-technique (accessed 2026-11-12)
[^s6]: Gregory Serper (GM), "How To Find The Best Chess Move", Chess.com. https://www.chess.com/article/view/how-to-find-the-best-chess-move (accessed 2026-11-12)
[^s7]: "Scholar's Mate", Chess.com Terms. https://www.chess.com/terms/scholars-mate-chess (accessed 2026-11-12)
