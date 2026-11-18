---
id: kt:static-exchange-evaluation
type: Algorithm
title: Static exchange evaluation
aliases: [SEE, Static exchange evaluator, Swap-off value, Swap-off analysis, Exchange evaluator, Swap algorithm]
domain: computer-chess
summary: >-
  A routine in chess engines that estimates, without searching, the material outcome of the
  sequence of captures on a single square, letting the engine sort captures into winning,
  equal and losing ones and prune those that lose material.
fen: "6k1/8/2n5/4p3/8/5N2/8/4R1K1 w - - 0 1"
status: current
volatile: false
verified: 2026-11-18
broader: [kt:computer-chess]
related: [kt:move-ordering, kt:quiescence-search, kt:evaluation-function, kt:material-advantage, kt:pin, kt:sargon]
relations:
  - {predicate: enables, object: kt:move-ordering}
  - {predicate: enables, object: kt:quiescence-search}
  - {predicate: developedBy, object: kt:john-maynard-smith}
  - {predicate: influencedBy, object: kt:alpha-beta-pruning}
sources:
  - id: s1
    title: "Static Exchange Evaluation"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org:443/Static_Exchange_Evaluation
    type: community
    accessed: 2026-11-18
  - id: s2
    title: "An Exchange Evaluator for Computer Chess (BYTE, Vol. 3 No. 11, November 1978)"
    publisher: Dan and Kathe Spracklen, BYTE Magazine, scan at vintageapple.org
    url: https://vintageapple.org/byte/pdf/197811_Byte_Magazine_Vol_03-11_OSCAR_amateur_radio_satellites.pdf
    type: primary-record
    accessed: 2026-11-18
  - id: s3
    title: "Static Exchange Evaluation with αβ-Approach (ICGA Journal 33(1), 2010, pp. 3–17)"
    publisher: Fritz Reul, ICGA Journal, IOS Press
    url: https://content.iospress.com/articles/icga-journal/icg33102
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "Stockfish 14 source code, src/position.cpp (Position::see_ge)"
    publisher: The Stockfish developers (GPL v3), mirrored in DragonFly BSD ports
    url: https://grok.dragonflybsd.org/raw/dports/games/stockfish/Stockfish-sf_14/src/position.cpp
    type: primary-record
    accessed: 2026-11-18
  - id: s5
    title: "New architectures in computer chess (PhD thesis, Tilburg University, 2009), research portal record"
    publisher: Tilburg University
    url: https://research.tilburguniversity.edu/en/publications/new-architectures-in-computer-chess/
    type: academic
    accessed: 2026-11-18
created: 2026-11-18
---

# Static exchange evaluation

Static exchange evaluation (SEE) answers a narrow but constant question inside a chess engine: if pieces keep capturing on one square, who comes out ahead, and by how much? It looks only at the attackers and defenders of that square and estimates the material balance of the exchange; a positive result marks a capture as winning, and some programs return only a flag saying whether the move loses material or not.[^s1] It is "static" because it plays out no real moves in the search tree: it simulates the capture sequence on a single square instead.[^s1][^s3]

## Origins

The idea predates modern engines. Donald Michie coined the term "swap-off value", and the swap-off algorithm is credited to John Maynard Smith's early-1960s one-move "paper machine" SOMA; some early programs relied on such swap-off analysis of capture sequences instead of a quiescence search.[^s1] In November 1978 Dan and Kathe Spracklen described the exchange evaluator of their microcomputer program Sargon in BYTE, saying its accuracy was the biggest single factor in the program's success.[^s2] Fritz Reul later treated SEE at length in his 2009 Tilburg doctoral thesis and in a 2010 ICGA Journal paper on deriving it from the alpha-beta window.[^s5][^s3][^s1]

## How it works

The basic procedure is a swap list. Each side's attackers of the square are collected and ordered from least to most valuable. The capturing side takes first; then the sides alternate, each always recapturing with its cheapest remaining piece, and the running material balance is recorded at every step.[^s1][^s2] Because either side may stop capturing when continuing would cost material, the final value is found by working back through the list, each side choosing the better of stopping or continuing; the wiki's recursive version takes the larger of zero and the captured piece's value minus the opponent's best reply.[^s1] The Spracklens describe the same logic in practical terms: an exchange stops once the next capturer is worth more than what it would win, and the result always lies between zero and the value of the attacked piece.[^s2]

Sliding pieces lined up behind one another matter. Sargon stored an x-ray attacker behind the piece in front of it, so it joined the exchange only after that piece had captured.[^s2] Stockfish's `see_ge` does the same by recomputing attackers after each capture: removing a pawn, bishop or queen can reveal diagonal sliders, and removing a rook or queen can reveal rooks and queens.[^s4] Stockfish also asks a simpler question than "what is the exact value?": it tests whether the exchange reaches a given threshold, using what its comment calls an alpha-beta-like algorithm with a null window, and it stops as soon as the answer is decided.[^s4] Reul's paper likewise shows how the alpha-beta window behind SEE yields pruning conditions that cut the iterative work.[^s3]

## Uses in an engine

SEE's main jobs are ordering and pruning. A threshold splits captures into good ones, searched before quiet moves, and bad ones, searched after them.[^s1] In quiescence search it works with delta pruning to skip captures that lose material, and in the main search SEE-based pruning can discard losing captures and even quiet moves that hang material, usually with a margin that grows with depth.[^s1]

## Limitations

SEE sees only one square. The Spracklens listed what their evaluator missed: discovered attacks, pins, overworked pieces and some transparent attacks.[^s2] Modern implementations patch some of this. Stockfish, for instance, removes pieces pinned to their own king from the attacker list while the pinning piece is still on the board, and lets a king recapture only if no enemy attacker remains.[^s4] Promotions, en passant and castling are not simulated at all in Stockfish 14's version, which simply treats them as an even exchange against the threshold.[^s4] Anything beyond one square's capture sequence, such as a counter-threat elsewhere or a zwischenzug, is left to the real search.[^s1]

## Example

In the diagram position (White: Kg1, Re1, Nf3; Black: Kg8, Nc6, pawn e5) both white pieces attack the pawn and the black knight defends it. Using the conventional pawn 1, knight 3, rook 5 scale, SEE rates Nxe5 as winning a pawn: after Nxe5 Nxe5 Rxe5 White has traded knights and kept the pawn, and if Black declines to recapture White is still a pawn up. Rxe5, by contrast, scores about minus one: Nxe5 Nxe5 gives White knight and pawn (4) for the rook (5). The difference comes only from which piece captures first, which is why engines evaluate a specific capture by forcing its first move before letting the cheapest attackers take over.[^s1][^s4]

## Connections

SEE is a supporting routine for **move ordering**, where it refines simple victim-attacker sorting, and for **quiescence search**, where it keeps the capture search small.[^s1] It is a material-only shortcut, separate from the full **evaluation function**, and its blind spots, such as **pins** and overloaded defenders, are classic tactical motifs.[^s2][^s4] Its history runs from **John Maynard Smith**'s swap-off idea through the Spracklens' **Sargon**, and Reul connects it formally to **alpha-beta pruning**.[^s1][^s2][^s3]

## Sources
[^s1]: Chess Programming Wiki, "Static Exchange Evaluation". https://www.chessprogramming.org:443/Static_Exchange_Evaluation (accessed 2026-11-18)
[^s2]: D. Spracklen and K. Spracklen, "An Exchange Evaluator for Computer Chess", *BYTE* 3(11), November 1978; scan at vintageapple.org. https://vintageapple.org/byte/pdf/197811_Byte_Magazine_Vol_03-11_OSCAR_amateur_radio_satellites.pdf (accessed 2026-11-18)
[^s3]: F. Reul, "Static Exchange Evaluation with αβ-Approach", *ICGA Journal* 33(1), 3–17 (2010), doi:10.3233/ICG-2010-33102. https://content.iospress.com/articles/icga-journal/icg33102 (accessed 2026-11-18)
[^s4]: The Stockfish developers, Stockfish 14 source, `src/position.cpp`, `Position::see_ge` (GPL v3), DragonFly BSD ports mirror. https://grok.dragonflybsd.org/raw/dports/games/stockfish/Stockfish-sf_14/src/position.cpp (accessed 2026-11-18)
[^s5]: F. M. H. Reul, *New Architectures in Computer Chess*, PhD thesis, Tilburg University (2009), TiCC Dissertation Series 6; research portal record. https://research.tilburguniversity.edu/en/publications/new-architectures-in-computer-chess/ (accessed 2026-11-18)
