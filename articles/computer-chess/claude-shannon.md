---
id: kt:claude-shannon
type: Person
title: Claude Shannon
aliases: [Claude E. Shannon, Claude Elwood Shannon, C. E. Shannon]
domain: computer-chess
summary: >-
  American mathematician and engineer (1916–2001), founder of information theory, whose 1950 paper
  "Programming a Computer for Playing Chess" set out the minimax search, evaluation function and
  Type A / Type B strategies on which chess programs have been built ever since.
status: historical
volatile: false
verified: 2026-11-08
broader: [kt:history-of-computer-chess, kt:computer-chess]
related: [kt:minimax, kt:evaluation-function, kt:game-tree-search, kt:quiescence-search, kt:horizon-effect]
relations:
  - {predicate: influencedBy, object: kt:leonardo-torres-y-quevedo}
sources:
  - id: s1
    title: "Programming a Computer for Playing Chess (Philosophical Magazine, 1950), full text"
    publisher: Claude E. Shannon, reproduced by Fermat's Library
    url: https://fermatslibrary.com/s/programming-a-computer-for-playing-chess
    type: primary-record
    accessed: 2026-11-08
  - id: s2
    title: "Claude Shannon"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/print/article/538577
    type: reference
    accessed: 2026-11-08
  - id: s3
    title: "Shannon and Lasker at Shannon's chess machine"
    publisher: Computer History Museum (Mastering the Game exhibit)
    url: https://www.computerhistory.org/chess/stl-430b9bbe92716/
    type: archive
    accessed: 2026-11-08
  - id: s4
    title: "A Chess-Playing Machine (Scientific American, February 1950), author listing"
    publisher: Scientific American
    url: https://www.scientificamerican.com/author/claude-e-shannon
    type: publication
    accessed: 2026-11-08
created: 2026-11-08
---

# Claude Shannon

Claude Elwood Shannon (born 30 April 1916 in Petoskey, Michigan; died 24 February 2001 in Medford, Massachusetts) was an American mathematician and electrical engineer best known as the founder of information theory.[^s2] For chess he matters as the author of the first technical blueprint for a chess-playing program: almost every idea a modern engine programmer takes for granted, from minimax search to a weighted evaluation of material and pawn structure, appears in his 1950 paper.[^s1]

## Career outside chess

Shannon graduated from the University of Michigan in 1936 with degrees in mathematics and electrical engineering, and in 1940 earned a master's degree and a doctorate at MIT. Britannica describes his master's thesis, *A Symbolic Analysis of Relay and Switching Circuits*, as laying the theoretical basis of digital circuits through Boolean algebra.[^s2] He joined Bell Labs in 1941, published "A Mathematical Theory of Communication" in 1948 (the paper that founded information theory and appears to be the first to use the word *bit* in print), and later taught at MIT, becoming professor emeritus in 1978.[^s2] Britannica also lists cryptography and chess-playing computers among the subjects of his influential papers, alongside a long series of playful mechanical inventions.[^s2]

## The 1950 chess paper

"Programming a Computer for Playing Chess" was first presented at the National IRE Convention in New York on 9 March 1949 and published in *Philosophical Magazine* in March 1950, with Shannon writing from Bell Telephone Laboratories in Murray Hill, New Jersey.[^s1] A popular version, "A Chess-Playing Machine", appeared in *Scientific American* in February 1950 and posed the question of whether such computers could be said to think.[^s4]

Shannon did not treat chess as an end in itself. He presented it as a wedge into harder problems such as designing switching circuits, routing telephone calls, translation and strategic decisions, and argued that chess suits the purpose because its rules and goal are sharply defined, it is neither trivial nor hopelessly hard, and its discrete board fits a digital machine.[^s1]

The paper's key contributions are:

- **Minimax on a depth-limited tree.** White chooses the move that maximises an evaluation after Black's best (minimising) reply, applied to a look-ahead of fixed length.[^s1]
- **An evaluation function f(P).** Shannon's rough formula weighted king 200, queen 9, rook 5, bishop and knight 3, pawn 1, subtracted half a point for each doubled, backward or isolated pawn, and added a tenth of a point per unit of mobility, with further factors such as passed pawns and rooks on open files listed in an appendix.[^s1]
- **Type A and Type B strategies.** A Type A program searches every variation to a fixed depth; Shannon estimated that even three moves deep it would need about 10^9 evaluations, over 16 minutes per move, and would misjudge positions in the middle of exchanges. A Type B program instead evaluates only quiet positions, follows forcing lines further, and uses a move-ranking function to discard poor candidates.[^s1]

## A worked example: the game-tree estimate

Shannon's best-known number comes from simple arithmetic. With about 30 legal moves in a typical position, one move by each side gives roughly 30 × 30 ≈ 10^3 possibilities; a typical game of about 40 such move pairs therefore yields around (10^3)^40 = 10^120 variations from the starting position.[^s1] At one variation per microsecond, calculating the first move this way would take more than 10^90 years, and a lookup table is ruled out because he put the number of possible positions at about 10^43.[^s1] The conclusion, which every engine still lives with, is that a program must search selectively and estimate rather than calculate to the end.

## Machines and limits

Shannon credited Leonardo Torres y Quevedo's 1914 machine, which mated with king and rook against king, as an honest early attempt, because it tackled a sub-problem with explicit rules.[^s1] A Computer History Museum photograph from about 1950 shows Shannon with the chess master Edward Lasker at MIT, at a relay-based chess machine Shannon had built.[^s3] Shannon was candid about weaknesses: his program would not learn from its mistakes, and he only sketched how a higher-level routine might tune evaluation coefficients from results.[^s1]

## Connections

Shannon's paper is the starting point of the **history of computer chess** and of **computer chess** as a field.[^s1] It formulated depth-limited **minimax** over a **game tree**, the first explicit chess **evaluation function**, and, through the Type B idea of evaluating only quiescent positions, the ancestor of **quiescence search**; his warning about misjudging positions in mid-exchange anticipates the **horizon effect**.[^s1] He acknowledged **Leonardo Torres y Quevedo**'s endgame machine as a predecessor.[^s1]

## Sources
[^s1]: C. E. Shannon, "Programming a Computer for Playing Chess", *Philosophical Magazine* Ser. 7, 41 (314), March 1950; full text at Fermat's Library. https://fermatslibrary.com/s/programming-a-computer-for-playing-chess (accessed 2026-11-08)
[^s2]: Encyclopaedia Britannica, "Claude Shannon". https://www.britannica.com/print/article/538577 (accessed 2026-11-08)
[^s3]: Computer History Museum, "Shannon and Lasker at Shannon's chess machine", Mastering the Game. https://www.computerhistory.org/chess/stl-430b9bbe92716/ (accessed 2026-11-08)
[^s4]: Scientific American, "A Chess-Playing Machine" (February 1950), Claude E. Shannon author page. https://www.scientificamerican.com/author/claude-e-shannon (accessed 2026-11-08)
