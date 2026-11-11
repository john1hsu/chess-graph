---
id: kt:template-theory
type: CognitiveConcept
title: Template theory
aliases: [Chess template theory, Gobet and Simon template theory, Templates in chess memory, Chess templates]
domain: training-and-improvement
summary: >-
  Fernand Gobet and Herbert Simon's 1996 revision of chunking theory, which holds that strong players
  store frequently met positions as long-term-memory templates: a fixed core of about a dozen pieces
  plus slots for variable details, plans and moves that can be filled within a fraction of a second.
fen: "6k1/5pb1/2pp2p1/2n5/2P1P3/2N1BP2/6PP/6K1 w - - 0 1"
status: current
volatile: false
verified: 2026-11-11
broader: [kt:chess-expertise, kt:cognitive-psychology-of-chess]
related: [kt:chunking-theory, kt:adriaan-de-groot, kt:einstellung-effect, kt:opening-repertoire]
relations:
  - {predicate: developedBy, object: kt:fernand-gobet}
  - {predicate: developedBy, object: kt:herbert-simon}
  - {predicate: influencedBy, object: kt:chunking-theory}
  - {predicate: contrastsWith, object: kt:long-term-working-memory}
  - {predicate: dependsOn, object: kt:chrest}
sources:
  - id: s1
    title: "Templates in chess memory: A mechanism for recalling several boards (Cognitive Psychology 31(1), 1-40)"
    publisher: Fernand Gobet and Herbert A. Simon, Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/1339/1/Multiple_boards.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "Five seconds or sixty? Presentation time in expert memory (Cognitive Science 24)"
    publisher: Fernand Gobet and Herbert A. Simon, via CORE
    url: https://core.ac.uk/download/333524.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "Expert memory: A comparison of four theories (Cognition 66, 115-152)"
    publisher: Fernand Gobet, Brunel University Research Archive
    url: https://bura.brunel.ac.uk/bitstream/2438/815/1/FullText.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "Recall of random and distorted chess positions: Implications for the theory of expertise (Memory & Cognition 24, 493-503)"
    publisher: Fernand Gobet and Herbert A. Simon, via CORE
    url: https://core.ac.uk/download/333533.pdf
    type: peer-reviewed
    accessed: 2026-11-11
created: 2026-11-11
---

# Template theory

Template theory is the main successor to Chase and Simon's chunking theory of chess skill. Fernand Gobet and Herbert Simon set it out in 1996 after experiments showed that strong players remember far more than a short-term memory of about seven chunks should allow.[^s1] The theory keeps chunks as the basic perceptual units, but adds larger long-term-memory structures, templates, that can absorb new information about a position almost instantly.[^s1][^s4] Gobet later described it as an elaboration of chunking theory rather than a replacement.[^s3]

## What a template is

A template is a chunk that has grown slots. Its core fixes the locations of roughly a dozen pieces and so defines a whole class of positions, typically familiar opening or middlegame set-ups; around that core sit slots for variable information such as further piece locations, the opening the position probably came from, and typical plans and moves.[^s1] Some slots carry default values, and templates can point to related templates.[^s1] Ordinary chunks in Chase and Simon's data seldom held more than four or five pieces, whereas templates hold about a dozen.[^s2]

Recognition works bottom-up: the player first spots a few chunks, these evoke a template, and the template's defaults are corrected and its slots filled.[^s4] In the computational version built into the CHREST model, creating a new chunk costs about 8 seconds, but filling an existing slot costs only about 250 milliseconds, which is why a master can encode a known type of position so quickly.[^s2] The price is that templates are slow to build: Gobet and Simon guessed that learning one takes on the order of hours, and expected masters to own several thousand of them, experts only for positions common in their own games, and Class A players few.[^s4] They are learned implicitly, from the games players play and study.[^s1]

## The evidence

The theory was tested with a multiple-board task. Players from Class A to grandmaster saw up to five positions for five seconds each; recall fell as boards were added, yet masters still replaced up to about 60 pieces, more than the original chunking account allows.[^s1] Longer pauses between boards improved recall, and one International Master, Gobet himself, trained over about 150 sessions until he could reconstruct up to nine boards at 60 percent accuracy or better, placing more than 160 pieces correctly in some sessions.[^s1] Since short-term memory need only hold a pointer to each board's template, the theory predicts a ceiling of roughly seven boards.[^s1]

Presentation-time studies gave a second test. With game positions, masters shown a board for one second did about as well as experts given ten seconds, and they approached their ceiling within about three seconds.[^s2] A CHREST simulation with 300,000 chunks but no slots reached 64.5 percent recall at ten seconds, against about 84 percent with templates enabled, close to the human masters' scores.[^s2] The theory also explains why interference tasks barely disturb masters and why their small advantage on random positions grows with longer viewing.[^s2][^s3]

## Rival accounts

Gobet's 1998 comparison set templates against chunking theory and against Ericsson and Kintsch's long-term working memory, which proposes a generic retrieval structure, such as a mental map of the 64 squares, available for any position.[^s3] He judged the square-based version of that rival hard to square with recall of random and modified positions, and argued that templates fit better because they are specific to classes of positions and encode only partially.[^s3]

## Example and practical lessons

The key position contains only the core of the example template printed by Gobet and Simon, with kings added: White pawns c4, e4, f3, g2, h2, bishop e3 and knight c3 against Black pawns c6, d6, f7, g6, knight c5 and bishop g7.[^s2] The paper's slots for this core include the white king on g1 and a black knight on d7; a player who owns the template sees such details as fillers of a familiar frame, not as new information.[^s2]

For training, the theory supports learning typical structures through many real games from the openings you play: templates come from repeated exposure to similar positions and carry plans and candidate moves with them.[^s1][^s4] Because they take hours to form, a few sessions will not install them; the knowledge builds slowly.[^s4]

## Connections

Template theory is part of the study of chess expertise and the cognitive psychology of chess. It was developed by Fernand Gobet and Herbert Simon and influenced by chunking theory, which it extends.[^s1][^s3] It depends on the CHREST model for its simulations and contrasts with Ericsson and Kintsch's long-term working memory.[^s2][^s3] It relates to Adriaan de Groot's recall experiments, which started this line of research, to the Einstellung effect, where familiar patterns can mislead, and to opening-repertoire study as the practical source of templates.[^s1]

## Sources

[^s1]: Gobet, F. & Simon, H. A. (1996), "Templates in chess memory: A mechanism for recalling several boards", *Cognitive Psychology* 31(1). https://bura.brunel.ac.uk/bitstream/2438/1339/1/Multiple_boards.pdf (accessed 2026-11-11)
[^s2]: Gobet, F. & Simon, H. A. (2000), "Five seconds or sixty? Presentation time in expert memory", *Cognitive Science* 24. https://core.ac.uk/download/333524.pdf (accessed 2026-11-11)
[^s3]: Gobet, F. (1998), "Expert memory: A comparison of four theories", *Cognition* 66. https://bura.brunel.ac.uk/bitstream/2438/815/1/FullText.pdf (accessed 2026-11-11)
[^s4]: Gobet, F. & Simon, H. A. (1996), "Recall of random and distorted chess positions: Implications for the theory of expertise", *Memory & Cognition* 24. https://core.ac.uk/download/333533.pdf (accessed 2026-11-11)
