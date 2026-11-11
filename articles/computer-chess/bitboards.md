---
id: kt:bitboards
type: Algorithm
title: Bitboards
aliases: [Bitboard, Bitmaps (computer chess), Bit boards, Rotated bitboards, Magic bitboards]
domain: computer-chess
summary: >-
  A board representation used by chess engines in which a set of squares is stored as one
  64-bit integer, one bit per square, so that questions about many squares at once (occupancy,
  attacks, pawn pushes) are answered with a few bitwise machine instructions.
fen: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
status: current
volatile: false
verified: 2026-11-11
broader: [kt:computer-chess, kt:board-representation]
related: [kt:move-generation, kt:game-tree-search, kt:evaluation-function, kt:stockfish, kt:robert-hyatt]
relations:
  - {predicate: developedBy, object: kt:kaissa}
  - {predicate: alternativeTo, object: kt:mailbox-board-representation}
sources:
  - id: s1
    title: "Avoiding Rotated Bitboards with Direct Lookup"
    publisher: Sam Tannous, arXiv:0704.3773
    url: https://arxiv.org/html/0704.3773
    type: academic
    accessed: 2026-11-11
  - id: s2
    title: "Rotated Bitboards in FUSc# and Reinforcement Learning in Computer Chess and Beyond (2025)"
    publisher: Johannes Buchner, arXiv:2503.10822
    url: https://arxiv.org/pdf/2503.10822v1
    type: academic
    accessed: 2026-11-11
  - id: s3
    title: "ICGA Journal 22(4), 1999, pp. 213-222: article on rotated bitmaps (DOI 10.3233/ICG-1999-22403)"
    publisher: Robert M. Hyatt, IOS Press
    url: https://content.iospress.com/articles/icga-journal/icg22403
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "General Setwise Operations"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/General_Setwise_Operations
    type: community
    accessed: 2026-11-11
  - id: s5
    title: "Pradu Kannan"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/Pradu_Kannan
    type: community
    accessed: 2026-11-11
created: 2026-11-11
---

# Bitboards

A bitboard is a 64-bit unsigned integer in which each bit stands for one square of the chessboard; a set bit means that some property holds on that square, for example "occupied by a white piece".[^s2] An engine describes a whole position with a handful of these words, typically one per piece type, one per colour and some derived sets such as all occupied squares.[^s2] Because a 64-bit processor applies AND, OR and NOT to all 64 bits in a single instruction, an engine can ask a question about every square of the board at once instead of looping over them.[^s2]

## Origins

The idea predates chess programs: Tannous traces bitboards to Arthur Samuel's checkers work of 1959, and credits the Soviet program KAISSA with bringing them to chess in the late 1960s.[^s1] Slate and Atkin's CHESS 4.5 in the 1970s and Hyatt's Cray Blitz were later bitboard programs, and Hyatt carried the approach into the open-source engine Crafty.[^s1][^s2] In his 1999 ICGA Journal paper Hyatt explains that, after a 1994 computer event, he began a successor to Cray Blitz partly to test whether the CHESS 4.x bitmap approach was practical on modern hardware.[^s3]

## How it works

Most engines number the squares a1 = 0 up to h8 = 63, so moving one rank north is a shift of 8 bits and one file east a shift of 1.[^s4] Board questions then become set operations: the union (OR) of white and black pieces gives all occupied squares, its complement (NOT) gives the empty squares, and an intersection (AND) of a piece's attack set with the enemy pieces gives its captures.[^s4] In the starting position above, all eight white pawns sit on the second rank, so their bitboard is simply bits 8 to 15, and a single instruction can ask whether any of them is attacked.[^s4]

Pawn moves are generated for the whole set at once: shifting the white-pawn bitboard north by 8 and ANDing with the empty squares yields every single push in one step.[^s4] Shifts by 1, 7 or 9 squares cross files and would wrap a pawn from the a-file to the h-file, so they are masked with constants that exclude the edge file.[^s4] To iterate over a set, an engine isolates the least significant set bit with `x & -x`, converts it to a square index (a bitscan), and clears it with `x & (x - 1)`.[^s4] The same set operations serve the [evaluation function](kt:evaluation-function), for instance to find which pieces are attacked or which squares are empty.[^s4]

## Sliding pieces: rotated and magic bitboards

Knights, kings and pawns have fixed attack patterns that can be precomputed per square, but rooks, bishops and queens are blocked by whatever stands in their way, and that is the hard part.[^s1] Rank attacks are easy because the eight bits of a rank are contiguous; files and diagonals are not.[^s2] Hyatt's answer, which he found necessary to make bitmaps perform well, was *rotated bitmaps*: extra occupancy boards rotated by 90 degrees and along both diagonals, so that a file or diagonal also becomes a run of adjacent bits that can index a lookup table.[^s3][^s2] These rotated boards must be updated incrementally on every make and unmake of a move.[^s1][^s2]

The later *magic* approach removes that bookkeeping: the relevant occupancy bits for a square are multiplied by a per-square "magic" constant and shifted, producing an index into a table of precomputed attacks.[^s1] Lasse Hansen proposed the idea on a forum in 2006, and Pradyumna Kannan made it practical in memory, publishing "Magic Move-Bitboard Generation in Computer Chess" in 2007.[^s5] Tannous proposed yet another alternative, direct lookup, to avoid the shifting and masking that rotated boards need.[^s1]

## Pitfalls

Bitboard code is compact but unforgiving. A classic bug is forgetting the edge-file masks on sideways or diagonal shifts, so that pieces "wrap" from one side of the board to the other.[^s4] With rotated bitboards, every extra board must be updated on each make and unmake of a move, and any slip leaves the engine generating moves from a position that does not exist.[^s2] The speed argument also rests on the hardware: the gain comes from 64-bit processors handling all 64 bits in one operation.[^s2]

## Connections

Bitboards are a [board representation](kt:board-representation) inside the broader field of [computer chess](kt:computer-chess), one in which the engine reasons about whole sets of squares at once rather than visiting squares one at a time.[^s2][^s4] They matter because fast [move generation](kt:move-generation) and cheap attack tests make each node of the [game-tree search](kt:game-tree-search) faster.[^s2] The technique entered chess through [KAISSA](kt:kaissa), and was carried forward by [Robert Hyatt](kt:robert-hyatt) in Cray Blitz and Crafty and by the Karlsruhe engine DarkThought.[^s1][^s2][^s3] Links to [Stockfish](kt:stockfish) and to the array-based mailbox layout are left as frontier nodes for those articles to substantiate.

## Sources

[^s1]: Sam Tannous, "Avoiding Rotated Bitboards with Direct Lookup", arXiv:0704.3773. https://arxiv.org/html/0704.3773 (accessed 2026-11-11)
[^s2]: Johannes Buchner, "Rotated Bitboards in FUSc# and Reinforcement Learning in Computer Chess and Beyond", arXiv:2503.10822 (2025). https://arxiv.org/pdf/2503.10822v1 (accessed 2026-11-11)
[^s3]: Robert M. Hyatt, article on rotated bitmaps, ICGA Journal 22(4), 1999, pp. 213-222. https://content.iospress.com/articles/icga-journal/icg22403 (accessed 2026-11-11)
[^s4]: Chess Programming Wiki, "General Setwise Operations". https://www.chessprogramming.org/General_Setwise_Operations (accessed 2026-11-11)
[^s5]: Chess Programming Wiki, "Pradu Kannan". https://www.chessprogramming.org/Pradu_Kannan (accessed 2026-11-11)
