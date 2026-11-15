---
id: kt:xiangqi
type: Variant
title: Xiangqi
aliases: [Chinese chess, Hsiang-chi, Xiang Qi]
domain: variants-and-compositions
summary: >-
  The Chinese member of the chess family, played on the 90 intersections of a 9×10 board divided
  by a river, in which each general is confined to a palace and the cannon captures by jumping a screen.
status: current
volatile: true
verified: 2026-11-15
broader: [kt:chess-variants]
related: [kt:shogi, kt:stalemate, kt:computer-chess, kt:janggi]
relations:
  - {predicate: influencedBy, object: kt:chaturanga}
  - {predicate: contrastsWith, object: kt:chess}
  - {predicate: sanctionedBy, object: kt:world-xiangqi-federation}
sources:
  - id: s1
    title: "Chinese chess"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/Chinese-chess
    type: reference
    accessed: 2026-11-15
  - id: s2
    title: "Xiangqi: Chinese Chess"
    publisher: "The Chess Variant Pages (Hans Bodlaender, rewritten by Fergus Duniho)"
    url: https://chessvariants.org/xiangqi.html
    type: community
    accessed: 2026-11-15
  - id: s3
    title: "Xiangqi (Chinese Chess) rules, XBoard"
    publisher: GNU Project
    url: https://www.gnu.org/software/xboard/whats_new/rules/Xiangqi.html
    type: community
    accessed: 2026-11-15
  - id: s4
    title: "About AXF: brief introduction to the AXF Rules (Felix Tan)"
    publisher: Asian Xiangqi Federation
    url: https://asianxiangqi.org/English/AXFrulesEng.htm
    type: governing-body
    accessed: 2026-11-15
  - id: s5
    title: "19th WXF World Xiangqi Championship Regulations"
    publisher: World Xiangqi Federation
    url: https://www.wxf-xiangqi.org/images/2025wxf_shanghai/19th_WXF__World_Xiangqi_Championship_Regulations.pdf
    type: governing-body
    accessed: 2026-11-15
  - id: s6
    title: "Computer Chinese Chess"
    publisher: "S.-J. Yen, J.-C. Chen, T.-N. Yang, S.-C. Hsu, ICGA Journal 27(1), 3–18 (2004)"
    url: https://content.iospress.com/articles/icga-journal/icg27102
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s7
    title: "Space-state complexity of Korean chess and Chinese chess (arXiv:1507.06401)"
    publisher: "Donghwi Park, Korea University"
    url: https://arxiv.org/pdf/1507.06401
    type: academic
    accessed: 2026-11-15
created: 2026-11-15
---

# Xiangqi

**Xiangqi**, usually called Chinese chess in English, is a strategy board game that has been played in China since about AD 700.[^s1] Like Western chess it is generally believed to descend from the Indian game chaturanga, although the writers Sam Sloan and David Li have argued the reverse, that chess itself began in China.[^s1][^s2] It has kept its present form for centuries and is played by millions of people in China, Taiwan, Southeast Asia and beyond.[^s2]

## Board and pieces

The pieces stand on the points where lines cross rather than inside squares: nine files and ten ranks give 90 points, a layout Britannica links to go, which was known in China before chess arrived.[^s1] A horizontal gap, the **river**, splits the board in two, and near each player's edge a nine-point **palace** is marked with diagonal lines.[^s1][^s2] Each side has sixteen flat, disc-shaped pieces labelled with Chinese characters: a general (king), two advisers, two elephants, two horses, two chariots, two cannons and five soldiers. Red moves first.[^s1][^s2]

The general steps one point orthogonally and the advisers one point diagonally, and all three must stay inside the palace.[^s1][^s2] The elephant moves exactly two points diagonally, can be blocked by a piece on the intermediate point, and may never cross the river, so it is a purely defensive piece.[^s2][^s3] The horse moves like a chess knight but does not jump: a piece standing next to it in the direction of travel blocks the move.[^s2][^s3] The chariot moves like a rook. The **cannon** also moves like a rook, but captures only by jumping over exactly one piece, friendly or enemy, called the screen.[^s2][^s3] A soldier moves one point straight forward; once it has crossed the river it may also move sideways, but it never moves backward and does not promote, so a soldier that reaches the last rank can only shuffle along it.[^s2][^s3]

## Winning, drawing and repetition

The aim is to checkmate the enemy general. Two rules change endgame thinking for a chess player. First, the two generals may never face each other on an open file, so a general can take part in a mating net from across the board.[^s2][^s3] Second, a player with no legal move loses: **stalemate is a win** for the side that inflicts it, not a draw.[^s2][^s3] A game is drawn when neither side can force mate or stalemate.[^s2]

Instead of a simple repetition draw, xiangqi forbids certain repeating plans. A player may not give perpetual check, and may not perpetually chase an unprotected enemy piece; in XBoard's implementation the offender loses on the third repetition, and the game is drawn if both sides are doing it.[^s3] The detail matters: a chariot counts as unprotected when attacked by a horse or cannon, and attacks by the general, or on a soldier that has not crossed the river, never count as a chase.[^s3] Codifying these cases was the main purpose of the Asian Xiangqi Federation's competition rules, first approved at an arbiters' conference in Macau in 1982 and revised in 1989 and 2003.[^s4]

## For chess players

The approximate values in the XBoard rules make the material balance concrete: chariot about 10, horse and cannon about 4–5 each, adviser and elephant 2, soldier 1.[^s3] The cannon is the piece with no chess counterpart, and it produces tactics that do not exist in Western chess: pins and double pins depend on which pieces happen to serve as screens, while skewers can only be delivered by chariots and cannons.[^s2] A typical surprise is that moving a defender *away* from a line can disarm a cannon by removing its screen, while moving one *onto* the line can arm it. Endgames are less decisive than in chess; with no promotion and with confined defenders, many simplified positions are drawn, so play is often a race to mate.[^s3]

Moves are recorded in several systems. Traditional Chinese notation names the piece, the file it stands on, its direction and its destination; the World Xiangqi Federation uses a similar English form with + and − for direction, while other systems use chess-style coordinates with files a–i.[^s2]

## Competition and computers

As of November 2026 the World Xiangqi Federation runs a world championship; its 19th edition was held in Shanghai from 22 to 27 September 2025 under the World Xiangqi Rules, with men's and women's team and individual events and a time control of 60 minutes plus 30 seconds per move.[^s5] In computing, a 2004 ICGA Journal survey placed the game's complexity between chess and go, named ELP and SHIGA as the leading programs at the 2001 and 2002 Computer Olympiads, and predicted that a program would beat a top human player before 2010.[^s6] An arXiv preprint by Donghwi Park counts the reachable positions of xiangqi at about 7.6 × 10^39, against about 2.35 × 10^44 for its Korean relative janggi.[^s7]

## Connections

Xiangqi sits under **chess variants** as a parallel descendant of **chaturanga** rather than a modification of modern chess, and it **contrasts with chess** in board geometry, the palace, the cannon and the treatment of **stalemate** as a win.[^s1][^s2] Its closest relatives are **shogi**, the other great Asian chess game, and **janggi**, the Korean game whose complexity Park compares with it.[^s7] The game's competitive rules are **sanctioned by the World Xiangqi Federation**, and it has been a long-running testbed for **computer chess** methods.[^s5][^s6]

## Sources
[^s1]: Encyclopaedia Britannica, "Chinese chess". https://www.britannica.com/topic/Chinese-chess (accessed 2026-11-15)
[^s2]: H. Bodlaender and F. Duniho, "Xiangqi: Chinese Chess", The Chess Variant Pages. https://chessvariants.org/xiangqi.html (accessed 2026-11-15)
[^s3]: GNU Project, "Xiangqi (Chinese Chess)", XBoard rules. https://www.gnu.org/software/xboard/whats_new/rules/Xiangqi.html (accessed 2026-11-15)
[^s4]: Asian Xiangqi Federation, "About AXF" (introduction by Felix Tan). https://asianxiangqi.org/English/AXFrulesEng.htm (accessed 2026-11-15)
[^s5]: World Xiangqi Federation, "19th WXF World Xiangqi Championship Regulations" (2025). https://www.wxf-xiangqi.org/images/2025wxf_shanghai/19th_WXF__World_Xiangqi_Championship_Regulations.pdf (accessed 2026-11-15)
[^s6]: S.-J. Yen, J.-C. Chen, T.-N. Yang, S.-C. Hsu, "Computer Chinese Chess", ICGA Journal 27(1), 3–18 (2004). https://content.iospress.com/articles/icga-journal/icg27102 (accessed 2026-11-15)
[^s7]: D. Park, "Space-state complexity of Korean chess and Chinese chess", arXiv:1507.06401. https://arxiv.org/pdf/1507.06401 (accessed 2026-11-15)
