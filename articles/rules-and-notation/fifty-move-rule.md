---
id: kt:fifty-move-rule
type: Rule
title: Fifty-move rule
aliases: [50-move rule, Fifty move rule, Fifty-move draw, Article 9.3, Seventy-five-move rule, 75-move rule]
domain: rules-and-notation
summary: >-
  The FIDE rule that the player on the move may claim a draw once each side has made 50
  consecutive moves without a pawn move or a capture; since 2014 FIDE also ends such a game
  automatically after 75 moves by each side.
fen: "3k4/7r/3K4/4B3/8/8/8/R7 w - - 90 140"
status: current
volatile: true
verified: 2026-11-12
broader: [kt:fide-laws-of-chess, kt:draw]
related: [kt:threefold-repetition, kt:dead-position, kt:stalemate, kt:endgame-tablebases, kt:arbiter, kt:forsyth-edwards-notation, kt:us-chess]
relations:
  - {predicate: partOf, object: kt:fide-laws-of-chess}
  - {predicate: developedBy, object: kt:fide}
  - {predicate: contrastsWith, object: kt:dead-position}
sources:
  - id: s1
    title: "Article 9: The Drawn Game"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/article9/
    type: governing-body
    accessed: 2026-11-12
  - id: s2
    title: "Summary of differences between the FIDE Laws of Chess and the US Chess Official Rules of Chess, 7th edition (updated 1 January 2022)"
    publisher: US Chess
    url: https://new.uschess.org/sites/default/files/media/documents/uschess-fide-rules-comparison.pdf
    type: governing-body
    accessed: 2026-11-12
  - id: s3
    title: "Chess: the 50-move Rule"
    publisher: Edward Winter, Chess Notes (chesshistory.com)
    url: https://chesshistory.com/winter/extra/fifty.html
    type: reference
    accessed: 2026-11-12
  - id: s4
    title: "The Saving 75"
    publisher: Amir Erfan Hashemi, FIDE Arbiters' Commission (arbiters.fide.com), April 2023
    url: https://arbiters.fide.com/wp-content/uploads/2023/06/The-Saving-75.pdf
    type: publication
    accessed: 2026-11-12
  - id: s5
    title: "Fifty Shades of a Draw"
    publisher: Tamas Gyomber, ChessBase News / ECU E-Magazine, February 2023
    url: https://en.chessbase.com/post/fifty-shades-of-a-draw
    type: publication
    accessed: 2026-11-12
  - id: s6
    title: "Chess Endgame Records (v7, 2014)"
    publisher: Guy Haworth, University of Reading
    url: https://reading-9.eprints-hosting.org/34268/2/chessendrecann.pdf
    type: academic
    accessed: 2026-11-12
  - id: s7
    title: "Frequently Asked Questions"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/frequently-asked-questions/
    type: governing-body
    accessed: 2026-11-12
created: 2026-11-12
---

# Fifty-move rule

The fifty-move rule lets a player end a game that is going nowhere. Under Article 9.3 of the FIDE Laws of Chess, as published by the FIDE Rules Commission (checked November 2026), the game is drawn on a correct claim by the player on the move if the last 50 moves by each player were made without any pawn move and without any capture, or if the move the claimant has written on the scoresheet and declared to the arbiter would complete such a sequence.[^s1] The count therefore restarts whenever a pawn moves or anything is captured; checks, king walks and piece manoeuvres do not reset it.[^s1]

## How a claim works

The rule is a claim, not an automatic result. The claimant, or the arbiter, pauses the clock and the claim cannot be withdrawn; if it is correct the game is drawn at once, and if it is wrong the arbiter adds two minutes to the opponent's time and play continues, with any declared move then played on the board.[^s1] A player who has touched a piece under the touch-move rule loses the right to claim on that move.[^s1] International Arbiter Tamas Gyomber lists the usual ways real claims go wrong: playing the move on the board before claiming, picking up a piece to show the intended move, or forgetting to write the move down first.[^s5] He also notes that the claim counts as a draw offer, so an opponent who disputes the count may simply accept it.[^s5]

US Chess handles timing differently. Its rules, as summarised by US Chess in January 2022, let a player stay "on the move" until the clock is pressed, so the claimant may make the 50th move on the board and claim before pressing the clock; under FIDE the move must instead be written but not played.[^s2]

## The automatic 75-move draw

Because the arbiter cannot act on the fifty-move rule unless someone claims, FIDE added a backstop.[^s4] Article 9.6 now ends the game as a draw, with no claim needed, once at least 75 moves by each player have been made without a pawn move or capture; a checkmate delivered on the last of those moves still stands.[^s1] IA Amir Erfan Hashemi dates the first version to the Laws in force from 1 July 2014, with the current wording from 1 January 2023, and describes a game at the 2022 World Rapid and Blitz Championships in which a flag fell one move after the 75-move limit had already ended the game, so the result was later changed to a draw.[^s4] US Chess has only a weaker form: its director may declare the draw but is not obliged to.[^s2]

## History and the endgame exceptions

Winter's research collection traces a 50-move requirement back to Ruy López's book of 1561 and shows that nineteenth-century versions were vague and disputed, with the count sometimes starting only from the moment of the claim.[^s3] Hashemi summarises how the rule then grew exceptions as analysts, beginning with Troitsky's work on two knights against a pawn, found endings that needed more than 50 moves to win.[^s4] FIDE allowed extended limits for such positions from 1928; a 1984 revision fixed 100 moves for a listed set of endings, and a 1989 revision cut this to 75 moves for six of them, including rook and bishop against rook and queen against two bishops.[^s4] The exceptions were short-lived: by the 2001 Laws, Article 9.3 gave 50 moves for every position.[^s4] The Rules Commission also recalls that in 1996 problemists asked for an exception for compositions and were told the Laws govern over-the-board play only.[^s7]

Computers explain why the exceptions were abandoned rather than extended. Guy Haworth's catalogue of endgame-table records lists wins far beyond any practical limit, such as a 523-ply (about 262-move) maximum depth to mate in rook and knight against two knights.[^s6] The same document notes that modern tables, such as Syzygy, now report results under the 50-move rule itself.[^s6]

## Practical points

- **Count from the scoresheet.** The key position above is a rook-and-bishop-versus-rook ending whose FEN halfmove clock reads 90, meaning 45 moves by each side since the last capture or pawn move; the defender needs only five more moves before claiming. In a real game the claimant's scoresheet is the evidence, which is why accurate recording matters.[^s1][^s5]
- **Write, then claim.** Under FIDE, write the move that completes the 50, do not play it, and call the arbiter.[^s1][^s2]
- **The attacker's resource.** A pawn move or capture resets the count, so the stronger side can sometimes buy time by exchanging or advancing a pawn.[^s1]

## Connections

The fifty-move rule is **part of** the **FIDE Laws of Chess** (Article 9), **developed by** **FIDE**, and is one route to a **draw**.[^s1] It sits next to **threefold repetition** in Article 9.2 and shares its claim procedure and its automatic fivefold/75-move backstop.[^s1][^s5] It **contrasts with** the **dead position** and **stalemate** rules, which end the game at once without a claim. Its history is tied to **endgame tablebases**, whose long wins showed no fixed limit could cover every ending, and the **Forsyth–Edwards Notation** halfmove clock exists to track it.[^s4][^s6] Claims are decided by the **arbiter**, and **US Chess** applies its own variant.[^s2]

## Sources

[^s1]: FIDE Rules Commission, "Article 9: The Drawn Game". https://rcc.fide.com/article9/ (accessed 2026-11-12)
[^s2]: US Chess, "Summary of differences between the FIDE Laws of Chess and the US Chess Official Rules of Chess, 7th edition" (updated 1 January 2022). https://new.uschess.org/sites/default/files/media/documents/uschess-fide-rules-comparison.pdf (accessed 2026-11-12)
[^s3]: Edward Winter, Chess Notes, "Chess: the 50-move Rule". https://chesshistory.com/winter/extra/fifty.html (accessed 2026-11-12)
[^s4]: Amir Erfan Hashemi, FIDE Arbiters' Commission, "The Saving 75" (April 2023). https://arbiters.fide.com/wp-content/uploads/2023/06/The-Saving-75.pdf (accessed 2026-11-12)
[^s5]: Tamas Gyomber, ChessBase News / ECU E-Magazine, "Fifty Shades of a Draw" (February 2023). https://en.chessbase.com/post/fifty-shades-of-a-draw (accessed 2026-11-12)
[^s6]: Guy Haworth, University of Reading, "Chess Endgame Records" (v7, 2014). https://reading-9.eprints-hosting.org/34268/2/chessendrecann.pdf (accessed 2026-11-12)
[^s7]: FIDE Rules Commission, "Frequently Asked Questions". https://rcc.fide.com/frequently-asked-questions/ (accessed 2026-11-12)
