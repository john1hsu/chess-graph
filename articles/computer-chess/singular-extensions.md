---
id: kt:singular-extensions
type: Algorithm
title: Singular extensions
aliases: [Singular extension, SE, Singular extension search]
domain: computer-chess
summary: >-
  A search-extension heuristic, introduced by Anantharaman, Campbell and Hsu for the Carnegie Mellon
  machines ChipTest and Deep Thought, that searches a move one ply deeper when it is clearly better
  than every alternative, so that forced lines are followed further than a uniform-depth search would.
fen: "rnbqkbnr/ppppp1pp/8/5p1Q/4P3/8/PPPP1PPP/RNB1KBNR b KQkq - 1 2"
status: current
volatile: false
verified: 2026-11-18
broader: [kt:game-tree-search]
related: [kt:horizon-effect, kt:quiescence-search, kt:principal-variation-search, kt:transposition-table, kt:deep-blue, kt:stockfish]
relations:
  - {predicate: counters, object: kt:horizon-effect}
  - {predicate: developedBy, object: kt:feng-hsiung-hsu}
  - {predicate: contrastsWith, object: kt:multi-cut-pruning}
  - {predicate: dependsOn, object: kt:alpha-beta-pruning}
sources:
  - id: s1
    title: "Deep Blue (Artificial Intelligence 134, 2002; authors' version dated 1 August 2001)"
    publisher: Murray Campbell, A. Joseph Hoane Jr. and Feng-hsiung Hsu, copy hosted by Northern Arizona University
    url: https://www.cefns.nau.edu/~edo/Classes/CS470-570_WWW/Readings/Campbell2002.pdf
    type: academic
    accessed: 2026-11-18
  - id: s2
    title: "Variable Depth Search (book chapter)"
    publisher: T. A. Marsland and Y. Björnsson, University of Alberta
    url: https://webdocs.cs.ualberta.ca/~tony/RecentPapers/01-Marsland-8b.pdf
    type: academic
    accessed: 2026-11-18
  - id: s3
    title: "Computer Chess and Search (Encyclopedia of Artificial Intelligence, 2nd ed., report version 1991)"
    publisher: T. A. Marsland, University of Alberta
    url: https://webdocs.cs.ualberta.ca/~tony/RecentPapers/encyc.mac-1991.pdf
    type: academic
    accessed: 2026-11-18
  - id: s4
    title: "Singular Extensions"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org:443/Singular_Extensions
    type: community
    accessed: 2026-11-18
created: 2026-11-18
---

# Singular extensions

Singular extensions are a way of making an otherwise uniform alpha-beta search selective. The idea is that when one move at a node is a lot better than all of its alternatives, the line is effectively forced, and the program should look at it more deeply than the nominal search depth.[^s4] Marsland and Björnsson describe the basic version as searching such a move one ply deeper in order to reduce the risk of a horizon effect.[^s2] Because the program cannot know in advance that a move is singular, it has to spend extra search effort testing for it.[^s4]

## Origin

The technique was introduced by Thomas Anantharaman, Murray Campbell and Feng-hsiung Hsu in "Singular extensions: Adding selectivity to brute-force searching", first published in the ICCA Journal 11(4) in 1988 and reprinted in *Artificial Intelligence* 43(1) in 1990.[^s1][^s3] According to the Chess Programming Wiki, Hsu traced the idea to a 1986 ACM game in which two programs played out a forced sequence that neither had seen in advance, prompting the remark that selective extensions rather than selective pruning were the way forward.[^s4] It was implemented in the Carnegie Mellon machines ChipTest and Deep Thought, where the authors reported encouraging tactical results.[^s4] Marsland's 1991 survey called singular extensions a first step toward a more sophisticated way of deciding which lines to extend, and described the method as being used to steer the search down appropriately forcing lines.[^s3]

## How it works

The test compares the candidate best move with its siblings. In the principal-variation version, the other moves are searched with zero-width windows lowered by a fixed margin; if none of them comes within that margin of the candidate's value, the candidate is declared singular and searched again with an extra ply.[^s2] Marsland and Björnsson apply this at PV nodes but not at the root, which they found awkward to implement.[^s2] In the fail-high version, used inside a zero-window search, a move that produces a cut-off is checked by searching the remaining moves at reduced depth; if none of them also cuts off with a margin, the move is singular and is searched a ply deeper.[^s2] The Chess Programming Wiki summarises the common modern form the same way: a reduced-depth null-window search with a lowered bound, and an extension if every alternative fails low.[^s4]

## In Deep Blue

Deep Blue generalised the idea. Its designers explain that a move significantly better than its alternatives is singular, but that the same reasoning extends to "binary" and "trinary" cases in which two or three moves are good, with less extension credit the more reasonable alternatives there are.[^s1] An **absolute singular** move, the only legal move in a position and usually a check evasion, could receive a large credit, possibly a full two-ply extension, at little risk.[^s1] These credits fed a "dual credit" scheme with fractional, delayed extensions tracked separately for each side, which formed the basis of Deep Blue's software search.[^s1] The chess chip also supported singular extensions, though the singular, binary and trinary tests were enabled only at the root of the hardware search, because without a transposition table a general implementation could produce non-terminating searches.[^s1]

## Example

In the position given, after 1.e4 f5 2.Qh5+, Black's only legal move is 2...g6, since f7 is covered by the queen. This is the absolute singular case Deep Blue's designers describe: with a single reply there is nothing to compare, so extending the line costs almost nothing and keeps the forced check from eating into the search depth.[^s1] In ordinary positions the singularity has to be established by the margin searches described above.[^s2]

## Costs and evidence

The verification searches are not free. Marsland and Björnsson note that the case for singular extensions is strong, especially in games against humans, but that there was little evidence of their value in computer-versus-computer play.[^s2] In their small feasibility study, a version of their program with singular extensions scored 52% against the unmodified program at 10 seconds a move but only about 42% and 38% at 30 and 100 seconds; given 10% more time, it again scored about 52%.[^s2] They called for larger experiments.[^s2] The Chess Programming Wiki records that Stockfish 1.6 (2009) adopted a relaxed form restricted to moves stored in the transposition table, a variant credited with a significant gain in strength, though the wiki gives no measured figure.[^s4]

## Connections

Singular extensions belong to **game-tree search** and work inside **alpha-beta pruning** and **principal variation search**, whose zero-window searches they reuse.[^s2] They are one of the tools against the **horizon effect**, alongside **quiescence search**.[^s2][^s3] Marsland and Björnsson describe **multi-cut pruning** as their complement: it prunes when several moves look viable at an expected cut node, while singular extensions extend when only one does.[^s2] Implementations based on the **transposition table** include Stockfish's, and the method was developed by **Feng-hsiung Hsu** and colleagues for the machines that led to **Deep Blue**.[^s1][^s4]

## Sources
[^s1]: M. Campbell, A. J. Hoane Jr. and F.-h. Hsu, "Deep Blue", *Artificial Intelligence* 134 (2002); authors' version dated 1 August 2001, hosted by Northern Arizona University. https://www.cefns.nau.edu/~edo/Classes/CS470-570_WWW/Readings/Campbell2002.pdf (accessed 2026-11-18)
[^s2]: T. A. Marsland and Y. Björnsson, "Variable Depth Search", book chapter, University of Alberta. https://webdocs.cs.ualberta.ca/~tony/RecentPapers/01-Marsland-8b.pdf (accessed 2026-11-18)
[^s3]: T. A. Marsland, "Computer Chess and Search", *Encyclopedia of Artificial Intelligence*, 2nd ed. (report version, University of Alberta, 1991). https://webdocs.cs.ualberta.ca/~tony/RecentPapers/encyc.mac-1991.pdf (accessed 2026-11-18)
[^s4]: Chess Programming Wiki, "Singular Extensions". https://www.chessprogramming.org:443/Singular_Extensions (accessed 2026-11-18)
