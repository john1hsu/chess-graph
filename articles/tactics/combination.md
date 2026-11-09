---
id: kt:combination
type: Concept
title: Combination
aliases: [Chess combination, Combinations, Combinative play]
domain: tactics
summary: >-
  A forcing sequence of moves, usually built from two or more tactical motifs and often including a
  sacrifice, by which a player compels a concrete result such as mate, a gain of material or a decisive
  change in the position.
fen: "4r1k1/3q1ppp/8/8/4Q3/8/5PPP/4R1K1 w - - 0 1"
status: current
volatile: false
verified: 2026-11-09
broader: [kt:chess-tactics]
related: [kt:emanuel-lasker, kt:back-rank-mate, kt:discovered-attack, kt:fork]
relations:
  - {predicate: usesTechnique, object: kt:sacrifice}
  - {predicate: dependsOn, object: kt:calculation}
  - {predicate: enables, object: kt:material-advantage}
  - {predicate: exemplifiedBy, object: kt:lasker-versus-bauer-amsterdam-1889}
sources:
  - id: s1
    title: "What is a Chess Combination?"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://www.chesshistory.com/winter/extra/combination.html
    type: reference
    accessed: 2026-11-09
  - id: s2
    title: "Are Tactics The Same As Combinations?"
    publisher: IM Jeremy Silman, Chess.com
    url: https://www.chess.com/article/view/are-tactics-the-same-as-combinations
    type: publication
    accessed: 2026-11-09
  - id: s3
    title: "Lasker vs Bauer chess position (Emanuel Lasker)"
    publisher: International Chess Federation (FIDE), via Google Arts & Culture
    url: https://artsandculture.google.com/asset/lasker-vs-bauer-chess-position-emanuel-lasker/lgHmqSF4RuWmnQ
    type: archive
    accessed: 2026-11-09
  - id: s4
    title: "Chess Notes (Lasker v Bauer and earlier double bishop sacrifices)"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/winter175.html
    type: reference
    accessed: 2026-11-09
  - id: s5
    title: "The art of chess combination: a guide for all players of the game (E. Znosko-Borovsky; Dover, New York, 1959) — catalogue record"
    publisher: Universiti Teknologi MARA Library
    url: https://search.library.uitm.edu.my/Record/wils-73794
    type: book
    accessed: 2026-11-09
  - id: s6
    title: "The Art of Chess Combination (Dover Chess) — publisher's description"
    publisher: OverDrive
    url: https://www.overdrive.com/media/1532247/the-art-of-chess-combination
    type: publication
    accessed: 2026-11-09
created: 2026-11-09
---

# Combination

A combination is a forcing sequence of moves in which a player makes several tactical ideas work together to reach a definite goal: mate, a gain of material, a won ending or sometimes a saving draw. The word is one of the oldest in chess writing, and also one of the least settled. Edward Winter's survey of definitions runs from James Mason in 1898, who called it two or more moves with a common object, to modern teachers who still admit that the line between a single tactic and a combination is blurred.[^s1]

## What counts as a combination

Most definitions share three ingredients.[^s1][^s2]

- **Force.** Emanuel Lasker described a combination as the whole set of forcing variations that lead to a desired result, and insisted that it must be sound: an unsound "combination" is simply a mistake.[^s1][^s2] C. J. S. Purdy stressed that combinations are made of violent moves (checks, captures and threats), with zugzwang as the one notable way to force matters quietly.[^s1]
- **More than one idea.** John Nunn and Ron Evers both describe a combination as a winning idea built from two or more tactical elements, such as a deflection followed by a fork, or a pin exploited by a discovered attack.[^s1] Yuri Averbakh's view, as summarised by Jeremy Silman, is that nearly all combinations ultimately rest on some form of double attack.[^s2]
- **A concrete outcome.** The sequence ends in something that can be checked: mate, material, promotion or a position the opponent cannot hold.[^s1]

## Does it need a sacrifice?

This is the classic dispute. Mikhail Botvinnik defined a combination as a forced manoeuvre combined with a sacrifice, and Yasser Seirawan and Silman adopt a similar formula, a sacrifice joined to a forced sequence.[^s2] Silman prefers his version because it also covers combinations that fail or merely restore the balance.[^s2] On the other side, W. H. Watts wrote in 1936 that a combination has nothing to do with sacrifice, and Ludek Pachman, Georges Renaud and Purdy likewise treated the sacrifice as a common feature rather than a requirement.[^s1] Winter shows how far the question can go: in one of Purdy's examples, critics argued that the most elegant continuation was a sacrifice even though a non-sacrificial line also won.[^s1]

In club usage the word usually implies a sacrifice, and the practical point is the same either way: a combination gives the opponent no time, so the calculation can be carried to the end.[^s2]

## Where combinations come from

Eugene Znosko-Borovsky's *The Art of Chess Combination* (Dover edition, New York, 1959) argued that combinations are not lucky inspirations but can be studied and prepared.[^s5][^s6] He traced even complicated sequences back to a simple starting feature: an undefended piece, a badly placed king, a pawn close to promotion or a possible discovered check.[^s6] Silman makes the same point in his own terms: combinations need targets such as a vulnerable king or loose and insufficiently guarded pieces, and the player's strategic work is what creates those targets.[^s2] Irving Chernev's remark that the master sets up the conditions for combinations, rather than hunting for them, belongs to the same tradition.[^s1]

## Example: a back-rank combination

In the diagram position (White to move), Black's rook on e8 attacks White's queen, and Black's king has no escape square on the second rank. **1.Qxe8+! Qxe8 2.Rxe8#** wins by force: the queen sacrifice drags Black's queen onto e8, where the rook captures it with mate. Two motifs work together, a deflecting sacrifice and the back-rank weakness, which is exactly the "two or more tactical elements" that Nunn's definition calls for.[^s1]

## A famous case: Lasker v Bauer, 1889

The best-known historical example is Emanuel Lasker against Johann Hermann Bauer at Amsterdam in 1889. Lasker sacrificed both bishops on the kingside: 15.Bxh7+ Kxh7 16.Qxh5+ Kg8 17.Bxg7 Kxg7 18.Qg4+ Kh7 19.Rf3, after which Black had to give up the queen to avoid mate, and Lasker won.[^s3] Wilhelm Steinitz called 15.Bxh7+ the start of a deep and elegant combination.[^s4] Winter notes, though, that it was not the first double bishop sacrifice: Amos Burn used the same idea against John Owen at Liverpool in 1884, and an even earlier game by Cecil De Vere from 1867 has been traced.[^s4] Silman uses the Lasker game to contrast a true combination with a quieter tactical operation earlier in the same game.[^s2]

## Pitfalls

- **Unsound sacrifices.** By Lasker's standard a combination that fails to a defence was never a combination at all; check the opponent's best reply at every step.[^s1]
- **Missing a non-forcing reply.** A quiet defensive move or an in-between check can break a sequence that looked forced.[^s1][^s2]
- **Looking without targets.** Without a weak king or loose pieces there is usually no combination to find; build the position first.[^s2][^s6]

## Connections

A combination is a compound form of **chess tactics**: it chains motifs such as the **fork** and the **discovered attack**, and it often ends in a pattern like the **back-rank mate**.[^s1][^s2] It commonly **uses** the **sacrifice** as its forcing technique, and it **depends on** **calculation**, since a combination is only as good as the variations behind it.[^s1][^s2] Its usual payoff is mate or a **material advantage**.[^s3] It is **exemplified by** **Lasker v Bauer, Amsterdam 1889**, a defining game for **Emanuel Lasker**, who also wrote one of the classic definitions.[^s1][^s3][^s4]

## Sources

[^s1]: Edward Winter, "What is a Chess Combination?", Chess Notes. https://www.chesshistory.com/winter/extra/combination.html (accessed 2026-11-09)
[^s2]: Jeremy Silman, "Are Tactics The Same As Combinations?", Chess.com. https://www.chess.com/article/view/are-tactics-the-same-as-combinations (accessed 2026-11-09)
[^s3]: International Chess Federation (FIDE), "Lasker vs Bauer chess position", Google Arts & Culture. https://artsandculture.google.com/asset/lasker-vs-bauer-chess-position-emanuel-lasker/lgHmqSF4RuWmnQ (accessed 2026-11-09)
[^s4]: Edward Winter, Chess Notes (Lasker v Bauer and earlier double bishop sacrifices). https://chesshistory.com/winter/winter175.html (accessed 2026-11-09)
[^s5]: Universiti Teknologi MARA Library catalogue, E. Znosko-Borovsky, *The art of chess combination: a guide for all players of the game* (New York: Dover, 1959). https://search.library.uitm.edu.my/Record/wils-73794 (accessed 2026-11-09)
[^s6]: OverDrive, *The Art of Chess Combination* (Dover Publications), publisher's description. https://www.overdrive.com/media/1532247/the-art-of-chess-combination (accessed 2026-11-09)
