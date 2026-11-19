---
id: kt:allen-newell
type: Person
title: Allen Newell
aliases: [A. Newell]
domain: training-and-improvement
summary: >-
  American computer scientist and cognitive psychologist (1927–1992) whose 1955 paper "The Chess
  Machine" and the goal-driven NSS chess program he built with Cliff Shaw and Herbert Simon treated
  chess as a laboratory for modelling selective, humanlike problem solving.
status: historical
volatile: false
verified: 2026-11-19
broader: [kt:cognitive-psychology-of-chess, kt:history-of-computer-chess]
related: [kt:herbert-simon, kt:claude-shannon, kt:game-tree-search, kt:candidate-moves, kt:alpha-beta-pruning]
relations:
  - {predicate: influencedBy, object: kt:oliver-selfridge}
sources:
  - id: s1
    title: "Allen Newell 1927–1992: A Biographical Memoir"
    publisher: Herbert A. Simon, National Academy of Sciences
    url: https://www.nasonline.org/wp-content/uploads/2024/06/newell-allen.pdf
    type: academic
    accessed: 2026-11-19
  - id: s2
    title: "Allen Newell — Computer Pioneers"
    publisher: IEEE Computer Society
    url: https://history.computer.org/newell.html
    type: reference
    accessed: 2026-11-19
  - id: s3
    title: "Chess-Playing Programs and the Problem of Complexity"
    publisher: Allen Newell, J. C. Shaw and H. A. Simon, archived by AITopics (AAAI)
    url: https://aitopics.org/download/aiclassics:F75D75A1
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s4
    title: "Allen Newell"
    publisher: IEEE Computer Society
    url: https://www.computer.org/profiles/allen-newell
    type: reference
    accessed: 2026-11-19
  - id: s5
    title: "Artificial Intelligence pioneers Allen Newell (right) and Herbert Simon — Mastering the Game"
    publisher: Computer History Museum
    url: https://www.computerhistory.org/chess/stl-431e1a07cf7a1/
    type: archive
    accessed: 2026-11-19
created: 2026-11-19
---

# Allen Newell

Allen Newell (born 19 March 1927 in San Francisco; died 19 July 1992 in Pittsburgh) was an American computer scientist and psychologist, one of the founders of artificial intelligence and cognitive science.[^s1][^s2] He took a physics degree at Stanford in 1949, spent a year of graduate study at Princeton, and joined the RAND Corporation in 1950. He completed a PhD in industrial administration at the Carnegie Institute of Technology in 1957 and taught there, at what became Carnegie Mellon University, until his death.[^s2] He shared the 1975 ACM Turing Award with Herbert Simon for contributions to artificial intelligence and the psychology of human cognition.[^s2][^s4] For chess, Newell matters because he used the game as an early test bed for a central question: how can a system with limited capacity play well in a domain far too large to search exhaustively?

## The Chess Machine (1955)

Newell traced his turn to this question to a RAND seminar in September 1954 in which Oliver Selfridge described a pattern-recognition program that learned; he later called it a "conversion experience".[^s1][^s4] The following March he presented "The Chess Machine" at the Western Joint Computer Conference. It sketched a program meant to play in a "humanoid fashion" rather than by brute force.[^s1][^s4] Its ideas included goals and aspiration levels that tell the search when to stop, accepting a move that is "good enough" instead of insisting on the best, evaluation along several dimensions at once, the generation of subgoals, and a symbolic description of the board.[^s1] The design was never implemented as written. Work with Cliff Shaw on RAND's JOHNNIAC computer turned first to geometry and then to logic, which produced the Logic Theory Machine of 1956.[^s1][^s4]

## The NSS program

Newell, Shaw and Simon returned to chess with the NSS program, described in the 1958 paper "Chess-Playing Programs and the Problem of Complexity".[^s1][^s3] It was built from independent goals, each standing for a chess concept such as material balance, centre control, development, pawn structure or king safety, and goals could be added or removed without disturbing the others.[^s3] At each move the program chose the goals relevant to the position and ranked them. Each goal had its own generator of candidate moves, its own static evaluation and its own generator of moves to analyse further. The paper summed up the split as "a generator proposes; the analysis procedure disposes".[^s3] Search on a line stopped once the position was quiet for every goal, values were compared goal by goal in order of priority, and the program played the first move that met its acceptance level.[^s3]

The authors compared NSS with the Los Alamos program, which looked at every move on a 6×6 board two moves deep, and with Alex Bernstein's IBM 704 program, which looked at no more than seven plausible moves in each position.[^s3] NSS was far slower than Bernstein's and was never fully debugged. In the sample game in the paper's appendix it lost to Simon, and the authors blamed missing goals for king safety, serious threats and promotion.[^s3] Simon later recalled critics' jibe that it once lost to a ten-year-old, and argued that they missed the point. The program was meant to show that highly selective search, steered by goals, could yield sensible behaviour in a complex task.[^s1] The Computer History Museum includes NSS on JOHNNIAC among the pioneering chess programs in its *Mastering the Game* exhibition.[^s5]

## Why it matters to players

NSS is a mechanical model of how strong players already think. They do not look at every legal move. Features of the position (an exposed king, an open centre, lagging development) suggest a handful of candidate moves, and a player stops analysing once one meets the needs of the position.[^s3] The goal-by-goal design also mirrors good training habits: name the position's priorities before calculating, and check every candidate against the most urgent of them first.[^s3] The appendix game makes the converse point. A thinker that never asks about king safety or threats will lose however sound its other judgements are.[^s3]

## Later work

After chess, Newell's research moved to general problem solving. He co-wrote *Human Problem Solving* (1972) with Simon, developed the Soar cognitive architecture from the early 1980s, and set out his programme in *Unified Theories of Cognition* (1990).[^s2] He was the first president of the American Association for Artificial Intelligence.[^s2]

## Connections

Newell belongs to the **cognitive psychology of chess** and the **history of computer chess**.[^s1][^s5] His closest partner was **Herbert Simon**, his doctoral adviser and Turing Award co-recipient.[^s4] He was **influenced by** Oliver Selfridge's learning program, and NSS followed the chess strategies that **Claude Shannon** had described without programming.[^s1][^s3] NSS's goal-driven, selective **game-tree search** stands in contrast to full-width search, and in the paper minimaxing runs alongside move generation so that some lines can be cut off, an early relative of **alpha-beta pruning**.[^s3] Its move generators model the human habit of choosing **candidate moves**.[^s3]

## Sources
[^s1]: Simon, H. A., "Allen Newell 1927–1992", Biographical Memoirs, National Academy of Sciences (1997). https://www.nasonline.org/wp-content/uploads/2024/06/newell-allen.pdf (accessed 2026-11-19)
[^s2]: IEEE Computer Society, "Allen Newell", Computer Pioneers. https://history.computer.org/newell.html (accessed 2026-11-19)
[^s3]: Newell, A., Shaw, J. C. & Simon, H. A., "Chess-Playing Programs and the Problem of Complexity" (1958), AITopics archive. https://aitopics.org/download/aiclassics:F75D75A1 (accessed 2026-11-19)
[^s4]: IEEE Computer Society, "Allen Newell". https://www.computer.org/profiles/allen-newell (accessed 2026-11-19)
[^s5]: Computer History Museum, "Artificial Intelligence pioneers Allen Newell (right) and Herbert Simon", *Mastering the Game*. https://www.computerhistory.org/chess/stl-431e1a07cf7a1/ (accessed 2026-11-19)
