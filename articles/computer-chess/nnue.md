---
id: kt:nnue
type: Algorithm
title: NNUE
aliases: [Efficiently updatable neural network, Efficiently updateable neural network, ƎUИИ, NNUE evaluation]
domain: computer-chess
summary: >-
  An efficiently updatable neural network: a small, integer-quantized evaluation network with sparse
  inputs whose first layer is updated incrementally after each move, invented for computer shogi by
  Yu Nasu and adopted by Stockfish in 2020 to replace hand-written evaluation inside alpha-beta search.
fen: "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"
status: current
volatile: true
verified: 2026-11-12
broader: [kt:evaluation-function]
related: [kt:stockfish, kt:leela-chess-zero, kt:game-tree-search]
relations:
  - {predicate: developedBy, object: kt:yu-nasu}
  - {predicate: enables, object: kt:alpha-beta-pruning}
  - {predicate: contrastsWith, object: kt:alphazero}
sources:
  - id: s1
    title: "Introducing NNUE Evaluation (7 August 2020)"
    publisher: The Stockfish developers (stockfishchess.org)
    url: https://stockfishchess.org/blog/2020/introducing-nnue-evaluation/
    type: official-project
    accessed: 2026-11-12
  - id: s2
    title: "NNUE (nnue-pytorch documentation)"
    publisher: The Stockfish developers (official-stockfish.github.io)
    url: https://official-stockfish.github.io/docs/nnue-pytorch-wiki/docs/nnue.html
    type: official-project
    accessed: 2026-11-12
  - id: s3
    title: "NNUE architecture history (nnue-pytorch documentation)"
    publisher: The Stockfish developers (official-stockfish.github.io)
    url: https://official-stockfish.github.io/docs/nnue-pytorch-wiki/docs/nnue_architecture_history.html
    type: official-project
    accessed: 2026-11-12
  - id: s4
    title: "Stockfish 16.1 (24 February 2024)"
    publisher: The Stockfish developers (stockfishchess.org)
    url: https://stockfishchess.org/blog/2024/stockfish-16-1/
    type: official-project
    accessed: 2026-11-12
  - id: s5
    title: "Neural Networks for Chess (2022), section 4.6"
    publisher: Dominik Klein, arXiv:2209.01506
    url: https://arxiv.org/pdf/2209.01506
    type: academic
    accessed: 2026-11-12
created: 2026-11-12
---

# NNUE

**NNUE** ("efficiently updatable neural network", sometimes written backwards as ƎUИИ) is a neural-network design for evaluating positions inside a classical alpha-beta search. It was invented for computer shogi by Yu Nasu, integrated into the shogi engine YaneuraOu by Motohiro Isozaki in May 2018, and ported to chess for Stockfish by Hisayori Noda in June 2019.[^s2] Stockfish merged NNUE into its main repository on 6 August 2020, where it initially ran alongside the hand-written evaluation.[^s1] With Stockfish 16.1 (February 2024) the handcrafted evaluation was removed entirely, so Stockfish's evaluation has since been purely neural.[^s4]

## Why it exists

An alpha-beta engine evaluates millions of positions per second, so its evaluation function has to be extremely cheap. The large deep networks behind AlphaZero-style engines need GPUs or TPUs and are paired with a much slower, more selective search; NNUE was designed instead to run on an ordinary home CPU fast enough to sit inside a conventional search.[^s5] The Stockfish documentation states the design goal as millions of evaluations per second per thread, with no batching and no accelerator hardware.[^s2]

## How it works

The trick rests on three properties. First, the inputs are **sparse**: of tens of thousands of possible input features, only a few dozen are active in any position (the documentation puts sparsity at roughly 0.1%). Second, the inputs **change little between positions**: a typical move switches off a few features and switches on a few others. Third, the network is small enough to be computed in **low-precision integer arithmetic**.[^s2]

Because of the first two properties, the output of the large first layer can be kept as a running sum, the **accumulator**. When a move adds a feature, the engine adds that feature's weight column to the accumulator; when it removes one, it subtracts it. Only the remaining small layers are computed from scratch at each node.[^s2] Klein's textbook implementation does exactly this with 16-bit SIMD add and subtract instructions.[^s5]

The classic input encoding, **HalfKP**, describes each piece by its square and type *relative to the square of one side's king*: (king square, piece square, piece type, piece colour), kings excluded, giving 64 × 64 × 5 × 2 = 40,960 features per side. Each side has its own accumulator, and they are concatenated with the side to move first, so the network can learn the value of having the move. The cost of tying features to the king is that a king move changes all of that side's features, forcing a full recomputation of its accumulator rather than an incremental update.[^s2]

Arithmetic is quantized: Stockfish uses 16-bit integer accumulators and 8-bit weights and activations, with clipped-ReLU activations clamped to a small range, so that wide vector instructions such as AVX2 can process many values at once.[^s2] Networks are trained on positions labelled with scores from a strong engine searching to moderate depth; Stockfish's first networks used evaluations of millions of positions, and later training also drew on Leela Chess Zero self-play data.[^s1][^s5]

## Example

In the diagram position, after 1.e4, take White's HalfKP perspective. The king is still on e1, so the only change is that the feature "king e1, white pawn on e2" switches off and "king e1, white pawn on e4" switches on. White's accumulator is updated by one subtraction and one addition of weight columns instead of re-summing all 30 non-king pieces; had White played a king move instead, that whole half would be rebuilt.[^s2]

## Impact and evolution

When it was introduced, Stockfish's own testing framework measured NNUE at roughly 90 Elo stronger than the classical evaluation in fast games (92.8 ± 2.1 Elo over 60,000 games at 10+0.1 on one thread).[^s1] Since then the architecture has been revised many times. The project's history lists the first design as the "Stockfish 12 architecture" (August 2020) and a long sequence of successors that widened the first layer from 1,024 to 3,072 neurons by 2024; from November 2025 new "threat" input features were added and the first layer cut back to 1,024. As of November 2026 the current revision is the seventeenth (SFNNv17, from September 2026).[^s3] Stockfish 16.1 also introduced a second, smaller network used for quickly judging positions that are easily decided.[^s4]

A common misunderstanding is that NNUE engines are "neural engines" in the AlphaZero sense. They are not: the search is still alpha-beta with all its classical enhancements, and only the evaluation function changed.[^s5]

## Connections

NNUE is a kind of **evaluation function**, sitting inside **game-tree search**; it is what lets **alpha-beta pruning** keep its speed while gaining a learned evaluation.[^s5] It was **developed by Yu Nasu** for shogi and is best known through **Stockfish**, which adopted it in 2020.[^s2][^s1] It **contrasts with** the AlphaZero approach and **Leela Chess Zero**, whose much larger networks need GPUs or TPUs, although Leela's self-play data has been used to train Stockfish's networks.[^s5]

## Sources
[^s1]: The Stockfish developers, "Introducing NNUE Evaluation" (7 August 2020). https://stockfishchess.org/blog/2020/introducing-nnue-evaluation/ (accessed 2026-11-12)
[^s2]: The Stockfish developers, "NNUE", nnue-pytorch documentation. https://official-stockfish.github.io/docs/nnue-pytorch-wiki/docs/nnue.html (accessed 2026-11-12)
[^s3]: The Stockfish developers, "NNUE architecture history", nnue-pytorch documentation. https://official-stockfish.github.io/docs/nnue-pytorch-wiki/docs/nnue_architecture_history.html (accessed 2026-11-12)
[^s4]: The Stockfish developers, "Stockfish 16.1" (24 February 2024). https://stockfishchess.org/blog/2024/stockfish-16-1/ (accessed 2026-11-12)
[^s5]: Dominik Klein, *Neural Networks for Chess* (2022), section 4.6, arXiv:2209.01506. https://arxiv.org/pdf/2209.01506 (accessed 2026-11-12)
