---
id: kt:herbert-simon
type: Person
title: Herbert Simon
aliases: [Herbert A. Simon, Herbert Alexander Simon, H. A. Simon]
domain: training-and-improvement
summary: >-
  American social scientist and computer-science pioneer (1916–2001) who co-wrote the NSS chess
  program with Allen Newell and Cliff Shaw and, with William Chase, founded chunking theory, the
  pattern-recognition account of chess mastery that shaped later expertise research.
status: historical
volatile: false
verified: 2026-11-11
broader: [kt:cognitive-psychology-of-chess]
related: [kt:chunking-theory, kt:template-theory, kt:chess-expertise, kt:allen-newell, kt:history-of-computer-chess, kt:deep-blue-versus-kasparov]
relations:
  - {predicate: influencedBy, object: kt:adriaan-de-groot}
  - {predicate: influencedBy, object: kt:claude-shannon}
sources:
  - id: s1
    title: "Herbert Simon — Biographical"
    publisher: The Nobel Prize (Nobel Prize Outreach)
    url: https://www.nobelprize.org/prizes/economic-sciences/1978/simon/biographical/
    type: reference
    accessed: 2026-11-11
  - id: s2
    title: "Herbert A. Simon — Computer Pioneers"
    publisher: IEEE Computer Society
    url: https://history.computer.org/pioneers/simon.html
    type: reference
    accessed: 2026-11-11
  - id: s3
    title: "Herbert A. Simon"
    publisher: Encyclopaedia Britannica
    url: https://britannica.com/biography/Herbert-A-Simon
    type: reference
    accessed: 2026-11-11
  - id: s4
    title: "Skill in Chess (American Scientist 61, 394-403, 1973)"
    publisher: Herbert A. Simon and William G. Chase, Carnegie-Mellon University
    url: https://www.Gwern.net/doc/psychology/chess/1973-simon.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "Allen Newell 1927–1992: A Biographical Memoir"
    publisher: Herbert A. Simon, National Academy of Sciences
    url: https://www.nasonline.org/wp-content/uploads/2024/06/newell-allen.pdf
    type: academic
    accessed: 2026-11-11
  - id: s6
    title: "Perception in chess and beyond: Commentary on Linhares and Freitas (2010) (New Ideas in Psychology 29, 156-161)"
    publisher: Peter C. R. Lane and Fernand Gobet, University of Hertfordshire Research Archive
    url: https://uhra.herts.ac.uk/id/eprint/235/1/904357.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s7
    title: "Within Ten Years a Digital Computer Will Be the World's Chess Champion"
    publisher: Quote Investigator
    url: https://quoteinvestigator.com/2024/04/18/ai-prediction/
    type: publication
    accessed: 2026-11-11
created: 2026-11-11
---

# Herbert Simon

Herbert Alexander Simon (born 15 June 1916 in Milwaukee, Wisconsin; died 9 February 2001 in Pittsburgh) was an American social scientist who moved from the study of administrative decision-making into computer science and cognitive psychology.[^s1][^s3] He is known outside chess for the idea of "satisficing", accepting a good-enough option instead of searching for the best, and he received the 1975 A.M. Turing Award with Allen Newell and the 1978 Nobel Prize in Economics.[^s2][^s3] For chess players he matters for two things: some of the first selective chess programs, and the chunking theory of chess skill.

## Career in outline

Simon studied at the University of Chicago, taking a PhD in political science in 1943, and in 1949 he moved to the Carnegie Institute of Technology (later Carnegie Mellon University) in Pittsburgh to help build its new Graduate School of Industrial Administration.[^s1][^s2] From 1965 he held a chair in computer science and psychology there.[^s2] He met Newell at the RAND Corporation in 1952, and from about 1954 the two set out to study human problem-solving by simulating it in computer programs. Simon later called this his central research interest.[^s1] Their group preferred the label "complex information processing" to "artificial intelligence".[^s2]

## Chess programs

Chess was an early test case for this programme. Turing and Shannon had described chess strategies by 1950 without programming them. In 1952 Simon sketched an unimplemented program that extended Shannon's ideas.[^s5] Newell's 1955 paper "The Chess Machine" proposed a humanlike design with goals, aspiration levels, "good enough" moves and multi-dimensional evaluation. Many of its ideas went into the **NSS program** (Newell, Shaw, Simon), published in 1958.[^s5] NSS was not the first chess program, since Alex Bernstein's team and others finished theirs a little earlier, and it did not play well. Simon himself recorded the jibe that it was once beaten by a ten-year-old.[^s5] Its point was different. It showed that a very selective search, steered by goals that features of the position switch on, could produce sensible play in a hugely complex domain.[^s5] Simon later built the mating program MATER with George Baylor.[^s2]

The same optimism produced a famous misjudgement. In a 1957 address to the Operations Research Society of America, published in 1958, Simon and Newell predicted that "within ten years a digital computer will be the world's chess champion".[^s7] A computer did not beat a reigning world champion in a match until Deep Blue defeated Garry Kasparov in 1997.[^s7]

## Chunking theory

Simon's lasting influence on chess thinking comes from his psychology. Building on Adriaan de Groot's finding that grandmasters do not search more moves or deeper than weaker players, Simon and his student William Chase used de Groot's brief-exposure recall task.[^s2][^s4] Positions with about 25 pieces were shown for a few seconds. Masters and grandmasters rebuilt about 93% of them correctly, experts about 72%, Class A players about half and novices about a third. With the same pieces placed at random, every group recalled only three or four pieces, so the advantage was specific to chess.[^s4] Pauses in reconstruction marked out "chunks", mostly stereotyped groups such as pawn chains and castled king positions.[^s4] Starting from a simulation that knew about 1,000 patterns, Chase and Simon estimated that a master holds on the order of 50,000 patterns, built up over 10,000 to 50,000 hours of study.[^s4]

Their conclusion was that mastery rests mainly on recognising familiar patterns, which in turn suggest plausible moves, not on calculating further.[^s4] The detailed figures were soon revised. Chase and Simon's own master recalled more chunks than weaker players, something the theory had not predicted, and later computer-display replications found master chunks of up to 15 pieces.[^s4][^s6] With Fernand Gobet in the 1990s Simon revisited the hypothesis and co-developed template theory, which the CHREST model implements.[^s6]

## Why it matters to players

For a club player the practical lesson is about how to train: build a large stock of meaningful patterns through years of study and play, not just raw calculating power.[^s4] Simon's chess programs also illustrate a point every strong player knows: good players and good programs alike have to select candidate moves, since nobody can examine everything.[^s5]

## Connections

Simon belongs to the **cognitive psychology of chess** and the study of **chess expertise**.[^s4] He was **influenced by** Adriaan de Groot's experiments and by Claude Shannon's early plan for a chess program.[^s4][^s5] His long partnership with **Allen Newell** produced the NSS program, part of the **history of computer chess**, and his 1958 forecast is often recalled in connection with **Deep Blue versus Kasparov**.[^s5][^s7] With Chase he founded **chunking theory**, and with Gobet he developed its successor, **template theory**.[^s4][^s6]

## Sources
[^s1]: The Nobel Prize, "Herbert Simon — Biographical". https://www.nobelprize.org/prizes/economic-sciences/1978/simon/biographical/ (accessed 2026-11-11)
[^s2]: IEEE Computer Society, "Herbert A. Simon", Computer Pioneers. https://history.computer.org/pioneers/simon.html (accessed 2026-11-11)
[^s3]: Encyclopaedia Britannica, "Herbert A. Simon". https://britannica.com/biography/Herbert-A-Simon (accessed 2026-11-11)
[^s4]: Simon, H. A. & Chase, W. G., "Skill in Chess", *American Scientist* 61 (1973), 394–403. https://www.Gwern.net/doc/psychology/chess/1973-simon.pdf (accessed 2026-11-11)
[^s5]: Simon, H. A., "Allen Newell 1927–1992", Biographical Memoirs, National Academy of Sciences (1997). https://www.nasonline.org/wp-content/uploads/2024/06/newell-allen.pdf (accessed 2026-11-11)
[^s6]: Lane, P. C. R. & Gobet, F., "Perception in chess and beyond: Commentary on Linhares and Freitas (2010)", *New Ideas in Psychology* 29 (2011), 156–161. https://uhra.herts.ac.uk/id/eprint/235/1/904357.pdf (accessed 2026-11-11)
[^s7]: Quote Investigator, "Within Ten Years a Digital Computer Will Be the World's Chess Champion" (18 April 2024). https://quoteinvestigator.com/2024/04/18/ai-prediction/ (accessed 2026-11-11)
