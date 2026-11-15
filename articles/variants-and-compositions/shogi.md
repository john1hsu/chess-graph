---
id: kt:shogi
type: Variant
title: Shogi
aliases: [Japanese chess, Shōgi, Shougi, 将棋]
domain: variants-and-compositions
summary: >-
  The Japanese member of the chess family, played on a 9×9 board with twenty pieces a side, in
  which captured pieces join the captor's hand and may later be dropped back onto the board.
status: current
volatile: true
verified: 2026-11-15
broader: [kt:chess-variants]
related: [kt:crazyhouse, kt:xiangqi, kt:alphazero, kt:nnue, kt:pawn-promotion]
relations:
  - {predicate: contrastsWith, object: kt:chess}
  - {predicate: sanctionedBy, object: kt:federation-of-european-shogi-associations}
sources:
  - id: s1
    title: "Shogi (summary)"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/summary/shogi
    type: reference
    accessed: 2026-11-15
  - id: s2
    title: "Shogi official playing rules (adopted 4 August 2017)"
    publisher: Federation of European Shogi Associations (FESA)
    url: https://fesashogi.eu/rules/
    type: governing-body
    accessed: 2026-11-15
  - id: s3
    title: "The rules of shogi (GNU Shogi manual)"
    publisher: GNU Project
    url: https://gnu.org/software/gnushogi/manual/The-rules-of-shogi.html
    type: community
    accessed: 2026-11-15
  - id: s4
    title: "Computer Shogi 2000 through 2004"
    publisher: "Takenobu Takizawa, Waseda University Repository"
    url: https://core.ac.uk/download/286924113.pdf
    type: academic
    accessed: 2026-11-15
  - id: s5
    title: "A System-Design Outline of the Distributed-Shogi-System Akara 2010"
    publisher: "Hoki, Yokoyama, Yamashita, Kaneko, Obata, Tsuruoka & Ito, SNPD 2013 (IEEE/ACIS)"
    url: https://ginza.tkl.iis.u-tokyo.ac.jp/new/uploads/publication_file/file/614/06598505.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s6
    title: "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (arXiv:1712.01815)"
    publisher: "D. Silver et al., DeepMind"
    url: https://ar5iv.arxiv.org/html/1712.01815
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s7
    title: "Neural Networks for Chess (arXiv:2209.01506)"
    publisher: "Dominik Klein"
    url: https://arxiv.org/pdf/2209.01506
    type: academic
    accessed: 2026-11-15
created: 2026-11-15
---

# Shogi

**Shogi** is the chess game of Japan, a two-player game that developed there between the eighth and twelfth centuries. Westerners often call it "Japanese chess", but its rules differ substantially from the Western game.[^s1] It is played on a 9×9 board of uncoloured squares with flat, wedge-shaped pieces of a single colour; ownership is shown by the direction the wedge points, and each piece carries its name on both faces so that it can be flipped when it promotes.[^s1][^s3] Its most distinctive rule is the **drop**: a captured piece is not removed from play but goes into the captor's hand, and may later be placed back on an empty square as a move.[^s1][^s3]

## Pieces and moves

Each side has twenty pieces of eight kinds, and Black (sente) moves first.[^s3] The king moves one square in any direction, and the rook and bishop move as in chess. The other pieces are mostly short-range and forward-leaning: the gold general steps one square orthogonally or diagonally forward; the silver general steps one square diagonally or straight forward; the lance slides any distance straight ahead; the pawn moves and captures one square straight forward, with no double step and no en passant.[^s3] The knight is the only jumper, landing two squares forward and one to the side, so it can only ever go forward.[^s2] There is no queen.[^s4]

## Promotion and drops

The promotion zone is the three ranks nearest the opponent. Rook, bishop, silver, knight, lance and pawn may promote when a move begins, ends or passes within that zone; promotion is optional unless the piece would otherwise have no legal move again, as with a pawn or lance on the last rank or a knight on the last two.[^s2][^s3] Silver, knight, lance and pawn all promote to the move of a gold general (a promoted pawn is a *tokin*), the rook becomes a dragon (adding one-step diagonal moves) and the bishop a horse (adding one-step orthogonal moves); kings and golds never promote.[^s3] A captured piece loses its promotion when it goes into hand, and a dropped piece always enters the board unpromoted, even inside the zone.[^s2][^s3]

Drops take a full turn and have three restrictions: no pawn on a file that already holds one of your own unpromoted pawns (*nifu*); no pawn, lance or knight on a square from which it could never move; and no pawn drop that gives immediate checkmate, although moving a pawn already on the board to mate is legal.[^s2][^s3] Drops are a common way to block a long-range check.[^s3]

## How games end

The aim is to checkmate the king, but in practice most games end by resignation.[^s3] Because material is never permanently lost, draws are rare: Takizawa put them at under 1% of professional games, and the GNU Shogi manual at about 1–2%.[^s3][^s4] A fourfold repetition of the same position, pieces in hand included, is a draw (*sennichite*), but a player may not force one with continuous checks.[^s2][^s3] When both kings have entered the enemy camp and cannot be mated (an impasse, *jishogi*), the result is settled by counting material, with rook and bishop worth five points and other pieces one; as of November 2026 FESA's tournament rules use a 27-point declaration system, while older descriptions give a 24-point threshold.[^s2][^s3] Under FESA rules an illegal move does not end the game by itself; the opponent must claim the win.[^s2]

## For chess players

The drop turns every exchange into an investment. A piece traded off is not gone; it is a resource that can reappear next to the king. A short example of the most common trap for newcomers: with the enemy king boxed in, dropping a pawn in front of it to deliver mate is illegal, so the attacker must mate with a different drop or with a piece already on the board.[^s2][^s3] Likewise a player who already has an unpromoted pawn on a file cannot drop a second pawn there to block a lance or rook on that file.[^s2] Handicap games, in which the stronger player removes pieces before play begins, are a normal part of teaching shogi.[^s3]

## Computer shogi

The drop rule makes the game tree much wider than in chess: the average number of legal moves is about 80 in shogi against about 35 in chess, and can exceed 200 in endgames.[^s4][^s5] The first shogi program was written in November 1974, the Computer Shogi Association was founded in 1986, and its first championship was held on 2 December 1990.[^s4] Machine-learned evaluation functions spread through the field after the program Bonanza used them successfully, and on 11 October 2010 the distributed system Akara 2010 beat the female professional Ichiyo Shimizu, described by its authors as the first public win by a shogi machine over a professional.[^s5] In DeepMind's 2017 preprint, AlphaZero outperformed Elmo, the 2017 Computer Shogi Association champion, after less than two hours of training and then won 90, drew 2 and lost 8 in a 100-game match.[^s6] The NNUE evaluation network now used in chess engines was proposed by Yu Nasu in 2018 for shogi and later ported back to Stockfish.[^s7]

## Connections

Shogi belongs under the family of **chess variants** and contrasts with **chess** in board size, piece set and above all the recycling of captured material.[^s1][^s4] Its drop rule is the one that **crazyhouse** grafts onto Western chess, and its optional, zone-based promotion is a broader cousin of chess **pawn promotion**, applying to six of its eight piece types.[^s2][^s3] **Xiangqi**, Chinese chess, is a neighbouring node in the same family. In computing, shogi was a proving ground for **AlphaZero** and the birthplace of **NNUE**.[^s6][^s7] Outside Japan, tournament play in Europe is regulated by the **Federation of European Shogi Associations**.[^s2]

## Sources
[^s1]: Encyclopaedia Britannica, "Shogi" (summary). https://www.britannica.com/summary/shogi (accessed 2026-11-15)
[^s2]: Federation of European Shogi Associations, "Shogi official playing rules" (adopted 4 August 2017). https://fesashogi.eu/rules/ (accessed 2026-11-15)
[^s3]: GNU Project, "The rules of shogi", GNU Shogi manual. https://gnu.org/software/gnushogi/manual/The-rules-of-shogi.html (accessed 2026-11-15)
[^s4]: T. Takizawa, "Computer Shogi 2000 through 2004", Waseda University Repository. https://core.ac.uk/download/286924113.pdf (accessed 2026-11-15)
[^s5]: K. Hoki, D. Yokoyama, H. Yamashita, T. Kaneko, T. Obata, Y. Tsuruoka, T. Ito, "A System-Design Outline of the Distributed-Shogi-System Akara 2010", SNPD 2013. https://ginza.tkl.iis.u-tokyo.ac.jp/new/uploads/publication_file/file/614/06598505.pdf (accessed 2026-11-15)
[^s6]: D. Silver et al., "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm", arXiv:1712.01815 (December 2017). https://ar5iv.arxiv.org/html/1712.01815 (accessed 2026-11-15)
[^s7]: D. Klein, "Neural Networks for Chess", arXiv:2209.01506 (2022). https://arxiv.org/pdf/2209.01506 (accessed 2026-11-15)
