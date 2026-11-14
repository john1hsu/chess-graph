---
id: kt:universal-chess-interface
type: Software
title: Universal Chess Interface
aliases: [UCI, UCI protocol, Universal Chess Interface protocol]
domain: computer-chess
summary: >-
  An open, text-based communication protocol, released in 2000 by Rudolf Huber and Stefan Meyer-Kahlen,
  through which a chess graphical user interface sends positions and search commands to an engine and
  receives its analysis and chosen move, so that any UCI engine can run in any UCI interface.
status: current
volatile: false
verified: 2026-11-14
broader: [kt:computer-chess]
related: [kt:stockfish, kt:leela-chess-zero, kt:chess960, kt:forsyth-edwards-notation, kt:algebraic-notation]
relations:
  - {predicate: developedBy, object: kt:rudolf-huber}
  - {predicate: developedBy, object: kt:stefan-meyer-kahlen}
  - {predicate: alternativeTo, object: kt:chess-engine-communication-protocol}
sources:
  - id: s1
    title: "UCI (Universal Chess Interface)"
    publisher: Shredder Computer Chess (Stefan Meyer-Kahlen)
    url: https://www.shredderchess.com/chess-features/uci-universal-chess-interface.html
    type: official-project
    accessed: 2026-11-14
  - id: s2
    title: "Description of the universal chess interface (UCI), April 2006 (copy distributed with GNOME Chess 41.1)"
    publisher: UCI specification text, GNOME Chess source tree
    url: https://grok.dragonflybsd.org/xref/dports/games/gnome-chess/gnome-chess-41.1/doc/Universal%20Chess%20Interface?a=true
    type: primary-record
    accessed: 2026-11-14
  - id: s3
    title: "UCI Protocol and Stockfish Commands"
    publisher: The Stockfish developers, GitHub wiki
    url: https://github.com/official-stockfish/Stockfish/wiki/UCI-Protocol-and-Stockfish-Commands
    type: official-project
    accessed: 2026-11-14
  - id: s4
    title: "Chess Engine Communication Protocol (version 2)"
    publisher: Tim Mann and H. G. Muller, GNU XBoard project
    url: https://www.gnu.org/software/xboard/engine-intf.html
    type: official-project
    accessed: 2026-11-14
created: 2026-11-14
---

# Universal Chess Interface

The **Universal Chess Interface (UCI)** is the protocol that lets a chess program with a board on screen (the graphical user interface, or GUI) talk to a separate chess engine that does the thinking. It was developed by Rudolf Huber and Stefan Meyer-Kahlen and released in 2000; the specification is distributed free from the website of Meyer-Kahlen's Shredder program. It is open and free of licence fees, and its stated purpose is interchangeability: any UCI engine can be plugged into any UCI-capable interface.[^s1] Almost all modern chess programs support it, and engines such as Stockfish and Leela Chess Zero describe themselves as UCI engines.[^s1][^s3]

## How it works

UCI is deliberately simple. The engine is an ordinary executable, and the two programs exchange plain-text lines over standard input and standard output; the protocol does not depend on the operating system.[^s2] The specification makes the GUI responsible for the game: it owns the clock and, by default, the opening book, and before every search it sends the position. The engine is always in what the specification calls forced mode, never searching or pondering until it is told to "go", and it must keep reading input even while it thinks so that it can be stopped.[^s2]

A session has a fixed rhythm. The GUI sends `uci`; the engine answers with its name and author (`id`), a list of configurable options, and `uciok`. The GUI then sets options with `setoption`, synchronises with `isready` / `readyok`, and may announce a fresh game with `ucinewgame`.[^s2][^s3] To analyse, it sends `position` (either `startpos` or a FEN string, followed by the moves played) and then `go`, with limits such as the remaining clock times and increments (`wtime`, `btime`, `winc`, `binc`), a fixed depth, a node count, a time per move, or `infinite`.[^s3] While searching, the engine streams `info` lines with depth, nodes, speed, the principal variation (`pv`) and a score; when it stops, it must send `bestmove`, optionally with a `ponder` move it expects in reply.[^s2][^s3]

## Notation and scores

Moves travel in a long algebraic form that names only the from- and to-squares: `e2e4`, `e1g1` for castling, `e7e8q` for promotion, and `0000` for a null move.[^s2] Scores are given in centipawns (`score cp`) or as a mate distance counted in moves (`score mate`), and the specification states that they are from the engine's point of view, so a negative mate score means the engine is being mated.[^s2] For example, the Ruy Lopez position after 1.e4 e5 2.Nf3 Nc6 3.Bb5 is sent as:

```
position startpos moves e2e4 e7e5 g1f3 b8c6 f1b5
go wtime 300000 btime 300000 winc 2000 binc 2000
```

Passing the move history, rather than only a FEN of the current position, matters because it lets the engine detect threefold repetition.[^s3]

## Options

Engines advertise their settings at start-up. The specification reserves names such as `Hash` (transposition-table size in MB), `Ponder`, `OwnBook`, `MultiPV`, and a family of `UCI_` options including `UCI_LimitStrength` with `UCI_Elo`, `UCI_AnalyseMode`, `UCI_Opponent` and `UCI_Chess960`.[^s2] Stockfish, for instance, exposes `Threads`, `Hash`, `MultiPV`, `UCI_Chess960`, strength limitation via `UCI_LimitStrength` and `UCI_Elo`, and `UCI_ShowWDL` for win/draw/loss estimates, and adds non-standard commands such as `d` (show the board), `eval` and `bench`.[^s3]

## Pitfalls for users

- **Score sign.** UCI scores are from the engine's own point of view, not White's, so raw engine logs must be read with the side to move in mind; the specification's one exception is the `UCI_SetPositionValue` option, whose value is from White's side.[^s2]
- **Resource settings.** Defaults are conservative (Stockfish starts with one thread and a 16 MB hash), so analysis is much weaker until `Threads` and `Hash` are raised; `MultiPV` above 1 costs strength in exchange for extra lines.[^s3]
- **Chess960.** With `UCI_Chess960` on, castling is written as the king capturing its own rook (for example `e1h1`), and castling rights in FEN use rook files such as `AHah`.[^s2]

## Connections

UCI is part of the infrastructure of **computer chess** and is the interface through which **Stockfish** and **Leela Chess Zero** are used.[^s1][^s3] It builds on **Forsyth–Edwards Notation** for positions and a long form of **algebraic notation** for moves, and it has explicit support for **Chess960**.[^s2] It was **developed by** Rudolf Huber and Stefan Meyer-Kahlen.[^s1] Its main **alternative** is the older **Chess Engine Communication Protocol** used by XBoard and WinBoard, written by Tim Mann and H. G. Muller, in which the GUI sends individual moves and clock readings and the engine is expected to track the position itself, and in force mode merely records moves without thinking.[^s4]

## Sources
[^s1]: Shredder Computer Chess, "UCI (Universal Chess Interface)". https://www.shredderchess.com/chess-features/uci-universal-chess-interface.html (accessed 2026-11-14)
[^s2]: "Description of the universal chess interface (UCI)", April 2006, copy distributed with GNOME Chess 41.1. https://grok.dragonflybsd.org/xref/dports/games/gnome-chess/gnome-chess-41.1/doc/Universal%20Chess%20Interface?a=true (accessed 2026-11-14)
[^s3]: The Stockfish developers, "UCI Protocol and Stockfish Commands", GitHub wiki. https://github.com/official-stockfish/Stockfish/wiki/UCI-Protocol-and-Stockfish-Commands (accessed 2026-11-14)
[^s4]: Tim Mann and H. G. Muller, "Chess Engine Communication Protocol" (version 2). https://www.gnu.org/software/xboard/engine-intf.html (accessed 2026-11-14)
