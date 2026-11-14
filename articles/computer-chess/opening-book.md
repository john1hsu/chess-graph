---
id: kt:opening-book
type: Concept
title: Opening book
aliases: [Opening books, Engine opening book, Book (computer chess), Opening library]
domain: computer-chess
summary: >-
  A database of opening positions and moves that a chess program consults before it starts
  searching, so it can reply instantly with prepared moves until the game leaves known theory
  ("out of book").
status: current
volatile: false
verified: 2026-11-14
broader: [kt:computer-chess]
related: [kt:chess-openings, kt:transposition-table, kt:universal-chess-interface, kt:top-chess-engine-championship, kt:deep-blue-versus-kasparov]
relations:
  - {predicate: alternativeTo, object: kt:game-tree-search}
  - {predicate: contrastsWith, object: kt:endgame-tablebases}
sources:
  - id: s1
    title: "Opening Book"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/Opening_Book
    type: community
    accessed: 2026-11-14
  - id: s2
    title: "Deep Blue (M. Campbell, A. J. Hoane Jr., F.-h. Hsu)"
    publisher: IBM T. J. Watson Research Center authors; course reading hosted by Northern Arizona University
    url: https://www.cefns.nau.edu/~edo/Classes/CS470-570_WWW/Readings/Campbell2002.pdf
    type: academic
    accessed: 2026-11-14
  - id: s3
    title: "Book Learning - a Methodology to Tune an Opening Book Automatically (ICGA Journal 22(1), 1999, pp. 3-12)"
    publisher: Robert M. Hyatt, University of Alabama at Birmingham; IOS Press
    url: https://content.iospress.com/articles/icga-journal/icg22102
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "Book Learning"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org/Book_Learning
    type: community
    accessed: 2026-11-14
  - id: s5
    title: "TCEC Openings FAQ"
    publisher: Top Chess Engine Championship
    url: https://tcec-chess.com/articles/TCEC_Openings_FAQ.html
    type: official-project
    accessed: 2026-11-14
  - id: s6
    title: "Stockfish (README)"
    publisher: Stockfish developers, GitHub
    url: https://github.com/official-stockfish/Stockfish
    type: official-project
    accessed: 2026-11-14
created: 2026-11-14
---

# Opening book

In computer chess, an **opening book** is a stored collection of opening positions and the moves a program should play in them. The program looks the current position up before it searches; as long as the opponent stays within the stored lines it answers at once, and when the opponent plays something the book does not contain, the program is "out of book" and its ordinary search takes over. Popular lines are usually stored much deeper than rare ones.[^s1]

## Why programs use books

A book does three jobs. It saves clock time in the phase where theory is already known; it can produce better early moves than a shallow search, which may misjudge long-term strategic factors or the compensation for a gambit; and, because the program can choose randomly among several book moves, it adds variety so that opponents cannot simply repeat a known win.[^s1] That last point matters in practice: Robert Hyatt reported that human players on internet servers would find a weak line in his program Crafty's book and repeat it until it won, which he had previously fixed by hand.[^s3]

## How books are stored

Early books were typed in by hand. Ken Thompson is reported to have spent about three years entering some 300,000 moves from the *Encyclopaedia of Chess Openings* for his machine Belle before writing a program to read the books automatically.[^s1] Text formats are human-readable but bulky: a book may be kept as PGN games, as EPD records of final positions, or as a nested move tree in which `(e4(e5)(c5))` stores 1.e4 with the two replies 1...e5 and 1...c5.[^s1]

Modern binary books instead key each entry by a 64-bit hash of the position, usually with extra data such as win/draw/loss counts or move weights, and keep the entries sorted so that a lookup is a fast binary search. Keying on the position rather than on the move sequence means that different move orders reaching the same position share one entry, so transpositions are handled automatically. The best-known binary formats are PolyGlot's `.bin` (16 bytes per entry), Arena's ABK and ChessBase's CTG.[^s1]

Many modern engines leave the book to the graphical interface altogether. Stockfish, for example, is distributed as a UCI engine without its own GUI, and users run it inside a separate interface,[^s6] which is where book handling usually lives; the Chess Programming Wiki notes that GUI-managed books make some engine-side book-learning techniques harder to apply.[^s1]

## Deep Blue's book and "extended book"

IBM's Deep Blue team describe a hand-made book of only about 4,000 positions, prepared mainly by Grandmaster Joel Benjamin with help from other grandmasters and checked by the machine in overnight runs; last-minute corrections went into a small "override" book.[^s2] The book was small by design because the team relied on an **extended book**: a database of roughly 700,000 grandmaster games that, when no book move existed, gave bonuses or penalties to moves according to how often and by whom they had been played, how recently, with what results, and how annotators marked them.[^s2]

The bonus was applied by shifting the search window for that move. In the authors' example, if 1.d4 carries a 10-point bonus, it is chosen unless another move is more than 10 points better; a bonus could be worth up to half a pawn, and a move with an overwhelming bonus could be played without searching at all.[^s2] The idea dates from Deep Thought 2 in 1991.[^s2]

## Book learning and pitfalls

A fixed book is a target. **Book learning** lets the program adjust it from experience: in Hyatt's scheme Crafty avoids the last book move of a lost game (propagating the penalty a few moves back) and also watches the trend of its evaluations just after leaving book to mark lines as good or bad.[^s3][^s4] Other programs drop or down-weight moves that score poorly once the game leaves book.[^s4] Typical pitfalls are book lines that end in positions the engine handles badly, errors copied from the source material, and narrow books that an opponent can prepare against.[^s1][^s3]

## Books in engine competitions

Engine-versus-engine events often replace the engines' own books with a common set of starting positions. The Top Chess Engine Championship (TCEC) issues its openings centrally, with depths ranging from 4 moves in its lowest league to 8 moves in its upper leagues, and a separate, specially chosen set for the Superfinal; each opening is played twice in consecutive games with colours reversed, which reduces the influence of a lucky pairing and stops engines steering every game into favourite lines.[^s5] Openings in the higher stages are deliberately biased to keep the draw rate down.[^s5]

## Connections

An opening book is the computer counterpart of human **chess openings** theory and an alternative to computing the first moves with **game tree search**; its position-keyed lookup relies on the same hashing idea as the **transposition table**.[^s1] It mirrors **endgame tablebases** at the other end of the game: a book stores human and statistical knowledge that can be wrong, whereas a tablebase stores proven results.[^s1] Deep Blue's extended book played a part in the **Deep Blue versus Kasparov** matches,[^s2] and the **Top Chess Engine Championship** shows how competitions now standardise openings instead of letting each **UCI** engine bring its own book.[^s5][^s6]

## Sources

[^s1]: Chess Programming Wiki, "Opening Book". https://www.chessprogramming.org/Opening_Book (accessed 2026-11-14)
[^s2]: M. Campbell, A. J. Hoane Jr. and F.-h. Hsu, "Deep Blue". https://www.cefns.nau.edu/~edo/Classes/CS470-570_WWW/Readings/Campbell2002.pdf (accessed 2026-11-14)
[^s3]: R. M. Hyatt, "Book Learning - a Methodology to Tune an Opening Book Automatically", ICGA Journal 22(1), 1999. https://content.iospress.com/articles/icga-journal/icg22102 (accessed 2026-11-14)
[^s4]: Chess Programming Wiki, "Book Learning". https://www.chessprogramming.org/Book_Learning (accessed 2026-11-14)
[^s5]: Top Chess Engine Championship, "TCEC Openings FAQ". https://tcec-chess.com/articles/TCEC_Openings_FAQ.html (accessed 2026-11-14)
[^s6]: Stockfish developers, Stockfish README, GitHub. https://github.com/official-stockfish/Stockfish (accessed 2026-11-14)
