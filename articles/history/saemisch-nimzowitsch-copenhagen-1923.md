---
id: kt:saemisch-nimzowitsch-copenhagen-1923
type: Game
title: Sämisch versus Nimzowitsch, Copenhagen 1923
aliases: [Immortal Zugzwang Game, Immortal Zugzwang, Saemisch versus Nimzowitsch, Sämisch vs Nimzowitsch, Samisch v Nimzowitsch, Sämisch–Nimzowitsch 1923, Saemisch versus Nimzovich]
domain: history
summary: >-
  Aron Nimzowitsch's 25-move win with Black over Friedrich Sämisch at Copenhagen in March 1923, a
  Queen's Indian in which a queenside blockade and a kingside piece sacrifice left White, with nearly
  every piece still on the board, without a move that did not lose material; known since 1925 as the
  "Immortal Zugzwang Game", though whether the finish is a true zugzwang is disputed.
fen: "6k1/3q2p1/p2bp2p/3p1r2/1p1Pp3/3bQ1PP/PP1B1rB1/1N2R1RK w - - 0 26"
eco: E18
status: historical
volatile: false
verified: 2026-11-21
broader: [kt:zugzwang, kt:hypermodernism]
related: [kt:alekhine-versus-nimzowitsch-san-remo-1930, kt:blockade, kt:queens-indian-defence, kt:emanuel-lasker]
relations:
  - {predicate: playedBy, object: kt:friedrich-saemisch}
  - {predicate: playedBy, object: kt:aron-nimzowitsch}
  - {predicate: playedIn, object: kt:copenhagen-1923}
  - {predicate: exemplifies, object: kt:zugzwang}
sources:
  - id: s1
    title: "Zugzwang"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/zugzwang.html
    type: reference
    accessed: 2026-11-21
  - id: s2
    title: "Aron Nimzowitsch"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/biography/Aron-Nimzowitsch
    type: reference
    accessed: 2026-11-21
  - id: s3
    title: "Nimzowitsch's My System"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://www.chesshistory.com/winter/extra/mysystem.html
    type: reference
    accessed: 2026-11-21
  - id: s4
    title: "Copenhagen (1923), tournament page and crosstable"
    publisher: chessgames.com
    url: https://chessgames.com/perl/chess.pl?tid=80023
    type: database
    accessed: 2026-11-21
  - id: s5
    title: "Friedrich Saemisch vs Aron Nimzowitsch, Copenhagen 1923 (game record)"
    publisher: chessgames.com
    url: https://www.chessgames.com/perl/chessgame?gid=1102400
    type: database
    accessed: 2026-11-21
  - id: s6
    title: "Chess column on the centenary of Nimzowitsch's My System (30 September 2025)"
    publisher: The Washington Times (David R. Sands)
    url: https://m.washingtontimes.com/news/2025/sep/30/100-iconoclasts-system-still-packs-punch/
    type: publication
    accessed: 2026-11-21
created: 2026-11-21
---

# Sämisch versus Nimzowitsch, Copenhagen 1923

**Sämisch versus Nimzowitsch** is the game Aron Nimzowitsch won with Black against Friedrich Sämisch at Copenhagen in March 1923, ending with White's resignation after 25...h6.[^s1] It is famous less for its combinations than for its final position: almost all the pieces are still on the board, yet White has no sensible move that does not lose material. Nimzowitsch himself publicised it in 1925 as a case of zugzwang on a full board, and the nickname "Immortal Zugzwang Game" has stuck ever since, even though several authorities deny that the finish is a zugzwang at all.[^s1]

## The setting

Copenhagen 1923 was a small double round robin of six players held in March 1923.[^s4] Nimzowitsch won it with 8 points from 10, unbeaten, ahead of Savielly Tartakower and Sämisch, who shared second place on 6; Rudolf Spielmann, Egil Jacobsen and Jørgen Møller completed the field.[^s4] The Washington Times columnist David R. Sands describes the game as Nimzowitsch's first big win after the break in international play caused by the First World War.[^s6] The exact date is reported differently: chessgames.com lists it as round 6 on 9 March, while a 1923 report in *Jyllands-Posten*, quoted in Winter's article, puts it on 10 March.[^s5][^s1]

## How the game unfolded

The opening was a Queen's Indian Defence (classified E18) in which White fianchettoed his king's bishop and Black did the same on the queenside.[^s5][^s1] After the exchange 9.cxd5 cxd5 the position looked symmetrical, but Black gained queenside space with ...a6 and ...b5, and after 17...b4 18.Nb1 White's knight was pushed back to its home square, where it stayed for the rest of the game.[^s1] This is the hypermodern recipe Nimzowitsch preached: restrain and blockade first, then strike once the opponent's pieces are tied up.[^s2][^s3]

The turning point is 20.e4, when Black answered with 20...fxe4! and allowed 21.Qxh5, giving up the knight on h5 for two pawns and a crushing grip on the f-file. After 21...Rxf2 the black rooks doubled on the f-file, the bishop on b5 came to d3, and White's queen, rooks and minor pieces were left guarding one another on the first two ranks.[^s1]

```pgn
[Event "Copenhagen"]
[Site "Copenhagen DEN"]
[Date "1923.03.??"]
[Round "6"]
[White "Friedrich Sämisch"]
[Black "Aron Nimzowitsch"]
[Result "0-1"]
[ECO "E18"]

1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 6. Nc3 O-O 7. O-O d5
8. Ne5 c6 9. cxd5 cxd5 10. Bf4 a6 11. Rc1 b5 12. Qb3 Nc6 13. Nxc6 Bxc6
14. h3 Qd7 15. Kh2 Nh5 16. Bd2 f5 17. Qd1 b4 18. Nb1 Bb5 19. Rg1 Bd6
20. e4 fxe4 21. Qxh5 Rxf2 22. Qg5 Raf8 23. Kh1 R8f5 24. Qe3 Bd3 25. Rce1 h6 0-1
```

## The final position

After the quiet 25...h6 (the `fen` above) White's pieces cannot stir without loss. In his notes in *De Telegraaf* of June 1923, Emanuel Lasker remarked that all White's pieces were in effect stalemated, showing that 26.g4 or 26.Kh2 runs into 26...R5f3.[^s1] Sands lists further tries such as 26.Rc1 Re2 and 26.Bf1 Bxf1, each costing material, and quotes Nimzowitsch's point that Black could even shuffle his king while White had to give something up.[^s6] According to *Politiken*, cited by Winter, Sämisch was also in time trouble when he resigned.[^s1]

## Was it really zugzwang?

Nimzowitsch annotated the game in *Wiener Schachzeitung* in 1925 under the heading of zugzwang on a full board, attributing the nickname to Danish chess circles, and *Mein System* calls it widely known as the Immortal Zugzwang Game.[^s1] Winter could find no earlier printed use of the phrase, and he doubts that Lasker coined it as sometimes claimed.[^s1] Wolfgang Heidenfeld argued in 1972 that White would rather move than pass, citing 26.Bc1 Bxb1 27.Rgf1; *The Oxford Companion to Chess* likewise says White is short of a good move rather than in zugzwang, and a reader's analysis printed by Winter treats 25...h6 as a threat, since Black was preparing 26...R5f3 27.Bxf3 Rxf3, winning the queen.[^s1] The lesson survives the definitional debate: a blockade that removes every useful move can be as decisive as a mating attack.

## Connections

The game was **played by** **Friedrich Sämisch** and **Aron Nimzowitsch** and **played in** **Copenhagen 1923**.[^s4][^s5] It is the stock example of **zugzwang** in the middlegame and a showcase of **hypermodernism** and the **blockade**, ideas that Nimzowitsch set out in *My System*, whose first instalment appeared in 1925.[^s1][^s2][^s3] It opened as a **Queen's Indian Defence**, and **Emanuel Lasker** was among its first annotators.[^s5][^s1] Writers have paired it with **Alekhine versus Nimzowitsch, San Remo 1930**, in which Nimzowitsch was on the receiving end of a similar paralysis.[^s1]

## Sources

[^s1]: Edward Winter, "Zugzwang", Chess Notes feature article (1997, with additions). https://chesshistory.com/winter/extra/zugzwang.html (accessed 2026-11-21)
[^s2]: Encyclopaedia Britannica, "Aron Nimzowitsch". https://www.britannica.com/biography/Aron-Nimzowitsch (accessed 2026-11-21)
[^s3]: Edward Winter, "Nimzowitsch's My System", Chess Notes. https://www.chesshistory.com/winter/extra/mysystem.html (accessed 2026-11-21)
[^s4]: chessgames.com, "Copenhagen (1923)", tournament page and crosstable. https://chessgames.com/perl/chess.pl?tid=80023 (accessed 2026-11-21)
[^s5]: chessgames.com, "Friedrich Saemisch vs Aron Nimzowitsch, Copenhagen 1923", game record. https://www.chessgames.com/perl/chessgame?gid=1102400 (accessed 2026-11-21)
[^s6]: David R. Sands, chess column, The Washington Times, 30 September 2025. https://m.washingtontimes.com/news/2025/sep/30/100-iconoclasts-system-still-packs-punch/ (accessed 2026-11-21)
