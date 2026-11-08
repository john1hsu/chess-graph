---
id: kt:touch-move
type: Rule
title: Touch-move
aliases: [Touch-move rule, Touch move, Touched piece rule, Touch-move law, J'adoube, I adjust, Adjusting pieces]
domain: rules-and-notation
summary: >-
  The rule of over-the-board chess that a player on the move who deliberately touches one of
  their own pieces must move it, and who touches an opponent's piece must capture it, if that is
  legal; pieces may be adjusted without obligation only after announcing "j'adoube" or "I adjust".
fen: "4r1k1/5ppp/8/8/8/8/4NPPP/4K2R w K - 0 1"
status: current
volatile: true
verified: 2026-11-08
broader: [kt:fide-laws-of-chess]
related: [kt:castling, kt:pawn-promotion, kt:arbiter, kt:us-chess, kt:illegal-move]
relations:
  - {predicate: partOf, object: kt:fide-laws-of-chess}
  - {predicate: developedBy, object: kt:fide}
sources:
  - id: s1
    title: "Article 4: The Act of Moving the Pieces"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/article4/
    type: governing-body
    accessed: 2026-11-08
  - id: s2
    title: "Arbiters' Manual 2024 (Laws of Chess applied from 1 January 2023, Article 4 with commentary)"
    publisher: FIDE Arbiters' Commission
    url: https://arbiters.fide.com/wp-content/uploads/Publications/Manual/Arbiters_Manual_2024.pdf
    type: governing-body
    accessed: 2026-11-08
  - id: s3
    title: "Summary of differences between the FIDE Laws of Chess and the US Chess Official Rules of Chess, 7th edition (updated 1 January 2022)"
    publisher: US Chess
    url: https://new.uschess.org/sites/default/files/media/documents/uschess-fide-rules-comparison.pdf
    type: governing-body
    accessed: 2026-11-08
  - id: s4
    title: "J'adoube"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/jadoube.html
    type: reference
    accessed: 2026-11-08
  - id: s5
    title: "Laws of Chess: For competitions starting from 1 July 2014 till 30 June 2017"
    publisher: FIDE Handbook
    url: https://handbook.fide.com/chapter/E012014
    type: governing-body
    accessed: 2026-11-08
created: 2026-11-08
---

# Touch-move

Touch-move is the principle that, in over-the-board play, touching a piece on purpose commits a player to it. It is set out in Article 4 of the FIDE Laws of Chess, "The act of moving the pieces", which also requires every move to be made with one hand.[^s1] As of November 2026 the text in force is the one applied from 1 January 2023; the FIDE Arbiters' Manual 2024 reproduces it with official commentary.[^s2] The core of the rule has been stable for years: the 2014–2017 edition already contained the same obligations to move a touched piece, capture a touched enemy piece and castle after touching king and rook.[^s5]

## What the Laws require

Only the player whose turn it is may adjust pieces on their squares, and only after first announcing it, for example by saying "j'adoube" or "I adjust".[^s1] Any other contact with a piece, apart from contact that is clearly accidental, is treated as intent to move or capture.[^s1] Then:

- touching one's own piece obliges the player to move the first touched piece that can legally move;[^s1]
- touching an opponent's piece obliges the player to capture the first touched piece that can legally be captured;[^s1]
- touching one piece of each colour obliges the player to capture the touched enemy piece with the touched own piece if that is legal, and otherwise to move or capture the first touched piece that can be moved or captured; if it is unclear which came first, the player's own piece counts as touched first.[^s1]

If none of the touched pieces can legally move or be captured, the player may make any legal move.[^s1] The right to complain is short-lived: a player who then touches one of their own pieces intending to move it loses the right to claim against the opponent's breach of Articles 4.1–4.7.[^s1]

A separate "release" rule decides when a move is finished. Once a piece has been released on a square as a legal move it cannot be moved elsewhere on that turn; a capture is complete when the captured piece is removed and the capturing piece released, and a promotion when the new piece is released on the promotion square and the pawn removed.[^s1] The Arbiters' Manual adds that a move only becomes an illegal move once the clock is pressed, so a player may still correct a released move before pressing, provided the correction obeys Article 4.[^s2]

## Castling and promotion

Because castling is a king move, the king should be touched first. Touching king and then rook obliges the player to castle on that side if legal; deliberately touching the rook first rules out castling with it on that move and leaves the rook as the touched piece; and if castling turns out to be illegal, the player must make another legal king move (which may be castling on the other side), or any legal move if the king has none.[^s1] For promotion, the choice of piece is final as soon as the new piece touches the promotion square.[^s1]

## Enforcement: FIDE and US Chess

Under FIDE rules the arbiter does not wait for a claim. The Arbiters' Manual says an arbiter who observes a breach of Article 4 must intervene at once, and that "accidental" is judged objectively rather than by guessing at the player's intentions.[^s2] Penalties for improper touching are drawn from the general list in Article 12.9.[^s2] US Chess handles this differently: its official comparison of the two rulebooks notes that touch-move violations under US Chess rules require the opponent to make a claim, and that a variation of its castling rule lets a player touch the rook first, which FIDE does not.[^s3] The Manual also warns that when no arbiter is watching, a dispute over whether "j'adoube" was said is close to a coin toss to resolve.[^s2]

## Key position

In the diagram, the knight on e2 is pinned against the white king by the rook on e8 and has no legal moves. If White touches only the knight, Article 4.5 applies and White may play any legal move. If White touches the knight and then the h1-rook, the rook becomes the first touched piece that can legally move, and it must move. If White touches the king and then the h1-rook, White must castle kingside, which is legal here because the knight blocks the e-file.[^s1]

## History and a famous incident

The rule is centuries old. Edward Winter cites Ruy López's book of 1561, which already required a touched piece to be moved unless the player had touched it only to straighten it and said so at once.[^s4] The French phrase "j'adoube" appears in the rules Philidor published in London in 1790 and in Sarratt's treatise of 1808, which let the opponent force a player to move a piece adjusted without the announcement.[^s4] The best-known breach came at the Sousse Interzonal on 26 October 1967: Milan Matulović played 38 Bf3 against Bilek of Hungary, took it back and played another move, claiming he had said "j'adoube"; the arbiter had not seen the incident, the game was drawn, and the episode earned Matulović a mocking nickname in the chess press.[^s4]

## Connections

Touch-move is **part of** the **FIDE Laws of Chess**, whose Rules Commission maintains it on behalf of **FIDE**.[^s1] It governs how **castling** and **pawn promotion** are physically carried out, and it sits beside the separate rules on the **illegal move**, which take over once the clock is pressed.[^s1][^s2] It is enforced by the **arbiter** under FIDE rules but by claim under **US Chess** rules.[^s2][^s3]

## Sources

[^s1]: FIDE Rules Commission, "Article 4: The Act of Moving the Pieces". https://rcc.fide.com/article4/ (accessed 2026-11-08)
[^s2]: FIDE Arbiters' Commission, "Arbiters' Manual 2024" (Laws of Chess applied from 1 January 2023, Article 4 with commentary). https://arbiters.fide.com/wp-content/uploads/Publications/Manual/Arbiters_Manual_2024.pdf (accessed 2026-11-08)
[^s3]: US Chess, "Summary of differences between the FIDE Laws of Chess and the US Chess Official Rules of Chess, 7th edition" (updated 1 January 2022). https://new.uschess.org/sites/default/files/media/documents/uschess-fide-rules-comparison.pdf (accessed 2026-11-08)
[^s4]: Edward Winter, Chess Notes, "J'adoube". https://chesshistory.com/winter/extra/jadoube.html (accessed 2026-11-08)
[^s5]: FIDE Handbook, "Laws of Chess: For competitions starting from 1 July 2014 till 30 June 2017". https://handbook.fide.com/chapter/E012014 (accessed 2026-11-08)
