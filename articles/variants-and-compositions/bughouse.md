---
id: kt:bughouse
type: Variant
title: Bughouse
aliases: [Bughouse chess, Double bughouse]
domain: variants-and-compositions
summary: >-
  A four-player team variant of chess played on two boards at once, in which each partner has the
  opposite colour and every piece a player captures is handed to the partner, who may drop it onto
  any empty square of their own board instead of making a normal move.
status: current
volatile: true
verified: 2026-11-13
broader: [kt:chess-variants]
related: [kt:crazyhouse, kt:blitz-chess, kt:checkmate, kt:pawn-promotion, kt:chess960]
relations:
  - {predicate: sanctionedBy, object: kt:us-chess}
  - {predicate: usesTechnique, object: kt:sacrifice}
sources:
  - id: s1
    title: "Laws of Bughouse chess (OTB), Document Version 1.00"
    publisher: Hellenic Chess Federation (chessfed.gr), WCCC 2007 event files
    url: https://www.chessfed.gr/old_site/wccc2007/files/bughouse_chess_complete_rules.pdf
    type: primary-record
    accessed: 2026-11-13
  - id: s2
    title: "Bughouse Rules (revised March 1, 2004; as posted by USCF at the 2006 National High School Championships)"
    publisher: Northwest Chess
    url: https://nwchess.com/articles/rules/bughouse_rules.htm
    type: publication
    accessed: 2026-11-13
  - id: s3
    title: "National Bughouse Championship, SuperNationals VIII"
    publisher: US Chess Federation
    url: https://new.uschess.org/supernationals-2025/bughouse
    type: official-project
    accessed: 2026-11-13
  - id: s4
    title: "Learning to Play the Chess Variant Crazyhouse Above World Champion Level With Deep Neural Networks and Human Data"
    publisher: "Czech, Willig, Beyer, Kersting & Fürnkranz, Frontiers in Artificial Intelligence 3:24 (2020)"
    url: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2020.00024/pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s5
    title: "What is Bughouse?"
    publisher: Chess.com Help Center
    url: https://support.chess.com/en/articles/8615092-what-is-bughouse
    type: publication
    accessed: 2026-11-13
  - id: s6
    title: "When Bughouse Was New!"
    publisher: Lichess blog (MrPushwood)
    url: https://lichess.org/@/MrPushwood/blog/when-bughouse-was-new/bUxg53cG
    type: community
    accessed: 2026-11-13
created: 2026-11-13
---

# Bughouse

Bughouse is a team game for four players on two boards. Two teams of two sit side by side, each partner playing the opposite colour from the other, so that one partner has White against one opponent while the other partner has Black against the second opponent.[^s1][^s5] The defining rule is the transfer of material: a piece captured on one board is passed to the capturer's partner, who may later place ("drop") it on their own board in place of a normal move.[^s1][^s2] Crazyhouse, or drop chess, is the two-player version of the same idea, in which captured pieces go into the capturer's own reserve.[^s4]

## How it is played

A drop may go on any empty square, but a pawn may not be dropped on the first or last rank, and a drop can never capture.[^s1][^s5] Drops may give check and even checkmate.[^s1][^s2] Under the widely used WBN-style laws, a dropped piece counts as unmoved, so a pawn dropped on its second rank may still advance two squares, while a dropped rook does not restore castling rights.[^s1][^s5] Promotion is only temporary: when a promoted piece is captured, it goes to the partner as a plain pawn.[^s2][^s5]

Checkmate is subtler than in ordinary chess. Because a teammate may still capture and pass a piece, a check that could be blocked by a drop is usually not mate, even when the defender's reserve is empty at that moment.[^s1][^s5] As a result, mates in bughouse are typically delivered by contact checks, knight checks or double checks that no interposition can stop.[^s1]

Games are fast. Common time controls are three or five minutes per player with no increment, each board has its own clock, and in over-the-board play a move is only complete when the clock is pressed.[^s1][^s2] Partners may talk throughout, ask for particular pieces and suggest moves, but may not touch the other board.[^s1][^s2] Rule sets differ on how a match ends: on online servers and in many scholastic events the whole match stops as soon as either board is decided, while the WBN laws score each board separately.[^s1][^s2][^s5] Illegal moves lose the game if claimed in time, and pieces in reserve must stay visible to the opponents.[^s1][^s2]

## Typical ideas and pitfalls

Material values change with the reserve. Because pieces never leave the game, sacrifices are cheap when they feed a partner's attack, and drop chess is far more tactical than standard chess, with long forced mating sequences and very few draws.[^s4] The larger branching factor created by drops also makes these games harder for engines to search deeply.[^s4] Because each capture also arms the partner of the opponent across the table, every trade has to be judged on both boards, and partners constantly tell each other which pieces they need or must not give away.[^s1][^s2] Time is a weapon too: early informal play had no rule against stalling, and some games ended with both sides waiting for the other board's flag to fall.[^s6]

A common pitfall is to treat a check as mate without asking whether the defender could interpose a dropped piece, or to forget that capturing a promoted queen yields only a pawn for one's partner.[^s1][^s5]

## History and organisation

Bughouse grew up as a between-rounds pastime at American tournaments. A player's recollection describes informal "double bughouse" games at five minutes per player during the 1970s, including at the 1976 U.S. Open.[^s6] The game later moved into organised scholastic chess: Northwest Chess reprints a rule sheet revised in 2004 and posted by the US Chess Federation at the 2006 National High School Championships.[^s2] US Chess now runs a National Bughouse Championship at its scholastic events; at SuperNationals VIII on 8 May 2025 it was played at G/5 with no delay, in K-12, K-8 and K-6 sections.[^s3] As of November 2026 bughouse is also a standard four-player mode on major online servers such as Chess.com.[^s5]

## Connections

Bughouse is a member of the family of chess variants, and crazyhouse is its single-player version, sharing the drop rule and its restriction on pawns.[^s4] Its handling of pawn promotion and checkmate modifies the standard rules, and it is usually played at blitz speeds.[^s1][^s2] US Chess sanctions a national championship for it.[^s3] Like Chess960, it keeps the ordinary moves of the pieces while changing what can happen to material.[^s1]

## Sources
[^s1]: Hellenic Chess Federation (WCCC 2007 files), "Laws of Bughouse chess (OTB)", v1.00. https://www.chessfed.gr/old_site/wccc2007/files/bughouse_chess_complete_rules.pdf (accessed 2026-11-13)
[^s2]: Northwest Chess, "Bughouse Rules" (revised 2004; posted by USCF at the 2006 National High School Championships). https://nwchess.com/articles/rules/bughouse_rules.htm (accessed 2026-11-13)
[^s3]: US Chess Federation, "National Bughouse Championship", SuperNationals VIII. https://new.uschess.org/supernationals-2025/bughouse (accessed 2026-11-13)
[^s4]: J. Czech, M. Willig, A. Beyer, K. Kersting, J. Fürnkranz, "Learning to Play the Chess Variant Crazyhouse Above World Champion Level With Deep Neural Networks and Human Data", Frontiers in Artificial Intelligence 3:24 (2020). https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2020.00024/pdf (accessed 2026-11-13)
[^s5]: Chess.com Help Center, "What is Bughouse?". https://support.chess.com/en/articles/8615092-what-is-bughouse (accessed 2026-11-13)
[^s6]: MrPushwood, "When Bughouse Was New!", Lichess blog. https://lichess.org/@/MrPushwood/blog/when-bughouse-was-new/bUxg53cG (accessed 2026-11-13)
