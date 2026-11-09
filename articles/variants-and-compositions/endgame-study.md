---
id: kt:endgame-study
type: ProblemGenre
title: Endgame study
aliases: [Chess study, Study, Endgame studies, Composed study, Etude]
domain: variants-and-compositions
summary: >-
  A composed chess position, usually with few pieces and resembling a game ending, in which White
  must force a win or a draw against best defence with no limit on the number of moves; the solution
  must be unique in its essential line.
status: current
volatile: true
verified: 2026-11-09
fen: "8/8/1KP5/3r4/8/8/8/k7 w - - 0 1"
broader: [kt:chess-composition]
related: [kt:chess-problems, kt:endgame-tablebases, kt:pawn-promotion, kt:stalemate]
relations:
  - {predicate: exemplifiedBy, object: kt:saavedra-position}
  - {predicate: governedBy, object: kt:codex-of-chess-composition}
sources:
  - id: s1
    title: "Chess: Chess composition"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/chess/Chess-composition
    type: reference
    accessed: 2026-11-09
  - id: s2
    title: "Codex of Chess Compositions (version Vilnius 2019)"
    publisher: World Federation for Chess Composition (WFCC)
    url: https://www.wfcc.ch/?p=198
    type: governing-body
    accessed: 2026-11-09
  - id: s3
    title: "Chess glossary (Freshman Seminar 23j: Chess and Mathematics)"
    publisher: Harvard University, Department of Mathematics
    url: https://people.math.harvard.edu/~elkies/FS23j.06/glossary_chess.html
    type: academic
    accessed: 2026-11-09
  - id: s4
    title: "The discovery of the Saavedra position, with the original 1895 Weekly Citizen columns"
    publisher: Tim Krabbé, Chess Curiosities
    url: https://timkr.home.xs4all.nl/chess/saavedra.htm
    type: primary-record
    accessed: 2026-11-09
  - id: s5
    title: "Fernando Saavedra"
    publisher: Chess Scotland, history biographies
    url: https://www.chessscotland.com/documents/history/biographies/saavedra.htm
    type: publication
    accessed: 2026-11-09
  - id: s6
    title: "Understanding chess composition competition (Study of the Month, August 2019)"
    publisher: Siegfried Hornecker, ChessBase News
    url: https://en.chessbase.com/post/study-of-the-month-2019-8
    type: publication
    accessed: 2026-11-09
created: 2026-11-09
---

# Endgame study

An endgame study (often just "study") is a composed position in which White, to move, must force either a win or a draw against Black's best defence. Unlike a mate-in-n problem, a study sets no move limit: the solver only has to reach a position that is clearly won or drawn, and solutions can run past twenty moves.[^s1][^s3] Studies usually contain few pieces and look as if they could have come from a real game, which is why they have long served both as art and as endgame instruction.[^s1]

## How a study differs from a problem

Britannica draws the line clearly. A problem typically has more material and demands checkmate in a fixed, small number of moves, often beginning with a quiet "key"; general strategy plays no part. A study, by contrast, rewards the same skills a player uses at the board—calculation, knowledge of theoretical endings and a feel for resources such as stalemate and underpromotion—but pushes them to their limit.[^s1] The WFCC's Codex, the guidelines of the world body for composition, describes the study stipulation as White to move and force a win (or a draw) without restriction to a specified number of moves, and reserves the word "problem" for most other genres.[^s2]

## Soundness: cooks and duals

What makes a study a work of art rather than an exercise is uniqueness. Under the Codex, a study is unsound if the stipulation can be met in a way other than the author's solution; a cook is a solution that differs from the author's at the first move, while a dual is an alternative way to fulfil the stipulation later on. Minor duals are usually tolerated, and the judge decides how serious one is.[^s2] An unintended second solution sharply lowers a composition's value, and judges also weigh originality, difficulty, beauty and economy of material.[^s1] A study identical to an earlier one is "anticipated" and cannot receive an award, though partial anticipation only lowers its standing.[^s2]

Computers changed the genre. In judging the World Championship in Composing for Individuals, the judges checked entries against endgame databases (the "Oracle Data-Base", i.e. tablebases) and shared lists of cooks and anticipations.[^s6] The Codex nonetheless holds that the author alone is responsible for soundness, and that a computer cannot be an author.[^s2]

## History in brief

The earliest studies are the *mansubat* of Arabic and Persian manuscripts, which taught endgame wins; positions with practical application were popular again in the 19th century.[^s1] Strong players have composed studies, among them Richard Réti, Max Euwe, Mikhail Botvinnik, Vasily Smyslov, Paul Keres and Jan Timman.[^s1] Réti's famous draw of about 1922 shows a king that seems hopelessly behind both a passed pawn and an enemy pawn, yet by walking diagonally it approaches both at once and saves the game.[^s1] FIDE awards the titles of International Master and Grandmaster of Chess Composition on the basis of works selected for the FIDE Albums.[^s1]

## Example: the Saavedra position

The best-known study grew out of a game ending. In April 1895 Georges Barbier, chess editor of the *Glasgow Weekly Citizen*, printed a position recalled from a game between Potter and Fenton and gave a drawing line; in the column of 18 May he reported that Fernando Saavedra, a member of Glasgow Chess Club, had found a win.[^s4][^s5] In its standard form (White Kb6, Pc6; Black Ka1, Rd5; White to play and win) it is the FEN above.[^s3]

After 1.c7 Rd6+ 2.Kb5 Rd5+ 3.Kb4 Rd4+ 4.Kb3 Rd3+ 5.Kc2 Rd4! Black sets a trap: 6.c8=Q? Rc4+ 7.Qxc4 is stalemate, which was Barbier's draw.[^s5] Saavedra's 6.c8=R! promotes to a rook instead; Black must parry Ra8 mate with 6...Ra4, and 7.Kb3 then attacks the rook while threatening mate on c1, so Black loses the rook or is mated.[^s4][^s5] The underpromotion caused a sensation at the time.[^s5]

```pgn
[Event "Saavedra position (Barbier/Saavedra, Glasgow Weekly Citizen, 1895)"]
[SetUp "1"]
[FEN "8/8/1KP5/3r4/8/8/8/k7 w - - 0 1"]
[Result "1-0"]

1. c7 Rd6+ 2. Kb5 Rd5+ 3. Kb4 Rd4+ 4. Kb3 Rd3+ 5. Kc2 Rd4 6. c8=R Ra4 7. Kb3 1-0
```

## Why club players should solve studies

Studies train exactly what practical endgames demand: seeing past the "obvious" move (here, queening), spotting stalemate defences for the opponent, and calculating forcing lines to a clear end. Because the composer has removed every irrelevant piece, the key idea stands out, which makes studies efficient material for practising calculation.[^s1][^s3]

## Connections

An endgame study is a genre of **chess composition**, the sister of **chess problems**, which demand mate in a set number of moves.[^s1] Its rules of soundness, cooks, duals and anticipation are set out in the WFCC **Codex of Chess Composition**.[^s2] Modern studies are routinely tested against **endgame tablebases**.[^s6] The **Saavedra position** is its most famous example, built on **pawn promotion** (an underpromotion) and on avoiding **stalemate**.[^s4][^s5]

## Sources
[^s1]: Encyclopaedia Britannica, "Chess: Chess composition". https://www.britannica.com/topic/chess/Chess-composition (accessed 2026-11-09)
[^s2]: World Federation for Chess Composition, "Codex of Chess Compositions" (version Vilnius 2019), Arts. 5, 8–10, 13, 24 and footnotes 3, 9, 34. https://www.wfcc.ch/?p=198 (accessed 2026-11-09)
[^s3]: Harvard University, Freshman Seminar 23j "Chess and Mathematics", chess glossary, entries "Study" and "Stipulation". https://people.math.harvard.edu/~elkies/FS23j.06/glossary_chess.html (accessed 2026-11-09)
[^s4]: Tim Krabbé, "The discovery of the Saavedra position, with the original 1895 Weekly Citizen columns". https://timkr.home.xs4all.nl/chess/saavedra.htm (accessed 2026-11-09)
[^s5]: Chess Scotland, "Fernando Saavedra" (history biographies). https://www.chessscotland.com/documents/history/biographies/saavedra.htm (accessed 2026-11-09)
[^s6]: Siegfried Hornecker, "Understanding chess composition competition", ChessBase News, August 2019. https://en.chessbase.com/post/study-of-the-month-2019-8 (accessed 2026-11-09)
