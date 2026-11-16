---
id: kt:puzzle-training
type: TrainingMethod
title: Puzzle training
aliases: ["Tactics training", "Tactical puzzles", "Chess puzzles", "Tactics puzzles", "Solving tactics", "Tactics trainer"]
domain: training-and-improvement
summary: >-
  Practising chess by solving positions with a forcing, clear-cut solution, usually tactics taken
  from real games; online sites rate both puzzles and solvers, and methods such as repeated cycles of
  the same set aim to turn calculation into fast pattern recognition.
fen: "6k1/5ppp/8/8/8/8/r4PPP/4R1K1 w - - 0 1"
status: current
volatile: true
verified: 2026-11-16
broader: [kt:deliberate-practice, kt:chess-tactics]
related: [kt:calculation, kt:chunking-theory, kt:einstellung-effect, kt:visualization, kt:chess-problems]
relations:
  - {predicate: usesTechnique, object: kt:calculation}
  - {predicate: hasPart, object: kt:woodpecker-method}
  - {predicate: exemplifiedBy, object: kt:back-rank-mate}
  - {predicate: contrastsWith, object: kt:chess-problems}
sources:
  - id: s1
    title: "New puzzles are here!"
    publisher: Lichess
    url: https://lichess.org/blog/X-S6gRUAAGjNX4ki/new-puzzles-are-here
    type: official-project
    accessed: 2026-11-16
  - id: s2
    title: "lichess.org open database: Puzzles"
    publisher: Lichess
    url: https://database.lichess.org/
    type: official-project
    accessed: 2026-11-16
  - id: s3
    title: "Chess and games (Cambridge Handbook of Expertise and Expert Performance, pp. 523-538)"
    publisher: Fernand Gobet and Neil Charness, via CORE
    url: https://core.ac.uk/download/334186.pdf
    type: academic
    accessed: 2026-11-16
  - id: s4
    title: "A psychometric analysis of chess expertise (American Journal of Psychology 118, 29-60)"
    publisher: Han L. J. van der Maas and Eric-Jan Wagenmakers, University of Amsterdam Digital Academic Repository
    url: https://dare.uva.nl/id/44227bd6-730b-4f8d-885d-6c7d08d1eebf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s5
    title: "Not All Practice Is Created Equal: Longitudinal Evidence From Over 40,000 Chess Players (Psychological Science 37(7), 514-523)"
    publisher: Daniel A. Southwick, Kyle W. Harwell, Garrett Wright, Joseph A. Olsen and Benjamin M. Ogles, via CiteDrive
    url: https://www.citedrive.com/en/discovery/not-all-practice-is-created-equal-longitudinal-evidence-from-over-40000-chess-players/
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s6
    title: "The Woodpecker Method"
    publisher: Axel Smith and Hans Tikkanen, Quality Chess (New in Chess shop page)
    url: https://newinchess.com/the-woodpecker-method
    type: book
    accessed: 2026-11-16
created: 2026-11-16
---

# Puzzle training

Puzzle training means improving at chess by solving positions that have a forcing, clear-cut solution, most often a tactic that arose in a real game. It differs from composed chess problems, which are artistic constructions with stipulations such as "mate in two"; a training puzzle simply asks the solver to find the best continuation from a practical position. Online, the largest open collection is Lichess's: as of November 2026 its database lists 6,193,530 rated and tagged puzzles, released under a CC0 licence.[^s2]

## How modern puzzle sets are made

Lichess built its set by scanning about 600 million games from its own site and re-checking promising positions with Stockfish NNUE at 40 meganodes, a job the project says took more than 100 years of CPU time.[^s2] The aim was puzzles with one crystal-clear solution: in the published file every move the solver must find is an only move, except that any checkmate in one is accepted.[^s2] Each puzzle starts one move earlier, with the opponent's move, so the solver sees how the chance arose, as in a game.[^s2]

Difficulty is handled by rating rather than by hand. Lichess treats every attempt as a Glicko-2 rated game between the solver and the puzzle, so both ratings move after each try; themed sessions award fewer points because the theme is itself a hint.[^s1] Players vote on puzzle quality and on theme tags such as forks or rook endgames, and the votes refine the tags and a popularity score.[^s1][^s2]

## Why it works

The research case rests on pattern recognition. Studies summarised by Gobet and Charness show that experts find good moves faster than weaker players rather than searching much deeper: in de Groot's classic think-aloud study grandmasters and experts looked about as deep, but grandmasters chose better moves and decided sooner.[^s3] Eye-tracking work found that experts take in chess relations across the board in parallel, while weaker players encode them one at a time.[^s3] Solving many positions is a way of stocking memory with such patterns, which is why puzzles fit the "serious study" that predicts rating.[^s3]

Choose-the-best-move items are also a good measure of strength. The Amsterdam Chess Test, whose tasks include choosing a move in set positions, proved very reliable and predicted Elo rating well, and adding solution speed to the score made it more valid still, especially on easy items.[^s4] Being quick and accurate on puzzles thus goes together with playing strength.[^s4]

## Methods and how to use them

A well-known structured approach is the Woodpecker Method, developed by Hans Tikkanen and named by his co-author Axel Smith: the trainee solves a large set of puzzles, then re-solves the same set repeatedly and faster. The book has over 1,100 exercises, and the publisher credits it with Tikkanen's three grandmaster norms in seven weeks in 2010.[^s6] The idea is to turn patterns that first need calculation into instant recognition.[^s6] A simple illustration is the key position above: White plays Re8, which is mate because Black's own pawns on f7, g7 and h7 block the king's escape (a back-rank mate). Spotting such motifs in a second is what repetition aims to train.[^s6]

## Pitfalls

Puzzles tell you a tactic exists; games do not. A known weakness of pattern knowledge is that strong players tend to grab the stereotyped solution and can miss shorter but unusual ones, which Saariluoma found in tactical positions.[^s3] Puzzle rating is also not the same as playing strength, and rushing for points rewards guessing over full calculation. A 2026 study of 44,213 Chess.com players found deliberate-practice activities about 3.61 times as efficient as playing games for rating gains, but not all such activities were equally effective, so how puzzles are used matters as much as how many are solved.[^s5] Good habits are to calculate to the end before moving, review failed puzzles, and pair solving with playing and analysing your own games.[^s5][^s3]

## Connections

Puzzle training is a form of deliberate practice aimed at chess tactics, and it exercises calculation and visualization.[^s3][^s5] Its explanation in memory research is chunking theory, and its blind spot is the Einstellung effect, the pull of familiar solutions.[^s3] The Woodpecker Method is one structured version of it.[^s6] It contrasts with chess problems, which are composed rather than taken from play; puzzle sets instead tag motifs from real games, such as forks, and the back-rank mate is a typical one.[^s1][^s2]

## Sources

[^s1]: Lichess, "New puzzles are here!". https://lichess.org/blog/X-S6gRUAAGjNX4ki/new-puzzles-are-here (accessed 2026-11-16)
[^s2]: Lichess, "lichess.org open database", Puzzles section. https://database.lichess.org/ (accessed 2026-11-16)
[^s3]: Gobet, F. & Charness, N. (2006), "Chess and games", in *The Cambridge Handbook of Expertise and Expert Performance*, Cambridge University Press, 523-538. https://core.ac.uk/download/334186.pdf (accessed 2026-11-16)
[^s4]: van der Maas, H. L. J. & Wagenmakers, E.-J. (2005), "A psychometric analysis of chess expertise", *American Journal of Psychology* 118(1), 29-60. https://dare.uva.nl/id/44227bd6-730b-4f8d-885d-6c7d08d1eebf (accessed 2026-11-16)
[^s5]: Southwick, D. A., Harwell, K. W., Wright, G., Olsen, J. A. & Ogles, B. M. (2026), "Not All Practice Is Created Equal: Longitudinal Evidence From Over 40,000 Chess Players", *Psychological Science* 37(7), 514-523. https://www.citedrive.com/en/discovery/not-all-practice-is-created-equal-longitudinal-evidence-from-over-40000-chess-players/ (accessed 2026-11-16)
[^s6]: Smith, A. & Tikkanen, H. (2018), *The Woodpecker Method*, Quality Chess. https://newinchess.com/the-woodpecker-method (accessed 2026-11-16)
