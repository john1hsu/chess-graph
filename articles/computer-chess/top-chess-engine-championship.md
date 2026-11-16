---
id: kt:top-chess-engine-championship
type: Event
title: Top Chess Engine Championship
aliases: [TCEC, Thoresen Chess Engines Competition, nTCEC, TCEC Superfinal]
domain: computer-chess
summary: >-
  A continuously running online competition for chess engines, founded by Martin Thoresen in 2010 and
  hosted by Chessdom since season 8, in which engines climb a ladder of divisions on fixed hardware and
  from assigned openings until the top two meet in a 100-game Superfinal.
status: current
volatile: true
verified: 2026-11-16
broader: [kt:computer-chess, kt:chess-tournament]
related: [kt:leela-chess-zero, kt:opening-book, kt:endgame-tablebases, kt:nnue, kt:chess960]
relations:
  - {predicate: wonBy, object: kt:stockfish}
  - {predicate: organizedBy, object: kt:chessdom}
  - {predicate: usesTechnique, object: kt:opening-book}
sources:
  - id: s1
    title: "TCEC Openings FAQ"
    publisher: Top Chess Engine Championship (tcec-chess.com)
    url: https://tcec-chess.com/articles/TCEC_Openings_FAQ.html
    type: official-project
    accessed: 2026-11-16
  - id: s2
    title: "TCEC15: the 15th Top Chess Engine Championship (ICGA Journal 41(3), 2019)"
    publisher: G. McC. Haworth and N. Hernandez (University of Reading repository)
    url: https://reading-9.eprints-hosting.org/83156/1/TCEC15.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "TCEC Cup 7 (ICGA Journal 42(4), 2020)"
    publisher: G. McC. Haworth and N. Hernandez, IOS Press
    url: https://content.iospress.com/articles/icga-journal/icg200174
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s4
    title: "TCEC"
    publisher: Chess Programming Wiki
    url: https://www.chessprogramming.org:443/TCEC
    type: community
    accessed: 2026-11-16
  - id: s5
    title: "Stockfish claims its 19th TCEC title defeating Reckless in the Superfinal"
    publisher: Chessdom
    url: https://www.chessdom.com/stockfish-claims-its-19th-tcec-title-defeating-reckless-in-the-superfinal/
    type: publication
    accessed: 2026-11-16
  - id: s6
    title: "TCEC Season 30, Swiss10, Game 624 (1 November 2026)"
    publisher: TCEC BayesElo (Chessdom)
    url: https://tcecbayeselo.chessdom.org/2026/11/01/tcec-season-30-swiss10-game-624-stockfish-dev-20260930-m-49ea5ded-obsidian-dev-16-15/
    type: primary-record
    accessed: 2026-11-16
created: 2026-11-16
---

# Top Chess Engine Championship

The Top Chess Engine Championship (TCEC) is the best-known long-time-control competition between chess programs. Its first season ran from December 2010 to February 2011 under the name Thoresen Chess Engines Competition, after its organiser and host Martin Thoresen; it was relaunched in January 2013, joined forces with Chessdom from season 5, took its present name before season 8 in 2015, and has since been hosted by Chessdom's Anton Mihailov.[^s4] Because every engine runs on the same server, at slow time controls, with games broadcast live, its Superfinal is widely treated as the unofficial championship of computer chess, and its results are written up season by season in the ICGA Journal.[^s2][^s3]

## How a season works

A season is a ladder. Engines enter at the bottom and are promoted or relegated by results through a series of round-robin divisions, with longer time controls the higher they climb. In season 15, for example, 44 engines started; the lower divisions played at 30 minutes plus 5 seconds per move, the Premier Division played three double round robins at 90+5, and the Superfinal was 100 games at 120 minutes plus 10 seconds per move.[^s2] Ties in a division are broken first by crashes, then by wins and Sonneborn-Berger score, following FIDE's order of tie-break priorities.[^s2] Alongside the main ladder, TCEC runs knockout Cups (TCEC Cup 7 in October 2020 had 32 engines in best-of-four rapid matches) and side events such as Swiss tournaments and Fischer Random competitions.[^s3][^s5]

Hardware is fixed by the organisers rather than by the engine authors. The season 15 report describes a 44-core main server with endgame tablebases on solid-state storage, plus a separate GPU machine for neural-network engines such as Leela Chess Zero.[^s2] Games can be adjudicated once the position is in tablebase territory, so engines are not asked to play out known wins and draws.[^s2]

## Forced openings

The feature that most distinguishes TCEC from engine self-play is that engines do not choose their own openings. The organisers argue that from the initial position strong engines at long time controls would mostly draw and keep repeating the same lines, so each game starts from an assigned position.[^s1] Lower leagues draw randomly from short books of four to eight moves, while the Superfinal uses a fresh book of 50 positions chosen by Jeroen Noomen; Nelson Hernandez selects the openings for every other stage.[^s1] Each opening is played twice in consecutive games with colours reversed, so a lopsided position does not decide a match by luck, and that is why a Superfinal is exactly 100 games.[^s1]

The positions are deliberately unbalanced. Hernandez aims for engine evaluations of roughly half a pawn to eight-tenths of a pawn in the Premier League, and Noomen sometimes exceeds a full pawn and includes gambits, with a target draw rate of 65–80% in the Superfinal.[^s1] The organisers openly accept that engines would rarely reach these positions themselves; the point is to test understanding across many structures rather than an engine's own preparation.[^s1]

## Results and eras

The early seasons were won by Houdini and Komodo, with Stockfish first taking the title in season 6 (2014).[^s4] Leela Chess Zero, a neural-network engine trained by self-play, beat Stockfish 53½–46½ in the season 15 Superfinal in 2019, the first TCEC title for an engine of that kind.[^s2] It won again in season 17, but from season 18 onwards Stockfish won one Superfinal after another, while efficiently updatable neural network (NNUE) evaluation spread through the field from 2020.[^s4][^s3] In season 29, played in the first months of 2026, the newcomer Reckless broke the long run of Stockfish–Leela finals; Stockfish beat it 59–41 for its 19th title, the most in TCEC history.[^s5] As of November 2026 season 30 was in progress, with Swiss events being played on 1 November.[^s6]

## Why it matters to a chess player

For a club player TCEC is a free library of very high-level games from unusual openings, and its Superfinal books are a good source of sharp, playable positions to study. Its pitfall is the same as any engine game: the moves are only as instructive as your understanding of why they were played, and the openings were picked for balance of chances in engine play, not as recommended repertoire.[^s1]

## Connections

TCEC is an event within [computer chess](kt:computer-chess) and a form of [chess tournament](kt:chess-tournament). [Stockfish](kt:stockfish) holds the most titles and [Leela Chess Zero](kt:leela-chess-zero) has been its most frequent Superfinal opponent.[^s5] The competition replaces each engine's [opening book](kt:opening-book) with its own assigned positions, relies on [endgame tablebases](kt:endgame-tablebases) for adjudication, and saw the [NNUE](kt:nnue) upgrade spread through its field around 2020.[^s1][^s2][^s3] Its side events include Fischer Random play, linking it to [Chess960](kt:chess960).[^s5]

## Sources

[^s1]: Top Chess Engine Championship, "TCEC Openings FAQ". https://tcec-chess.com/articles/TCEC_Openings_FAQ.html (accessed 2026-11-16)
[^s2]: G. McC. Haworth and N. Hernandez, "TCEC15: the 15th Top Chess Engine Championship", ICGA Journal 41(3), 2019. https://reading-9.eprints-hosting.org/83156/1/TCEC15.pdf (accessed 2026-11-16)
[^s3]: G. McC. Haworth and N. Hernandez, "TCEC Cup 7", ICGA Journal 42(4), 2020. https://content.iospress.com/articles/icga-journal/icg200174 (accessed 2026-11-16)
[^s4]: Chess Programming Wiki, "TCEC". https://www.chessprogramming.org:443/TCEC (accessed 2026-11-16)
[^s5]: Chessdom, "Stockfish claims its 19th TCEC title defeating Reckless in the Superfinal". https://www.chessdom.com/stockfish-claims-its-19th-tcec-title-defeating-reckless-in-the-superfinal/ (accessed 2026-11-16)
[^s6]: TCEC BayesElo, "TCEC Season 30, Swiss10, Game 624". https://tcecbayeselo.chessdom.org/2026/11/01/tcec-season-30-swiss10-game-624-stockfish-dev-20260930-m-49ea5ded-obsidian-dev-16-15/ (accessed 2026-11-16)
