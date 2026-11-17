---
id: kt:bishop-and-knight-checkmate
type: EndgameType
title: Bishop and knight checkmate
aliases: [Bishop and knight mate, Knight and bishop mate, Knight and bishop checkmate, KBN versus K, KBNK, King, bishop and knight versus king, W-manoeuvre, W-maneuver]
domain: endgames
summary: >-
  The basic ending of king, bishop and knight against a lone king, a forced win in which the defending
  king must be driven to a corner of the bishop's colour; the method is demanding enough that it has to be
  learned to beat the fifty-move rule.
fen: "7k/8/5BKN/8/8/8/8/8 b - - 0 1"
status: current
volatile: false
verified: 2026-11-17
broader: [kt:checkmate, kt:chess-endgame]
related: [kt:wrong-bishop, kt:endgame-tablebases, kt:knight-versus-bishop, kt:jose-raul-capablanca]
relations:
  - {predicate: governedBy, object: kt:fifty-move-rule}
  - {predicate: dependsOn, object: kt:cutting-off-the-king}
  - {predicate: contrastsWith, object: kt:wrong-bishop}
sources:
  - id: s1
    title: "Chess Fundamentals (1921), Project Gutenberg eBook #33870"
    publisher: José Raúl Capablanca; Project Gutenberg
    url: https://gutenberg.org/cache/epub/33870/pg33870-images.html
    type: book
    accessed: 2026-11-17
  - id: s2
    title: "The bishop and knight checkmate on a large chessboard"
    publisher: Johan Wästlund, Games of No Chance 6, MSRI Publications vol. 71 (2025)
    url: https://library.slmath.org/books/Book71/files/GONC6-15.pdf
    type: academic
    accessed: 2026-11-17
  - id: s3
    title: "Mating with bishop and knight: W-manoeuvre (The Endgame Academy Vol.1, chapter 1.4)"
    publisher: Karsten Müller, ChessBase Books
    url: https://tutorials3.chessbase.com/en/the-endgame-academy-vol1-checkmate-pawn-endga-2/mating-with-bishop-and-knight-w-manoeuvre
    type: book
    accessed: 2026-11-17
  - id: s4
    title: "The W-manoeuvre"
    publisher: ChessBase News (13 January 2011), introducing Karsten Müller's ChessBase Magazine column
    url: https://en.chessbase.com/post/the-w-manoeuvre
    type: publication
    accessed: 2026-11-17
  - id: s5
    title: "How to mate with Bishop and Knight"
    publisher: Exeter Chess Club (notes by Norbert Friedrich, 2010)
    url: https://exeterchessclub.org.uk/content/how-mate-bishop-and-knight
    type: community
    accessed: 2026-11-17
created: 2026-11-17
---

# Bishop and knight checkmate

King, bishop and knight against a bare king is the hardest of the basic mates and the only one with minor pieces that can be forced: two knights alone cannot mate, while bishop and knight can, but only in a corner of the bishop's colour.[^s1] Capablanca's *Chess Fundamentals* states the rule plainly and treats the ending in its own section, warning that it is laborious and that the win has to be completed within the fifty-move limit.[^s1] Because the ending turns up rarely, many players never learn it; ChessBase notes that plenty of players avoid the material balance altogether for fear of failing to mate.[^s4]

## How the pieces cooperate

The bishop controls only one colour, so the work is divided. Müller's description has the attacking king standing in opposition to the defending king or a knight's move away from it, usually on squares of the opposite colour to the bishop, while the knight takes away the escape squares the bishop cannot reach.[^s3] Capablanca draws attention to the same two features: the close pursuit by the king, and the way king and knight together cover the squares of the colour the bishop does not.[^s1]

## The three stages

Müller breaks the procedure into three steps: force the king to the edge, drive it from the "wrong" corner (the one the bishop does not control) to the "right" corner, and give mate there.[^s3] The defender's best try is to run to a wrong corner, because mate is impossible there, and to make every move count against the fifty-move rule.[^s2][^s3]

The middle stage is where most players go wrong. The standard method is the **W-manoeuvre**: with the defending king on the edge near the wrong corner, the knight hops c7-d5-e7-f5-g7, tracing a letter W, while the bishop seals off the way back to the safe corner and the king follows alongside.[^s5] Starting from White Kc6, Nc7, Bc5 against Black Kb8 (Black to move), the Exeter club notes give this line, which ends in the diagram mate on h8:[^s5]

```pgn
[Event "W-manoeuvre (instructional line)"]
[White "White"]
[Black "Black"]
[Result "1-0"]
[SetUp "1"]
[FEN "1k6/2N5/2K5/2B5/8/8/8/8 b - - 0 2"]

2... Kc8 3. Ba7 Kd8 4. Nd5 Ke8 5. Kd6 Kf7 6. Ne7 Kf6 7. Be3 Kf7 8. Bd4 Ke8
9. Ke6 Kd8 10. Bb6+ Ke8 11. Nf5 Kf8 12. Bc7 Ke8 13. Ng7+ Kf8 14. Kf6 Kg8
15. Kg6 Kf8 16. Bd6+ Kg8 17. Nf5 Kh8 18. Be7 Kg8 19. Nh6+ Kh8 20. Bf6# 1-0
```

The notes stress that the final drive into the corner must be a knight check on g8 rather than a bishop move from f6.[^s5] An older alternative, traced back to Philidor and found in the endgame books of Fine and Averbakh, works the king along the edge in a different order.[^s5] A third approach, the Delétang triangles method, confines the king behind a series of shrinking diagonal barriers set up by the bishop and knight.[^s2]

## Pitfalls

- **Losing the race with the clock and the count.** The ending is long enough that hesitation or a single detour can run into the fifty-move rule.[^s1][^s3]
- **Letting the king slip out.** If the bishop leaves the diagonal that blocks the escape, the defender returns to the safe corner and the work starts again.[^s5]
- **Treating it as theoretical.** The Exeter notes recall Galliamova choosing the ending as a drawing attempt against Susan Lalic, who then mated in 45 moves; ChessBase cited an Ivanchuk–Morozevich game as a demonstration of the technique.[^s4][^s5]

## Beyond the 8×8 board

Mathematicians have asked whether the method scales. Wästlund formalises a 1983 method by Julius Telesin, a refinement of the Delétang idea, and proves that bishop and knight can force mate on an arbitrarily large board provided it has a corner of the bishop's colour; the method takes time roughly proportional to the board's area.[^s2] He also reports tablebase work giving a 93-move maximum on a 16×16 board.[^s2]

## Connections

The ending is a special case of checkmate and a staple of basic endgame study, governed in practice by the fifty-move rule, which sets the defender's target.[^s1][^s3] It depends on cutting off the king, since every stage restricts the defender to a shrinking area.[^s3][^s5] It contrasts with the wrong-bishop ending: there a bishop that cannot control the corner square leaves an extra piece useless, while here the same colour question decides which corner is the mating one.[^s1] Endgame tablebases have solved the ending exactly and are used to measure its length on larger boards.[^s2] Capablanca's treatment in *Chess Fundamentals* is a classic textbook exposition.[^s1]

## Sources
[^s1]: José Raúl Capablanca, *Chess Fundamentals* (1921), section "How to Mate with a Knight and a Bishop"; Project Gutenberg. https://gutenberg.org/cache/epub/33870/pg33870-images.html (accessed 2026-11-17)
[^s2]: Johan Wästlund, "The bishop and knight checkmate on a large chessboard", *Games of No Chance 6*, MSRI Publications vol. 71 (2025). https://library.slmath.org/books/Book71/files/GONC6-15.pdf (accessed 2026-11-17)
[^s3]: Karsten Müller, "Mating with bishop and knight: W-manoeuvre", *The Endgame Academy Vol.1: Checkmate & pawn endgames*, ChessBase Books. https://tutorials3.chessbase.com/en/the-endgame-academy-vol1-checkmate-pawn-endga-2/mating-with-bishop-and-knight-w-manoeuvre (accessed 2026-11-17)
[^s4]: "The W-manoeuvre", ChessBase News, 13 January 2011. https://en.chessbase.com/post/the-w-manoeuvre (accessed 2026-11-17)
[^s5]: Norbert Friedrich (notes), "How to mate with Bishop and Knight", Exeter Chess Club, 2010. https://exeterchessclub.org.uk/content/how-mate-bishop-and-knight (accessed 2026-11-17)
