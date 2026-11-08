---
id: kt:computer-chess
type: Concept
title: Computer chess
aliases: [Chess programming, Chess engines, Machine chess]
domain: computer-chess
summary: >-
  The design and study of machines and programs that play or analyse chess, from early mechanical
  and electromechanical devices through search-based programs to today's neural-network engines,
  and the effects those programs have had on human play, preparation and endgame knowledge.
fen: "8/8/8/8/3k4/8/8/R3K3 w - - 0 1"
status: current
volatile: false
verified: 2026-11-08
broader: [kt:artificial-intelligence]
related: [kt:history-of-computer-chess, kt:claude-shannon, kt:deep-blue-versus-kasparov, kt:endgame-tablebases, kt:stockfish, kt:leela-chess-zero]
relations:
  - {predicate: hasPart, object: kt:game-tree-search}
  - {predicate: hasPart, object: kt:evaluation-function}
  - {predicate: usesTechnique, object: kt:alpha-beta-pruning}
  - {predicate: usesTechnique, object: kt:monte-carlo-tree-search}
  - {predicate: usesTechnique, object: kt:nnue}
sources:
  - id: s1
    title: "Chess: Chess and artificial intelligence"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/chess/Chess-and-artificial-intelligence
    type: reference
    accessed: 2026-11-08
  - id: s2
    title: "Mastering the Game: A History of Computer Chess — Introduction"
    publisher: Computer History Museum
    url: https://www.computerhistory.org/chess/introduction/
    type: archive
    accessed: 2026-11-08
  - id: s3
    title: "Mastering the Game: A History of Computer Chess — Chess for Everyone"
    publisher: Computer History Museum
    url: https://www.computerhistory.org/chess/chess-for-everyone/
    type: archive
    accessed: 2026-11-08
  - id: s4
    title: "Introducing NNUE Evaluation (7 August 2020)"
    publisher: The Stockfish developers
    url: https://stockfishchess.org/blog/2020/introducing-nnue-evaluation/
    type: official-project
    accessed: 2026-11-08
  - id: s5
    title: "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (arXiv:1712.01815, December 2017)"
    publisher: D. Silver et al., DeepMind, via arXiv (ar5iv full text)
    url: https://ar5iv.labs.arxiv.org/html/1712.01815
    type: academic
    accessed: 2026-11-08
  - id: s6
    title: "What is Lc0?"
    publisher: The Leela Chess Zero project
    url: https://lczero.org/dev/wiki/what-is-lc0
    type: official-project
    accessed: 2026-11-08
created: 2026-11-08
---

# Computer chess

Computer chess is the field concerned with building machines and programs that play or analyse chess. The Computer History Museum presents its first fifty years, roughly 1945 to 1997, as a long effort on a hard intellectual problem that ran in step with general advances in hardware and software and produced many software techniques along the way.[^s2] For today's club player the field matters mainly through its products: engines that analyse positions, check opening preparation and settle endgames far beyond human calculation.[^s1]

## Before programs

Interest in chess machines is older than the computer. The Turk, built by Wolfgang von Kempelen in 1770, toured courts and fairs for decades before being exposed as a magic trick with a hidden operator.[^s2] The first genuine automaton was Leonardo Torres y Quevedo's electromagnetic device of 1890, which could mate with king and rook against a lone king, though it sometimes needed around fifty moves where a human would need fewer than twenty.[^s1] Its task is the one in the key position above: White's king and rook against Black's king, a mate any club player learns early.

## How a chess program works

Britannica credits Alan Turing with a simple program around 1947 that looked only one move ahead, and Claude Shannon with setting out the criteria for judging positions that later programmers followed.[^s1] The two ingredients have stayed the same since. A **search** looks ahead through possible moves, and the numbers grow fast: about 900 positions for two plies from a typical middlegame position and about 27,000 for three, against the roughly 50 a human is estimated to examine.[^s1] An **evaluation** scores the positions at the end of the search; Turing's counted material, while Shannon added positional factors such as pawn structure, central control, mobility and rooks on open files or the seventh rank, each of which had to be turned into numbers.[^s1] Britannica cites an estimate that each extra half-move of search was worth about 250 rating points, which explains why speed dominated the field for decades.[^s1]

## From laboratory to living room

Early milestones came from universities and laboratories. Richard Greenblatt's MacHack VI played in a US Chess Federation tournament in 1967, and Northwestern University's Chess 3.0 won the first American computer championship in 1970.[^s1] Until the mid-1970s only people with access to expensive institutional machines could play a computer; microprocessors changed that, first through hobbyists sharing programs in clubs and magazines and then through commercial products.[^s3] By the mid-1980s, according to the museum, microprocessor programs were beating supercomputer programs in tournaments and scoring wins against top players.[^s3]

Special-purpose hardware drove the top end. Carnegie Mellon's HiTech, with one chip per square, beat grandmaster Arnold Denker in a short match in 1988, and the same year Deep Thought beat Bent Larsen in a tournament game.[^s1] Its successor Deep Blue lost to Garry Kasparov in 1996 and won the 1997 rematch, reportedly searching about 200 million positions per second.[^s1]

## The neural-network era

In 2017 DeepMind's AlphaZero paper described a single algorithm that started from random play, knew nothing but the rules, and reached superhuman strength in chess, shogi and Go within 24 hours of self-play training.[^s5] That broke with the tradition of hand-tuned evaluation functions refined by experts over decades.[^s5] The open project Leela Chess Zero followed the same approach; its engine is guided by a trained network and runs best on a powerful GPU rather than the CPU that traditional engines use.[^s6] Classical engines answered by absorbing the idea: in August 2020 Stockfish added an efficiently updatable neural network (NNUE) evaluation, first developed for shogi, which its developers measured at more than 80 Elo stronger than the hand-crafted evaluation while still running on ordinary CPUs inside an alpha-beta search.[^s4]

## Effects on human chess

Programs became serious professional tools by the 1990s, first for analysing adjourned games and then for testing preparation; Kasparov checked a rook-sacrifice idea for his 1995 title match on a computer.[^s1] In 1993 the International Correspondence Chess Federation accepted that computer use in postal chess could not be controlled.[^s1] Ken Thompson's retrograde endgame analysis of 1986 overturned accepted judgements, showing for example that king and two bishops beat king and knight in most positions, an ending long thought drawn.[^s1] The practical pitfall for a club player is to treat an engine's number as understanding: a program's verdict is only as good as its search and evaluation, and the useful work is finding out why it prefers a move.[^s1][^s6]

## Connections

Computer chess is a branch of **artificial intelligence** research and is built from two parts with their own nodes, **game-tree search** and the **evaluation function**.[^s1] Classical engines search with **alpha-beta pruning**; AlphaZero replaced it with a general-purpose **Monte Carlo tree search** guided by its network, an approach followed by **Leela Chess Zero**, while **Stockfish** has since 2020 paired alpha-beta search with **NNUE**.[^s4][^s5][^s6] Its founding ideas come from **Claude Shannon**, its best-known event is **Deep Blue versus Kasparov**, Thompson's work leads to **endgame tablebases**, and the chronology is treated in **history of computer chess**.[^s1][^s2]

## Sources
[^s1]: Encyclopaedia Britannica, "Chess: Chess and artificial intelligence". https://www.britannica.com/topic/chess/Chess-and-artificial-intelligence (accessed 2026-11-08)
[^s2]: Computer History Museum, *Mastering the Game: A History of Computer Chess*, "Introduction". https://www.computerhistory.org/chess/introduction/ (accessed 2026-11-08)
[^s3]: Computer History Museum, *Mastering the Game: A History of Computer Chess*, "Chess for Everyone". https://www.computerhistory.org/chess/chess-for-everyone/ (accessed 2026-11-08)
[^s4]: The Stockfish developers, "Introducing NNUE Evaluation" (7 August 2020). https://stockfishchess.org/blog/2020/introducing-nnue-evaluation/ (accessed 2026-11-08)
[^s5]: D. Silver et al., "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm", arXiv:1712.01815 (December 2017). https://ar5iv.labs.arxiv.org/html/1712.01815 (accessed 2026-11-08)
[^s6]: Leela Chess Zero project, "What is Lc0?". https://lczero.org/dev/wiki/what-is-lc0 (accessed 2026-11-08)
