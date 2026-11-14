---
id: kt:portable-game-notation
type: Notation
title: Portable Game Notation
aliases: [PGN, PGN format, PGN standard, Portable Game Notation standard]
domain: rules-and-notation
summary: >-
  A plain-text format for recording and exchanging chess games, consisting of bracketed tag
  pairs (led by the Seven Tag Roster) followed by movetext in Standard Algebraic Notation; it
  was defined in a 1994 standard coordinated by Steven J. Edwards and is the common
  interchange format of chess software, databases and broadcasts.
status: current
volatile: true
verified: 2026-11-14
broader: [kt:algebraic-notation]
related: [kt:forsyth-edwards-notation, kt:extended-position-description, kt:numeric-annotation-glyphs, kt:computer-chess, kt:chess-titles, kt:universal-chess-interface]
relations:
  - {predicate: developedBy, object: kt:steven-j-edwards}
  - {predicate: hasPart, object: kt:forsyth-edwards-notation}
  - {predicate: dependsOn, object: kt:algebraic-notation}
sources:
  - id: s1
    title: "Standard: Portable Game Notation Specification and Implementation Guide (revised 1994-03-12)"
    publisher: Steven J. Edwards (coordinator), rec.games.chess; copy distributed with Apple's Chess application
    url: https://opensource.apple.com/source/Chess/Chess-105.0.14/Documentation/PGN-Standard.txt.auto.html
    type: primary-record
    accessed: 2026-11-14
  - id: s2
    title: "FIDE Title Regulations effective from 1 January 2024, article 1.9 (Submission of Reports on Title Tournaments)"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/B012024
    type: governing-body
    accessed: 2026-11-14
  - id: s3
    title: "PGN Standard: Proposed Supplement (final draft, 8 September 2001)"
    publisher: Alan Cowderoy, Ben Bulsink, Andrew Templeton, Eric Bentzen, Mathias Feist and Victor Zakharov; copy distributed with pgn4web
    url: https://codesearch.dokuwiki.org/xref/plugin/pgn4web/pgn4web/pgn-standard-proposed-supplement.txt
    type: primary-record
    accessed: 2026-11-14
  - id: s4
    title: "PGN (Fritz 19 help)"
    publisher: ChessBase
    url: https://help.chessbase.com/Fritz/19/Eng/000047.htm
    type: publication
    accessed: 2026-11-14
  - id: s5
    title: "PGN (.pgn) — Wolfram Language import/export format reference"
    publisher: Wolfram Research
    url: https://reference.wolfram.com/language/ref/format/PGN.html
    type: publication
    accessed: 2026-11-14
created: 2026-11-14
---

# Portable Game Notation

Portable Game Notation (PGN) is the standard plain-text format for storing and exchanging chess games. A PGN file is ordinary ASCII text that a person can read in any editor and that a program can parse and generate without difficulty; the standard recommends the `.pgn` file extension.[^s1] It was set out in "Standard: Portable Game Notation Specification and Implementation Guide", revised on 12 March 1994, written by readers of the rec.games.chess newsgroup with Steven J. Edwards as coordinator.[^s1] Software documentation describes it as an internationally accepted format in which many games on the internet are distributed, and Wolfram's format reference registers it with the media type `application/vnd.chess-pgn`.[^s4][^s5] For a club player, PGN is what comes out when you download a game from a playing site, and what goes in when you paste a score into an analysis board.

## Structure of a game

Each game has two sections: a tag-pair section and a movetext section.[^s1] A tag pair is a tag name and a quoted value in square brackets, such as `[Event "Casual Game"]`; tag names are case-sensitive.[^s1] Every exported game must carry the **Seven Tag Roster** in a fixed order: Event, Site, Date, Round, White, Black and Result.[^s1] Dates are written `YYYY.MM.DD` with question marks for unknown parts (`1993.??.??`), player names are given surname first, and the Result tag takes one of four values: `1-0`, `0-1`, `1/2-1/2`, or `*` for a game that is unfinished, abandoned or of unknown result.[^s1] Optional tags such as WhiteElo, BlackElo, ECO, TimeControl and Termination add further detail, and a game that starts from a non-standard position carries SetUp and FEN tags.[^s1]

The movetext records the moves in Standard Algebraic Notation: piece letters K, Q, R, B and N, no letter for pawns, `x` for captures, `O-O` and `O-O-O` (letter O, not zero) for castling, `=Q` for promotion, and `+` or `#` for check and mate.[^s1] White's moves are preceded by a number and a period, and the movetext must end with a single termination marker that matches the Result tag.[^s1]

## Annotations and variations

PGN can carry commentary. Text between braces `{ }` is a comment, as is anything after a semicolon to the end of a line; brace comments do not nest.[^s1] Alternative lines go in parentheses as Recursive Annotation Variations, which may be nested and stand for an alternative to the move just played.[^s1] Evaluative symbols are stored as Numeric Annotation Glyphs, a dollar sign plus a number from 0 to 255: `$1` is a good move ("!"), `$2` a poor move ("?"), and values from 10 upward describe the position, such as `$14` for a slight advantage to White.[^s1] Import software accepts the familiar suffixes `!`, `?`, `!!`, `!?`, `?!` and `??` and converts them to glyphs on export.[^s1]

## Import, export and later extensions

The standard deliberately defines two dialects. **Import format** is lenient so that hand-typed games can be read; **export format** is strict, with one tag per line and fixed spacing, so that output from different programs is identical. The minimum an exporter must support is the **reduced export format**: only the Seven Tag Roster, and no comments, variations or glyphs.[^s1] Lines beginning with `%` are an escape mechanism for private software data and are ignored by standard readers.[^s1]

Because comments are free text, later extensions were added inside them rather than by new syntax. A 2001 supplement drafted by developers from Palamede, DGT Projects, ChessBase and Chess Assistant proposed "embedded commands" of the form `[%command value]` in a comment, chiefly to carry clock times from electronic boards in live broadcasts: `%clk` for the time remaining, `%emt` for time spent on a move and `%egt` for elapsed game time.[^s3] Software that does not understand a command is supposed to pass it through untouched.[^s3]

## Example and pitfalls

The standard's own sample game is the 29th game of the 1992 Fischer–Spassky return match, recorded as a draw:[^s1]

```pgn
[Event "F/S Return Match"]
[Site "Belgrade, Serbia JUG"]
[Date "1992.11.04"]
[Round "29"]
[White "Fischer, Robert J."]
[Black "Spassky, Boris V."]
[Result "1/2-1/2"]

1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3
O-O 9. h3 Nb8 10. d4 Nbd7 11. c4 c6 12. cxb5 axb5 13. Nc3 Bb7 14. Bg5 b4 15.
Nb1 h6 16. Bh4 c5 17. dxe5 Nxe4 18. Bxe7 Qxe7 19. exd6 Qf6 20. Nbd2 Nxd6 21.
Nc4 Nxc4 22. Bxc4 Nb6 23. Ne5 Rae8 24. Bxf7+ Rxf7 25. Nxf7 Rxe1+ 26. Qxe1 Kxf7
27. Qe3 Qg5 28. Qxg5 hxg5 29. b3 Ke6 30. a3 Kd6 31. axb4 cxb4 32. Ra5 Nd5 33.
f3 Bc8 34. Kf2 Bf5 35. Ra7 g6 36. Ra6+ Kc5 37. Ke1 Nf4 38. g3 Nxh3 39. Kd2 Kb5
40. Rd6 Kc5 41. Ra6 Nf2 42. g4 Bd3 43. Re6 1/2-1/2
```

Common faults when preparing PGN by hand are castling with zeros, leaving out the termination marker or letting it disagree with the Result tag, using braces inside a comment, and writing an ambiguous move such as `Nd2` when two knights can reach the square; the standard requires the origin file, then rank, to be added in that case.[^s1] Annotated files exported to plain PGN can also lose program-specific features; ChessBase notes that its own database formats offer functions such as faster duplicate searches that a text file does not.[^s4]

## Official use

PGN is also part of title administration. As of November 2026, the FIDE Title Regulations in force since 1 January 2024 require a report on a title tournament to include a PGN file: for Swiss and team events, at least the games of players who achieved title results, and for other events, all games.[^s2]

## Connections

PGN builds on **algebraic notation**, its broader node, and **depends on** Standard Algebraic Notation for its movetext.[^s1] It **has as a part** **Forsyth–Edwards Notation**, which the same 1994 document defines for recording starting positions, alongside the related **Extended Position Description**.[^s1] It was **developed by** **Steven J. Edwards** as coordinator.[^s1] Its **numeric annotation glyphs** encode the evaluation symbols familiar from printed annotations.[^s1] In **computer chess**, it is the exchange format between engines, databases and GUIs that speak protocols such as the **Universal Chess Interface**, and it feeds the paperwork behind FIDE **chess titles**.[^s2][^s4]

## Sources

[^s1]: Steven J. Edwards (coordinator), "Standard: Portable Game Notation Specification and Implementation Guide", revised 12 March 1994. https://opensource.apple.com/source/Chess/Chess-105.0.14/Documentation/PGN-Standard.txt.auto.html (accessed 2026-11-14)
[^s2]: FIDE Handbook, "FIDE Title Regulations effective from 1 January 2024", article 1.9.1. https://handbook.fide.com/chapter/B012024 (accessed 2026-11-14)
[^s3]: Alan Cowderoy et al., "PGN Standard: Proposed Supplement", final draft, 8 September 2001. https://codesearch.dokuwiki.org/xref/plugin/pgn4web/pgn4web/pgn-standard-proposed-supplement.txt (accessed 2026-11-14)
[^s4]: ChessBase, "PGN", Fritz 19 help. https://help.chessbase.com/Fritz/19/Eng/000047.htm (accessed 2026-11-14)
[^s5]: Wolfram Research, "PGN (.pgn)", Wolfram Language format reference. https://reference.wolfram.com/language/ref/format/PGN.html (accessed 2026-11-14)
