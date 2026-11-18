---
id: kt:steven-j-edwards
type: Person
title: Steven J. Edwards
aliases: [Steven Edwards, Steven James Edwards, S. J. Edwards]
domain: rules-and-notation
summary: >-
  Computer scientist and chess programmer who coordinated the 1994 Portable Game Notation
  standard, extended Forsyth notation into FEN, co-developed Extended Position Description with
  John Stanback, and built the Edwards endgame tablebases for his research program Spector.
fen: "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
status: historical
volatile: false
verified: 2026-11-18
broader: [kt:computer-chess]
related: [kt:portable-game-notation, kt:forsyth-edwards-notation, kt:extended-position-description, kt:endgame-tablebases, kt:bratko-kopec-test]
relations:
  - {predicate: influencedBy, object: kt:david-forsyth}
  - {predicate: contrastsWith, object: kt:nalimov-tablebases}
sources:
  - id: s1
    title: "Standard: Portable Game Notation Specification and Implementation Guide (revised 1994-03-12)"
    publisher: Steven J. Edwards (coordinator), rec.games.chess; copy in the GNU Emacs ELPA repository
    url: https://code.delx.au/gnu-emacs-elpa/blob/65de55274ce8d49fa67bb555050e2481ebcad2c5:/PGN.txt
    type: primary-record
    accessed: 2026-11-18
  - id: s2
    title: "EPD_Spec: Extended Position Description Specification"
    publisher: Steven J. Edwards (technical contact); copy in the GNU Emacs ELPA repository
    url: https://code.delx.au/gnu-emacs-elpa/blob/65de55274ce8d49fa67bb555050e2481ebcad2c5:/EPD.txt
    type: primary-record
    accessed: 2026-11-18
  - id: s3
    title: "Endgame tablebases: A short history"
    publisher: Albert Silver, ChessBase News (16 March 2018)
    url: https://en.chessbase.com/newsroom/post/endgame-tablebases-a-short-history
    type: publication
    accessed: 2026-11-18
  - id: s4
    title: "Edwards' Tablebases"
    publisher: Chess Programming Wiki
    url: https://chessprogramming.org/Edwards%27_Tablebases
    type: community
    accessed: 2026-11-18
created: 2026-11-18
---

# Steven J. Edwards

Steven J. Edwards is a computer scientist and chess programmer whose name is attached to three of the plain-text formats that chess software still uses to exchange data: Portable Game Notation (PGN), Forsyth–Edwards Notation (FEN) and Extended Position Description (EPD).[^s1][^s3] He also built one of the first widely used sets of endgame tablebases in the early 1990s.[^s3][^s4] For a club player his work is mostly invisible but constant: every downloaded game file and every "copy position" button in an analysis board relies on conventions he helped write down.

## Portable Game Notation

The PGN standard, revised on 12 March 1994, names its authors as interested readers of the rec.games.chess newsgroup and lists Edwards as coordinator.[^s1] Its stated aim was to make it easy to share public-domain game data among players, and it set out the tag-pair header, the Seven Tag Roster, Standard Algebraic Notation movetext and the import/export rules that let programs agree on one text form.[^s1] The same document describes his "SAN Kit", a free ANSI C chess programming toolkit by Edwards that implemented PGN import and export and FEN input and output.[^s1]

## Forsyth–Edwards Notation and EPD

FEN takes its first name from David Forsyth, a nineteenth-century Scottish newspaper journalist whose method of recording positions it adapts; the PGN standard says the system was slightly extended by Edwards for use with chess software and first implemented in the SAN Kit.[^s1] The extension adds fields after the board diagram for side to move, castling rights, en passant target, halfmove clock and fullmove number. The standard's own example after 1.e4 is the position in this article's `fen` field, where `b` gives Black the move and `e3` marks the square a pawn could capture onto en passant.[^s1]

EPD, created in 1993, was developed by John Stanback and Edwards; Stanback's commercial program Zarkov implemented it first and Edwards' research program Spector second.[^s2] It keeps FEN's first four fields but drops the two move counters, and adds semicolon-terminated "operations" such as `bm` (best move), `am` (move to avoid), `ce` (centipawn evaluation) and `id` (a position label, for example `BK.15` for a Bratko–Kopec test position).[^s2] That design made EPD the usual container for engine test suites and their results.[^s2]

## Endgame tablebases

Edwards built three-, four- and some five-piece tablebases for Spector, finishing in 1994 and then releasing the data, documentation and an ANSI C test program on the internet.[^s3][^s4] They stored a distance-to-mate value for every position with either side to move, one byte per position, counted in full moves; each file covered one material balance and one side to move.[^s4] ChessBase's history says his design addressed the problems Ken Thompson's earlier databases posed for use inside a program's search, and that the Edwards files were popular with programs such as Crafty, Gromit and MChess Pro until compressed Nalimov tablebases arrived in 1998.[^s3] He also published analyses of the KBNKN and KBBKN endings in the ICCA Journal in 1995 and 1996.[^s4]

## Connections

Edwards is the person behind the **developed by** edges of **Portable Game Notation**, **Forsyth–Edwards Notation** and **Extended Position Description**, and sits under **computer chess** as a broader field.[^s1][^s2] FEN was **influenced by** **David Forsyth**'s older notation.[^s1] His tablebases belong to the history of **endgame tablebases**, and they **contrast with** the later **Nalimov tablebases**, which displaced them.[^s3][^s4] EPD's labelled positions tie him to test sets such as the **Bratko–Kopec test**.[^s2]

## Sources

[^s1]: Steven J. Edwards (coordinator), "Standard: Portable Game Notation Specification and Implementation Guide", revised 12 March 1994. https://code.delx.au/gnu-emacs-elpa/blob/65de55274ce8d49fa67bb555050e2481ebcad2c5:/PGN.txt (accessed 2026-11-18)
[^s2]: Steven J. Edwards (technical contact), "EPD_Spec: Extended Position Description Specification". https://code.delx.au/gnu-emacs-elpa/blob/65de55274ce8d49fa67bb555050e2481ebcad2c5:/EPD.txt (accessed 2026-11-18)
[^s3]: Albert Silver, "Endgame tablebases: A short history", ChessBase News, 16 March 2018. https://en.chessbase.com/newsroom/post/endgame-tablebases-a-short-history (accessed 2026-11-18)
[^s4]: Chess Programming Wiki, "Edwards' Tablebases". https://chessprogramming.org/Edwards%27_Tablebases (accessed 2026-11-18)
