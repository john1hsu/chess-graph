---
id: kt:progressive-deepening
type: CognitiveConcept
title: Progressive deepening
aliases: [Progressive deepening of search, Reinvestigation, Move reinvestigation]
domain: training-and-improvement
summary: >-
  Adriaan de Groot's name for the way chess players return again and again to the same candidate
  move or variation while thinking, each time looking a little further or with new information,
  instead of analysing every option once to a fixed depth.
status: current
volatile: false
verified: 2026-11-13
broader: [kt:calculation, kt:cognitive-psychology-of-chess]
related: [kt:candidate-moves, kt:iterative-deepening, kt:chess-expertise, kt:template-theory]
relations:
  - {predicate: partOf, object: kt:calculation}
  - {predicate: developedBy, object: kt:adriaan-de-groot}
sources:
  - id: s1
    title: "Adriaan Dingeman de Groot (1914–2006) — obituary, Psychologische Rundschau"
    publisher: Fernand Gobet and Jochen Musch, Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/2617/1/De%20Groot%20Obituary%20-%20%20Psychologische%20Rundschau.pdf
    type: academic
    accessed: 2026-11-13
  - id: s2
    title: "Chess players' thinking revisited (Swiss Journal of Psychology 57, 1998)"
    publisher: Fernand Gobet, Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/822/4/1791.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "Expertise in Chess (Cambridge Handbook of Expertise and Expert Performance, 2006, pp. 523–538)"
    publisher: Fernand Gobet and Neil Charness, Cambridge University Press
    url: https://www.cambridge.org/core/books/cambridge-handbook-of-expertise-and-expert-performance/expertise-in-chess/80ECEE9EB4E29866F90C8A45B9F8034E
    type: academic
    accessed: 2026-11-13
  - id: s4
    title: "Adaptive expert decision making: Skilled chessplayers search more and deeper (ICGA Journal 27(4), 2004)"
    publisher: Guillermo Campitelli and Fernand Gobet, Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/825/1/Gobet_Search_ICGA.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s5
    title: "Iterative Deepening"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org:443/Iterative_Deepening
    type: community
    accessed: 2026-11-13
created: 2026-11-13
---

# Progressive deepening

**Progressive deepening** is the term the Dutch psychologist and chess master Adriaan de Groot gave to a pattern he found in the spoken thoughts of chess players choosing a move: they examined the same continuation several times, sometimes straight away and sometimes after turning to a different move in between.[^s1] Instead of analysing each candidate once and filing a verdict, players kept coming back to a line, looked at it a little further or from a new angle, and carried what they had learned elsewhere back into it.[^s1][^s3] De Groot reported it in his 1946 thesis, published in English as *Thought and Choice in Chess*.[^s3]

## How it works

De Groot gave the phenomenon two functions. Returning to a line compensates for the limits of working memory, since a player cannot hold a whole analysis tree in mind at once; and it lets information discovered in one branch of the search, such as a new threat or a defensive resource, be passed to another branch.[^s3] He explained it as the product of a cyclical organisation of thought: a nested sequence of phases of observation, checking and evaluation that solve a problem and the subproblems it throws up.[^s1] He believed this stepwise deepening was not special to chess but typical of most complex, goal-directed thinking, and used scientific research as his comparison.[^s1]

Progressive deepening was one of two features de Groot found in players of every strength. The other was selectivity: out of roughly thirty legal moves, players usually examined only three or four.[^s1] Later writers on expertise list progressive deepening, selective search, pattern recognition and experts' memory for positions as findings first made in chess that have since been seen in other fields of expertise.[^s3]

## Measuring it

Fernand Gobet's 1998 replication of de Groot's think-aloud study, with 48 Swiss players, split reinvestigation into two measures. **Immediate reinvestigation** means analysing the same first move again in the very next episode of thought; **non-immediate reinvestigation** means returning to it after at least one other move has been looked at.[^s2] The total number of reinvestigations did not differ reliably by skill. But the largest number of immediate returns to any single move rose with playing strength, while the largest number of non-immediate returns fell with it.[^s2] Masters also spent the least time in the opening orientation phase, about a minute on average against more than four for Class B players.[^s2] Pooled across levels, the Swiss figures were not significantly different from de Groot's own.[^s2]

Gobet read these results as support for pattern-recognition accounts of skill: strong players spot good moves quickly, so they name fewer first moves, stay with one of them longer, and jump between alternatives less.[^s2] A weaker player's thinking, by contrast, tends to hop from move to move and back again without settling.[^s2]

Later work showed that progressive deepening is not the whole story. In Campitelli and Gobet's study of four players from Class B to grandmaster, the grandmaster's protocols also showed repeated returns to the same variation, but his search was not limited to that pattern; the authors concluded that search can be placed under strategic control and that players adapt their method to the task.[^s4]

## Practical lessons

For a club player the research suggests a few habits. Revisiting a line is normal and useful when each return adds something, such as checking a defence found while analysing another move. Endless switching between candidates without new information is a sign of the weaker players' pattern in Gobet's data.[^s2] A short, purposeful orientation before calculating, identifying threats, plans and the few moves worth examining, was a feature of the strongest players.[^s2]

## Connections

Progressive deepening is **part of** the study of **calculation** and a classic finding of the **cognitive psychology of chess**; it was **developed by** **Adriaan de Groot**.[^s1][^s3] It describes how players work through their **candidate moves**, and its dependence on fast recognition of good moves links it to **chess expertise** research and to the pattern-based **template theory** that Gobet's interpretation supports.[^s2][^s3] In computer chess the similar-sounding **iterative deepening** is a different idea: Jim Gillogly coined that term for a full-width search repeated to increasing depths, to separate it from the progressively more focused search de Groot had described.[^s5]

## Sources
[^s1]: Gobet, F. & Musch, J., obituary of Adriaan Dingeman de Groot, *Psychologische Rundschau*. https://bura.brunel.ac.uk/bitstream/2438/2617/1/De%20Groot%20Obituary%20-%20%20Psychologische%20Rundschau.pdf (accessed 2026-11-13)
[^s2]: Gobet, F., "Chess players' thinking revisited", *Swiss Journal of Psychology* 57 (1998). https://bura.brunel.ac.uk/bitstream/2438/822/4/1791.pdf (accessed 2026-11-13)
[^s3]: Gobet, F. & Charness, N., "Expertise in Chess", in Ericsson, Charness, Feltovich & Hoffman (eds.), *The Cambridge Handbook of Expertise and Expert Performance*, Cambridge University Press, 2006, pp. 523–538. https://www.cambridge.org/core/books/cambridge-handbook-of-expertise-and-expert-performance/expertise-in-chess/80ECEE9EB4E29866F90C8A45B9F8034E (accessed 2026-11-13)
[^s4]: Campitelli, G. & Gobet, F., "Adaptive expert decision making: Skilled chessplayers search more and deeper", *ICGA Journal* 27(4) (2004), 209–216. https://bura.brunel.ac.uk/bitstream/2438/825/1/Gobet_Search_ICGA.pdf (accessed 2026-11-13)
[^s5]: Chess Programming Wiki, "Iterative Deepening". https://www.chessprogramming.org:443/Iterative_Deepening (accessed 2026-11-13)
