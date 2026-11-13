---
id: kt:alphazero
type: Engine
title: AlphaZero
aliases: [Alpha Zero, DeepMind AlphaZero]
domain: computer-chess
summary: >-
  A game-playing system from DeepMind that learned chess, shogi and Go from the rules alone by
  reinforcement learning through self-play, combining a deep neural network with Monte Carlo tree
  search; announced in December 2017 and published in Science in December 2018 after it defeated
  Stockfish in a 1,000-game match.
moves: "1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6"
status: historical
volatile: false
verified: 2026-11-13
broader: [kt:computer-chess]
related: [kt:leela-chess-zero, kt:nnue, kt:berlin-defence, kt:vladimir-kramnik]
relations:
  - {predicate: usesTechnique, object: kt:monte-carlo-tree-search}
  - {predicate: usesTechnique, object: kt:reinforcement-learning}
  - {predicate: developedBy, object: kt:deepmind}
  - {predicate: contrastsWith, object: kt:stockfish}
  - {predicate: contrastsWith, object: kt:alpha-beta-pruning}
sources:
  - id: s1
    title: "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (arXiv:1712.01815)"
    publisher: Silver et al., DeepMind (arXiv)
    url: https://arxiv.org/html/1712.01815
    type: academic
    accessed: 2026-11-13
  - id: s2
    title: "A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play (Science 362(6419):1140-1144, 2018)"
    publisher: Silver et al., Science (copy hosted by UNAM IIMAS course materials)
    url: https://turing.iimas.unam.mx/~luis/cursos/IA2022-1/lecturas/AlphaZero.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "AlphaZero: Shedding new light on chess, shogi, and Go (6 December 2018)"
    publisher: Google DeepMind
    url: https://deepmind.google/blog/alphazero-shedding-new-light-on-chess-shogi-and-go/
    type: official-project
    accessed: 2026-11-13
  - id: s4
    title: "Acquisition of chess knowledge in AlphaZero (PNAS 119(47):e2206625119, 2022)"
    publisher: McGrath et al., Proceedings of the National Academy of Sciences (PubMed Central)
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9704706
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s5
    title: "Game Changer: AlphaZero's Groundbreaking Chess Strategies and the Promise of AI"
    publisher: Matthew Sadler and Natasha Regan, New In Chess (2019)
    url: https://www.newinchess.com/game-changer
    type: book
    accessed: 2026-11-13
created: 2026-11-13
---

# AlphaZero

**AlphaZero** is a game-playing program built by DeepMind that taught itself chess, shogi and Go starting from random play, with no knowledge beyond the rules of each game. A preprint announcing it appeared on arXiv on 5 December 2017, reporting superhuman strength in all three games within 24 hours of training.[^s1] The full, revised evaluation was published in *Science* on 7 December 2018.[^s2] AlphaZero was a research system rather than a released engine, but its approach reshaped computer chess and prompted a wave of human study of its games.[^s3][^s5]

## How it works

Classical engines of the time paired alpha-beta search with an evaluation function hand-tuned by experts over decades. AlphaZero replaced both. A single deep neural network takes the board (plus a short history of previous positions, castling rights, repetition and no-progress counters) and outputs two things: a **policy**, a probability for each possible move, and a **value**, an estimate of the expected game result. In chess the policy covers 4,672 move encodings, with illegal moves masked out.[^s1]

The network guides a **Monte Carlo tree search** (MCTS): instead of examining every move to a fixed depth, the search expands lines the policy considers promising and averages the network's value estimates. It is therefore far more selective than an alpha-beta engine. In the *Science* match AlphaZero searched about 60,000 positions per second against roughly 60 million for Stockfish.[^s2]

Training was by **reinforcement learning through self-play**. The program played games against itself (800 MCTS simulations per move during training), and the network was continually updated to predict the moves its own search chose and the eventual results. Compared with its predecessor AlphaGo Zero, it modelled draws as expected outcomes, did not exploit board symmetries, and kept one continually updated network. For chess, training ran about 9 hours over roughly 44 million games, using 5,000 first-generation TPUs to generate games and 64 second-generation TPUs to train; it surpassed Stockfish after about 4 hours.[^s1]

## Results

The 2017 preprint reported a 100-game match against Stockfish 8 at one minute per move in which AlphaZero lost no games.[^s1] The 2018 paper superseded that preliminary result with a 1,000-game match at three hours per game plus 15 seconds per move against the 2016 TCEC champion version of Stockfish on 44 CPU cores. AlphaZero won 155 games and lost 6, the rest drawn. It also won matches starting from the TCEC opening positions and from popular human openings, and against newer Stockfish versions; it still won when given only a tenth of Stockfish's thinking time.[^s2][^s3] In shogi it beat the 2017 computer champion Elmo, and in Go it beat AlphaGo Zero.[^s3]

## Style and influence on human chess

DeepMind and commentators stressed a dynamic style: AlphaZero readily gave up material for long-term activity and attacks on the king, and Garry Kasparov likened its play to his own.[^s3] Grandmaster Matthew Sadler and Natasha Regan studied more than two thousand of its games, with access to the developers, in *Game Changer* (New In Chess, 2019), organising its lessons around themes such as piece activity, initiative and long-term sacrifices.[^s5]

A 2022 *PNAS* study co-authored by former world champion Vladimir Kramnik probed the network for human chess concepts. Material and space emerged first in training; king safety, threats and mobility came later; and piece values settled near conventional ones by about 128,000 training steps. AlphaZero did not retrace human opening history: it began with nearly uniform first moves and narrowed them, rather than starting with 1.e4 and widening as humans did.[^s4]

## Example

The same study traced how AlphaZero handled the Ruy Lopez after **1.e4 e5 2.Nf3 Nc6 3.Bb5**. In three of four training runs its network ended up placing around 89–93% of its prior on **3...Nf6**, the Berlin Defence, adopted rapidly after about 100,000 steps; one run preferred 3...a6 instead. The authors point out that human appreciation of the Berlin is relatively recent, and credit Kramnik with being the first champion to rely on it at the top level.[^s4]

A common pitfall is to treat AlphaZero's published games as proof that one style is "correct". Its strength came from a large learned evaluation combined with search on specialised hardware (four TPUs in the 2018 match), and most games against Stockfish were still drawn: 839 of 1,000.[^s2] Kramnik's checkpoint comparisons also showed its understanding growing in stages, from material to king safety to sacrificial attack, so early-training games are a poor guide to its mature judgement.[^s4]

## Connections

AlphaZero is a landmark in **computer chess**. It **uses** **Monte Carlo tree search** and **reinforcement learning**, and was **developed by DeepMind**.[^s1][^s3] It **contrasts with** **Stockfish** and the **alpha-beta** tradition, which search thousands of times more positions with a cheaper evaluation.[^s2] It is related to **Leela Chess Zero** and **NNUE**, the later neural approaches in open-source engines covered in their own articles. Its handling of the **Berlin Defence** was analysed with **Vladimir Kramnik**.[^s4]

## Sources
[^s1]: D. Silver et al., "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm", arXiv:1712.01815 (5 December 2017). https://arxiv.org/html/1712.01815 (accessed 2026-11-13)
[^s2]: D. Silver et al., "A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play", *Science* 362(6419):1140–1144 (7 December 2018). https://turing.iimas.unam.mx/~luis/cursos/IA2022-1/lecturas/AlphaZero.pdf (accessed 2026-11-13)
[^s3]: Google DeepMind, "AlphaZero: Shedding new light on chess, shogi, and Go" (6 December 2018). https://deepmind.google/blog/alphazero-shedding-new-light-on-chess-shogi-and-go/ (accessed 2026-11-13)
[^s4]: T. McGrath et al., "Acquisition of chess knowledge in AlphaZero", *PNAS* 119(47):e2206625119 (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9704706 (accessed 2026-11-13)
[^s5]: Matthew Sadler and Natasha Regan, *Game Changer* (New In Chess, 2019). https://www.newinchess.com/game-changer (accessed 2026-11-13)
