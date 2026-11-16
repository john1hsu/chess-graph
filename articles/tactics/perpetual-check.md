---
id: kt:perpetual-check
type: TacticalMotif
title: Perpetual check
aliases: [Perpetual, Eternal check, Échec perpétuel, Ewiges Schach]
domain: tactics
summary: >-
  A sequence of checks that the defending king cannot escape, so that the checking side can keep
  giving check indefinitely; in practice it ends the game as a draw, by agreement or under the
  repetition rules.
fen: "2k5/pp2n2Q/8/P2p4/6q1/P1p5/2P2PKP/5R2 w - - 1 22"
status: current
volatile: false
verified: 2026-11-16
broader: [kt:chess-tactics, kt:draw]
related: [kt:stalemate, kt:fortress, kt:sacrifice, kt:king-safety, kt:mikhail-tal, kt:bobby-fischer]
relations:
  - {predicate: dependsOn, object: kt:threefold-repetition}
  - {predicate: exemplifiedBy, object: kt:fischer-versus-tal-leipzig-1960}
  - {predicate: contrastsWith, object: kt:checkmate}
sources:
  - id: s1
    title: "Article 9: The Drawn Game"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/article9/
    type: governing-body
    accessed: 2026-11-16
  - id: s2
    title: "Laws of Chess (1997 edition)"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/wp-content/uploads/2022/12/Laws_of_Chess-1997_ENG.pdf
    type: governing-body
    accessed: 2026-11-16
  - id: s3
    title: "Repetition of Position or Moves in Chess"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://www.chesshistory.com/winter/extra/repetition.html
    type: reference
    accessed: 2026-11-16
  - id: s4
    title: "perpetual check"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/perpetual-check
    type: reference
    accessed: 2026-11-16
  - id: s5
    title: "Perpetual Check"
    publisher: Chess.com
    url: https://www.chess.com/terms/perpetual-check-chess
    type: publication
    accessed: 2026-11-16
  - id: s6
    title: "FISCHER.PGN (Fischer game collection; Fischer v Tal, Leipzig Olympiad Finals 1960, round 5)"
    publisher: Chess.iso CD-ROM collection (via Discmaster)
    url: https://discmaster.textfiles.com/view/29139/Chess.iso/Chess/PROGRAMS/BOBBY/BOOKS/FISCHER.PGN
    type: database
    accessed: 2026-11-16
created: 2026-11-16
---

# Perpetual check

A **perpetual check** is a run of checks from which the defending king can never get away: every king move or interposition is answered by another check, so the attacker can repeat the cycle for as long as they like.[^s5] Reference works list it among the ordinary ways a game of chess ends drawn, alongside stalemate and repetition.[^s4] For the side that is losing on material, finding a perpetual is one of the most important saving resources in chess; for the side that is winning, preventing one is part of converting the advantage.[^s5]

## How the rules treat it

The modern FIDE Laws of Chess contain no article called "perpetual check". The draw comes through the repetition rules in Article 9: the player to move can claim a draw when the same position (same side to move, same pieces on the same squares, same possible moves) is about to occur or has occurred for at least the third time, and the game ends automatically once a position has appeared five times.[^s1] An endless series of checks almost always produces exactly such repeated positions, which is why the term survives as a description rather than a rule. The 1997 edition of the Laws likewise handled the situation only through its threefold-repetition article, without naming perpetual check.[^s2]

Older codes did name it. Edward Winter's survey of repetition rules shows that a list of drawing conditions published in *Le Palamède* in 1846 gave persistent perpetual check as a separate ground, explaining that repeating moves amounted to the same thing, and that the German *Schach-Ordnung* of 1858 described perpetual check as a special kind of intentional repetition.[^s3] Winter also documents game 11 of the 1886 world championship, where Zukertort began a series of queen checks from h5 aiming for a draw, and Steinitz wrote that the checks were made with the object of drawing by perpetual check before he deviated.[^s3]

## Key ideas

- **Exposed king, mobile queen.** The classic perpetual is a queen (sometimes with a knight or rook) checking a king whose pawn cover is broken; the king has only two or three squares and the checker can reach a check on each of them.[^s5]
- **Material does not matter.** Because the game is drawn, a player far behind in material can sacrifice to strip the enemy king and then take the perpetual; Chess.com's instructional examples include a side a full rook down saving the game this way.[^s5]
- **Prevention.** The stronger side should look for a square where the king escapes the checks, or a piece that can block a check with tempo; in the same examples a rook interposition or a timely king step ends the series.[^s5]

## Example: Fischer v Tal, Leipzig 1960

At the Leipzig Olympiad of 1960, Bobby Fischer and Mikhail Tal played a wild French Winawer (1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.a3 Ba5 6.b4 cxd4 7.Qg4) that ended in a draw after 21...Qg4+.[^s6][^s5] In the final position (FEN above, White to move), White has an extra rook, but the king on g2 has no shelter. Its only legal move is 22.Kh1, after which 22...Qf3+ leaves 23.Kg1 as the only reply and 23...Qg4+ repeats the position: Black can check for ever, and the game was drawn at that point.[^s6][^s5]

```pgn
[Event "Olympiad Finals"]
[Site "Leipzig"]
[Date "1960"]
[Round "5"]
[White "Robert James Fischer"]
[Black "Mikhail Tal"]
[Result "1/2-1/2"]

1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Ba5 6. b4 cxd4 7. Qg4 Ne7 8. bxa5 dxc3 9. Qxg7 Rg8 10. Qxh7 Nbc6 11. Nf3 Qc7 12. Bb5 Bd7 13. O-O O-O-O 14. Bg5 Nxe5 15. Nxe5 Bxb5 16. Nxf7 Bxf1 17. Nxd8 Rxg5 18. Nxe6 Rxg2+ 19. Kh1 Qe5 20. Rxf1 Qxe6 21. Kxg2 Qg4+ 1/2-1/2
```

## Pitfalls

Defenders sometimes check without first confirming that the king really has no escape route, and a "perpetual" that runs out leaves them simply lost on material.[^s5] Attackers, conversely, can be tempted to play on for a win and end up with nothing; and under the repetition rules a draw claim must follow the procedure in Article 9, so a player who wants the half point should claim it correctly rather than check aimlessly.[^s1]

## Connections

Perpetual check is a **tactical motif** within **chess tactics** and one of the practical routes to a **draw**. It **depends on** **threefold repetition**, the rule that actually ends the game, and it **contrasts with** **checkmate**: the attacker controls the king but cannot trap it.[^s1][^s4] Like **stalemate** and the **fortress**, it is a defensive resource for the weaker side, often reached by a **sacrifice** that wrecks **king safety**.[^s5] It is **exemplified by** the 1960 Leipzig game between **Bobby Fischer** and **Mikhail Tal**.[^s6]

## Sources

[^s1]: FIDE Rules Commission, "Article 9: The Drawn Game". https://rcc.fide.com/article9/ (accessed 2026-11-16)
[^s2]: FIDE Rules Commission, *Laws of Chess* (1997 edition). https://rcc.fide.com/wp-content/uploads/2022/12/Laws_of_Chess-1997_ENG.pdf (accessed 2026-11-16)
[^s3]: Edward Winter, "Repetition of Position or Moves in Chess", Chess Notes. https://www.chesshistory.com/winter/extra/repetition.html (accessed 2026-11-16)
[^s4]: Encyclopaedia Britannica, "perpetual check". https://www.britannica.com/topic/perpetual-check (accessed 2026-11-16)
[^s5]: Chess.com, "Perpetual Check". https://www.chess.com/terms/perpetual-check-chess (accessed 2026-11-16)
[^s6]: FISCHER.PGN, Fischer game collection from the Chess.iso CD-ROM (via Discmaster), game Fischer–Tal, Leipzig Olympiad Finals 1960, round 5. https://discmaster.textfiles.com/view/29139/Chess.iso/Chess/PROGRAMS/BOBBY/BOOKS/FISCHER.PGN (accessed 2026-11-16)
