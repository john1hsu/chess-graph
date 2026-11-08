---
id: kt:castling
type: Rule
title: Castling
aliases: [Castle, Castling kingside, Castling queenside, O-O, O-O-O, Short castling, Long castling, Roque, Rochade]
domain: rules-and-notation
summary: >-
  The special move in which a player moves the king two squares along the first rank towards an
  unmoved rook and places that rook on the square the king crossed; it counts as a single king
  move and is allowed only under conditions set out in the FIDE Laws of Chess.
fen: "5rk1/ppp3pp/8/3p4/3Pb3/2P5/PP4PP/R3K2R w KQ - 0 1"
status: current
volatile: true
verified: 2026-11-08
broader: [kt:fide-laws-of-chess]
related: [kt:chess960, kt:en-passant, kt:pawn-promotion, kt:touch-move, kt:king-safety, kt:algebraic-notation]
relations:
  - {predicate: partOf, object: kt:fide-laws-of-chess}
  - {predicate: governedBy, object: kt:touch-move}
sources:
  - id: s1
    title: "Arbiters' Manual 2024 (Laws of Chess applied from 1 January 2023, with commentary; Articles 3.8.2, 4.4, 4.7, 7.5, Appendix C and Chess960 Guidelines)"
    publisher: FIDE Arbiters' Commission
    url: https://arbiters.fide.com/wp-content/uploads/Publications/Manual/Arbiters_Manual_2024.pdf
    type: governing-body
    accessed: 2026-11-08
  - id: s2
    title: "castling"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/castling
    type: reference
    accessed: 2026-11-08
  - id: s3
    title: "Castling in Chess"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/castling.html
    type: reference
    accessed: 2026-11-08
  - id: s4
    title: "The Evolution of Modern Chess Rules: Castling"
    publisher: John McCrary, US Chess
    url: https://new.uschess.org/news/evolution-modern-chess-rules-castling
    type: publication
    accessed: 2026-11-08
  - id: s5
    title: "The 'Suicidal' Pawn Storm (Don't Get Brainwashed, part 4)"
    publisher: GM Gregory Serper, Chess.com
    url: https://www.chess.com/article/view/dont-get-brainwashed-part-four
    type: publication
    accessed: 2026-11-08
created: 2026-11-08
---

# Castling

Castling is the only move in standard chess in which a player moves two pieces at once. Britannica describes it as the single exception to the one-piece-per-turn rule: the king goes two squares towards a rook and the rook jumps to the square the king has just crossed, so that, for example, the king travels e1–g1 and the rook h1–f1.[^s2] In the FIDE Laws of Chess in force as of November 2026 (the text applied from 1 January 2023), Article 3.8.2 defines it as a move of king and rook along the first rank that counts as a single move of the king.[^s1]

## Conditions

The Laws separate permanent from temporary restrictions.[^s1] The right to castle is lost for good if the king has already moved, and on one side if that rook has already moved. Castling is prevented for the moment if the king's current square, the square it crosses, or its destination is attacked by an enemy piece, or if any piece stands between king and rook.[^s1] Britannica adds the practical summary: once per game, never out of check, never through or into check.[^s2] Two consequences catch club players out. A rook may castle while it is attacked, and in queenside castling the b1/b8 square may be attacked, since the king never crosses it; only the squares between king and rook must be empty. Edward Winter cites several games in which Korchnoi's opponents castled with an attacked rook, and records that Korchnoi himself was unsure of the rule during the 1974 Candidates final.[^s3]

In the key position above, White may play 0-0-0 even though the bishop on e4 attacks b1, but cannot castle kingside, because the rook on f8 attacks f1, a square the king would cross. The rights themselves survive; kingside castling becomes possible again once f1 is no longer attacked.[^s1]

## Executing the move

Castling is a king move, so the king should be touched first. Under Article 4.4.2, a player who deliberately touches the rook first may not castle on that side on that move; under 4.4.3, a player who touches king and rook intending an illegal castle must make another legal king move, which may be castling on the other side.[^s1] Each move must be made with one hand; the FIDE Arbiters' Manual notes that castling with two hands is penalised like an illegal move once the clock is pressed, and that the move is complete only when the rook is released on its new square.[^s1] The king-first convention is old: Winter quotes *Bell's Life in London* insisting on it in 1835, while *Le Palamède* argued in 1837 that touching the rook first was harmless.[^s3] Winter also recounts Miles v Polugayevsky, Tilburg 1985, in which Miles castled queenside after moving the rook first.[^s3] In algebraic notation, Appendix C of the Laws writes kingside castling as 0-0 and queenside castling as 0-0-0.[^s1]

## History

John McCrary, a former US Chess president, traces castling to the medieval "king's leap", a one-time king jump that could cover two squares or a knight's distance. Once the queen and bishop gained their modern powers around 1475, players used the leap to tuck the king into a corner, at first over two moves (rook to f1, then king to g1), which later merged into one move.[^s4] Local rules varied. In the early nineteenth century parts of Italy and Germany allowed "free castling", in which king and rook could be placed on a range of squares; Howard Staunton campaigned in the 1840s for a single international rule, and free castling died out.[^s4] Early wording that allowed castling with any unmoved rook allowed a published problem "solution" that castled with a promoted rook; modern wording, requiring the king to move along the first rank towards a rook on its original square, closes that loophole.[^s4][^s1]

## Strategy and pitfalls

Castling usually serves two purposes at once: it shelters the king behind pawns and connects the rooks. Its value was not always taken for granted; Winter quotes an eighteenth-century Swedish treatise advising that great players never castle.[^s3] Today the main strategic question is which side to choose. GM Gregory Serper notes that when the kings stand on opposite wings, the usual plan for both sides is a pawn storm that trades pawns to open files against the enemy king, and that pushing the pawns in front of one's own king generally helps the opponent; the Yugoslav Attack against the Dragon Sicilian, with White's h-pawn rushing forward, is the classic case.[^s5] Queenside castling also carries a tactical trap: Winter collects games such as Palmer v Euwe, Detroit 1949 (14...0-0-0+), where long castling gave check with the rook and won material, a device known as the Thornton castling trap.[^s3] Castling can even deliver mate, as in Löwy II v Felix, Vienna 1904, which ended 25 0-0-0 mate.[^s3]

## Connections

Castling is one of the special moves defined in the **FIDE Laws of Chess**, alongside **en passant** and **pawn promotion**, and how it is physically carried out is governed by the **touch-move** rules of Article 4.4.[^s1] It is recorded with dedicated symbols in **algebraic notation**.[^s1] In **Chess960** the starting squares vary, but FIDE's guidelines keep the same end squares as standard chess (king on g1 or c1, rook on f1 or d1) and recommend that the player may announce the intention to castle.[^s1][^s2] Its practical purpose ties it to **king safety** and to opposite-side pawn storms.[^s5]

## Sources

[^s1]: FIDE Arbiters' Commission, "Arbiters' Manual 2024" (Laws of Chess applied from 1 January 2023: Articles 3.8.2, 4.4, 4.7, 7.5, Appendix C, Chess960 Guidelines). https://arbiters.fide.com/wp-content/uploads/Publications/Manual/Arbiters_Manual_2024.pdf (accessed 2026-11-08)
[^s2]: Encyclopaedia Britannica, "castling". https://www.britannica.com/topic/castling (accessed 2026-11-08)
[^s3]: Edward Winter, Chess Notes, "Castling in Chess". https://chesshistory.com/winter/extra/castling.html (accessed 2026-11-08)
[^s4]: John McCrary, US Chess, "The Evolution of Modern Chess Rules: Castling" (2021). https://new.uschess.org/news/evolution-modern-chess-rules-castling (accessed 2026-11-08)
[^s5]: GM Gregory Serper, Chess.com, "The 'Suicidal' Pawn Storm". https://www.chess.com/article/view/dont-get-brainwashed-part-four (accessed 2026-11-08)
