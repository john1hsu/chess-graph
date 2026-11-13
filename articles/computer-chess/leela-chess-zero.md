---
id: kt:leela-chess-zero
type: Engine
title: Leela Chess Zero
aliases: [Lc0, LCZero, Leela, Leela Chess]
domain: computer-chess
summary: >-
  A free, open-source UCI chess engine, inspired by AlphaZero, that chooses moves with a Monte Carlo
  tree search guided by a neural network trained through distributed self-play, and that won the
  Top Chess Engine Championship in Season 15 (2019).
status: current
volatile: true
verified: 2026-11-13
broader: [kt:computer-chess]
related: [kt:alphazero, kt:stockfish, kt:nnue, kt:evaluation-function]
relations:
  - {predicate: usesTechnique, object: kt:monte-carlo-tree-search}
  - {predicate: usesTechnique, object: kt:universal-chess-interface}
  - {predicate: influencedBy, object: kt:alphazero}
  - {predicate: influencedBy, object: kt:leela-zero}
  - {predicate: playedIn, object: kt:top-chess-engine-championship}
sources:
  - id: s1
    title: "What is Lc0?"
    publisher: Leela Chess Zero project (lczero.org)
    url: https://lczero.org/dev/wiki/what-is-lc0
    type: official-project
    accessed: 2026-11-13
  - id: s2
    title: "Project overview"
    publisher: Leela Chess Zero project (lczero.org)
    url: https://lczero.org/dev/overview
    type: official-project
    accessed: 2026-11-13
  - id: s3
    title: "LeelaChessZero/lczero (deprecated original repository, README)"
    publisher: Leela Chess Zero project, GitHub
    url: https://github.com/leelachesszero/lczero
    type: official-project
    accessed: 2026-11-13
  - id: s4
    title: "LeelaChessZero/lc0 (README) and releases"
    publisher: Leela Chess Zero project, GitHub
    url: https://github.com/LeelaChessZero/lc0
    type: official-project
    accessed: 2026-11-13
  - id: s5
    title: "Project History"
    publisher: Leela Chess Zero project (lczero.org)
    url: https://lczero.org/dev/wiki/project-history
    type: official-project
    accessed: 2026-11-13
  - id: s6
    title: "Leela Chess Zero Blog, posts of January–March 2019"
    publisher: Leela Chess Zero project (lczero.org)
    url: https://lczero.org/blog/page/5
    type: official-project
    accessed: 2026-11-13
  - id: s7
    title: "Leela Chess Zero Blog, posts of March–July 2019"
    publisher: Leela Chess Zero project (lczero.org)
    url: https://lczero.org/blog/page/4
    type: official-project
    accessed: 2026-11-13
  - id: s8
    title: "The TCEC15 Computer Chess Superfinal: a perspective"
    publisher: Matthew Sadler, Top Chess Engine Championship (tcec-chess.com)
    url: https://tcec-chess.com/articles/Sufi_15_-_Sadler.pdf
    type: publication
    accessed: 2026-11-13
  - id: s9
    title: "First major title for a neural network in chess: Lc0 wins TCEC Cup"
    publisher: Chessdom
    url: https://www.chessdom.com/first-major-title-for-a-neural-network-in-chess-lc0-wins-tcec-cup/
    type: news
    accessed: 2026-11-13
created: 2026-11-13
---

# Leela Chess Zero

Leela Chess Zero, usually shortened to Lc0, is a chess engine that plays by consulting a trained neural network. Its own documentation describes it as inspired by DeepMind's AlphaZero project and splits it into two parts that a user must download separately: the engine binary, which sees the board and makes the moves, and the network file, which tells it which moves are good.[^s1] The project stresses that Lc0 is only as strong as the network it loads.[^s1] It is free software under the GNU GPL version 3, speaks the UCI protocol, and is built for GPU acceleration across NVIDIA, AMD, Apple and Intel hardware, with a slower CPU path as well.[^s4] As of November 2026 the latest stable release listed on the project's GitHub page is v0.32.1, with a v0.33.0 release candidate also published.[^s4]

## Origins

The original lczero repository describes itself as a chess adaptation of Leela Zero, the Go engine by the programmer known as GCP, and as a fork of an earlier "leela-chess" project. It borrowed only Stockfish's board representation and move generator, explicitly carrying over no chess heuristics or prior knowledge, and aimed to build a strong engine with the techniques of the AlphaZero paper.[^s3] Development moved to the current lc0 repository in 2018, and the old one is now marked deprecated.[^s3] The project's history log shows how fast the early networks grew: from 6 blocks of 64 filters to 10x128 in April 2018 and 15x192 by the end of that month, while the first rapid match on TCEC servers, against Scorpio 2.79 in mid-April 2018, was still lost heavily.[^s5]

## How it works

Instead of the alpha-beta search used by Stockfish, the lc0 engine runs Monte Carlo tree search with the PUCT selection rule, and its search algorithms are pluggable.[^s2] Its network has three heads: a value head that scores the position, a policy head that rates candidate moves, and a moves-left head that estimates how long the game will last.[^s2] Because each network call is expensive, Lc0 searches far fewer positions than a classical engine and relies on the network's judgement to steer the search, which is why it runs best on a powerful GPU.[^s1]

The networks are trained by reinforcement learning. Volunteers run a training client that downloads the latest network, makes lc0 play games against itself and uploads them; a data server passes the games to training servers, which train new networks and publish them back.[^s2][^s3] Before training, a rescorer checks positions against Syzygy endgame tablebases and flags intentional blunders.[^s2] Training proceeds in named "runs" with different architectures; for example, the T80 run begun in April 2022 used 15 blocks of 512 filters with an attention-based policy head.[^s5]

## Competitive record

Lc0 broke through at the Top Chess Engine Championship (TCEC) in early 2019. It won the 32-engine TCEC Cup knockout without losing a game, beating Komodo in the semi-final and Houdini 4.5-3.5 in the final; Chessdom called it the first major title for a neural network in computer chess.[^s9][^s6] It then reached its first Superfinal, in Season 14, and lost to Stockfish by the narrowest margin, 49.5-50.5.[^s6] In Season 15 it went one better, qualifying undefeated and winning the Superfinal against Stockfish in May 2019.[^s7]

## Example: a Season 15 Superfinal game

Reviewing that match, grandmaster Matthew Sadler gave the final score as 53.5-46.5, fourteen wins to seven, and judged it a fair reflection of strength.[^s8] He found Lc0 more purposeful from level starting positions, more willing to seek activity than to defend passively, and better at positions where play on both wings interacts.[^s8] One game he highlights, game 61, began as a Trompowsky with Stockfish as White:

```pgn
[Event "TCEC Season 15 Superfinal, game 61 (opening only)"]
[White "Stockfish"]
[Black "Lc0"]
[Result "*"]

1. d4 Nf6 2. Bg5 Ne4 3. Bf4 c5 4. f3 Qa5+ *
```

Lc0 steered the game toward a pawn structure that favoured Black while Stockfish still rated the position as level.[^s8] For a club player the practical lesson is that an engine's evaluation is an estimate, and a network-guided engine and a search-heavy engine can disagree about the same structure.[^s8]

## Connections

Lc0 is part of [computer chess](kt:computer-chess). It is a public re-creation of the ideas in [AlphaZero](kt:alphazero), adapted from the Go engine [Leela Zero](kt:leela-zero), and it uses [Monte Carlo tree search](kt:monte-carlo-tree-search) in place of alpha-beta.[^s1][^s2][^s3] It is driven through the [Universal Chess Interface](kt:universal-chess-interface).[^s4] Its great rival is [Stockfish](kt:stockfish), whose [NNUE](kt:nnue) network is a different, CPU-friendly answer to replacing a hand-written [evaluation function](kt:evaluation-function); the two met in successive Superfinals of the [Top Chess Engine Championship](kt:top-chess-engine-championship).[^s6][^s7]

## Sources

[^s1]: Leela Chess Zero project, "What is Lc0?". https://lczero.org/dev/wiki/what-is-lc0 (accessed 2026-11-13)
[^s2]: Leela Chess Zero project, "Project overview". https://lczero.org/dev/overview (accessed 2026-11-13)
[^s3]: Leela Chess Zero project, LeelaChessZero/lczero repository README (deprecated), GitHub. https://github.com/leelachesszero/lczero (accessed 2026-11-13)
[^s4]: Leela Chess Zero project, LeelaChessZero/lc0 repository README and releases, GitHub. https://github.com/LeelaChessZero/lc0 (accessed 2026-11-13)
[^s5]: Leela Chess Zero project, "Project History". https://lczero.org/dev/wiki/project-history (accessed 2026-11-13)
[^s6]: Leela Chess Zero Blog, posts of January–March 2019 ("Leela won the TCEC CUP!", 4 February 2019; "Leela falls just short in first TCEC Superfinal appearance", 16 March 2019). https://lczero.org/blog/page/5 (accessed 2026-11-13)
[^s7]: Leela Chess Zero Blog, posts of March–July 2019 ("Competition Season!", 11 May 2019; "Lc0 won TCEC 15", 28 May 2019). https://lczero.org/blog/page/4 (accessed 2026-11-13)
[^s8]: M. Sadler, "The TCEC15 Computer Chess Superfinal: a perspective", Top Chess Engine Championship. https://tcec-chess.com/articles/Sufi_15_-_Sadler.pdf (accessed 2026-11-13)
[^s9]: Chessdom, "First major title for a neural network in chess: Lc0 wins TCEC Cup". https://www.chessdom.com/first-major-title-for-a-neural-network-in-chess-lc0-wins-tcec-cup/ (accessed 2026-11-13)
