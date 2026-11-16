---
id: kt:grimshaw-theme
type: ProblemTheme
title: Grimshaw theme
aliases: [Grimshaw, Grimshaw interference, Grimshaw (chess problem), Mutual interference, Pawn Grimshaw]
domain: variants-and-compositions
summary: >-
  A chess problem theme in which two black line pieces of different kinds, classically a rook and a bishop,
  each block the other's line by moving to the square where their lines cross, so that each defence lets
  in a different white mate; named after the English composer Walter Grimshaw.
fen: "B5Q1/B3P1K1/4p3/4p3/bb6/R4P2/3R3P/2r1N1Nk w - - 0 1"
status: current
volatile: false
verified: 2026-11-16
broader: [kt:chess-problems, kt:interference]
related: [kt:chess-composition, kt:helpmate]
relations:
  - {predicate: namedAfter, object: kt:walter-grimshaw}
  - {predicate: contrastsWith, object: kt:novotny-theme}
  - {predicate: usesTechnique, object: kt:interference}
sources:
  - id: s1
    title: "Grimshaw v Steinitz"
    publisher: Edward Winter, Chess Notes (2011, updated 2025)
    url: https://www.chesshistory.com/winter/extra/grimshawsteinitz.html
    type: reference
    accessed: 2026-11-16
  - id: s2
    title: "Chess (Philidor No. 97)"
    publisher: The Spectator, 12 April 1957, page 29 (The Spectator Archive)
    url: https://archive.spectator.co.uk/article/12th-april-1957/30/chess
    type: archive
    accessed: 2026-11-16
  - id: s3
    title: "Grimshaw Problem Theme"
    publisher: Stephen John Mann, Yorkshire Chess History (2012)
    url: https://mannchess.org.uk/Made%20in%20Yorkshire/Grimshaw%20Problem%20Theme.htm
    type: publication
    accessed: 2026-11-16
  - id: s4
    title: "Grimshaw"
    publisher: Peter Wong, OzProblems, Problem World
    url: https://www.ozproblems.com/problem-world/grimshaw
    type: community
    accessed: 2026-11-16
  - id: s5
    title: "The Problemist Diary Part III: Understanding the Grimshaw"
    publisher: Satanick Mukhuty, ChessBase India (20 May 2019)
    url: https://chessbase.in/news/Understanding-the-Grimshaw
    type: publication
    accessed: 2026-11-16
  - id: s6
    title: "Problem chess: Forgive me interfering, won't you?"
    publisher: Steve Giddins, ChessBase News (31 July 2011)
    url: https://en.chessbase.com/post/problem-che-forgive-me-interfering-won-t-you-
    type: publication
    accessed: 2026-11-16
created: 2026-11-16
---

# Grimshaw theme

The **Grimshaw** is one of the oldest and best-known themes of the chess problem. Two black pieces that move along lines in different ways, normally a rook and a bishop, both have access to the square where their lines cross. Whichever of them goes there cuts off the other, and White mates by exploiting the line that has just been closed.[^s2][^s4] Edward Winter describes it as reciprocal interference between two pieces of unlike motion.[^s1]

## Origin

The theme is named after the English composer **Walter Grimshaw** (1832–1890).[^s1][^s5] His mate-in-five, published in the *Illustrated London News* on 24 August 1850, is regarded as the first problem composed deliberately to show it.[^s1] In that problem a black rook and bishop both defend from e6. After the key and Black's capture of the bishop, the play turns on the fact that 2...Re6 and 2...Be6 each shut off the other piece, so White can break through.[^s3] Winter notes a French reference work crediting an earlier, unintentional example by Brede from 1844, while still treating Grimshaw's 1850 problem as the first deliberate one.[^s1]

## How it works

A Grimshaw needs three ingredients. There must be a **critical square** where a black orthogonal line and a black diagonal line intersect. Both pieces must have a reason to go there, usually because a White threat or zugzwang forces Black to move something. And each arrival must cost Black a different defence, so that White answers with a **different mate** after each.[^s4][^s6] Composers prize the pairing: two black moves to the same square, two white mates, each mate made possible only by the interference.[^s6]

Two-movers often show the theme in a **waiting-move** setting. In Lev Loshinsky's 1930 two-mover the key 1.Bb3 changes nothing, and Black's own moves create the weaknesses. 1...Rb7 is answered by 2.Rc6 and 1...Bb7 by 2.Re7, and a second Grimshaw on g7 follows (1...Bg7 2.Qxf7, 1...Rg7 2.Qe5).[^s4][^s6] The same composer showed three separate Grimshaws in one position in another 1930 problem.[^s6]

## Variants of the idea

- **Pawn Grimshaw.** A pawn can take part if it still stands on its starting rank. A black piece landing on the square in front of it stops the double step, and the pawn's double step can in turn block a piece's line.[^s4] ChessBase India gives the names *Pickabish* (pawn and bishop), *Nesic* (pawn and rook) and *Kubbel* (pawn and queen) to these forms.[^s5]
- **Helpmate Grimshaws.** In helpmates the interference is cooperative. Black blocks his own line to make room for a White mate, and the two solutions often show the rook and bishop interferences in turn.[^s4]
- **Novotny.** If White *sacrifices* a piece on the critical square, whichever black piece captures it blocks the other. That forced form is the Novotny, which an English column of 1957 described as a subdivision of the Grimshaw.[^s2][^s6]

## Example

The diagram position is Sergey Pugachev's mate-in-three, which won first prize in 1950.[^s5] White's king on g7 blocks the queen's route to g2 but cannot simply step aside, because each flight square allows a bishop or rook check. The key **1.h4!** threatens 2.f4+ and 3.Rh3#. Black's defences put the c1-rook and a bishop on the same squares in turn. After 1...Rc5 the rook cuts the b4-bishop off from e7, so 2.Kf6 is safe. After 1...Bc5 the bishop cuts the rook off from c8, so 2.Kh8 works. The pairs 1...Rc3/1...Bc3 and 1...Rc6/1...Bc6 work the same way. In every case 3.Qg2# follows.[^s5]

## Typical pitfalls

For the solver, the first thing to notice is the crossing square: once it is seen, the black defences and the white mates usually follow.[^s4] For the composer, the key must not spoil the set play. In Loshinsky's problem the only key that works is the one waiting move that leaves every prepared Grimshaw variation intact.[^s4][^s6] In Isaac Birbrager's 1948 two-mover the tries 1.Be4? and 1.Re4? each fail to one half of the black Grimshaw on d2, while the key 1.Bh7! answers both halves.[^s6] Tries of this kind show that one side of a Grimshaw can also defend, and they are part of the solver's work.[^s4][^s6]

## Connections

The Grimshaw is a problem form of the tactical motif of **interference**, and it sits among the themes of **chess problems** and wider **chess composition**.[^s2][^s6] It is **named after** Walter Grimshaw.[^s1] It **contrasts with** the **Novotny**, where the interference is forced by a White sacrifice on the critical square instead of chosen by Black.[^s2][^s6] Composers also use it in **helpmates**, and pawn forms of it involve the pawn's double step.[^s4][^s5] The theme dates from 1850, which makes it one of the oldest named ideas in problem composition.[^s1][^s3]

## Sources

[^s1]: Edward Winter, "Grimshaw v Steinitz", Chess Notes. https://www.chesshistory.com/winter/extra/grimshawsteinitz.html (accessed 2026-11-16)
[^s2]: "Chess" (Philidor No. 97), The Spectator, 12 April 1957, p. 29. https://archive.spectator.co.uk/article/12th-april-1957/30/chess (accessed 2026-11-16)
[^s3]: Stephen John Mann, "Grimshaw Problem Theme", Yorkshire Chess History. https://mannchess.org.uk/Made%20in%20Yorkshire/Grimshaw%20Problem%20Theme.htm (accessed 2026-11-16)
[^s4]: Peter Wong, "Grimshaw", OzProblems, Problem World. https://www.ozproblems.com/problem-world/grimshaw (accessed 2026-11-16)
[^s5]: Satanick Mukhuty, "The Problemist Diary Part III: Understanding the Grimshaw", ChessBase India, 20 May 2019. https://chessbase.in/news/Understanding-the-Grimshaw (accessed 2026-11-16)
[^s6]: Steve Giddins, "Problem chess: Forgive me interfering, won't you?", ChessBase News, 31 July 2011. https://en.chessbase.com/post/problem-che-forgive-me-interfering-won-t-you- (accessed 2026-11-16)
