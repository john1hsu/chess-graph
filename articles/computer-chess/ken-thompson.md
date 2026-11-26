---
id: kt:ken-thompson
type: Person
title: Ken Thompson
aliases: [Kenneth Thompson, Kenneth Lane Thompson, Ken Thompson (computer scientist)]
domain: computer-chess
summary: >-
  American computer scientist (born 1943), co-creator of Unix, who with Joe Condon built the
  special-purpose chess machine Belle at Bell Labs, the 1980 world computer chess champion and the
  first computer to reach a master rating, and who later pioneered endgame databases.
status: historical
volatile: false
verified: 2026-11-26
broader: [kt:history-of-computer-chess, kt:computer-chess]
related: [kt:belle, kt:endgame-tablebases, kt:retrograde-analysis, kt:transposition-table, kt:queen-versus-rook, kt:world-computer-chess-championship]
sources:
  - id: s1
    title: "Belle chess-playing computer"
    publisher: Computer History Museum (Mastering the Game exhibit)
    url: https://www.computerhistory.org/chess/stl-43305190f1a84/
    type: archive
    accessed: 2026-11-26
  - id: s2
    title: "In 1983, This Bell Labs Computer Was the First Machine to Become a Chess Master"
    publisher: Allison Marsh, IEEE Spectrum (Past Forward), 26 April 2019
    url: https://spectrum.ieee.org/in-1983-this-bell-labs-computer-was-the-first-machine-to-become-a-chess-master
    type: publication
    accessed: 2026-11-26
  - id: s3
    title: "Kenneth Lane Thompson, A.M. Turing Award laureate profile"
    publisher: Association for Computing Machinery (profile by Tom van Vleck)
    url: https://amturing.acm.org/award_recipient/thompson_4588371
    type: academic
    accessed: 2026-11-26
  - id: s4
    title: "Ken Thompson"
    publisher: Encyclopaedia Britannica (William L. Hosch)
    url: https://www.britannica.com/biography/Kenneth-Lane-Thompson
    type: reference
    accessed: 2026-11-26
  - id: s5
    title: "Ken, Unix, and Games (ICGA Journal 24, no. 2, June 2001)"
    publisher: Dennis M. Ritchie, hosted by Bell Labs
    url: https://bell-labs.com/usr/dmr/www/ken-games.html
    type: academic
    accessed: 2026-11-26
  - id: s6
    title: "Brute Force vs Knowledge"
    publisher: Computer History Museum (Mastering the Game exhibit)
    url: https://www.computerhistory.org/chess/brute-force-vs-knowledge/
    type: archive
    accessed: 2026-11-26
created: 2026-11-26
---

# Ken Thompson

Kenneth Lane Thompson, born in New Orleans on 4 February 1943, is an American computer scientist best known outside chess as the co-creator of the Unix operating system, for which he and Dennis Ritchie shared the 1983 A.M. Turing Award.[^s3][^s4] Inside chess he matters for two contributions: Belle, the special-purpose chess machine he built with Joe Condon at Bell Labs, and the endgame databases that grew out of it.[^s1][^s5]

## From a Unix program to Belle

Thompson's chess interest predates the hardware. He wrote a chess-playing program that is mentioned in the first edition of the Unix manual in 1971, and Belle began life as software before turning into a hybrid machine, with Thompson writing the programs and Condon designing the circuits.[^s2][^s5] Ritchie, his longtime colleague, describes the earliest hardware as little more than a move generator; later versions moved board evaluation and parts of the tree search into circuitry as well.[^s5] IEEE Spectrum's history column breaks the mature design into three pieces: a move generator, a board evaluator and a transposition table.[^s2]

## The brute-force champion

Belle was a deliberate bet on speed rather than chess knowledge. The Computer History Museum dates the custom machine to 1977 and says that by 1980 its specialised circuitry let it examine 160,000 positions per second.[^s6] Early versions searched about four plies; when Belle won its first ACM North American Computer Chess Championship in 1978 it was searching eight, and it went on to win that event four more times.[^s2] In 1980 it won the third World Computer Chess Championship in Linz.[^s3][^s4] The museum highlights its 1982 North American win, in which a machine costing about $17,000 beat Cray Blitz running on a $10 million supercomputer, a vivid case for dedicated hardware over raw general-purpose power.[^s6] In 1983 Belle became the first computer to earn a master rating.[^s2][^s3]

## Endgame databases

After Belle, Thompson turned to what Ritchie calls his long-term endgame database project.[^s5] The museum credits Belle's custom hardware and its endgame database together with revolutionising computer chess.[^s1]

## Example: Belle's mating combination

Ritchie's 2001 tribute reprints a game from round 4 of the ACM championship in Washington on 5 December 1978, captioned as Blitz 6.5 against Belle. Belle, with Black, gave up a rook on h2 to drag the white king forward, and the game ended with a knight interposition on f3 that blocked a check while delivering double check and mate. Ritchie quotes Levy and Newborn calling it the most beautiful combination yet produced by a program.[^s5]

```pgn
[Event "ACM North American Computer Chess Championship"]
[Site "Washington DC"]
[Date "1978.12.05"]
[Round "4"]
[White "Blitz 6.5"]
[Black "Belle"]
[Result "0-1"]

1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Nd4 5. Bc4 Bc5 6. Nxe5 Qe7 7. Bxf7+ Kf8
8. Ng6+ hxg6 9. Bc4 Nxe4 10. O-O Rxh2 11. Kxh2 Qh4+ 12. Kg1 Ng3 13. Qh5 gxh5
14. fxg3+ Nf3# 0-1
```

For club players the game is a reminder that the open h-file after ...hxg6 can be a weapon for the side that recaptured, and that a queen and two knights near a castled king need very little help.[^s5]

## Legacy

Belle was later donated to the Smithsonian, and the museum pairs it with Thompson's 2005 oral history in its account of how brute-force search overtook knowledge-based programs.[^s3][^s1][^s6] Thompson himself stayed at Bell Labs until December 2000 and later helped design the Go programming language at Google.[^s4]

## Connections

Thompson sits within the **history of computer chess** and **computer chess**, where Belle became the museum's emblem of brute-force search winning out over knowledge-based programs.[^s6] His machine **Belle**, built around a **transposition table**, won the **World Computer Chess Championship** in 1980.[^s2][^s3] His endgame work is the root of **retrograde analysis** as used for **endgame tablebases**, whose early landmark was the solution of **queen versus rook**.[^s1][^s5]

## Sources
[^s1]: Computer History Museum, "Belle chess-playing computer". https://www.computerhistory.org/chess/stl-43305190f1a84/ (accessed 2026-11-26)
[^s2]: A. Marsh, "In 1983, This Bell Labs Computer Was the First Machine to Become a Chess Master", *IEEE Spectrum*, 26 April 2019. https://spectrum.ieee.org/in-1983-this-bell-labs-computer-was-the-first-machine-to-become-a-chess-master (accessed 2026-11-26)
[^s3]: ACM, "Kenneth Lane Thompson", A.M. Turing Award laureate profile. https://amturing.acm.org/award_recipient/thompson_4588371 (accessed 2026-11-26)
[^s4]: Encyclopaedia Britannica, "Ken Thompson". https://www.britannica.com/biography/Kenneth-Lane-Thompson (accessed 2026-11-26)
[^s5]: D. M. Ritchie, "Ken, Unix, and Games", *ICGA Journal* 24 (2), June 2001. https://bell-labs.com/usr/dmr/www/ken-games.html (accessed 2026-11-26)
[^s6]: Computer History Museum, "Brute Force vs Knowledge". https://www.computerhistory.org/chess/brute-force-vs-knowledge/ (accessed 2026-11-26)
