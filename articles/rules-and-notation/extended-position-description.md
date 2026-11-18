---
id: kt:extended-position-description
type: Notation
title: Extended Position Description
aliases: [EPD, EPD record, EPD notation, Extended Position Description notation]
domain: rules-and-notation
summary: >-
  A one-line ASCII format for a chess position that keeps the first four fields of FEN and adds
  any number of semicolon-terminated "operations" (such as bm for best move or id for a label);
  developed by John Stanback and Steven J. Edwards and defined in the 1994 PGN standard, it is
  the usual format for engine test suites and position data exchanged between programs.
fen: "1k1r4/pp1b1R2/3q2pp/4p3/2B5/4Q3/PPP2B2/2K5 b - - 0 1"
status: current
volatile: false
verified: 2026-11-18
broader: [kt:forsyth-edwards-notation]
related: [kt:portable-game-notation, kt:computer-chess, kt:opening-book, kt:threefold-repetition, kt:fifty-move-rule, kt:bratko-kopec-test]
relations:
  - {predicate: developedBy, object: kt:steven-j-edwards}
  - {predicate: developedBy, object: kt:john-stanback}
  - {predicate: partOf, object: kt:portable-game-notation}
sources:
  - id: s1
    title: "Standard: Portable Game Notation Specification and Implementation Guide (revised 1994-03-12), section 16.2"
    publisher: Steven J. Edwards (coordinator); copy in the GNU Emacs ELPA repository
    url: https://code.delx.au/gnu-emacs-elpa/blob/65de55274ce8d49fa67bb555050e2481ebcad2c5:/PGN.txt
    type: primary-record
    accessed: 2026-11-18
  - id: s2
    title: "python-chess: a chess library for Python (stable documentation)"
    publisher: Niklas Fiekas, python-chess project
    url: https://python-chess.readthedocs.io/en/stable/
    type: official-project
    accessed: 2026-11-18
  - id: s3
    title: "The Bratko-Kopec Test Revisited"
    publisher: T. Anthony Marsland, University of Alberta (revised from a 1989 New Directions in Game-Tree Search workshop paper)
    url: https://webdocs.cs.ualberta.ca/~tony/OldPapers/Workshop-BK-1989.pdf
    type: academic
    accessed: 2026-11-18
  - id: s4
    title: "The Bratko-Kopec Test Recalibrated"
    publisher: Shawn Benn and Danny Kopec, Brooklyn College (CUNY) publications page
    url: https://www.sci.brooklyn.cuny.edu/~kopec/Publications/THE%20BRATKO-KOPEC%20TEST%20RECALIBRATED.htm
    type: academic
    accessed: 2026-11-18
  - id: s5
    title: "epd.c: Extended Position Description routines (Crafty 25.2 source)"
    publisher: Steven J. Edwards (1996), distributed with the Crafty chess engine; DragonFly BSD source browser
    url: https://grok.dragonflybsd.org/xref/dports/games/crafty/crafty-25.2_1/epd.c
    type: official-project
    accessed: 2026-11-18
  - id: s6
    title: "EPD (ChessDB 2.5 help, June 2001)"
    publisher: ChessDB project, SourceForge
    url: https://chessdb.sourceforge.net/tutorial/help/EPD.html
    type: community
    accessed: 2026-11-18
created: 2026-11-18
---

# Extended Position Description

Extended Position Description (EPD) is a plain-text format for recording a single chess position together with structured information about it. Section 16.2 of the 1994 Portable Game Notation standard defines it as a way to describe positions with an extensible set of attribute values, intended for data and command interchange between chess programs and for portable opening-library repositories.[^s1] Where FEN answers "what is on the board?", an EPD line can also say "what is the best move here, what is it called, and how did an engine evaluate it?" That is why a club player usually meets EPD not in game scores but in engine test suites and training position files.

## Origins

The standard credits John Stanback and Steven Edwards with developing EPD, and records that its first implementation was in Stanback's program Zarkov.[^s1] Edwards, who coordinated the PGN standard, also wrote a freely redistributable library of EPD routines; a 1996 revision of that file, covering EPD parsing and encoding, legal move generation and SAN output, still ships with the engine Crafty.[^s5]

## Structure of a record

An EPD record starts with four data fields that are the same as the first four fields of FEN: piece placement, active colour, castling availability and the en passant target square.[^s1] One difference in detail is that EPD writes an en passant square only when a pawn has just made a two-square advance.[^s1] FEN's fifth and sixth fields, the halfmove clock and fullmove number, are deliberately left out because they do not affect move generation; the standard says they were dropped to save space, and they can be restored when needed with the `hmvc` and `fmvn` operations.[^s1]

After the four fields come zero or more **operations**, each separated by a single space.[^s1] An operation is an opcode, followed by zero or more operands, and closed by a semicolon. Opcodes begin with a letter and may run to fifteen characters of letters, digits and underscores; operands are either unbroken runs of printing characters or quoted strings, moves are written in SAN, and a program that meets an opcode it does not recognise simply ignores it.[^s1] That last rule is what makes the format extensible: new opcodes can be added without breaking older readers.[^s1]

## The common opcodes

The standard defines a vocabulary of opcodes.[^s1]

- **bm** (best move) and **am** (avoid move): one or more moves in SAN, all legal in the position. Test suites rely on `bm`.[^s1]
- **id**: a string naming the position, for example a suite label and number.[^s1]
- **ce**: a centipawn evaluation from the side to move's point of view; zero means a draw and values beyond ±32000 indicate mate.[^s1]
- **dm**: direct mate in a given number of full moves, as in `dm 3;`.[^s1]
- **pm** and **pv**: a predicted move and a predicted variation, whose first move should match `pm`.[^s1]
- **acn** and **acs**: analysis counts in nodes and seconds.[^s1]
- **c0–c9** and **v0–v9**: comment and variation-name registers; **eco** and **nic** hold opening classification codes.[^s1]
- **rc**: how often the position has occurred, where a value of three flags a possible repetition claim; **sm** is the move actually supplied from the position.[^s1]
- **draw_offer**, **draw_claim**, **draw_accept**, **draw_reject** and **resign**, plus the telecommunication opcodes **tcgs**, **tcri** and **tcsi** for games played by e-mail.[^s1]

Database programs adopted the same vocabulary: the ChessDB help, for instance, lists `bm`, `ce`, `eco`, `id`, `pv` and comment opcodes, and describes using an EPD file to classify games by ECO code.[^s6]

## A worked example: BK.01

The Bratko-Kopec test, devised by Danny Kopec and his co-author Bratko in 1982 (*Advances in Computer Chess 3*), is a set of 24 positions (12 tactical, 12 built around pawn levers) used to estimate the playing strength of programs and people.[^s3][^s4] Its scoring gives full credit for finding the key move within two minutes and partial credit at shorter intervals.[^s4] Suites like this are normally distributed as EPD. The python-chess documentation uses its first position as an example of parsing a record:[^s2]

`1k1r4/pp1b1R2/3q2pp/4p3/2B5/4Q3/PPP2B2/2K5 b - - bm Qd1+; id "BK.01";`

Read left to right: the placement field, Black to move, no castling rights, no en passant square, then two operations, the best move `Qd1+` and the label `BK.01`.[^s2] Marsland's review of the test lists Qd1 as the key move of position 1.[^s3] The same library can write EPD as well: from the initial position, asking for a record with `d4` as best move yields the four FEN-style fields followed by `bm d4;`.[^s2]

## Uses and pitfalls

Because EPD lines are self-describing and order-independent, they are the standard currency for engine test suites, tuning sets and position collections, and the opcode set was designed so that programs could exchange commands such as draw offers as well as data.[^s1] Common mistakes when preparing EPD by hand are pasting a full six-field FEN and leaving the two counters in front of the operations, forgetting the closing semicolon on the last operation, or writing a `bm` move in coordinate form instead of SAN.[^s1] Remember too that a bare EPD carries no game history: a repetition or fifty-move question needs `rc` or `hmvc` to be supplied explicitly.[^s1]

## Connections

EPD is a narrower relative of **Forsyth–Edwards Notation**, sharing its first four fields, and both are defined **as part of** the **Portable Game Notation** standard.[^s1] It was **developed by** **Steven J. Edwards** and **John Stanback**.[^s1][^s5] Its opcodes touch the rules on **threefold repetition** (`rc`) and the **fifty-move rule** (`hmvc`), it serves as an interchange format for **opening book** libraries, and it is the usual carrier for **computer chess** test sets such as the **Bratko-Kopec test**.[^s1][^s2][^s3]

## Sources

[^s1]: Steven J. Edwards (coordinator), "Standard: Portable Game Notation Specification and Implementation Guide", revised 12 March 1994, section 16.2. https://code.delx.au/gnu-emacs-elpa/blob/65de55274ce8d49fa67bb555050e2481ebcad2c5:/PGN.txt (accessed 2026-11-18)
[^s2]: Niklas Fiekas, "python-chess: a chess library for Python", stable documentation. https://python-chess.readthedocs.io/en/stable/ (accessed 2026-11-18)
[^s3]: T. Anthony Marsland, "The Bratko-Kopec Test Revisited", University of Alberta. https://webdocs.cs.ualberta.ca/~tony/OldPapers/Workshop-BK-1989.pdf (accessed 2026-11-18)
[^s4]: Shawn Benn and Danny Kopec, "The Bratko-Kopec Test Recalibrated". https://www.sci.brooklyn.cuny.edu/~kopec/Publications/THE%20BRATKO-KOPEC%20TEST%20RECALIBRATED.htm (accessed 2026-11-18)
[^s5]: Steven J. Edwards, "epd.c: Extended Position Description routines" (revised 23 June 1996), Crafty 25.2 source. https://grok.dragonflybsd.org/xref/dports/games/crafty/crafty-25.2_1/epd.c (accessed 2026-11-18)
[^s6]: ChessDB project, "EPD", ChessDB 2.5 help (June 2001). https://chessdb.sourceforge.net/tutorial/help/EPD.html (accessed 2026-11-18)
