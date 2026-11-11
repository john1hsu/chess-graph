---
id: kt:excelsior
type: ProblemTheme
title: Excelsior
aliases: [Excelsior theme, Excelsior (chess problem), Loyd's Excelsior, Pawn Excelsior]
domain: variants-and-compositions
summary: >-
  A chess problem theme in which a pawn standing on its starting square in the diagram walks all the way
  up the board and promotes during the solution; named after Sam Loyd's 1861 mate-in-five.
status: current
volatile: false
verified: 2026-11-11
fen: "8/K1N1p3/2k1N3/4P3/8/8/1P6/8 w - - 0 1"
broader: [kt:chess-problems]
related: [kt:pawn-promotion, kt:helpmate, kt:chess-composition, kt:allumwandlung]
relations:
  - {predicate: developedBy, object: kt:sam-loyd}
  - {predicate: usesTechnique, object: kt:underpromotion}
sources:
  - id: s1
    title: "Chess Problems: Tasks and Records (3rd edition), Chapter 19: Onwards and Upwards"
    publisher: Jeremy Morse; hosted by the British Chess Problem Society (The Problemist)
    url: https://www.theproblemist.org/dloads/cjm/Chapter_19.pdf
    type: book
    accessed: 2026-11-11
  - id: s2
    title: "Sam Loyd (1841–1911)"
    publisher: World Chess Hall of Fame
    url: https://worldchesshof.org/?p=775
    type: archive
    accessed: 2026-11-11
  - id: s3
    title: "Sam Loyd"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com:443/biography/Sam-Loyd
    type: reference
    accessed: 2026-11-11
  - id: s4
    title: "Glossary"
    publisher: Peter Wong, OzProblems
    url: https://www.ozproblems.com/glossary
    type: community
    accessed: 2026-11-11
  - id: s5
    title: "Chess Problems: Excelsior Again"
    publisher: David Friedgood, ChessBase News (5 December 2013)
    url: https://en.chessbase.com/post/chess-problems-excelsior-again
    type: publication
    accessed: 2026-11-11
  - id: s6
    title: "ChessBase puzzles: Loyd's Excelsior"
    publisher: Frederic Friedel, ChessBase News (26 October 2013)
    url: https://en.chessbase.com/newsroom/post/chebase-puzzles-loyds-excelsior-261013
    type: publication
    accessed: 2026-11-11
created: 2026-11-11
---

# Excelsior

The Excelsior is one of the oldest named themes in problem chess: a pawn that stands on its original square in the diagram makes its whole journey up the board during the solution and promotes.[^s4] Jeremy Morse, in his survey of problem tasks and records, describes it as a pawn's five- or six-step walk from its starting square to promotion and calls it the problemist's favourite theme of the "walk" kind.[^s1] For a White pawn on the second rank that means five moves if it uses its double step and six if it does not, so the theme fits naturally into a mate in five or a longer helpmate or selfmate.[^s1][^s5]

## Origin and name

The theme takes its name from a mate-in-five that Sam Loyd composed in 1858 and that was first published in the *London Era* in 1861. Friedel reports that Loyd made it to tease a fellow problemist who claimed he could always guess which white piece would give the mate. Loyd's answer was a position where the least likely unit, a humble pawn on b2, marches to the eighth rank and mates. The name was borrowed from Longfellow's poem *Excelsior* (1841), about a climber who keeps pressing upward.[^s6] Morse calls Loyd's problem the "evergreen pioneer" of the theme.[^s1] The World Chess Hall of Fame, which inducted Loyd in 1987, lists *Excelsior* among his two best-known problems.[^s2] Loyd was the leading American composer of his day and later problem editor of *Chess Monthly*.[^s3]

Loyd was not quite the first. David Friedgood points out that a mate in five by Robert Wormald in the *Illustrated London News* of 1857 already showed a white pawn travelling from d2, capturing its way across the board, to promote on b8 with mate, one year before Loyd composed his. A practical-play precursor turned up in an 1850 game between Shumov and Jaenisch, in which White's f-pawn ran up from f2 and captured on e8, promoting to a knight with check.[^s5]

## What makes a good Excelsior

A pawn walk alone is easy to arrange; the art lies in forcing every step. In a directmate each pawn move must be the only way to keep the threat going, so Black's defences have to be met by the pawn advancing, often by capturing on a different file, rather than by a piece move.[^s5][^s6] Promotion to a minor piece adds value: the knight or bishop mate shows that a queen would not do, and Morse singles out a 1987 mate in five by L. Joudon as a fine modern example with underpromotion.[^s1]

Composers have long since pushed the theme into tasks. Morse records a 1972 series-helpmate by A. Atanasiević that combines four Excelsiors with an Allumwandlung (all four promotion pieces), and a 2012 series-selfmate by U. Heinonen with five Excelsiors and the same four promotions ending in a model mate.[^s1] In helpmates both sides cooperate, so a composer can show one Excelsior per solution, or a White and a Black pawn running at the same time.[^s5]

## Example: Hendel, mate in five (1859)

A clear early setting is J. Hendel's mate in five from *Payne's Family Journal*, 1859 (FEN above, White to move): White Ka7, Nc7, Ne6, pawns b2 and e5; Black Kc6, pawn e7.[^s5] The pawn on b2 does all the work, step by step, and promotes to a knight to mate. Black's e-pawn is blocked, so only the king can move, and it shuffles between c6, d7 and c8 while the pawn advances; the new knight on b8 then gives mate.[^s5]

```pgn
[Event "Payne's Family Journal 1859 — mate in 5 (Hendel)"]
[SetUp "1"]
[FEN "8/K1N1p3/2k1N3/4P3/8/8/1P6/8 w - - 0 1"]
[Result "1-0"]

1. b4 Kd7 2. b5 Kc8 3. b6 Kd7 4. b7 Kc6 5. b8=N# 1-0
```

## Example: a helpmate with two Excelsiors

J. Pitkänen and Timo Koistinen (Commended, *The Problemist*, 2007) set a helpmate in six with two solutions, Black to move. In both, White's h-pawn walks from h2 to the eighth rank and becomes a knight: once via captures on g5 and f6, ending 6.f8=N and a knight mate, and once straight up the h-file to h8=N#, while Black's f-pawn promotes to a bishop to help.[^s5]

```pgn
[Event "The Problemist 2007, Commended — h#6, solution 1"]
[SetUp "1"]
[FEN "4nbn1/4pkp1/5p2/5p2/8/1ppp4/2p4P/2K5 b - - 0 1"]
[Result "1-0"]

1... g5 2. h4 Kg7 3. hxg5 Kh8 4. gxf6 Bg7 5. f7 Nef6 6. f8=N Nh7 7. Ng6# 1-0
```

```pgn
[Event "The Problemist 2007, Commended — h#6, solution 2"]
[SetUp "1"]
[FEN "4nbn1/4pkp1/5p2/5p2/8/1ppp4/2p4P/2K5 b - - 0 1"]
[Result "1-0"]

1... f4 2. h3 f3 3. h4 f2 4. h5 f1=B 5. h6 Bh3 6. h7 Be6 7. h8=N# 1-0
```

(The PGN uses game numbering; problemists would write the helpmate with Black's move first in each pair.)

## Connections

The Excelsior is a theme of the **chess problem**, the main branch of **chess composition**, and it is built on **pawn promotion**: the climax of every setting is the pawn reaching the last rank.[^s4][^s1] It was **developed by Sam Loyd**, whose 1861 problem gave it its name.[^s1][^s6] Many settings use **underpromotion** to a knight or bishop, and task composers combine it with the **Allumwandlung**.[^s1][^s5] The **helpmate** has become a natural home for it, because cooperative play lets both solutions show a full pawn walk.[^s5]

## Sources
[^s1]: Jeremy Morse, *Chess Problems: Tasks and Records* (3rd edition, 2016), Chapter 19 "Onwards and Upwards", §19.4, problems 951–955; chapter PDF hosted by the British Chess Problem Society. https://www.theproblemist.org/dloads/cjm/Chapter_19.pdf (accessed 2026-11-11)
[^s2]: World Chess Hall of Fame, "Sam Loyd (1841–1911)", Hall of Fame inductee page. https://worldchesshof.org/?p=775 (accessed 2026-11-11)
[^s3]: Encyclopaedia Britannica, "Sam Loyd". https://www.britannica.com:443/biography/Sam-Loyd (accessed 2026-11-11)
[^s4]: Peter Wong, OzProblems, "Glossary", entries "Excelsior" and "Allumwandlung". https://www.ozproblems.com/glossary (accessed 2026-11-11)
[^s5]: David Friedgood, "Chess Problems: Excelsior Again", ChessBase News, 5 December 2013. https://en.chessbase.com/post/chess-problems-excelsior-again (accessed 2026-11-11)
[^s6]: Frederic Friedel, "ChessBase puzzles: Loyd's Excelsior", ChessBase News, 26 October 2013. https://en.chessbase.com/newsroom/post/chebase-puzzles-loyds-excelsior-261013 (accessed 2026-11-11)
