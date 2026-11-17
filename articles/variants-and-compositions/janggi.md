---
id: kt:janggi
type: Variant
title: Janggi
aliases: [Korean chess, Changgi, Jang-gi, Tjyang Keui]
domain: variants-and-compositions
summary: >-
  The Korean member of the chess family, a close relative of xiangqi played on the points of a 9×10 grid,
  in which players choose their horse and elephant placement, may pass instead of moving, and settle
  some drawn situations by counting material.
status: current
volatile: false
verified: 2026-11-17
broader: [kt:chess-variants]
related: [kt:xiangqi, kt:shogi, kt:stalemate, kt:perpetual-check]
relations:
  - {predicate: influencedBy, object: kt:xiangqi}
  - {predicate: contrastsWith, object: kt:chess}
sources:
  - id: s1
    title: "Space-state complexity of Korean chess and Chinese chess (arXiv:1507.06401)"
    publisher: "Donghwi Park, Korea University"
    url: https://pdf.arxiv.org/pdf/1507.06401
    type: academic
    accessed: 2026-11-17
  - id: s2
    title: "Development of Artificial Intelligence Janggi Game based on Machine Learning Algorithm"
    publisher: "M. Jang, Y. Kim, D. Min, K. Park, S. Lee, C. Woo, Journal of Information Technology Services 16(4), 2017"
    url: https://koreascience.kr/article/JAKO201712965731619.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "쟝기두고 (men playing jang-gi), watercolour by Gisan, 1886, object 21574S"
    publisher: Penn Museum, University of Pennsylvania
    url: https://collections.penn.museum/collections/object/17292
    type: archive
    accessed: 2026-11-17
  - id: s4
    title: "Janggi (variant guide)"
    publisher: PyChess
    url: https://www.pychess.org/variants/janggi
    type: community
    accessed: 2026-11-17
  - id: s5
    title: "Fairy-Stockfish (README)"
    publisher: Fairy-Stockfish project, GitHub
    url: https://github.com/ianfab/Fairy-Stockfish
    type: official-project
    accessed: 2026-11-17
created: 2026-11-17
---

# Janggi

**Janggi** (장기), Korean chess, is the chess game traditionally played in Korea. A mathematical study of its positions describes it as derived from Chinese chess, sharing very similar pieces and a very similar board, but giving most pieces far more freedom of movement than they have in xiangqi.[^s1] The game has a long documented presence in Korean life: the Penn Museum holds an 1886 watercolour by the Busan-area artist Gisan showing two men in traditional dress at a jang-gi board, one of a set of 23 paintings of Korean games, and it is illustrated in Robert S. Culin's 1895 study *Korean Games*.[^s3]

## Board, sides and pieces

As in xiangqi, the pieces stand on the intersections of a grid of nine files and ten ranks, and each side has a 3×3 **palace** marked with diagonal lines.[^s4] The two sides are called **Cho** and **Han**.[^s2] Each side has a king (general), two advisors (guards), two chariots, two cannons, two horses, two elephants and a row of soldiers.[^s1][^s2]

- **King and advisors** step one point along the palace lines, including the diagonals, and may never leave the palace.[^s4]
- **Chariot** moves like a chess rook, and inside a palace it may also travel along the diagonals.[^s4]
- **Cannon** moves as well as captures by jumping over exactly one piece, the screen. A cannon cannot use another cannon as a screen and cannot capture a cannon, so without a screen it cannot move at all.[^s4]
- **Horse** goes one step orthogonally and then one step diagonally outward; a piece on the first point blocks it.[^s4]
- **Elephant** goes one step orthogonally and then two steps diagonally, and can be blocked anywhere along that path, so it is a long-range relative of the horse rather than the confined defender of xiangqi.[^s4]
- **Soldier** moves one point forward or sideways, and diagonally forward inside the enemy palace. It never moves backward, and like every janggi piece it never promotes.[^s1][^s4]

Because elephants and horses are free to roam the whole board, Park counts eight free-moving labelled pieces in janggi against six in xiangqi; he puts the number of legal positions at about 2.35 × 10^44, roughly 30,000 times the 7.59 × 10^39 he finds for xiangqi.[^s1]

## Setups, passing and counting

Before play each player decides whether each horse–elephant pair stands with the elephant inside or outside, giving four possible arrangements; a recorded game notes both sides' setups along with the result and moves.[^s2][^s4] Cho moves first, and in tournament scoring Han receives 1.5 points of compensation (*deom*) for that advantage.[^s4]

A player may **pass** instead of moving, so stalemate cannot arise.[^s4] When the two kings face each other on an open file, the position is **bikjang**: the player to move must break it or pass, and passing ends the game. In casual play that is a draw, while tournament-style rules decide it by counting material, with chariot 13, cannon 7, horse 5, elephant 3, advisor 3 and soldier 2, plus Han's 1.5.[^s4] The same values appear in a 2017 Korean research paper on a janggi-playing program.[^s2] Perpetual check loses for the checking side after the third repetition; other repetitions, and 100 half-moves without a capture, are settled by the same count.[^s4]

## For chess players

The two big adjustments are the elephant and the cannon. Since the elephant's long Y-shaped jump can be blocked, and the cannon needs a screen even to move, piece activity depends heavily on what stands between the pieces.[^s4] Palace diagonals turn the palace into the main battlefield: a chariot or cannon that reaches one of its corners can strike along the diagonal at the king.[^s4] The pass rule removes zugzwang and stalemate tricks, and material counting means a player who is ahead in points can aim for bikjang or repetition rather than mate.[^s4]

## Computers

Janggi is a natural testbed for game programs. The 2017 study combined reinforcement learning and Monte Carlo tree search with a minimax fallback, stored positions in a graph because janggi positions repeat, and reported winning about 59% of decisive games against an online program.[^s2] The open-source engine Fairy-Stockfish, a multi-variant derivative of Stockfish, supports janggi and publishes dedicated releases with built-in NNUE networks for janggi, xiangqi and makruk.[^s5]

## Connections

Janggi sits under **chess variants** as an East Asian member of the chess family, **influenced by xiangqi**, from which it derives its board and pieces.[^s1] It **contrasts with chess** in having no promotion, a confined king and a pass rule that abolishes **stalemate**, and it shares xiangqi's ban on **perpetual check**.[^s1][^s4] Like **shogi** and xiangqi it has drawn the attention of computer-game researchers and multi-variant engines.[^s2][^s5]

## Sources
[^s1]: D. Park, "Space-state complexity of Korean chess and Chinese chess", arXiv:1507.06401. https://pdf.arxiv.org/pdf/1507.06401 (accessed 2026-11-17)
[^s2]: M. Jang, Y. Kim, D. Min, K. Park, S. Lee, C. Woo, "Development of Artificial Intelligence Janggi Game based on Machine Learning Algorithm", Journal of Information Technology Services 16(4) (2017). https://koreascience.kr/article/JAKO201712965731619.pdf (accessed 2026-11-17)
[^s3]: Penn Museum, "쟝기두고", watercolour by Gisan of Choryang, 1886, object 21574S. https://collections.penn.museum/collections/object/17292 (accessed 2026-11-17)
[^s4]: PyChess, "Janggi". https://www.pychess.org/variants/janggi (accessed 2026-11-17)
[^s5]: Fairy-Stockfish project, README. https://github.com/ianfab/Fairy-Stockfish (accessed 2026-11-17)
