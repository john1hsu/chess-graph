---
id: kt:novotny-theme
type: ProblemTheme
title: Novotny theme
aliases: [Novotny, Nowotny, Novotny interference, Novotný theme, Novotny (chess problem)]
domain: variants-and-compositions
summary: >-
  A chess problem theme in which White places or sacrifices a piece on the square where the lines of two
  differently moving black pieces, classically a rook and a bishop, cross, so that whichever black piece
  captures it blocks the other; named after the Czech composer Antonín Novotný.
status: current
volatile: false
verified: 2026-11-16
broader: [kt:chess-problems, kt:interference]
related: [kt:endgame-study, kt:sacrifice, kt:chess-composition]
relations:
  - {predicate: namedAfter, object: kt:antonin-novotny}
  - {predicate: contrastsWith, object: kt:grimshaw-theme}
  - {predicate: contrastsWith, object: kt:plachutta-theme}
  - {predicate: usesTechnique, object: kt:interference}
sources:
  - id: s1
    title: "The Novotny and Plachutta Themes in Chess Play"
    publisher: Edward Winter, Chess Notes (updated 24 March 2024)
    url: https://chesshistory.com/winter/extra/novotnyplachutta.html
    type: reference
    accessed: 2026-11-16
  - id: s2
    title: "Chess (Philidor No. 97)"
    publisher: The Spectator, 12 April 1957, page 29 (The Spectator Archive)
    url: https://archive.spectator.co.uk/article/12th-april-1957/30/chess
    type: archive
    accessed: 2026-11-16
  - id: s3
    title: "Jon Speelman: A few patterns"
    publisher: GM Jon Speelman, ChessBase News
    url: https://en.chessbase.com/post/speelman-agony-225
    type: publication
    accessed: 2026-11-16
  - id: s4
    title: "Problem chess: Forgive me interfering, won't you? (part two)"
    publisher: Steve Giddins, ChessBase News (15 August 2011)
    url: https://en.chessbase.com/post/problem-che-forgive-me-interfering-won-t-you-part-two-
    type: publication
    accessed: 2026-11-16
  - id: s5
    title: "Patterns of interference"
    publisher: GM Jon Speelman, ChessBase News
    url: https://en.chessbase.com/post/speelman-agony-183
    type: publication
    accessed: 2026-11-16
  - id: s6
    title: "Novotny"
    publisher: By-Play chess problem blog (kmoen.people.ua.edu)
    url: https://kmoen.people.ua.edu/by-play-blog/novotny
    type: community
    accessed: 2026-11-16
  - id: s7
    title: "The Art of Interference"
    publisher: Mcie, Lichess blog
    url: https://lichess.org/@/Mcie/blog/the-art-of-interference/VqdhinwI
    type: community
    accessed: 2026-11-16
created: 2026-11-16
---

# Novotny theme

The **Novotny** is a classic interference theme of the chess problem. Two black pieces that move in different ways, normally a rook and a bishop, both guard something along lines that cross on one square. White puts a piece on that **cutting point**, usually as a sacrifice. If the rook captures, it now stands in the bishop's way; if the bishop captures, it blocks the rook. Either way Black loses one of the two defences.[^s1][^s2] A 1957 *Spectator* problem column (which spelt it *Nowotny*) treated it as a subdivision of the Grimshaw, with White's key going to the square where the black lines intersect.[^s2]

## Origin and name

The theme is named after **Antonín Novotný** (1827–1871), a Czech problem composer and lawyer, who used it in a problem published in 1854.[^s3][^s5] Jon Speelman notes that the Englishman Henry Turton had shown the idea about three years earlier, but the name stuck to Novotný.[^s3]

## How it works

A Novotny needs a white **double threat**, each half parried by a different black line piece, and a crossing square shared by both lines. The key typically places a white piece on that square and creates both threats at once. Capturing it is Black's most natural reply, but each capture shuts off the other defender, so White carries out whichever threat is no longer covered.[^s6] If Black ignores the piece, the threats still stand.[^s6]

Problemists distinguish the Novotny from its neighbours by two questions: *do the two black pieces move alike or differently,* and *is there a white sacrifice on the cutting point?* Following the problemist Luc Winants, Edward Winter's notes set out four related themes:[^s1]

- **Grimshaw:** two unlike pieces (rook and bishop) interfere with each other, with no white sacrifice.[^s1]
- **Novotny:** two unlike pieces, with a white sacrifice on the cutting point.[^s1]
- **Wurzburg-Plachutta:** two pieces moving alike interfere, with no sacrifice.[^s1]
- **Plachutta:** two pieces moving alike, with a white sacrifice on the cutting point.[^s1]

Winants regards the Plachutta as related to the Novotny but not as a sub-category of it.[^s1]

## In problems and studies

Because a single Novotny is now nearly two centuries old, the bare theme is rarely enough for a prize; composers combine or multiply it.[^s6] Comins Mansfield's mate-in-two that won first prize in *Die Schwalbe* in 1956 stacks black rooks and bishops on the h-file, the "organ pipes" arrangement first shown by Sam Loyd in 1859, so that rook-and-bishop interferences are possible on both g3 and g4. Steve Giddins presents it as a fourfold Novotny. Tries such as 1.g4? and 1.g3? each fail to a single defence, and the key is 1.f3!.[^s4] The idea can also be reversed. In Hans-Peter Rehm's mate-in-four (first prize, *Themes-64*, 1959), Black's knight defends by going to the square where a white bishop's and rook's lines cross, a black Novotny against White.[^s4]

The theme also appears in endgame studies; Speelman cites a study by Pal Benko in which White must manoeuvre before the decisive Novotny is possible.[^s3]

## Over the board

In tournament play the Novotny is rare, and many "practical Novotnys" are really deflections with a Novotny element. In some lines a line is blocked, but in others a piece is simply drawn away from its duty.[^s5] Speelman notes that the Swedish grandmaster Emanuel Berg missed a well-known one.[^s3] Classification causes confusion. Tarrasch's game against consultants at Naples in 1914, where a bishop lands on the crossing of a black queen's and rook's lines, is described by one Lichess author as the most famous Novotny in a real game.[^s7] Winter's correspondents instead treat it as the standard practical example of the related **Plachutta**.[^s1] In that position the two defenders, a queen on d7 and a rook on c8, both guard along a rank or file.[^s7]

## Pitfalls for solvers

The first clue is a white double threat whose two halves are stopped by unlike black line pieces: look for where their lines cross.[^s6] Do not assume every sacrifice on a crossing square is a Novotny. If the two defenders move alike, it is a Plachutta, and if a capture merely forks or removes a guard without blocking a line, it is something else.[^s1][^s5]

## Connections

The Novotny belongs to the family of **interference** themes in **chess problems**, and it uses a **sacrifice** to force the interference.[^s1][^s2] It is **named after** Antonín Novotný.[^s3] It **contrasts with** the **Grimshaw**, where Black interferes voluntarily without a white sacrifice, and with the **Plachutta**, where the two defenders move alike.[^s1][^s2] It also appears in **endgame studies** and, occasionally, in games.[^s3][^s5]

## Sources

[^s1]: Edward Winter, "The Novotny and Plachutta Themes in Chess Play", Chess Notes. https://chesshistory.com/winter/extra/novotnyplachutta.html (accessed 2026-11-16)
[^s2]: "Chess" (Philidor No. 97), The Spectator, 12 April 1957, p. 29. https://archive.spectator.co.uk/article/12th-april-1957/30/chess (accessed 2026-11-16)
[^s3]: Jon Speelman, "A few patterns", ChessBase News. https://en.chessbase.com/post/speelman-agony-225 (accessed 2026-11-16)
[^s4]: Steve Giddins, "Problem chess: Forgive me interfering, won't you? (part two)", ChessBase News, 15 August 2011. https://en.chessbase.com/post/problem-che-forgive-me-interfering-won-t-you-part-two- (accessed 2026-11-16)
[^s5]: Jon Speelman, "Patterns of interference", ChessBase News. https://en.chessbase.com/post/speelman-agony-183 (accessed 2026-11-16)
[^s6]: "Novotny", By-Play chess problem blog. https://kmoen.people.ua.edu/by-play-blog/novotny (accessed 2026-11-16)
[^s7]: Mcie, "The Art of Interference", Lichess blog. https://lichess.org/@/Mcie/blog/the-art-of-interference/VqdhinwI (accessed 2026-11-16)
