---
id: kt:two-knights-versus-pawn
type: EndgameType
title: Two knights versus pawn
aliases: [Two knights endgame, Two knights against pawn, Two knights vs pawn, Two knights vs. pawn, Troitzky line, Troitsky line, KNNKP]
domain: endgames
summary: >-
  The endgame of king and two knights against king and pawn. Two knights alone cannot force mate,
  but the defender's pawn removes the stalemate defence, so the knights usually win when one knight
  can blockade the pawn on or behind the Troitzky line.
fen: "8/8/8/5K2/7k/7p/7N/7N w - - 0 1"
status: current
volatile: false
verified: 2026-11-27
broader: [kt:chess-endgame]
related: [kt:stalemate, kt:endgame-tablebases, kt:blockade, kt:endgame-study, kt:knight-versus-pawn]
relations:
  - {predicate: developedBy, object: kt:alexey-troitzky}
  - {predicate: governedBy, object: kt:fifty-move-rule}
  - {predicate: dependsOn, object: kt:blockade}
sources:
  - id: s1
    title: "Chess Fundamentals (1921), Project Gutenberg eBook #33870"
    publisher: José Raúl Capablanca; Project Gutenberg
    url: https://gutenberg.org/cache/epub/33870/pg33870-images.html
    type: book
    accessed: 2026-11-27
  - id: s2
    title: "The Saving 75-move rule"
    publisher: IA Amir Erfan Hashemi, FIDE Arbiters' Commission (April 2023)
    url: https://arbiters.fide.com/wp-content/uploads/2023/06/The-Saving-75.pdf
    type: governing-body
    accessed: 2026-11-27
  - id: s3
    title: "Chess Endgame Records (v7, 2014-08-14)"
    publisher: Guy Haworth, University of Reading (dataset, first published December 2013)
    url: https://reading-9.eprints-hosting.org/34268/2/chessendrecann.pdf
    type: academic
    accessed: 2026-11-27
  - id: s4
    title: "Two knights and a pawn too many"
    publisher: Karsten Müller, ChessBase News (2019-05-21)
    url: https://en.chessbase.com/newsroom/post/endgame-blog-karsten-mueller-1009e?page=0
    type: publication
    accessed: 2026-11-27
  - id: s5
    title: "Troitzky: In Memoriam"
    publisher: Nagesh Havanur, ChessBase News (2016-03-21)
    url: https://en.chessbase.com/post/troitzky-in-memoriam
    type: publication
    accessed: 2026-11-27
  - id: s6
    title: "The Troitzky Line"
    publisher: Sid Pickard, Chess Advocate vol. 7 no. 3, pp. 45-58; hosted by chessjournalism.org
    url: https://chessjournalism.org/wp-content/uploads/2023/06/The-Troitzky-Line-by-Sid-Pickard-Chess-Advocate-Volume-7-Number-3-.pages-45-to-58.pdf
    type: publication
    accessed: 2026-11-27
created: 2026-11-27
---

# Two knights versus pawn

King and two knights cannot force checkmate against a bare king: the best they can achieve against correct defence is stalemate. Capablanca stated the paradox in *Chess Fundamentals*: two knights alone cannot mate, but under certain conditions they can if the opponent has one or more pawns.[^s1] The extra pawn helps the stronger side because it gives the defender a legal move at the moment when a lone king would be stalemated, so the knights can build a mating net that would otherwise be impossible.[^s1] The ending is the most intricate of the "basic" mates and is rarely seen at the board, though it does occur in practice.[^s5][^s6]

## The Troitzky line

Whether the knights win depends mainly on how far the pawn has advanced when a knight blockades it. For a black pawn, the critical boundary runs a4-b6-c5-d4-e4-f5-g6-h4: if White can blockade the pawn on one of these squares or further back, White wins, although some wins take longer than the fifty-move rule allows.[^s4] For a white pawn the line is mirrored, a5-b3-c4-d5-e5-f4-g3-h5.[^s6] Once the pawn has crossed the line the outcome is less clear and depends on the defending king: there are drawing zones and losing zones, the losing ones lying near particular corners.[^s4] Pickard points out that Troitzky himself never spoke of a "line"; the term was distilled later from his remarks and individual studies.[^s6]

## How the win works

The plan has two jobs for two knights. One knight holds the pawn in a blockade, while the king and the other knight drive the defending king along the edge into a mating corner; only at the last moment is the blockading knight released so that the pawn's advance gives Black a move and avoids stalemate.[^s6] The mating corner depends on the pawn's file: Pickard's analysis finds that against best defence a d-pawn case can be finished only in one specific corner, as can the f- and g-pawn cases, while a careless defender can be mated elsewhere.[^s6] Because the blockading knight cannot help with the mating net until the end, the manoeuvres are long, and the stronger side often has no simple way to lose a tempo.[^s6]

The diagram position, which Havanur's article credits to the Rev. Horatio Bolton (1840), shows the finish in miniature. White's knight on h2 blocks the h-pawn and the black king is already near the corner: 1.Nf2 Kh5 2.Nfg4 Kh4 3.Kg6 Kg3 4.Kg5 Kg2 5.Kf4 Kh1 6.Kf3 Kg1 7.Kg3 Kh1 8.Nf3 h2 9.Nf2 mate. The pawn's move 8...h2 is forced, and it is exactly this move that the defender would lack without the pawn.[^s5]

## Pitfalls

The commonest practical error is capturing the pawn. In Capablanca's example White must leave it alone, because taking it leaves only the drawn two-knights-against-king ending; instead White lets it run and mates as it promotes.[^s1] A second danger is the clock: Müller notes that some theoretically won blockade positions cannot be converted within fifty moves.[^s4] Precision also matters inside the winning zone. In Solomon–Steadman, Doeberl Cup 2011, Müller's analysis given by Havanur calls 92.Ng6 a mistake and shows the win with 92.Ne6!, which eventually mates on move 107.[^s5]

## History and the rules

Havanur traces the theme back to the eighteenth-century French player Chapais, who noticed that a defender's blocked pawn makes mate possible, and to Bolton, who showed how to carry it out; the problem later appeared in Berger's *Theorie und Praxis der Endspiele* (1890).[^s5] Alexey Troitzky (1866–1942) worked out the general theory, published as a supplement to his *Collection of Chess Studies* (1937).[^s6][^s2] His analysis was one of the findings that showed some won endings need more than fifty moves.[^s2] FIDE's rules reacted: by 1952 the list of positions allowed 100 moves (by prior agreement) included two knights against a pawn safely blocked behind the Troitsky line; in 1989 two knights against a pawn was one of six endings given 75 moves; and by 2001 Article 9.3 allowed 50 moves in all positions.[^s2]

Endgame tables have since measured the ending exactly. Haworth's catalogue of records gives the deepest five-piece KNNKP win as 114 moves to conversion, and it lists separate record positions for the depth to mate under the fifty-move rule.[^s3]

## Connections

Two knights versus pawn is a branch of the chess endgame in which the defender's own pawn defeats the stalemate defence that otherwise holds against two knights.[^s1] Its theory was developed by Troitzky, whose blockade line depends on a knight holding the pawn in place.[^s4][^s6] The length of its wins made it a test case for the fifty-move rule, and endgame tablebases have since mapped its record depths.[^s2][^s3] It is closely related to endgame studies, through which Bolton and Troitzky first explored it, and stands beside the single knight-against-pawn endings.[^s5]

## Sources

[^s1]: José Raúl Capablanca, *Chess Fundamentals* (1921), chapter II, section 14 "The Relative Value of Knight and Bishop", Example 29, Project Gutenberg eBook #33870. https://gutenberg.org/cache/epub/33870/pg33870-images.html (accessed 2026-11-27)
[^s2]: IA Amir Erfan Hashemi, "The Saving 75-move rule", FIDE Arbiters' Commission, April 2023. https://arbiters.fide.com/wp-content/uploads/2023/06/The-Saving-75.pdf (accessed 2026-11-27)
[^s3]: Guy Haworth, "Chess Endgame Records", University of Reading dataset, v7 (2014-08-14). https://reading-9.eprints-hosting.org/34268/2/chessendrecann.pdf (accessed 2026-11-27)
[^s4]: Karsten Müller, "Two knights and a pawn too many", ChessBase News, 21 May 2019. https://en.chessbase.com/newsroom/post/endgame-blog-karsten-mueller-1009e?page=0 (accessed 2026-11-27)
[^s5]: Nagesh Havanur, "Troitzky: In Memoriam", ChessBase News, 21 March 2016. https://en.chessbase.com/post/troitzky-in-memoriam (accessed 2026-11-27)
[^s6]: Sid Pickard, "The Troitzky Line", *Chess Advocate* vol. 7 no. 3, pp. 45-58. https://chessjournalism.org/wp-content/uploads/2023/06/The-Troitzky-Line-by-Sid-Pickard-Chess-Advocate-Volume-7-Number-3-.pages-45-to-58.pdf (accessed 2026-11-27)
