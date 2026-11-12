---
id: kt:correspondence-chess
type: Concept
title: Correspondence chess
aliases: [Correspondence Chess, Postal chess, Chess by mail, Email chess, Server chess, CC, Fernschach]
domain: variants-and-compositions
summary: >-
  Chess played at a distance, with moves sent by messenger, post, email or (today) a game server, and
  with days rather than minutes per move; players may consult books, databases and, under current
  ICCF rules, chess engines, but not other people.
status: current
volatile: true
verified: 2026-11-12
broader: [kt:chess]
related: [kt:chess-titles, kt:endgame-tablebases, kt:computer-chess, kt:fifty-move-rule]
relations:
  - {predicate: sanctionedBy, object: kt:iccf}
  - {predicate: contrastsWith, object: kt:fide-laws-of-chess}
  - {predicate: championedBy, object: kt:paul-keres}
sources:
  - id: s1
    title: "Correspondence chess"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/correspondence-chess
    type: reference
    accessed: 2026-11-12
  - id: s2
    title: "ICCF Rules (valid from 1 January 2025)"
    publisher: International Correspondence Chess Federation (copy hosted by the Czech correspondence chess association SKSČR)
    url: https://skscr.cz/wp-content/uploads/2025/01/2025-ICCF-Rules-.pdf
    type: governing-body
    accessed: 2026-11-12
  - id: s3
    title: "ICCF Rules (valid from 1 December 2022)"
    publisher: International Correspondence Chess Federation
    url: https://webfiles.iccf.com/rules/2023/2023%20ICCF%20Rules%20%20-%20final.pdf
    type: governing-body
    accessed: 2026-11-12
  - id: s4
    title: "Correspondence Chess (Chess Notes feature)"
    publisher: Edward Winter, Chess History
    url: https://chesshistory.com/winter/extra/correspondencechess.html
    type: publication
    accessed: 2026-11-12
  - id: s5
    title: "L'histoire de l'ICCF (Alain Rogemont, trad. Jean-François Épinoux)"
    publisher: AJEC (Association des Joueurs d'Échecs par Correspondance)
    url: https://ajec-echecs.org/2024/02/08/lhistoire-de-liccf-traduit-par-jean-francois-epinoux/?print=pdf
    type: publication
    accessed: 2026-11-12
created: 2026-11-12
---

# Correspondence chess

Correspondence chess is chess played at a distance rather than across a board. Its defining difference from over-the-board play is that players may study the position at leisure, moving the pieces on an analysis board and consulting reference books, which over-the-board rules forbid.[^s1] The game itself follows the ordinary rules of chess; what changes is the medium, the time scale and what help a player may use.

## History

Games conducted by messengers who carried the moves go back at least to the 17th century, and cheap postal services produced a boom in postal chess in the early 19th century.[^s1] Club matches by mail were already under way in America in 1838–39, when New York and Washington clubs played each other, and the game between the brothers Karl and Francis Eugene Brenzinger, begun in 1859 and finished on 18 March 1875, is often cited as the longest game by elapsed time.[^s4] Strong masters took part: Steinitz and Chigorin played a cable match in 1890–91, and Paul Keres was playing about 70 postal games at once when he won the IFSB championship in 1935.[^s4]

Organised international play began with the Internationaler Fernschachbund (IFSB), founded in 1928 as the first international correspondence chess league. Its successor, the International Correspondence Chess Association, was formed in 1945 and reorganised in 1951 as the International Correspondence Chess Federation (ICCF), which runs the world championship and international events today.[^s5]

## How it is played today

Almost all ICCF play now takes place on its web server. As of the rules valid from 1 January 2025, the standard time control gives each player 50 days for every 10 moves, cumulatively; time is counted in whole days, the first 24 hours of reflection on a move are free, and beyond 20 days on a single move each extra day counts double.[^s2] Each player may also take up to 45 days of leave per calendar year, during which the clock stops.[^s2] A faster "Triple Block" format uses a clock with a per-move increment and a bank of days instead.[^s3] A player who runs out of time loses the game and is barred from entering new server events for a period.[^s3] For a server event to be rated, it must allow at least 150 days of reflection for 50 moves.[^s3]

Conditional moves ("if you play X, I reply Y") are allowed in all international events begun since 1 January 2020 and are binding until the opponent plays something else.[^s2][^s3]

## Engines and assistance

The most important modern rule is §2.2.6: before choosing a move, a player may consult any publicly available source, explicitly including chess engines, books, game databases and endgame tablebases, but may not consult another person about a live game; only team-mates in team events may confer.[^s2] Britannica notes that by the 1990s most serious postal players used computers, which it describes as a major problem for the form.[^s1] ICCF's answer was to legalise engines, so that skill now lies in steering the analysis: choosing which lines to examine deeply, judging positions engines misread, and managing dozens of games and the clock across months.

Tablebases are written into the rules. A player may claim a result from a 7-piece tablebase position, and a tablebase win overrides the fifty-move rule; such claims, like repetition and fifty-move claims, must be made before a move is entered, not after.[^s2]

## Example

Correspondence chess has its own traps for the careless. In a 1930 postal game recorded by Edward Winter, A. M. Warren fell for a Budapest Defence trick against Jan Selman: after 6.g3? Nxf2, White resigned, because 7.Kxf2 Bxg3+ is a check that also opens the d-file, so Black wins the queen on d1.[^s4]

```pgn
[Event "Correspondence"]
[Date "1930.??.??"]
[White "A. M. Warren"]
[Black "Jan Selman"]
[Result "0-1"]

1. d4 Nf6 2. c4 e5 3. dxe5 Ne4 4. a3 d6 5. exd6 Bxd6 6. g3 Nxf2 0-1
```

## Pitfalls for newcomers

Common errors are practical rather than theoretical: losing on time through the doubled-day count, forgetting to register leave in advance, entering a move before making a tablebase or repetition claim (which forfeits the claim), and taking on more games than one can analyse properly.[^s2][^s3]

## Connections

Correspondence chess is a form of **chess** played under the rules of the **ICCF** rather than the over-the-board **FIDE Laws of Chess**, with which it contrasts on time limits and outside help.[^s2][^s5] ICCF awards its own **chess titles**, separate from FIDE's. Its rules lean directly on **computer chess** and **endgame tablebases**, and modify the **fifty-move rule** where a tablebase decides the result.[^s2] **Paul Keres** is the best-known world-class player who also excelled by post.[^s4]

## Sources
[^s1]: Encyclopaedia Britannica, "Correspondence chess". https://www.britannica.com/topic/correspondence-chess (accessed 2026-11-12)
[^s2]: International Correspondence Chess Federation, "ICCF Rules" (valid from 1 January 2025), §2.2.6, §2.4, §2.5, §2.7, §2.10. https://skscr.cz/wp-content/uploads/2025/01/2025-ICCF-Rules-.pdf (accessed 2026-11-12)
[^s3]: International Correspondence Chess Federation, "ICCF Rules" (valid from 1 December 2022), §1.4.2, §2.4. https://webfiles.iccf.com/rules/2023/2023%20ICCF%20Rules%20%20-%20final.pdf (accessed 2026-11-12)
[^s4]: Edward Winter, "Correspondence Chess", Chess Notes. https://chesshistory.com/winter/extra/correspondencechess.html (accessed 2026-11-12)
[^s5]: AJEC, "L'histoire de l'ICCF" (Alain Rogemont, translated by Jean-François Épinoux), 8 February 2024. https://ajec-echecs.org/2024/02/08/lhistoire-de-liccf-traduit-par-jean-francois-epinoux/?print=pdf (accessed 2026-11-12)
