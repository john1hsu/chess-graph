---
id: kt:pawn-structure
type: StrategicConcept
title: Pawn structure
aliases: [Pawn formation, Pawn skeleton, Pawn configuration]
domain: middlegame-strategy
summary: >-
  The arrangement of both sides' pawns on the board, treated as a semi-permanent framework that
  decides which squares are strong or weak, where the pieces belong and which plans make sense.
fen: "rnbqk2r/pp2bppp/2p2n2/3p2B1/3P4/2N1P3/PP3PPP/R2QKBNR w KQkq - 0 7"
status: current
volatile: false
verified: 2026-11-08
broader: [kt:chess-strategy]
related: [kt:isolated-queens-pawn, kt:outpost, kt:hanging-pawns]
relations:
  - {predicate: hasPart, object: kt:carlsbad-structure}
  - {predicate: enables, object: kt:minority-attack}
  - {predicate: championedBy, object: kt:francois-andre-danican-philidor}
sources:
  - id: s1
    title: "Chess: Development of theory"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/chess/Development-of-theory
    type: reference
    accessed: 2026-11-08
  - id: s2
    title: "Chess Structures: A Grandmaster Guide (sample pages)"
    publisher: Mauricio Flores Rios, Quality Chess (2014), excerpt hosted by New In Chess
    url: https://www.newinchess.com/media/wysiwyg/product_pdf/7495.pdf
    type: book
    accessed: 2026-11-08
  - id: s3
    title: "Pawn Structure Chess (publisher's catalogue entry)"
    publisher: Andrew Soltis, Batsford / Anova Books (2013), via NetGalley
    url: https://www.netgalley.co.uk/catalog/book/34358
    type: book
    accessed: 2026-11-08
  - id: s4
    title: "Are Pawns The Soul Of Chess?"
    publisher: GM Gregory Serper, Chess.com
    url: https://www.chess.com/article/view/are-pawns-the-soul-of-chess
    type: publication
    accessed: 2026-11-08
  - id: s5
    title: "Minority Attack"
    publisher: Chess.com (Chess Terms)
    url: https://www.chess.com/terms/minority-attack-chess
    type: publication
    accessed: 2026-11-08
  - id: s6
    title: "Pawn Types"
    publisher: Chess.com (Chess Terms)
    url: https://www.chess.com/terms/types-of-pawns
    type: publication
    accessed: 2026-11-08
  - id: s7
    title: "Understanding before Moving 96: Queen's Gambit Declined (3)"
    publisher: IM Herman Grooten, ChessBase News (30 October 2022)
    url: https://en.chessbase.com/post/understanding-before-moving-96-queen-s-gambit-declined-3
    type: publication
    accessed: 2026-11-08
created: 2026-11-08
---

# Pawn structure

Pawn structure is the configuration of all the pawns on the board, taken together for both sides. Because pawns move slowly and can never retreat, the structure changes far less often than the placement of the pieces, and Soltis describes pawns as the semi-permanent "playing fields" on which a game is fought.[^s3] The structure tells a player where the pieces stand best, which pawns should be advanced or exchanged, and why some formations are healthy while others are disastrous.[^s3] Flores Rios argues that grouping positions by pawn structure is the clearest and least ambiguous way to organise chess knowledge.[^s2]

## Historical background

François-André Danican Philidor was the first major writer to put pawns at the centre of strategy. In his 1749 *L'Analyze des échecs* he held that pawns are the basis of any attack, that a mobile, supported pawn mass is the decisive middlegame factor, and that isolated, doubled and backward pawns should be avoided.[^s1] He also showed that the value of a bishop depends on how much a fixed pawn chain hems it in.[^s1] Wilhelm Steinitz later systematised these weaknesses, adding the idea of a "hole", a square that has lost its pawn protection, and the principle that structural weaknesses matter more as pieces are exchanged.[^s1] The hypermodern school around Aron Nimzowitsch then challenged the classical view, treating a broad pawn centre as a possible target and preferring to control central squares with pieces.[^s1]

Philidor's famous dictum that pawns are the soul of chess is still quoted, but GM Gregory Serper points out that it overstates the case: a good structure does not stop a direct attack on the king or make up for a whole rook, and he suggests Philidor exaggerated because pawns were neglected in his era.[^s4] Serper's own conclusion is that no modern master ignores the structure, even if it is not the only factor.[^s4]

## Elements of a structure

Club players usually learn structure through a vocabulary of individual pawn types:[^s6]

- **Doubled pawns**: two pawns of one side on the same file, usually the result of a capture.[^s6][^s1]
- **Isolated pawn**: a pawn with no friendly pawns on the adjacent files, so no pawn can ever defend it.[^s6]
- **Backward pawn**: a pawn whose neighbours have advanced or disappeared; the square in front of it is a ready-made outpost for the opponent.[^s6][^s1]
- **Passed pawn**: a pawn that has got past all the enemy pawns that could stop it, valuable above all in the endgame because it threatens to promote.[^s6]

None of these labels is absolute. Doubled pawns can be outweighed by piece activity, and an isolated pawn can be strong when it is passed or when it supports active play.[^s6] Britannica likewise notes that an isolated pawn may give its owner control of central squares and open files for the rooks.[^s1]

## Structures as families of positions

Strong players think less about single pawns than about whole recurring formations, each with its own typical plans. Flores Rios organises his book into families such as the d4 and ...d5 structures (the isolani, hanging pawns, the Caro-Kann and Slav formations, the Carlsbad, the Stonewall), the Open Sicilian structures (Najdorf types, the Hedgehog, the Maroczy bind), the Benoni and King's Indian complexes, and the French structures.[^s2] Knowing a formation lets a player transfer plans from model games to positions that arise from quite different move orders.[^s2]

## Example: the Carlsbad structure

After 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.cxd5 exd5 5.Bg5 Be7 6.e3 c6, the Exchange Variation of the Queen's Gambit Declined has produced the Carlsbad structure shown in the `fen`: White has a d4-pawn and a queenside pair on a2 and b2, Black has d5 supported by c6 and b7.[^s5] White's best-known plan is the minority attack, advancing b4 and b5 with two pawns against Black's three in order to leave Black with a backward or isolated c-pawn that can be besieged for the rest of the game.[^s5] Black, for his part, can try to delay the queenside play or build an initiative on the kingside once White has castled short.[^s7] The plans flow directly from the structure rather than from the particular position of the pieces.

## Typical mistakes

- **Pawn moves made for no structural reason.** Every pawn advance gives up control of squares for good, which is how the holes Steinitz described arise.[^s1]
- **Treating rules as absolute.** Flores Rios notes that general strategy maxims often contradict one another, and says model games grouped by structure show when a guideline applies and when it does not.[^s2]
- **Ignoring dynamics.** A damaged structure can be fully playable when it brings activity or a strong centre, as many French Winawer games show.[^s4]

## Connections

Pawn structure sits under general **chess strategy** and is the parent of many specific formations, among them the **Carlsbad structure**, the **isolated queen's pawn** and **hanging pawns**.[^s2] The weaknesses it creates give rise to **outposts** in front of backward pawns.[^s6][^s1] The Carlsbad formation is the classic setting for the **minority attack**.[^s5] The modern study of pawn play traces back to **Philidor**.[^s1]

## Sources
[^s1]: Encyclopaedia Britannica, "Chess: Development of theory". https://www.britannica.com/topic/chess/Development-of-theory (accessed 2026-11-08)
[^s2]: M. Flores Rios, *Chess Structures: A Grandmaster Guide*, Quality Chess, sample pages (foreword, preface and contents). https://www.newinchess.com/media/wysiwyg/product_pdf/7495.pdf (accessed 2026-11-08)
[^s3]: A. Soltis, *Pawn Structure Chess*, Batsford (2013 edition), catalogue entry. https://www.netgalley.co.uk/catalog/book/34358 (accessed 2026-11-08)
[^s4]: G. Serper, "Are Pawns The Soul Of Chess?", Chess.com. https://www.chess.com/article/view/are-pawns-the-soul-of-chess (accessed 2026-11-08)
[^s5]: Chess.com, "Minority Attack", Chess Terms. https://www.chess.com/terms/minority-attack-chess (accessed 2026-11-08)
[^s6]: Chess.com, "Pawn Types", Chess Terms. https://www.chess.com/terms/types-of-pawns (accessed 2026-11-08)
[^s7]: H. Grooten, "Understanding before Moving 96: Queen's Gambit Declined (3)", ChessBase News, 30 October 2022. https://en.chessbase.com/post/understanding-before-moving-96-queen-s-gambit-declined-3 (accessed 2026-11-08)
