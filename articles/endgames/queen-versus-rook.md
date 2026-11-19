---
id: kt:queen-versus-rook
type: EndgameType
title: Queen versus rook
aliases: [Queen against rook, Queen vs rook, Queen vs. rook, Queen versus rook endgame, Queen against a solitary rook, KQKR]
domain: endgames
summary: >-
  The pawnless endgame of king and queen against king and rook. The queen wins from almost every
  position, but the win can take up to 31 moves and demands a precise technique, so the defender's
  checks, forks and stalemate tricks make it one of the hardest basic wins to carry out in practice.
fen: "K3r3/8/5k2/Q7/8/8/8/8 w - - 0 1"
status: current
volatile: false
verified: 2026-11-19
broader: [kt:chess-endgame]
related: [kt:endgame-tablebases, kt:queen-versus-pawn, kt:rook-versus-pawn, kt:fifty-move-rule, kt:ken-thompson]
relations:
  - {predicate: usesTechnique, object: kt:zugzwang}
  - {predicate: usesTechnique, object: kt:triangulation}
  - {predicate: usesTechnique, object: kt:fork}
  - {predicate: contrastsWith, object: kt:stalemate}
  - {predicate: exemplifiedBy, object: kt:browne-versus-belle-1978}
sources:
  - id: s1
    title: "Reference Fallible Endgame Play"
    publisher: G. McC. Haworth, ICGA Journal 26(2), pp. 81-91 (2003)
    url: https://centaur.reading.ac.uk/4550/1/2003a_ICGA_J_H_Reference_Fallible_Endgame_Play.pdf
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s2
    title: "Performance and Prediction: Bayesian Modelling of Fallible Choice in Chess"
    publisher: G. Haworth, K. Regan and G. Di Fatta, Advances in Computer Games (ACG 2009), LNCS 6048, Springer (2010)
    url: https://cse.buffalo.edu/~regan/papers/pdf/HRdF10.pdf
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s3
    title: "How God plays chess"
    publisher: Frederic Friedel, ChessBase News (23 January 2018)
    url: https://en.chessbase.com/post/how-god-plays-chess
    type: publication
    accessed: 2026-11-19
  - id: s4
    title: "Dvoretsky's Endgame Manual, Sixth Edition (sample pages: contents)"
    publisher: Mark Dvoretsky, revised by Karsten Müller and Alex Fishbein, Russell Enterprises (2025)
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/89025.pdf
    type: book
    accessed: 2026-11-19
  - id: s5
    title: "Endgame. Queen vs Rook"
    publisher: catalanFischer, Chess.com blog
    url: https://www.chess.com/blog/catalanFischer/endgame-queen-vs-rook
    type: community
    accessed: 2026-11-19
  - id: s6
    title: "Triangulation"
    publisher: Chessprogramming wiki
    url: https://chessprogramming.org/Triangulation
    type: community
    accessed: 2026-11-19
created: 2026-11-19
---

# Queen versus rook

Queen versus rook is the ending of king and queen against king and rook, with no pawns on the board. Dvoretsky's manual treats it as the opening section ("A Solitary Rook") of its chapter on queen against rook, before the far more complicated cases in which the rook side also has a pawn.[^s4] In theory the matter is settled: when Ken Thompson's program classified all of the roughly 1.9 million legal positions, more than 90 per cent turned out to be wins for the queen; the unmarked remainder includes drawn "pathological" positions in which the rook side has an immediate tactical escape.[^s3]

## How hard is the win?

The difficulty lies in the length and precision of the win, not in the result. Thompson's database showed that the longest forced win, counting to mate or to the capture of the rook, is 31 moves, and only two positions need that many.[^s3] Haworth's analysis of the database by depth to conversion confirms the 31-move maximum and shows that the rook side, from a few freak positions, can itself win within three moves.[^s1] Because the queen side must also beat the fifty-move rule, a player who loses the thread for even a few moves can let a won position slip into a draw.[^s2]

The diagram shows one of the two 31-move positions as Friedel gives it (White Ka8, Qa5; Black Kf6, Re8), with White to move.[^s3] Haworth's paper lists the two maximal positions as White-to-move positions at depth 31.[^s1]

## Typical method

The winning idea is to drive the defending king to the edge, bring the attacking king close, and then reach a position in which the rook cannot stay next to its king. In the ideal set-up the queen controls one of the squares in front of the defending king, so a rook check from that square leaves the rook hanging, while the attacking king steps forward and the rook cannot keep checking for ever.[^s5] When the rook is finally forced away from its king, a queen check that also attacks the rook (a fork) wins it.[^s5]

Defenders try to keep the rook glued to the king. In the second-rank defence the rook stands just in front of its king and shuffles back and forth; the third-rank defence, with the rook one rank further out, is described as the toughest to crack, though still lost with correct play.[^s5] Breaking these set-ups often turns on zugzwang, with the side to move worse off.[^s5] The Chessprogramming wiki points to Philidor's classical queen-against-rook position as the standard illustration of queen triangulation, a manoeuvre that hands the move back to the defender.[^s6]

## Pitfalls

The rook side's main resources are tactical. The rook can give long series of checks, set up stalemates, or skewer the king and queen; Friedel shows a position (White Kb1, Qa1; Black Kb8, Rh1) in which the rook simply wins the queen and the game is drawn at once.[^s3][^s5] Thompson also noted that his program sometimes gave away material in drawn positions, since doing so did not change the result; database play follows the evaluation, not human intuition, which is one reason optimal defence can feel so unfamiliar.[^s3]

## Browne versus Belle

The ending's reputation was made in 1978. Thompson's machine Belle, using the new database to defend, played two games against grandmaster Walter Browne, who had accepted a $100 challenge to win the ending within fifty moves.[^s2] In the first game, on 19 December 1978, Browne could not make progress and the game was agreed drawn at move 45; after studying the computer's play he won the second game, on 30 December, by capturing the rook on the fiftieth move, the last one available.[^s1][^s2] Haworth's statistical study of the two games concludes that Browne lost ground to perfect play repeatedly, but that his overall level was consistent across both.[^s1] Friedel reports that later champions, Karpov and Kasparov among them, also failed to beat a computer defence in demonstrations.[^s3]

## Connections

Queen versus rook belongs to the **chess endgame** as one of the basic pawnless material balances, and its full solution was one of the first triumphs of **endgame tablebases**, built by **Ken Thompson** through retrograde analysis.[^s3] Like **queen versus pawn** and **rook versus pawn**, it pits a stronger piece against a weaker one, but here there is no pawn to stop, only a mobile defender to trap.[^s4] The win relies on **zugzwang**, often reached with **triangulation**, and on the queen **fork** that finally wins the rook, while the defence hopes for **stalemate** or for the **fifty-move rule**, the limit that decided the **Browne versus Belle** match of 1978.[^s1][^s2][^s6]

## Sources
[^s1]: G. McC. Haworth, "Reference Fallible Endgame Play", *ICGA Journal* 26(2), 2003, pp. 81-91. https://centaur.reading.ac.uk/4550/1/2003a_ICGA_J_H_Reference_Fallible_Endgame_Play.pdf (accessed 2026-11-19)
[^s2]: G. Haworth, K. Regan and G. Di Fatta, "Performance and Prediction: Bayesian Modelling of Fallible Choice in Chess", in *Advances in Computer Games (ACG 2009)*, LNCS 6048, Springer, 2010, pp. 99-110. https://cse.buffalo.edu/~regan/papers/pdf/HRdF10.pdf (accessed 2026-11-19)
[^s3]: F. Friedel, "How God plays chess", ChessBase News, 23 January 2018. https://en.chessbase.com/post/how-god-plays-chess (accessed 2026-11-19)
[^s4]: M. Dvoretsky, *Dvoretsky's Endgame Manual*, 6th edition, revised by K. Müller and A. Fishbein, Russell Enterprises, 2025, sample pages (contents, chapter 13 "Queen versus Rook"). https://www.newinchess.com/media/wysiwyg/product_pdf/89025.pdf (accessed 2026-11-19)
[^s5]: catalanFischer, "Endgame. Queen vs Rook", Chess.com blog. https://www.chess.com/blog/catalanFischer/endgame-queen-vs-rook (accessed 2026-11-19)
[^s6]: Chessprogramming wiki, "Triangulation". https://chessprogramming.org/Triangulation (accessed 2026-11-19)
