---
id: kt:makruk
type: Variant
title: Makruk
aliases: [Thai chess, Mak ruk, Makrook, Mak-ruk]
domain: variants-and-compositions
summary: >-
  The traditional chess of Thailand, a descendant of chaturanga played on an 8×8 board with a
  one-step diagonal queen (met), a silver-general-like bishop (khon), pawns that start on the third rank
  and promote on the sixth, and counting rules that limit how long the stronger side has to deliver mate.
status: current
volatile: true
verified: 2026-11-19
broader: [kt:chess-variants]
related: [kt:shogi, kt:xiangqi, kt:janggi, kt:stalemate, kt:endgame-tablebases, kt:pawn-promotion]
relations:
  - {predicate: influencedBy, object: kt:chaturanga}
  - {predicate: contrastsWith, object: kt:chess}
  - {predicate: sanctionedBy, object: kt:thai-sports-association-under-royal-patronage}
  - {predicate: alternativeTo, object: kt:sittuyin}
sources:
  - id: s1
    title: "Building Makruk Endgame Tablebases: A Computational Study of Ma-Bia Ngai and Khon-Bia Ngai Endgames"
    publisher: "T. Tudsuan and T. Thanatipanonda, Journal of Science Ladkrabang 35(1), 2026, pp. 112–129"
    url: https://li01.tci-thaijo.org/index.php/science_kmitl/article/view/270913
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s2
    title: "Communicating the Soft Power of Thailand's Cultural Heritage through Traditional Sport (Thai Chess)"
    publisher: "P. Rodloytuk, Arts of Management Journal 8(3), 2024, pp. 15–38"
    url: https://so02.tci-thaijo.org/index.php/jam/article/view/269725
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s3
    title: "Makruk (variant guide)"
    publisher: PyChess
    url: https://www.pychess.org/variants/makruk
    type: community
    accessed: 2026-11-19
  - id: s4
    title: "Makruk (Thai Chess) — XBoard variant rules"
    publisher: GNU XBoard project
    url: https://www.gnu.org/software/xboard/whats_new/rules/Makruk.html
    type: community
    accessed: 2026-11-19
  - id: s5
    title: "Makruk: Thai Chess"
    publisher: "Hans Bodlaender, The Chess Variant Pages"
    url: https://chessvariants.org/oriental.dir/thai.html
    type: community
    accessed: 2026-11-19
  - id: s6
    title: "From Happenstance to First International Makruk Open Champion"
    publisher: "Peter Long (FM, FIDE Trainer, International Arbiter), ChessBase India, 18 March 2024"
    url: https://chessbase.in/news/From-Happenstance-to-First-International-Makruk-Open-Champion
    type: publication
    accessed: 2026-11-19
created: 2026-11-19
---

# Makruk

**Makruk** (หมากรุก), known in the West as Thai chess, is the chess game traditionally played in Thailand. Like international chess it descends from the Indian game chaturanga, and it keeps more of the old slow-moving pieces than its European cousin does.[^s3][^s6] A survey-based study of the game as Thai cultural heritage describes it as a traditional sport that began to be played competitively around 1952.[^s2] Bodlaender's long-standing variant reference calls it the most played chess variant in Thailand, citing an estimate of some two million Thais who know the rules.[^s5]

## Board and pieces

Makruk uses an ordinary 8×8 board. The back ranks are set up as in chess except that the king and the met (the queen's counterpart) trade places, and each player's king stands on that player's left: White's king on d1 and Black's on e8, so the kings do not face each other on a file.[^s3][^s4] Pawns start on the **third** rank rather than the second, and there is no castling.[^s3][^s5]

- **Khun** (king) moves as in chess.[^s5]
- **Met** steps one square diagonally only, making it worth roughly one and a half to two pawns.[^s3][^s4]
- **Khon** steps one square diagonally in any direction or one square straight forward, the same move as the shogi silver general; it is valued above the met but usually below a knight.[^s3][^s4]
- **Ma** (knight) and **ruea** (rook) move exactly as in chess, so the rook is the only long-range piece and the only one that can pin or skewer.[^s3]
- **Bia** (pawn) moves and captures like a chess pawn, but with no double step and therefore no en passant.[^s3][^s4]

A pawn **promotes on the sixth rank**, the opponent's starting pawn rank, and always becomes a met; several promoted pawns can be on the board at once.[^s3][^s5] The piece names carry meanings of their own: Bodlaender glosses *met* as a seed or fruit pit and *bia* as a cowry shell, the material once used for pawns, which were turned over on promotion.[^s5] Older practice allowed special first moves, such as a knight-like jump for the king, which have since fallen out of use in Thai play; XBoard still lists them as part of Cambodian rules.[^s4][^s5]

## Winning, drawing and counting

Checkmate wins and stalemate is a draw.[^s3][^s4] Because the minor pieces are so weak, many material advantages that win easily in chess cannot be converted: a lone met, khon or knight cannot force mate against a bare king, nor can two knights or two mets.[^s4]

Instead of a fifty-move rule, makruk limits long endgames with **counting**. Once no unpromoted pawns remain, the defending side may start a "board's honour" count from 1 to 64; if mate has not come by then, the game is drawn.[^s3][^s5] When the defender is reduced to a bare king, a stricter "piece's honour" count applies: it starts at the number of pieces on the board (both kings included) plus one, and its limit depends on the attacker's force — 8 with two rooks, 16 with one rook, 22 with two khons, 32 with two knights, 44 with one khon, 64 with one knight or only mets.[^s3][^s5] For example, with two rooks against a bare king there are five pieces, so the count runs from 5 to 8 and the attacker has only a few moves to finish the job; a later capture does not reset the count or change the limit.[^s3]

These limits change real results. A 2026 tablebase study of king, khon and promoted pawn against a bare king found that 85.77% of its 12,170,304 legal positions are wins without counting, but only 83.49% once the 41-move allowance left by the counting rule is applied; with a knight instead of the khon, only about 4% of positions are wins at all.[^s1]

## For chess players

Without a long-range queen or bishop, play is slower and more strategic, and exchanges of the unfamiliar met and khon tend to leave dull, drawish endings.[^s3] The rook dominates tactics, and knowing which material can mate within the count matters as much as in a chess endgame.[^s1][^s3]

## Organisation

In Thailand makruk is administered as a traditional sport under the Thai Sports Association under Royal Patronage; as of March 2024 its national championship drew about 300 qualifiers, and a first International Makruk Open and an English-language referee seminar opened the game to foreign players.[^s6]

## Connections

Makruk sits under **chess variants** and, like international chess, is **influenced by chaturanga**, from which it keeps the weak diagonal queen and short-range pieces.[^s3][^s6] It **contrasts with chess** in its promotion rank, its piece moves and its counting rules, and its khon links it to **shogi**'s silver general.[^s3] Its Burmese relative **sittuyin** is a natural alternative with pawns on the fourth rank.[^s3] Its endgames have been mapped with **endgame tablebases** much as in chess.[^s1]

## Sources
[^s1]: T. Tudsuan and T. Thanatipanonda, "Building Makruk Endgame Tablebases: A Computational Study of Ma-Bia Ngai and Khon-Bia Ngai Endgames", Journal of Science Ladkrabang 35(1) (2026), 112–129. https://li01.tci-thaijo.org/index.php/science_kmitl/article/view/270913 (accessed 2026-11-19)
[^s2]: P. Rodloytuk, "Communicating the Soft Power of Thailand's Cultural Heritage through Traditional Sport (Thai Chess)", Arts of Management Journal 8(3) (2024), 15–38. https://so02.tci-thaijo.org/index.php/jam/article/view/269725 (accessed 2026-11-19)
[^s3]: PyChess, "Makruk". https://www.pychess.org/variants/makruk (accessed 2026-11-19)
[^s4]: GNU XBoard, "Makruk (Thai Chess)". https://www.gnu.org/software/xboard/whats_new/rules/Makruk.html (accessed 2026-11-19)
[^s5]: H. Bodlaender, "Makruk: Thai Chess", The Chess Variant Pages. https://chessvariants.org/oriental.dir/thai.html (accessed 2026-11-19)
[^s6]: P. Long, "From Happenstance to First International Makruk Open Champion", ChessBase India, 18 March 2024. https://chessbase.in/news/From-Happenstance-to-First-International-Makruk-Open-Champion (accessed 2026-11-19)
