---
id: kt:zobrist-hashing
type: Algorithm
title: Zobrist hashing
aliases: [Zobrist keys, Zobrist key, Zobrist hash, Zobrist signature]
domain: computer-chess
summary: >-
  A method, published by Albert Zobrist in 1970, of turning a board position into a single
  large number by combining (with exclusive-or) pre-generated random numbers for each piece on
  each square and for side to move, castling and en passant rights, so that the key can be
  updated cheaply move by move.
fen: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 4 3"
status: current
volatile: false
verified: 2026-11-17
broader: [kt:computer-chess]
related: [kt:transposition-table, kt:threefold-repetition, kt:bitboards, kt:stockfish, kt:opening-book]
relations:
  - {predicate: enables, object: kt:transposition-table}
  - {predicate: developedBy, object: kt:albert-zobrist}
  - {predicate: namedAfter, object: kt:albert-zobrist}
sources:
  - id: s1
    title: "A New Hashing Method With Application for Game Playing (Technical Report TR88, 1970)"
    publisher: Albert L. Zobrist, University of Wisconsin–Madison (MINDS@UW repository)
    url: https://minds.wisc.edu/items/992e8337-5597-4a51-89d3-3fbe3559201a/full
    type: academic
    accessed: 2026-11-17
  - id: s2
    title: "A New Hashing Method with Application for Game Playing (reprint)"
    publisher: ICGA Journal, vol. 13, no. 2 (1990), pp. 69–73, IOS Press
    url: https://content.iospress.com/articles/icga-journal/icg13-2-03
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "Lecture 7: Hashing, GHI, Expecti-minimax (AI for Traditional Games)"
    publisher: Nathan Sturtevant, University of Denver
    url: https://www.cs.du.edu/~sturtevant/w13-games/Lecture7.pdf
    type: academic
    accessed: 2026-11-17
  - id: s4
    title: "Stockfish 14 source code, src/position.cpp (sf_14 release, DragonFly BSD ports copy)"
    publisher: The Stockfish developers
    url: https://grok.dragonflybsd.org/raw/dports/games/stockfish/Stockfish-sf_14/src/position.cpp
    type: primary-record
    accessed: 2026-11-17
  - id: s5
    title: "Guide: Zobrist keys"
    publisher: Jonatan Pettersson, Mediocre Chess
    url: https://mediocrechess.sourceforge.net/guides/zobristkeys.html
    type: community
    accessed: 2026-11-17
  - id: s6
    title: "Chess::Opening::Book::Polyglot::Random64"
    publisher: Guido Flohr, MetaCPAN
    url: https://metacpan.org/pod/Chess::Opening::Book::Polyglot::Random64
    type: community
    accessed: 2026-11-17
created: 2026-11-17
---

# Zobrist hashing

**Zobrist hashing** is the standard way a chess program gives every position a compact numeric fingerprint. Albert Zobrist described it in an April 1970 technical report at the University of Wisconsin, presenting a general hash-coding method for board-game programs such as checkers, chess and Go, together with an auxiliary scheme for detecting retrieval errors.[^s1] The report was reprinted in the ICGA Journal in 1990, a sign of how central the idea had become to game programming.[^s2]

## How a key is built

Before play begins the program generates a table of random numbers, usually 64 bits wide: one for every combination of piece (type and colour) and square, plus extra numbers for the parts of the position that are not visible on the board.[^s3] The key of a position is the exclusive-or (XOR) of the numbers for everything present in it.[^s3] In Stockfish the tables are a piece-square array, one value per en passant file, one per combination of castling rights, and a single "side" value that is mixed in only when Black is to move.[^s4] Pettersson's tutorial engine follows the same pattern, adding the side value only for Black so that otherwise identical positions with different players to move get different keys.[^s5]

The numbers need not be truly random, only fixed and well spread. Stockfish fills its tables from a pseudo-random generator with a hard-coded seed, so the keys are identical every time the engine starts.[^s4]

## Why XOR: incremental updates

The point of the method is speed. XOR is its own inverse, so applying the same number twice cancels it; a move can therefore be reflected in the key by XOR-ing out the numbers that no longer apply and XOR-ing in the new ones, and unmaking the move restores the old key exactly.[^s3] Sturtevant's lecture stresses that the hash is updated inside the make and unmake routines rather than recomputed from the whole board.[^s3] Stockfish computes the key from scratch only when a position is set up and afterwards updates it incrementally: a normal move flips the side value, removes the moving piece from its origin square, adds it on the destination, and removes any captured piece, with en passant and castling values swapped as those rights change.[^s4] A promotion replaces the pawn's number with that of the new piece, and a "null move" used in search changes only the side and en passant values.[^s4]

## Collisions

A 64-bit key cannot distinguish every possible position, so two positions can share a key. Zobrist already treated such retrieval errors as something to detect, with an error rate controlled by how much table space is devoted to checking.[^s1] Sturtevant gives the usual birthday-style estimate: collisions become likely once the number of stored items approaches the square root of the key space, which makes 32-bit keys too small for serious work while 64-bit keys are generally adequate.[^s3] Stockfish in debug mode recomputes the key from the board to catch errors in the incremental updates.[^s4]

## Example

The FEN above is the starting position reached after 1.Nf3 Nf6 2.Ng1 Ng8. The pieces, side to move and castling rights are as at the start, so the Zobrist key is identical to the initial one, even though the half-move clock now reads 4. Move counters are normally left out of the key, which is exactly why it can recognise a repeated position.[^s3][^s5] Likewise 1.e4 e5 2.Nf3 Nc6 and 1.Nf3 Nc6 2.e4 e5 reach the same position with the same key.[^s3]

## Uses and pitfalls

The main consumer of Zobrist keys is the **transposition table**, which uses the key both to pick a slot and to confirm that the stored entry belongs to the current position. Keys are also the cheap way to detect **repetitions**: Pettersson found that comparing FEN strings had cost his engine about 35% of its processor time in repetition checks, whereas keys are small to store and fast to compare.[^s5] Stockfish additionally builds "cuckoo" tables over its keys to spot upcoming repetitions.[^s4]

Common bugs include forgetting to update the key when castling rights are lost or an en passant square appears or disappears, leaving out the side-to-move value, and including move counters, which defeats repetition detection.[^s5][^s4]

## Connections

Zobrist hashing **enables** the transposition table and is a prerequisite for most practical repetition detection, tying it to the **threefold repetition** rule. It is named after and was **developed by** Albert Zobrist.[^s1] It pairs naturally with **bitboards**, since both represent pieces by square-indexed data, and it is part of every modern engine such as **Stockfish**.[^s4] Opening-book formats such as Polyglot also index positions by Zobrist keys, linking it to the **opening book**.[^s6]

## Sources
[^s1]: Albert L. Zobrist, "A New Hashing Method With Application for Game Playing", Technical Report TR88, University of Wisconsin–Madison, 1970. https://minds.wisc.edu/items/992e8337-5597-4a51-89d3-3fbe3559201a/full (accessed 2026-11-17)
[^s2]: Albert L. Zobrist, "A New Hashing Method with Application for Game Playing", ICGA Journal 13(2), 1990, pp. 69–73. https://content.iospress.com/articles/icga-journal/icg13-2-03 (accessed 2026-11-17)
[^s3]: Nathan Sturtevant, "Lecture 7: Hashing, GHI, Expecti-minimax", AI for Traditional Games, University of Denver. https://www.cs.du.edu/~sturtevant/w13-games/Lecture7.pdf (accessed 2026-11-17)
[^s4]: The Stockfish developers, Stockfish 14 source, src/position.cpp. https://grok.dragonflybsd.org/raw/dports/games/stockfish/Stockfish-sf_14/src/position.cpp (accessed 2026-11-17)
[^s5]: Jonatan Pettersson, "Guide: Zobrist keys", Mediocre Chess. https://mediocrechess.sourceforge.net/guides/zobristkeys.html (accessed 2026-11-17)
[^s6]: Guido Flohr, "Chess::Opening::Book::Polyglot::Random64", MetaCPAN. https://metacpan.org/pod/Chess::Opening::Book::Polyglot::Random64 (accessed 2026-11-17)
