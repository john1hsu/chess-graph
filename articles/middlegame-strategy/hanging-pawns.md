---
id: kt:hanging-pawns
type: PawnStructure
title: Hanging pawns
aliases: [Hanging pawn pair, Hanging c- and d-pawns, Hängende Bauern]
domain: middlegame-strategy
summary: >-
  A pawn structure in which one side has two pawns side by side on adjacent half-open files,
  typically c5 and d5 (or c4 and d4), with no friendly pawns on the neighbouring files; they
  give space and dynamic potential but can only be defended by pieces.
fen: "rnr3k1/4qpp1/p3b2p/1Bpp4/8/Q3PN2/PP3PPP/2R1K2R w K - 0 16"
status: current
volatile: false
verified: 2026-11-12
broader: [kt:pawn-structure]
related: [kt:isolated-queens-pawn, kt:blockade, kt:queens-gambit-declined, kt:queens-gambit, kt:fischer-spassky-1972]
relations:
  - {predicate: contrastsWith, object: kt:isolated-queens-pawn}
  - {predicate: exemplifiedBy, object: kt:fischer-spassky-1972-game-6}
  - {predicate: leadsTo, object: kt:passed-pawn}
sources:
  - id: s1
    title: "Hanging Pawns in Chess"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/hangingpawns.html
    type: reference
    accessed: 2026-11-12
  - id: s2
    title: "How to Play the Queen's Gambit (Games 10-12)"
    publisher: Garry Kasparov, ChessBase Books
    url: https://books.chessbase.com/perma/c/68945b8ee30c7d2f77098b5a
    type: book
    accessed: 2026-11-12
  - id: s3
    title: "50 years ago today: Fischer-Spassky, game six"
    publisher: Frederic Friedel and Nagesh Havanur, ChessBase News
    url: https://en.chessbase.com/post/50-years-ago-today-fischer-spassky-game-six
    type: publication
    accessed: 2026-11-12
  - id: s4
    title: "Hanging Pawns"
    publisher: Chess.com (Chess Terms)
    url: https://www.chess.com/terms/hanging-pawns-chess
    type: publication
    accessed: 2026-11-12
  - id: s5
    title: "The fight against hanging pawns"
    publisher: GM Matthew Sadler
    url: https://matthewsadler.me.uk/the-middlegame/fight-hanging-pawns/
    type: publication
    accessed: 2026-11-12
  - id: s6
    title: "Hanging pawns"
    publisher: English Chess Federation (Substack)
    url: https://englishchessfederation.substack.com/p/hanging-pawns
    type: publication
    accessed: 2026-11-12
created: 2026-11-12
---

# Hanging pawns

Hanging pawns are two pawns of the same colour standing side by side on adjacent files, with no friendly pawns on the files next to them, so that no pawn can ever protect them and they rely on pieces for defence.[^s4][^s6] By far the most common case is a pair on the c- and d-files, such as Black pawns on c5 and d5 facing half-open c- and d-files.[^s4][^s2] Kasparov describes such central pawns as potentially powerful if they can advance but exposed to pressure from well-placed enemy pieces.[^s2]

## Origins of the term

The idea is older than the name. In 1883 Wilhelm Steinitz, annotating Mason–Zukertort, already judged that a pair of centre pawns without neighbours was weaker than it looked.[^s1] Reference works have credited Steinitz with coining the phrase and Aron Nimzowitsch with popularising it, but Edward Winter found no use of it in Steinitz's own writings. The earliest instance he traced is the German *hängende Bauern* in the *Wiener Schachzeitung* of 1902; Tarrasch used it in his book on St Petersburg 1914, and Maróczy's book of London 1922 is the earliest English example Winter gives.[^s1]

## How they arise

Hanging pawns typically appear after exchanges in queen's-pawn openings: the Queen's Gambit Declined (notably the Tartakower Variation), the Queen's Indian, the Nimzo-Indian and the Symmetrical English.[^s4][^s2] In the Fischer–Spassky example below, the pair is born when White exchanges on c5 and Black recaptures with the b-pawn, bringing a second pawn next to the d-pawn.[^s3] Kasparov's chapter on the Tartakower traces the same structure through Korchnoi–Karpov (1981) and Karpov–Kasparov (1984).[^s2]

## Plans for the side with the pawns

- **Keep pieces on.** The pawns are supported by pieces, so their owner generally avoids simplification.[^s4][^s6]
- **Use the space.** The side with the pair usually has more space and should develop its pieces behind the pawns.[^s4]
- **Advance at the right moment.** A timely ...d4 or ...c4 opens the position for an attack or creates a passed pawn; the pawns only work when backed by active pieces.[^s4][^s6]

## Plans against them

- **Pressure both pawns.** Rooks on the half-open c- and d-files, a bishop on the long diagonal and a knight that can switch between targets keep the defender's pieces tied down.[^s5]
- **Blockade, then attack.** Stopping the pawns on their squares and then targeting them is the standard recipe.[^s4]
- **Strike with a pawn break.** Moves such as e4 or b4 attack the pair from the side and can break it up before it becomes mobile.[^s5][^s6]
- **Exchange pieces.** Fewer defenders make the pawns easier to win.[^s4]

Karpov was a well-known practitioner of the patient, piece-based approach against the c5/d5 pair.[^s2] In Bogoljubow–Réti (London 1927) Sadler shows how a knight route to f4, aimed at d5, decided the game.[^s5]

## Example: Fischer–Spassky, game 6, 1972

In game six of the 1972 world championship match, a Tartakower Queen's Gambit Declined, Spassky accepted hanging pawns on c5 and d5 after 15.dxc5 bxc5 (the diagram position).[^s3][^s6] Fischer exchanged his knight for Black's light-squared bishop, then struck with 20.e4. Commentators judged that this probed Black's centre at its weakest point; after 20...d4 the pawns were fixed, and White turned to a kingside attack with f4–f5 on an open f-file.[^s3] Chess.com cites the game as a model of blockading and then attacking the pair.[^s4]

```pgn
[Event "World Championship"]
[Site "Reykjavik"]
[Date "1972.07.23"]
[Round "6"]
[White "Robert James Fischer"]
[Black "Boris Spassky"]
[Result "1-0"]
[ECO "D59"]

1. c4 e6 2. Nf3 d5 3. d4 Nf6 4. Nc3 Be7 5. Bg5 O-O 6. e3 h6 7. Bh4 b6 8. cxd5 Nxd5 9. Bxe7 Qxe7 10. Nxd5 exd5 11. Rc1 Be6 12. Qa4 c5 13. Qa3 Rc8 14. Bb5 a6 15. dxc5 bxc5 16. O-O Ra7 17. Be2 Nd7 18. Nd4 Qf8 19. Nxe6 fxe6 20. e4 d4 21. f4 Qe7 22. e5 Rb8 23. Bc4 Kh8 24. Qh3 Nf8 25. b3 a5 26. f5 exf5 27. Rxf5 Nh7 28. Rcf1 Qd8 29. Qg3 Re7 30. h4 Rbb7 31. e6 Rbc7 32. Qe5 Qe8 33. a4 Qd8 34. R1f2 Qe8 35. R2f3 Qd8 36. Bd3 Qe8 37. Qe4 Nf6 38. Rxf6 gxf6 39. Rxf6 Kg8 40. Bc4 Kh8 41. Qf4 1-0
```

## Pitfalls

The most common error for the owner is passivity: pawns that merely occupy space while the pieces defend them tend to be ground down.[^s5][^s6] Sadler's example shows the same danger from the defending side: a passive retreat in Bogoljubow–Réti cost Black a pawn.[^s5] Seirawan's rule of thumb, quoted by Winter, captures the balance: hanging pawns that can be attacked and forced to move are weak, while those that can be held in place are strong.[^s1]

## Connections

Hanging pawns are a type of **pawn structure** and are contrasted with the **isolated queen's pawn**: both stand on half-open files and must be defended by pieces, but the hanging pair has two pawns that can take turns advancing.[^s4][^s6] Play against them relies on **blockade**, and a successful advance by their owner can **lead to a passed pawn**.[^s4] They are typical of the **Queen's Gambit Declined**, an offshoot of the **Queen's Gambit**, and are exemplified by game six of **Fischer–Spassky 1972**.[^s2][^s3]

## Sources
[^s1]: Edward Winter, "Hanging Pawns in Chess", Chess Notes. https://chesshistory.com/winter/extra/hangingpawns.html (accessed 2026-11-12)
[^s2]: G. Kasparov, *How to Play the Queen's Gambit*, ChessBase Books, games 10–12. https://books.chessbase.com/perma/c/68945b8ee30c7d2f77098b5a (accessed 2026-11-12)
[^s3]: F. Friedel and N. Havanur, "50 years ago today: Fischer-Spassky, game six", ChessBase News. https://en.chessbase.com/post/50-years-ago-today-fischer-spassky-game-six (accessed 2026-11-12)
[^s4]: Chess.com, "Hanging Pawns", Chess Terms. https://www.chess.com/terms/hanging-pawns-chess (accessed 2026-11-12)
[^s5]: M. Sadler, "The fight against hanging pawns". https://matthewsadler.me.uk/the-middlegame/fight-hanging-pawns/ (accessed 2026-11-12)
[^s6]: English Chess Federation, "Hanging pawns". https://englishchessfederation.substack.com/p/hanging-pawns (accessed 2026-11-12)
