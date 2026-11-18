---
id: kt:queen-versus-pawn
type: EndgameType
title: Queen versus pawn
aliases: [Queen against pawn, Queen vs pawn, Queen vs. pawn, Queen versus pawn endgame, Queen vs. pawn on the seventh, KQKP]
domain: endgames
summary: >-
  The endgame of king and queen against king and a single pawn. The queen wins easily unless the pawn
  has reached the seventh rank with its king's support; then a centre or knight's pawn still loses to a
  standard checking manoeuvre, while a rook's or bishop's pawn usually draws by a stalemate defence
  unless the attacking king is already close.
fen: "4Q1K1/8/8/8/8/8/5kp1/8 w - - 0 1"
status: current
volatile: false
verified: 2026-11-18
broader: [kt:chess-endgame]
related: [kt:rook-versus-pawn, kt:king-and-pawn-endgames, kt:passed-pawn, kt:endgame-tablebases]
relations:
  - {predicate: usesTechnique, object: kt:stalemate}
  - {predicate: dependsOn, object: kt:counting-in-pawn-races}
  - {predicate: contrastsWith, object: kt:knight-versus-pawn}
sources:
  - id: s1
    title: "100 Basic Endgames You Must Know: A Starter's Guide to Chess Endings (sample pages, chapter 9 \"Queen vs pawn\")"
    publisher: Jesús de la Villa, New In Chess (2026)
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/9242.pdf
    type: book
    accessed: 2026-11-18
  - id: s2
    title: "The 100 Endgames You Must Know Workbook (sample pages, chapter 3 \"Queen vs. pawn\")"
    publisher: Jesús de la Villa, New In Chess (2019)
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/9076.pdf
    type: book
    accessed: 2026-11-18
  - id: s3
    title: "Queen versus Pawn"
    publisher: Chessprogramming wiki
    url: https://www.chessprogramming.org/Queen_versus_Pawn
    type: community
    accessed: 2026-11-18
  - id: s4
    title: "Queen vs. Pawn on 7th"
    publisher: TonightOnly, Chess.com (2008)
    url: https://www.chess.com/article/view/queen-vs-pawn-on-7th
    type: community
    accessed: 2026-11-18
created: 2026-11-18
---

# Queen versus pawn

Queen versus pawn is the ending of king and queen against king and one pawn. It usually comes out of a pawn ending, when both sides have run a passed pawn and one of them promotes first.[^s1][^s4] Jesús de la Villa stresses how narrow the difficult zone is: the queen wins without trouble unless the pawn stands at least on the sixth rank, and almost always the seventh, and even then the win is easy if the queen can occupy a square in front of the pawn, from which it cannot be driven away.[^s1] The practical questions are therefore which file the pawn is on and how far away the stronger side's king stands.

## Centre and knight's pawns: the winning manoeuvre

Against a centre or knight's pawn on the seventh rank, supported by its king, the queen wins with a repeating routine, provided it can begin with a check.[^s1] First the queen gives checks that stop the pawn from promoting while drawing closer to it. As soon as the geometry allows, it stops checking and attacks the pawn instead, so that a further check forces the defending king onto the promotion square in front of its own pawn. That move blocks the pawn and gives the attacker one free tempo, which is spent bringing the king a step closer. Repeating the cycle walks the king in until a mating net appears, sometimes even allowing the pawn to promote.[^s1][^s3]

```pgn
[Event "Queen vs knight's pawn on the seventh (de la Villa, position 55.1)"]
[SetUp "1"]
[FEN "4Q1K1/8/8/8/8/8/5kp1/8 w - - 0 1"]
[Result "1-0"]

1. Qf7+ Ke2 2. Qe6+ Kf2 3. Qf5+ Ke2 4. Qe4+ Kf2 5. Qf4+ Ke2 6. Qg3 Kf1
7. Qf3+ Kg1 8. Kg7 Kh2 9. Qf2 Kh1 10. Qh4+ Kg1 11. Kg6 Kf1 12. Qf4+ Ke2
13. Qg3 Kf1 14. Qf3+ Kg1 15. Kg5 Kh2 16. Kh4 g1=Q 17. Qh3# 1-0
```

In this line (White Kg8, Qe8; Black Kf2, Pg2) the moves 6.Qg3 and 7.Qf3+ show the key step: attack the pawn, then check so that the king must stand on g1, and use the spare move for the white king.[^s1] De la Villa adds two rarities: if the queen has no first check at all the pawn simply promotes and it is a draw, but a queen that can at least pin the pawn still wins.[^s1]

## Rook's and bishop's pawns: the stalemate defence

The same manoeuvre fails against a rook's pawn. When the defending king is driven into the corner in front of its pawn, it has no legal moves, so the attacker gains no tempo: any quiet move is stalemate, and the queen must keep checking while the pawn threatens to promote again.[^s1][^s4] In de la Villa's example (White Ke5, Qg8; Black Kb2, Pa2) the queen reaches b3 with check, Black answers ...Ka1, and nothing better than another check remains.[^s1]

A bishop's pawn draws for a related reason. The defender steps to the far side of the pawn, towards the rook's file, and when checked retreats into the corner instead of in front of the pawn; if the queen then captures the pawn, the result is stalemate.[^s1][^s4] De la Villa's position (White Kg7, Qf8; Black Kd2, Pc2) shows the king reaching the safe side and answering Qb3+ with ...Ka1, after which the draw cannot be prevented.[^s1] The Chessprogramming wiki notes that the result depends on which side of the pawn the defending king stands, and that a defender on the "wrong" side gives the attacker extra time.[^s3]

## When the attacker's king is close

These drawing rules assume a distant attacking king. The Chessprogramming wiki, summarising the classical literature from Fine to Müller and Lamprecht, describes winning zones: against a rook's pawn the king must be near enough to the promotion corner, and against a bishop's pawn it must reach a critical square next to the pawn within one or two moves, depending on the defending king's side, so that it can help the queen deliver mate.[^s3] A second pawn for the defender can also spoil the stalemate defence, because the king is no longer without moves; de la Villa notes that this is simple with a rook's pawn and much harder with a bishop's pawn.[^s1]

## Pitfalls

Trusting the queen too much is the usual error. De la Villa's workbook includes a 1999 game in which Black, a full queen up against a pawn on the sixth, chose the wrong capture and let White reach a drawn queen-versus-bishop's-pawn position; he warns that even a sixth-rank pawn is not always lost.[^s2] For the weaker side, the lesson is to head for the right corner rather than block the pawn early.[^s1]

## Connections

Queen versus pawn belongs to the **chess endgame** and is one of the piece-against-pawn endings alongside **rook versus pawn** and **knight versus pawn**; de la Villa notes that the queen's difficulties are limited to sixth- and seventh-rank pawns, whereas rook against pawn can be hard on any rank.[^s1] It usually arises from **king and pawn endgames** in which a **passed pawn** race is decided, so **counting in pawn races** tells a player whether the resulting queen ending will be won.[^s3][^s4] Its main drawing resource is **stalemate**, and, like every ending with this little material, its exact results can be looked up in **endgame tablebases**; the Chessprogramming wiki describes how engines recognise its drawn cases.[^s3]

## Sources
[^s1]: J. de la Villa, *100 Basic Endgames You Must Know: A Starter's Guide to Chess Endings*, New In Chess (2026), sample pages, chapter 9 "Queen vs pawn". https://www.newinchess.com/media/wysiwyg/product_pdf/9242.pdf (accessed 2026-11-18)
[^s2]: J. de la Villa, *The 100 Endgames You Must Know Workbook*, New In Chess (2019), sample pages, exercise 46 (Husari–Voloshin, Koszalin 1999). https://www.newinchess.com/media/wysiwyg/product_pdf/9076.pdf (accessed 2026-11-18)
[^s3]: Chessprogramming wiki, "Queen versus Pawn". https://www.chessprogramming.org/Queen_versus_Pawn (accessed 2026-11-18)
[^s4]: TonightOnly, "Queen vs. Pawn on 7th", Chess.com, 12 July 2008. https://www.chess.com/article/view/queen-vs-pawn-on-7th (accessed 2026-11-18)
