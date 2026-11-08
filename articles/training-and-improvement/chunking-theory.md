---
id: kt:chunking-theory
type: CognitiveConcept
title: Chunking theory
aliases: [Chunking hypothesis, Chase and Simon chunking theory, Chess chunks, Perceptual chunking in chess]
domain: training-and-improvement
summary: >-
  The theory, proposed by William Chase and Herbert Simon in 1973, that chess skill rests on a large
  store of familiar piece configurations ("chunks") held in long-term memory, which strong players
  recognise as single units and which cue relevant moves.
fen: "r1bq1rk1/ppp2ppp/2np1n2/2b1p3/2B1P3/2NP1N2/PPP2PPP/R1BQ1RK1 w - - 2 7"
status: current
volatile: false
verified: 2026-11-08
broader: [kt:chess-expertise, kt:cognitive-psychology-of-chess]
related: [kt:deliberate-practice, kt:visualization, kt:einstellung-effect, kt:game-tree-search]
relations:
  - {predicate: developedBy, object: kt:herbert-simon}
  - {predicate: developedBy, object: kt:william-chase}
  - {predicate: influencedBy, object: kt:adriaan-de-groot}
  - {predicate: leadsTo, object: kt:template-theory}
  - {predicate: contrastsWith, object: kt:game-tree-search}
sources:
  - id: s1
    title: "Perception in chess and beyond: Commentary on Linhares and Freitas (2010) (New Ideas in Psychology 29, 156-161)"
    publisher: Peter C. R. Lane and Fernand Gobet, University of Hertfordshire Research Archive
    url: https://uhra.herts.ac.uk/id/eprint/235/1/904357.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s2
    title: "Recall of random and distorted chess positions: Implications for the theory of expertise (Memory & Cognition 24(4), 493-503)"
    publisher: Fernand Gobet and Herbert A. Simon, Springer / Psychonomic Society
    url: https://link.springer.com/content/pdf/10.3758%2FBF03200937.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s3
    title: "Five seconds or sixty? Presentation time in expert memory (Cognitive Science)"
    publisher: Fernand Gobet and Herbert A. Simon, via CORE
    url: https://core.ac.uk/download/333524.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s4
    title: "Implicit learning of expert chess knowledge (AISB Quarterly 114)"
    publisher: Fernand Gobet, via CORE
    url: https://core.ac.uk/download/334663.pdf
    type: academic
    accessed: 2026-11-08
  - id: s5
    title: "What's in a name? The multiple meanings of 'chunk' and 'chunking' (Frontiers in Psychology 7:102)"
    publisher: Fernand Gobet, Martyn Lloyd-Kelly and Peter C. R. Lane, Frontiers
    url: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.00102/pdf
    type: peer-reviewed
    accessed: 2026-11-08
created: 2026-11-08
---

# Chunking theory

Chunking theory is the best-known psychological account of why strong chess players see the board differently from weaker ones. It grew out of Adriaan de Groot's studies, which found that grandmasters chose better moves than strong amateurs without searching more: all his players were selective and examined roughly a hundred positions, yet masters could recall a game position almost perfectly after seeing it for a few seconds.[^s4] William Chase and Herbert Simon's 1973 paper "Perception in chess" turned that observation into a theory: expertise is the acquisition of many perceptual chunks, groups of features that are handled as single units.[^s4][^s5]

## How the theory works

Chase and Simon measured chunks directly. In a copying task the player rebuilt a position while it stayed visible, and the glances back at the model marked where one chunk ended; in a recall task the player rebuilt it from memory after a short exposure.[^s1] Placements made less than two seconds apart were counted as one chunk, and longer pauses as a boundary between chunks.[^s1][^s2] Their master's between-glance latencies averaged 2.8 seconds against 3.2 for a Class A player and 3.5 for a beginner, and his recall chunks were larger (2.5 pieces against 2.1 and 1.9) and more numerous.[^s1]

Because short-term memory holds only a few chunks, the theory explains the master's recall advantage by chunk size, not by a bigger memory.[^s3] Simon and Gilmartin estimated that a master knows about 50,000 chunks, comparable to an educated adult's vocabulary.[^s2] Chunks are also more than memory: in Gobet's computational model CHREST, which descends from this work, each chunk node stores piece locations together with pointers to possible moves, so recognising a pattern brings candidate moves to mind.[^s4] That is why chunking is often contrasted with the brute-force search of computers.

## Evidence and revisions

The theory's strongest support is the game-versus-random contrast. With a few seconds' exposure, the gap between masters and Class A players is about 60 percentage points on game positions but only about 20 on random ones, because familiar patterns are nearly absent from random boards.[^s3] The original finding was that skill made no difference on random positions; later work showed a small but real advantage, which the theory attributes to masters' larger stock of small chunks that occasionally match by chance.[^s3][^s4] Chunks are also tied to exact squares: mirror-image positions impair recall, mostly through omissions.[^s2]

Some details did not survive. Chase and Simon's physical board limited what a hand could place, and computer-display replications found masters' chunks reaching up to 15 pieces with fewer than three chunks per position.[^s1] Charness (1976) and others also found masters relatively insensitive to interference tasks, a result any account of expert memory must explain.[^s3] Gobet and Simon's template theory answered this: frequently met configurations grow into templates with a fixed core of about a dozen pieces and slots that can be filled quickly, learned over hours and numbering several thousand for a master.[^s2][^s3] A rival account, Ericsson and Kintsch's long-term working memory, was criticised for predicting too high a recall of random positions.[^s3]

## Example and practical lessons

The key position (after 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.O-O d6 6.Nc3 O-O) shows a common Italian Game structure with both sides castled. To a strong player the castled kings, the c4 and c5 bishops and the d3/d6 pawn chains are a handful of familiar units rather than 32 separate pieces, which is what the theory predicts: experts handle groups of features as single units.[^s4]

For club players the practical message is modest but useful. Because chunks are location-specific and grow from exposure to real games, studying many typical positions from your own openings builds the patterns that make positions easier to read, while random drills do little.[^s2][^s3] Templates take a long time to form, so pattern knowledge accumulates slowly rather than from a few sessions.[^s2]

## Connections

Chunking theory is a part of the broader study of chess expertise and the cognitive psychology of chess. It was developed by Herbert Simon and William Chase, building on Adriaan de Groot's recall experiments.[^s4] It leads to template theory, its main revision, and contrasts with game-tree search, since de Groot's players searched little and relied on recognition.[^s2][^s4] It relates to deliberate practice, visualisation and the Einstellung effect as other topics in chess training and cognition; the term "chunk" itself now spans many fields beyond chess.[^s5]

## Sources

[^s1]: Lane, P. C. R. & Gobet, F. (2011), "Perception in chess and beyond", *New Ideas in Psychology* 29. https://uhra.herts.ac.uk/id/eprint/235/1/904357.pdf (accessed 2026-11-08)
[^s2]: Gobet, F. & Simon, H. A. (1996), "Recall of random and distorted chess positions", *Memory & Cognition* 24(4). https://link.springer.com/content/pdf/10.3758%2FBF03200937.pdf (accessed 2026-11-08)
[^s3]: Gobet, F. & Simon, H. A., "Five seconds or sixty? Presentation time in expert memory", *Cognitive Science*. https://core.ac.uk/download/333524.pdf (accessed 2026-11-08)
[^s4]: Gobet, F. (2003), "Implicit learning of expert chess knowledge", *AISB Quarterly* 114. https://core.ac.uk/download/334663.pdf (accessed 2026-11-08)
[^s5]: Gobet, F., Lloyd-Kelly, M. & Lane, P. C. R. (2016), "What's in a name? The multiple meanings of 'chunk' and 'chunking'", *Frontiers in Psychology* 7:102. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.00102/pdf (accessed 2026-11-08)
