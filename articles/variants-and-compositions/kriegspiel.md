---
id: kt:kriegspiel
type: Variant
title: Kriegspiel
aliases: [Kriegspiel chess, Invisible chess, War game chess]
domain: variants-and-compositions
summary: >-
  A chess variant of hidden information in which each player sees only their own pieces, while a
  referee keeps the true position on a third board, rejects illegal tries and announces only
  limited facts such as captures, checks and available pawn captures.
status: current
volatile: false
verified: 2026-11-18
broader: [kt:chess-variants]
related: [kt:blindfold-chess, kt:arbiter, kt:touch-move, kt:computer-chess, kt:checkmate]
relations:
  - {predicate: developedBy, object: kt:michael-henry-temple}
  - {predicate: usesTechnique, object: kt:monte-carlo-tree-search}
  - {predicate: usesTechnique, object: kt:minimax}
sources:
  - id: s1
    title: "Kriegspiel"
    publisher: "Franco Pratesi (article, naibi.net)"
    url: https://naibi.net/b/047.pdf
    type: publication
    accessed: 2026-11-18
  - id: s2
    title: "Kriegspiel (rules article by David Moeser, J'ADOUBE! The Cincinnati Chess Magazine, 30 March 1977)"
    publisher: The Chess Variant Pages
    url: https://www.chessvariants.org/incinf.dir/kriegspiel2.html
    type: community
    accessed: 2026-11-18
  - id: s3
    title: "Kriegspiel (wild 16) help file"
    publisher: Internet Chess Club
    url: https://www.chessclub.com/help/Kriegspiel
    type: official-project
    accessed: 2026-11-18
  - id: s4
    title: "The dark side of the board: advances in chess Kriegspiel (PhD thesis, Università di Bologna, 2010)"
    publisher: "Gian Piero Favini, Alma Mater Studiorum – Università di Bologna"
    url: https://amsdottorato.unibo.it/id/eprint/2403/1/favini_gianpiero_tesi.pdf
    type: academic
    accessed: 2026-11-18
  - id: s5
    title: "Monte Carlo Tree Search Techniques in the Game of Kriegspiel"
    publisher: "Paolo Ciancarini & Gian Piero Favini, Proceedings of IJCAI 2009, pp. 474–478"
    url: https://www.ijcai.org/Abstract/09/086
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s6
    title: "ICGA Journal paper on representing Kriegspiel states with metapositions"
    publisher: "Paolo Ciancarini & Gian Piero Favini, ICGA Journal 30(1):3–24 (2007)"
    url: https://content.iospress.com/articles/icga-journal/icg30102
    type: peer-reviewed
    accessed: 2026-11-18
created: 2026-11-18
---

# Kriegspiel

Kriegspiel is chess played in the dark. Each player has a board showing only their own pieces, while a referee (often called the umpire) sits between them with a third board holding the true position and the game score.[^s1][^s2] The player to move proposes a move; if it is legal it is played, and if it is not the referee says so and the player must try again.[^s1][^s2] The name, German for "war game", echoes the Prussian military simulation of the same spirit, and the chess version replaces that game's three-board arrangement with a referee who rules on legality.[^s4] Computer scientists often describe it as "invisible chess".[^s5]

## Origins

The chess historian Franco Pratesi attributes the game to the English journalist Michael Henry Temple, who introduced it in London around 1898 at a club meeting in a Fleet Street tavern; Pratesi also notes an earlier recollection of the variant being played at the Hampstead Chess Club in 1890, so the attribution is not beyond doubt.[^s1] The game flourished at The Gambit, a famous London club in Cannon Street where strong English players met, and whose rules were among the strictest.[^s1] The oldest rule set is still called the "English rules".[^s4] After the Second World War the mathematician J. K. Wilkins brought the game to the RAND Corporation, where a faster "RAND" style developed and game theorists such as Lloyd Shapley took an interest.[^s4] In the United States a Cincinnati style, halfway between English and RAND practice, was published in 1977 and later became the basis of the Internet Chess Club's version.[^s2][^s4]

## How it is played

Rule sets differ mainly in what the referee announces.[^s1][^s4] In the Cincinnati and ICC versions the referee says whose turn it is, announces a capture by the square on which it happened and whether a pawn or a piece was taken, and announces check by its direction: rank, file, long diagonal, short diagonal or knight.[^s2][^s3] The referee also tells the side to move how many pawn captures are available ("pawn tries"), without saying where they are.[^s3] An illegal try is reported only to the player who made it, so the opponent learns nothing.[^s3] Promotions and castling are not announced, nor is the material left on the board.[^s2] A player's own pieces are subject to touch-move, while any opposing pieces a player places on their own board as guesses have no standing.[^s2]

The English rules make information cost something. Before moving, a player may ask "Are there any?"; if the referee answers that a pawn capture exists, the player must try one, which limits their choice of move.[^s4] Some rule sets, including the Cincinnati rules, answer a try that the player should know is impossible with "Nonsense", a rule meant to stop players from probing with deliberate illegal moves to mislead an opponent who hears the referee's replies.[^s2][^s4]

## Ideas and pitfalls

Because every try that fails reveals something, a skilled player probes with moves that are useful if they succeed and informative if they fail.[^s4] Capture and check announcements are the main clues: the square of a capture shows where an enemy unit stands, and the direction of a check narrows down which piece is giving it.[^s2][^s3] Pawn-try announcements tell a player that an enemy unit stands diagonally in front of one of their pawns.[^s3] In the endgame the stronger side may be able to force mate with certainty in some positions, while in others it must accept a small risk that the defender escapes into a draw.[^s4] A typical pitfall is to trust one's guesses too much: the board of guessed enemy pieces is only an estimate, and a confident piece move into an unseen attacker can lose material at once.[^s2]

## Computer Kriegspiel

Kriegspiel is hard for programs because the set of positions consistent with what a player knows is enormous; one estimate puts a typical middlegame information set at about 10^27 positions.[^s4] Paolo Ciancarini and Gian Piero Favini at the University of Bologna introduced "metapositions", which merge many possible states into one object so that minimax search can be applied without assuming the opponent always finds the best reply.[^s6] They later showed that Monte Carlo tree search agents needing little game-specific knowledge played significantly better than the strongest minimax-based Kriegspiel program then known.[^s5] Their program, Darkboard, plays under ICC rules, which the Computer Olympiads adopted for their Kriegspiel events.[^s4]

## Connections

Kriegspiel is one of the classic chess variants, keeping the moves of the pieces while hiding information.[^s1][^s4] It differs from blindfold chess, where players know every move but cannot see the board; here the moves themselves are secret.[^s2] It depends on a referee, an extreme form of the arbiter's role, and keeps the touch-move rule for a player's own pieces.[^s2] It is credited to Michael Henry Temple.[^s1] Its computer side links it to computer chess through minimax search over metapositions and Monte Carlo tree search.[^s5][^s6] As in ordinary chess, the object is checkmate.[^s4]

## Sources
[^s1]: Franco Pratesi, "Kriegspiel" (article with Italian and English abstract). https://naibi.net/b/047.pdf (accessed 2026-11-18)
[^s2]: David Moeser, "Kriegspiel", J'ADOUBE! The Cincinnati Chess Magazine (30 March 1977), reproduced by The Chess Variant Pages. https://www.chessvariants.org/incinf.dir/kriegspiel2.html (accessed 2026-11-18)
[^s3]: Internet Chess Club, "Kriegspiel" (wild 16) help file. https://www.chessclub.com/help/Kriegspiel (accessed 2026-11-18)
[^s4]: Gian Piero Favini, "The dark side of the board: advances in chess Kriegspiel", PhD thesis, Università di Bologna (2010). https://amsdottorato.unibo.it/id/eprint/2403/1/favini_gianpiero_tesi.pdf (accessed 2026-11-18)
[^s5]: Paolo Ciancarini and Gian Piero Favini, "Monte Carlo Tree Search Techniques in the Game of Kriegspiel", Proceedings of IJCAI 2009, pp. 474–478. https://www.ijcai.org/Abstract/09/086 (accessed 2026-11-18)
[^s6]: Paolo Ciancarini and Gian Piero Favini, paper on representing Kriegspiel states with metapositions, ICGA Journal 30(1):3–24 (2007). https://content.iospress.com/articles/icga-journal/icg30102 (accessed 2026-11-18)
