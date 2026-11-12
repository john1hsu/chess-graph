---
id: kt:stockfish
type: Engine
title: Stockfish
aliases: [Stockfish chess engine, Stockfish NNUE, SF]
domain: computer-chess
summary: >-
  A free, open-source UCI chess engine, forked from Glaurung in 2008 and developed by a volunteer
  community, which combines alpha-beta search with an efficiently updatable neural network (NNUE)
  evaluation and has been the dominant engine in computer-chess championships.
status: current
volatile: true
verified: 2026-11-12
broader: [kt:computer-chess]
related: [kt:alphazero, kt:leela-chess-zero, kt:evaluation-function, kt:bitboards, kt:endgame-tablebases]
relations:
  - {predicate: usesTechnique, object: kt:alpha-beta-pruning}
  - {predicate: usesTechnique, object: kt:nnue}
  - {predicate: usesTechnique, object: kt:universal-chess-interface}
  - {predicate: developedBy, object: kt:tord-romstad}
  - {predicate: developedBy, object: kt:marco-costalba}
  - {predicate: playedIn, object: kt:top-chess-engine-championship}
sources:
  - id: s1
    title: "About Stockfish"
    publisher: The Stockfish developers (stockfishchess.org)
    url: https://stockfishchess.org/about/
    type: official-project
    accessed: 2026-11-12
  - id: s2
    title: "official-stockfish/Stockfish (README)"
    publisher: The Stockfish developers, GitHub
    url: https://github.com/official-stockfish/Stockfish
    type: official-project
    accessed: 2026-11-12
  - id: s3
    title: "Stockfish 12"
    publisher: The Stockfish developers (stockfishchess.org)
    url: https://stockfishchess.org/blog/2020/stockfish-12/
    type: official-project
    accessed: 2026-11-12
  - id: s4
    title: "Stockfish 19"
    publisher: The Stockfish developers (stockfishchess.org)
    url: https://stockfishchess.org/blog/2026/stockfish-19/
    type: official-project
    accessed: 2026-11-12
  - id: s5
    title: "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm"
    publisher: David Silver et al. (DeepMind), arXiv:1712.01815
    url: https://arxiv.org/html/1712.01815
    type: academic
    accessed: 2026-11-12
  - id: s6
    title: "Stockfish claims its 19th TCEC title, defeating Reckless in the Superfinal"
    publisher: Chessdom
    url: https://www.chessdom.com/stockfish-claims-its-19th-tcec-title-defeating-reckless-in-the-superfinal/
    type: news
    accessed: 2026-11-12
created: 2026-11-12
---

# Stockfish

Stockfish is a free chess engine whose source code is published under the GNU General Public License version 3: anyone may use, share or sell it, but whoever distributes it must also make the source available, and modified versions must stay under the same licence.[^s1][^s2] It is a command-line engine that speaks the UCI protocol and ships without a graphical board, so players reach it through a separate chess GUI, an online analysis board or a database program.[^s2] As of November 2026 its current major release is Stockfish 19, published in September 2026.[^s4]

## History

Stockfish grew out of Glaurung, an engine by Tord Romstad. In November 2008 Marco Costalba forked Glaurung 2.1 and released Stockfish 1.0; Romstad and Joona Kiiski then joined the project, and Glaurung itself faded away.[^s1] The three original authors have since been succeeded by a broad volunteer community that develops and maintains the engine.[^s1] Development is driven by Fishtest, a distributed testing framework to which volunteers donate computer time: because the README notes that improving Stockfish needs a massive amount of testing, every proposed change is played in large numbers of engine-versus-engine games before it is accepted.[^s2]

## How it works

Like the classical engines before it, Stockfish chooses moves with an alpha-beta (principal variation) search over the game tree, scoring the leaf positions with an evaluation function.[^s3] Until 2020 that evaluation was hand-written, built from chess concepts designed by experts. Stockfish 12, released on 2 September 2020, added NNUE, an "efficiently updatable neural network" that computes a score from simple inputs and was trained on evaluations of millions of positions; the idea was first developed for shogi engines and then ported to chess.[^s3] The developers reported that Stockfish 12 won at least ten times more game pairs than it lost against Stockfish 11.[^s3] The network is distributed as a `.nnue` file that release binaries embed.[^s2]

The network has kept evolving. Stockfish 19 introduced the SFNNv16 architecture, which drops redundant threat features and adds pawn-pair features, retired the secondary network introduced in version 16.1, and was trained on hundreds of billions of positions rescored by a strong Leela Chess Zero network.[^s4] Against Stockfish 18 it gained up to 44 Elo in the project's tests.[^s4] The same release added universal binaries that detect the processor's features automatically, and stricter validation of FEN strings and UCI commands.[^s4]

## Example: the 2017 AlphaZero match

Stockfish became the standard benchmark for new approaches. In DeepMind's 2017 AlphaZero preprint, Stockfish 8, described as the open-source winner of the 2016 TCEC championship and an alpha-beta engine with handcrafted evaluation, played a 100-game match at one minute per move, running on 64 threads with a 1 GB hash table.[^s5] AlphaZero lost no game in that match, while searching about 80 thousand positions per second against Stockfish's roughly 70 million.[^s5] The contrast between deep, cheap search and shallow, expensive neural evaluation fed directly into the NNUE era, in which Stockfish kept its fast search but gained a learned evaluation.[^s3][^s5]

## Competitive record and pitfalls for users

In April 2026 Stockfish won the Season 29 Superfinal of the Top Chess Engine Championship (TCEC) against the newer engine Reckless by 59–41 over 100 games, its 19th TCEC title and 12th consecutive season championship, according to the event's host site.[^s6] Lc0 had been its Superfinal opponent the season before.[^s6] For a club player using it at home, two practical cautions follow from the sources. First, any engine result is tied to its conditions: published comparisons state time per move, thread count and hash size because those settings shape how deeply the engine searches.[^s5] Second, since Stockfish 19 the engine treats an invalid FEN or malformed UCI command as a critical error and stops, so a crashed analysis often means a badly entered position rather than a broken program.[^s4]

## Connections

Stockfish belongs to [computer chess](kt:computer-chess), and its search is an application of [alpha-beta pruning](kt:alpha-beta-pruning) over a game tree, scored by an [evaluation function](kt:evaluation-function) that is now an [NNUE](kt:nnue) network.[^s3] It is reached through the [Universal Chess Interface](kt:universal-chess-interface).[^s2] It was created by [Tord Romstad](kt:tord-romstad) and [Marco Costalba](kt:marco-costalba) with Joona Kiiski.[^s1] Its rivals and foils are [AlphaZero](kt:alphazero), which beat it in 2017, and [Leela Chess Zero](kt:leela-chess-zero), whose evaluations now help train Stockfish's networks.[^s4][^s5] Its main proving ground is the [Top Chess Engine Championship](kt:top-chess-engine-championship).[^s6] Links to [bitboards](kt:bitboards) and [endgame tablebases](kt:endgame-tablebases) come from those articles.

## Sources

[^s1]: The Stockfish developers, "About". https://stockfishchess.org/about/ (accessed 2026-11-12)
[^s2]: The Stockfish developers, official-stockfish/Stockfish repository README, GitHub. https://github.com/official-stockfish/Stockfish (accessed 2026-11-12)
[^s3]: The Stockfish developers, "Stockfish 12", 2 September 2020. https://stockfishchess.org/blog/2020/stockfish-12/ (accessed 2026-11-12)
[^s4]: The Stockfish developers, "Stockfish 19", September 2026. https://stockfishchess.org/blog/2026/stockfish-19/ (accessed 2026-11-12)
[^s5]: D. Silver et al., "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm", arXiv:1712.01815 (2017). https://arxiv.org/html/1712.01815 (accessed 2026-11-12)
[^s6]: Chessdom, "Stockfish claims its 19th TCEC title, defeating Reckless in the Superfinal", 21 April 2026. https://www.chessdom.com/stockfish-claims-its-19th-tcec-title-defeating-reckless-in-the-superfinal/ (accessed 2026-11-12)
