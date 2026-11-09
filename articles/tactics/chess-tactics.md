---
id: kt:chess-tactics
type: Concept
title: Chess tactics
aliases: [Tactics, Tactic, Tactical play, Tactical motifs]
domain: tactics
summary: >-
  The short-term, concrete side of chess: forcing moves or sequences, worked out by calculation, that
  win material, give mate or gain another immediate advantage, as opposed to the long-term planning of strategy.
fen: "4k3/q4ppp/8/8/8/4B3/5PPP/4R1K1 w - - 0 1"
status: current
volatile: false
verified: 2026-11-09
broader: [kt:chess]
related: [kt:combination, kt:fork, kt:pin, kt:skewer, kt:discovered-attack, kt:calculation]
relations:
  - {predicate: contrastsWith, object: kt:chess-strategy}
  - {predicate: hasPart, object: kt:fork}
  - {predicate: hasPart, object: kt:discovered-attack}
  - {predicate: enables, object: kt:material-advantage}
sources:
  - id: s1
    title: "Chess Strategy and Tactics"
    publisher: Edward Winter, Chess Notes
    url: https://chesshistory.com/winter/extra/strategytactics.html
    type: reference
    accessed: 2026-11-09
  - id: s2
    title: "Strategy & tactics in chess (Dr. M. Euwe; G. Bell & Sons, London, 1937) — catalogue record"
    publisher: National Library of Ireland
    url: https://catalogue.nli.ie/Record/vtls000404097
    type: book
    accessed: 2026-11-09
  - id: s3
    title: "The Double Threat (The Elements of Tactics: A Primer), Predator at the Chessboard"
    publisher: Ward Farnsworth, chesstactics.org
    url: https://chesstactics.org/introductory-matters/the-elements-of-tactics_a-primer/the-double-threat/1_3_1_1.html
    type: publication
    accessed: 2026-11-09
  - id: s4
    title: "Discovered Attacks (Chess Skills leaflet)"
    publisher: English Chess Federation
    url: https://www.englishchess.org.uk/wp-content/uploads/2010/01/discoveredattacks.pdf
    type: governing-body
    accessed: 2026-11-09
  - id: s5
    title: "Chess Tactics: 38 Definitions and Examples"
    publisher: Chess.com
    url: https://www.chess.com/article/view/chess-tactics
    type: publication
    accessed: 2026-11-09
  - id: s6
    title: "Expertise in Chess (Gobet & Charness, Cambridge Handbook of Expertise and Expert Performance, 2006)"
    publisher: Cambridge University Press, via CORE
    url: https://core.ac.uk/download/334186.pdf
    type: academic
    accessed: 2026-11-09
created: 2026-11-09
---

# Chess tactics

Chess tactics are the concrete, short-range operations of the game: a move or a short forcing sequence that gains something definite, such as material, a mating attack or a decisive positional concession. Chess.com's teaching glossary defines a tactic simply as a move or series of moves that brings a player an advantage, whether winning a piece or launching an attack on the king.[^s5] Tactics are usually set against strategy, the long-term choice of aims and plans; the two words are borrowed from military language, and chess writers have argued over the boundary between them for more than a century.[^s1]

## Tactics and strategy

The classic formulation comes from Max Euwe's *Strategy & Tactics in Chess* (London, 1937), first published in Dutch: strategy sets the aims and forms the plan, tactics carries it out; strategy is abstract and calls for thought, tactics is concrete and calls for observation.[^s1][^s2] The Australian writer C. J. S. Purdy reduced tactics to the calculation of moves and replies, and Fred Reinfeld described tactics as the art of turning advantageous situations into victory.[^s1] Gerald Abrahams put the distinction in a well-known aphorism: tactics is what you do when there is something to do, strategy what you do when there is nothing to do.[^s1] Not everyone accepted the split: Edward Winter records Josef Krejcik arguing in 1913 that chess has only tactics and no strategy, and Richard Teichmann is credited with the claim that chess is 99% tactics.[^s1][^s3]

In practice the two are intertwined. A good strategic position tends to create tactical chances, and a tactic is often the means by which a strategic plan, such as an attack on a weak king or the advance of a passed pawn, is finally cashed in.[^s1]

## The building blocks

Ward Farnsworth's field guide *Predator at the Chessboard* organises tactics around one central idea, the **double threat**: a move that sets the opponent two problems at once, so that only one can be solved.[^s3] He groups most tactics into four families built on it:[^s3]

- **Fork** — one piece attacks two targets.[^s3]
- **Discovered attack** — one piece moves and uncovers an attack by another, so two pieces threaten at once.[^s3]
- **Pin and skewer** — two enemy pieces stand on one line and a single attacker exploits them both.[^s3]
- **Removing the guard** — capturing, chasing or overloading a defender so that what it protected falls.[^s3]

**Mating patterns**, the recurring ways in which a king gets trapped, form a fifth family that need not rely on a double threat.[^s3] Teaching collections list many more named motifs that are refinements or combinations of these: deflection and decoy, interference, overloading, the zwischenzug (in-between move), the desperado, the windmill, clearance and exchange sacrifices, back-rank and smothered mates, and stalemate and perpetual-check resources for the defender.[^s5]

When several motifs are linked into a forcing sequence, usually including a sacrifice, the result is called a **combination**.[^s5]

## Example: discovered check

In the diagram position (White to move), the bishop on e3 stands between White's rook on e1 and Black's king on e8. **1.Bc5+** uncovers check from the rook and at the same time attacks the queen on a7. Black must deal with the check first (by moving the king, or by interposing 1...Qe7, which loses the queen to 2.Bxe7), so the queen is lost. This is the pattern of the English Chess Federation's first discovered-attack exercise, where a bishop moves off the e-file with discovered check and lands on c5 to hit the queen.[^s4] The federation's advice is to look for your own pieces lined up behind other pieces, because moving the front one can unleash a second, often unanswerable, threat.[^s4]

## Seeing tactics: pattern recognition

Research on expertise suggests tactical strength rests heavily on stored patterns rather than on brute-force calculation. In their review of chess expertise, Fernand Gobet and Neil Charness report that strong players rely on knowledge of familiar configurations to propose a few plausible moves, and that in choose-a-move experiments experts fixated relevant squares within the first second of seeing a position.[^s6] The same review notes two side effects: strong players tend to reach for a stereotyped tactical solution and can miss a shorter but unusual one (the Einstellung effect), and novices taught a particular combination transferred it mainly to positions that looked similar.[^s6] Tactics embedded in realistic game positions were also easier to solve blindfold than the same ideas in random positions.[^s6]

## Pitfalls

- **Stopping at the first idea.** A tactic is only as good as the opponent's best reply; in-between moves, counter-checks and defensive resources such as stalemate refute many plausible-looking shots.[^s5][^s6]
- **Ignoring loose pieces.** Unprotected pieces and an exposed king are the raw material of most double threats, so they are the first things to check, for both sides.[^s3]
- **Treating tactics as separate from planning.** Without a sound position there may be no tactic to find; strategy prepares the ground on which tactics succeed.[^s1]

## Connections

Chess tactics is the umbrella for the motif articles in this graph. It **has parts** such as the **fork** and the **discovered attack**, and is **related** to the **pin** and **skewer**, which Farnsworth treats as one family.[^s3] Several motifs chained into a forcing sequence make a **combination**.[^s5] Tactics **contrasts with** **chess strategy**, its long-term counterpart in the definitions of Euwe, Purdy and Abrahams,[^s1] and depends on **calculation**, the skill of working out moves and replies.[^s1][^s6] Its usual payoff is a **material advantage** or a mating attack.[^s5]

## Sources

[^s1]: Edward Winter, "Chess Strategy and Tactics", Chess Notes. https://chesshistory.com/winter/extra/strategytactics.html (accessed 2026-11-09)
[^s2]: National Library of Ireland catalogue, M. Euwe, *Strategy & tactics in chess* (London: G. Bell & Sons, 1937). https://catalogue.nli.ie/Record/vtls000404097 (accessed 2026-11-09)
[^s3]: Ward Farnsworth, *Predator at the Chessboard*, "The Double Threat". https://chesstactics.org/introductory-matters/the-elements-of-tactics_a-primer/the-double-threat/1_3_1_1.html (accessed 2026-11-09)
[^s4]: English Chess Federation, "Discovered Attacks" (Chess Skills leaflet). https://www.englishchess.org.uk/wp-content/uploads/2010/01/discoveredattacks.pdf (accessed 2026-11-09)
[^s5]: Chess.com, "Chess Tactics: 38 Definitions and Examples". https://www.chess.com/article/view/chess-tactics (accessed 2026-11-09)
[^s6]: Fernand Gobet and Neil Charness, "Expertise in Chess", in *The Cambridge Handbook of Expertise and Expert Performance* (Cambridge University Press, 2006). https://core.ac.uk/download/334186.pdf (accessed 2026-11-09)
