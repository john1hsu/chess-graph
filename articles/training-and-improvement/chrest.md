---
id: kt:chrest
type: CognitiveConcept
title: CHREST
aliases: [Chunk Hierarchy and REtrieval STructures, Chunk Hierarchy REtrieval STructures, CHREST cognitive architecture, CHREST model]
domain: training-and-improvement
summary: >-
  A computational cognitive architecture, built mainly by Fernand Gobet and Peter Lane, that learns
  chess patterns as chunks in a discrimination network and simulates how players of different
  strength look at, recognise and remember positions.
fen: "6k1/5ppp/8/8/8/8/5PPP/5RK1 w - - 0 1"
status: current
volatile: false
verified: 2026-11-24
broader: [kt:cognitive-psychology-of-chess, kt:chess-expertise]
related: [kt:template-theory, kt:chunking-theory, kt:visualization, kt:adriaan-de-groot]
relations:
  - {predicate: developedBy, object: kt:fernand-gobet}
  - {predicate: developedBy, object: kt:peter-lane}
  - {predicate: influencedBy, object: kt:epam}
  - {predicate: influencedBy, object: kt:chunking-theory}
  - {predicate: contrastsWith, object: kt:long-term-working-memory}
sources:
  - id: s1
    title: "Attention Mechanisms in the CHREST Cognitive Architecture"
    publisher: Peter C. R. Lane, Fernand Gobet and Richard Ll. Smith, University of Hertfordshire Research Archive
    url: https://uhra.herts.ac.uk/id/eprint/197/1/903377.pdf
    type: academic
    accessed: 2026-11-24
  - id: s2
    title: "Checking Chess Checks with Chunks: A Model of Simple Check Detection (Proceedings of the Ninth International Conference on Cognitive Modeling, 2009)"
    publisher: Richard Ll. Smith, Fernand Gobet and Peter C. R. Lane, Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/3503/1/Checking%20chess%20checks%20with%20chunks%3a%20A%20model%20of%20simple%20check%20detection.pdf
    type: peer-reviewed
    accessed: 2026-11-24
  - id: s3
    title: "Chunks, Schemata, and Retrieval Structures: Past and Current Computational Models (Frontiers in Psychology 6:1785, 2015)"
    publisher: Fernand Gobet, Peter C. R. Lane and Martyn Lloyd-Kelly, via PubMed Central
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4657374
    type: peer-reviewed
    accessed: 2026-11-24
  - id: s4
    title: "Mental Imagery and Chunks: Empirical and Computational Findings"
    publisher: Andrew J. Waters and Fernand Gobet, Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/1618/1/Mental%20imagery%20and%20chunks.pdf
    type: academic
    accessed: 2026-11-24
created: 2026-11-24
---

# CHREST

CHREST (Chunk Hierarchy and REtrieval STructures) is a computer model of human learning and perception that has been used to test theories of chess skill. It descends from EPAM, the Elementary Perceiver and Memoriser of Edward Feigenbaum and Herbert Simon, to which it adds templates and a more detailed model of perception.[^s1] Its main authors are Fernand Gobet and Peter Lane, and it is one of the two programs that implement template theory.[^s1][^s4] Its value for chess psychology is that it turns verbal claims about "chunks" into a program with timing parameters, so its predictions can be checked against human data.[^s3]

## How the architecture works

CHREST has a simulated eye, a small short-term memory, a long-term memory and a "mind's eye" for imagining moves.[^s4] Long-term memory is a discrimination network: a tree of nodes joined by test links, each node holding a chunk of piece-on-square features.[^s1][^s2] When the model meets a pattern that does not match what it already knows, it **discriminates**, growing a new branch; when the pattern matches, it **familiarises**, adding detail to the existing chunk.[^s1] Short-term memory holds only a handful of pointers to chunks in long-term memory (three visual items in one version, four in another).[^s2][^s4]

The model's timings are fixed in advance rather than tuned to each experiment. Creating a new chunk takes about eight seconds, filling a slot of a template about 250 milliseconds, and sorting a pattern through the network 10 milliseconds plus 10 per item.[^s4] Chunks that are recognised often enough grow into templates, and chunks can be linked to moves, plans and tactical ideas, or to each other by similarity links.[^s1][^s4]

## Eye movements and perception

The simulated eye sees only a couple of squares around its fixation point.[^s4] Where to look next is decided first by what long-term memory suggests, then by chess heuristics, such as looking at typical king squares or at a square attacked by the piece just fixated, and finally at random.[^s1] With a network of about 300,000 chunks, CHREST's average fixation was 272 ms against 315 ms for a novice network, close to the 260 ms and 310 ms measured in human masters and novices, and the large network spread its fixations over the important parts of the board as the masters did.[^s1]

## What it has explained

CHREST predicted, against the common view of the time, that strong players should recall even random positions slightly better than weaker ones, simply because a bigger chunk store finds more chance patterns; later data on fully random boards came close to the model's figures.[^s3] In a mental-imagery study, networks from about 1,000 to 300,000 chunks reproduced how much worse players recall positions whose pieces are drawn between squares, supporting the idea that pieces are shifted serially in the mind's eye before chunks are recognised.[^s4]

A 2009 study modelled the classic check-detection task, in which a player sees a king and one enemy piece and must say whether it is check. Networks of 100 to 100,000 nodes, trained on 10,000 games between players rated over 2000, took from about 1.3 seconds down to 0.6 seconds and fitted the human times with r² of 0.94; the model's weakness was that it never made the errors humans made.[^s2] A related program, CHUMP (Gobet and Jansen, 1994), linked patterns to master moves to choose moves, but played weakly because it did not look ahead.[^s1]

## Example and lessons for players

The key position shows the castled-king pattern that CHREST papers use as a typical chunk: king g1, rook f1 and pawns f2, g2 and h2, stored as a single unit.[^s2] A strong player sees such a group at a glance, and CHREST's attention model skips such standard areas to fixate unusual, salient pieces.[^s1]

The practical message matches the model's design: skill comes from a very large stock of patterns, built slowly through exposure to real positions, and that stock speeds even simple judgements such as spotting checks.[^s2][^s3] Fast recognition is not deep calculation, though; CHUMP's weakness shows that patterns need search to become strong play.[^s1]

## Connections

CHREST belongs to the cognitive psychology of chess and the study of chess expertise.[^s3] It was developed by Fernand Gobet and Peter Lane, influenced by EPAM and by Chase and Simon's chunking theory, and serves as the running version of template theory.[^s1][^s4] Its mind's eye models visualization, and its recall simulations continue Adriaan de Groot's experiments.[^s1][^s4] It contrasts with Ericsson and Kintsch's long-term working memory, which its authors criticise as too loosely specified to test.[^s3]

## Sources

[^s1]: Lane, P. C. R., Gobet, F. & Smith, R. Ll., "Attention Mechanisms in the CHREST Cognitive Architecture". https://uhra.herts.ac.uk/id/eprint/197/1/903377.pdf (accessed 2026-11-24)
[^s2]: Smith, R. Ll., Gobet, F. & Lane, P. C. R. (2009), "Checking Chess Checks with Chunks: A Model of Simple Check Detection", Proceedings of the Ninth International Conference on Cognitive Modeling. https://bura.brunel.ac.uk/bitstream/2438/3503/1/Checking%20chess%20checks%20with%20chunks%3a%20A%20model%20of%20simple%20check%20detection.pdf (accessed 2026-11-24)
[^s3]: Gobet, F., Lane, P. C. R. & Lloyd-Kelly, M. (2015), "Chunks, Schemata, and Retrieval Structures: Past and Current Computational Models", *Frontiers in Psychology* 6:1785. https://pmc.ncbi.nlm.nih.gov/articles/PMC4657374 (accessed 2026-11-24)
[^s4]: Waters, A. J. & Gobet, F., "Mental Imagery and Chunks: Empirical and Computational Findings". https://bura.brunel.ac.uk/bitstream/2438/1618/1/Mental%20imagery%20and%20chunks.pdf (accessed 2026-11-24)
