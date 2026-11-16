---
id: kt:long-term-working-memory
type: CognitiveConcept
title: Long-term working memory
aliases: [LT-WM, LTWM, Long-term working memory theory, Ericsson and Kintsch theory of expert memory]
domain: training-and-improvement
summary: >-
  K. Anders Ericsson and Walter Kintsch's 1995 theory that skilled performers, including strong chess
  players, extend working memory by encoding information rapidly into long-term memory through acquired
  retrieval structures and knowledge-based associations, leaving only retrieval cues in short-term memory.
status: contested
volatile: false
verified: 2026-11-16
broader: [kt:chess-expertise, kt:cognitive-psychology-of-chess]
related: [kt:blindfold-chess, kt:visualization, kt:chunking-theory, kt:calculation]
relations:
  - {predicate: developedBy, object: kt:anders-ericsson}
  - {predicate: developedBy, object: kt:walter-kintsch}
  - {predicate: influencedBy, object: kt:skilled-memory-theory}
  - {predicate: contrastsWith, object: kt:template-theory}
sources:
  - id: s1
    title: "Some shortcomings of long-term working memory (British Journal of Psychology 91, 551-570)"
    publisher: Fernand Gobet, via CORE
    url: https://core.ac.uk/download/333525.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "Long-term working memory: A computational implementation for chess expertise (Proceedings of the 3rd International Conference on Cognitive Modelling, 142-149)"
    publisher: Fernand Gobet, Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/2127/1/LTWM-ICCM.pdf
    type: academic
    accessed: 2026-11-16
  - id: s3
    title: "Retrieval structures and schemata: A brief reply to Ericsson and Kintsch (British Journal of Psychology 91, 591-594)"
    publisher: Fernand Gobet, via CORE
    url: https://core.ac.uk/download/15038.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s4
    title: "Contributions of K. Anders Ericsson to Experimental Cognitive Psychology (Journal of Expertise 4(2), 131-143)"
    publisher: Neil Charness, Journal of Expertise
    url: https://www.journalofexpertise.org/articles/volume4_issue2/JoE_4_2_Charness.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s5
    title: "Expert memory: A comparison of four theories (Cognition 66, 115-152)"
    publisher: Fernand Gobet, Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/815/1/FullText.pdf
    type: peer-reviewed
    accessed: 2026-11-16
created: 2026-11-16
---

# Long-term working memory

Long-term working memory (LT-WM) is a theory of expert memory proposed by K. Anders Ericsson and Walter Kintsch in 1995. It was offered as a counterweight to views that locate working memory entirely in a small short-term store: experts, it says, keep the products of their thinking in long-term memory, while short-term memory holds only the cues needed to get back to them.[^s4] The theory grew out of the skilled memory theory of Chase and Ericsson and was presented as general, covering digit-span experts, waiters memorising orders, mental calculators, medical diagnosis, text comprehension and chess.[^s1][^s5] In chess psychology it is the main rival to Gobet and Simon's template theory, and the two camps disagree sharply about the evidence.[^s1][^s3]

## How the theory works

LT-WM names two encoding mechanisms. The first is the retrieval structure, a stable set of cues in long-term memory to which new items can be attached and later found again; the second is knowledge-based association, in which incoming information is linked to patterns and schemas the expert already owns.[^s1][^s2] Neil Charness summarises the picture as chunks and retrieval structures in long-term memory, retrieval cues in short-term memory, and association processes that let experts get round normal capacity limits.[^s4] The theory was used to explain feats such as memory experts recalling about 100 random digits and grandmasters recalling about 80 plies of a game.[^s4]

For chess, Ericsson and Kintsch proposed that strong players use a hierarchical retrieval structure corresponding to the 64 squares, linking pieces to their locations and to one another.[^s1] Such a structure was meant to explain fast encoding of positions, blindfold play and the ability to plan by holding imagined positions in mind.[^s1] Gobet distinguished a literal "square" reading, in which any piece can be stored on its square, from a looser "hierarchy" reading in which patterns are stored at various levels of the structure.[^s5]

## The case against it

Random positions became the key test. If a master can attach any piece to its square, the square version predicts a large skill effect on random boards; chunking and template theories predict only a small one.[^s5] In the data Gobet reviewed, masters placed about 5.5 pieces of a random position after five seconds against about 2.6 for weaker players, managed roughly a third of the pieces at five seconds and no more than about two thirds even after a minute.[^s5] When four random positions were dictated one after another, masters recalled only about 10 percent of each, against about 60 percent for game positions.[^s1] Mirror-image positions were recalled slightly worse than originals, and swapping quadrants of the board cut recall sharply, which a uniform square-by-square structure does not predict.[^s5] In blindfold experiments masters recalled over 90 percent of positions from legal random games but only about 20 percent from illegal ones.[^s1]

Gobet also argued that the theory leaves encoding times, decay and the structure's organisation unspecified, and that its notion of a retrieval structure mixes three kinds of memory structure with different properties.[^s1] He concluded that generic retrieval structures apply mainly when people deliberately train their memory, as the digit-span experts did.[^s1] Charness, writing in a tribute to Ericsson, likewise described the theory as vague and hard to test.[^s4]

## A worked example: the dictation experiment

To make the theory testable, Gobet implemented it as a computer model and ran it on Saariluoma's dictation task, in which about 25 pieces are read aloud at two seconds each.[^s2] The model had a three-piece articulatory loop, about 100,000 chunks borrowed from CHREST, and a 64-square retrieval structure, and it was tested on 1,000 game and 1,000 random positions.[^s2] Human masters scored about 58 percent on random positions; the model exceeded that once the probability of storing a piece in the retrieval structure reached 0.4, so Gobet argued the data require low encoding probabilities, averaging no more than about 0.5.[^s2]

## The reply and what remains contested

Ericsson and Kintsch replied that their 1995 theory set aside expert-memory results unless superior memory defined the expertise, and that template theory covers memory for positions rather than move selection.[^s3] Gobet answered that template theory also models search, and that LT-WM itself lacks an account of search and evaluation.[^s3] Strong researchers agree that experts encode quickly into long-term memory; they disagree about whether a generic square-based structure or position-specific templates do the work.[^s3][^s5]

For training, the debate is a caution against assuming that board memory is a general-purpose skill: the evidence above suggests that recall and visualisation in chess lean on familiar, meaningful patterns, so they tend to grow with study of real games rather than with memory drills on arbitrary positions.[^s1][^s5]

## Connections

Long-term working memory belongs to the study of chess expertise and the cognitive psychology of chess. It was developed by Anders Ericsson and Walter Kintsch and influenced by skilled memory theory.[^s1][^s4] It contrasts with template theory, Gobet's extension of chunking theory, which uses position-specific structures instead of a generic 64-square one.[^s5] It relates to blindfold chess and visualisation, which it was meant to explain, and to calculation, where holding imagined positions in mind matters most.[^s1][^s3]

## Sources

[^s1]: Gobet, F. (2000), "Some shortcomings of long-term working memory", *British Journal of Psychology* 91, 551-570. https://core.ac.uk/download/333525.pdf (accessed 2026-11-16)
[^s2]: Gobet, F. (2000), "Long-term working memory: A computational implementation for chess expertise", *Proceedings of the 3rd International Conference on Cognitive Modelling*, 142-149. https://bura.brunel.ac.uk/bitstream/2438/2127/1/LTWM-ICCM.pdf (accessed 2026-11-16)
[^s3]: Gobet, F. (2000), "Retrieval structures and schemata: A brief reply to Ericsson and Kintsch", *British Journal of Psychology* 91, 591-594. https://core.ac.uk/download/15038.pdf (accessed 2026-11-16)
[^s4]: Charness, N. (2021), "Contributions of K. Anders Ericsson to Experimental Cognitive Psychology", *Journal of Expertise* 4(2), 131-143. https://www.journalofexpertise.org/articles/volume4_issue2/JoE_4_2_Charness.pdf (accessed 2026-11-16)
[^s5]: Gobet, F. (1998), "Expert memory: A comparison of four theories", *Cognition* 66, 115-152. https://bura.brunel.ac.uk/bitstream/2438/815/1/FullText.pdf (accessed 2026-11-16)
