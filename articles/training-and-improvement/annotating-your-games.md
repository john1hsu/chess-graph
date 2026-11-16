---
id: kt:annotating-your-games
type: TrainingMethod
title: Annotating your games
aliases: ["Analysing your own games", "Analyzing your own games", "Analysing your games", "Analyzing your games", "Game annotation", "Annotating your own games", "Post-mortem analysis", "Self-analysis of games"]
domain: training-and-improvement
summary: >-
  Reviewing your own finished games and writing down your thoughts, alternatives and lessons
  move by move, first unaided and only then checked with an engine, so that recurring errors in
  thinking become visible and can be trained away.
status: current
volatile: false
verified: 2026-11-16
broader: [kt:deliberate-practice]
related: [kt:calculation, kt:puzzle-training, kt:opening-repertoire, kt:time-management-in-games, kt:chess-expertise]
relations:
  - {predicate: dependsOn, object: kt:algebraic-notation}
  - {predicate: governedBy, object: kt:fide-laws-of-chess}
  - {predicate: usesTechnique, object: kt:portable-game-notation}
  - {predicate: hasPart, object: kt:numeric-annotation-glyphs}
  - {predicate: contrastsWith, object: kt:puzzle-training}
sources:
  - id: s1
    title: "FIDE Laws of Chess (applied from 1 January 2023), full text"
    publisher: FIDE Rules Commission
    url: https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/
    type: governing-body
    accessed: 2026-11-16
  - id: s2
    title: "The Impact of Domain-Specific Experience on Chess Skill: Reanalysis of a Key Study (American Journal of Psychology 132(1), 27-38)"
    publisher: Alexander P. Burgoyne, Christopher D. Nye, Brooke N. Macnamara, Neil Charness and David Z. Hambrick, via Georgia Tech Engle Lab
    url: https://englelab.gatech.edu/articles/2019/Burgoyne_et_al_2019_AJP.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "The Role of Practice in Chess: A Longitudinal Study (Learning and Individual Differences, author manuscript)"
    publisher: Guillermo Campitelli and Fernand Gobet, Brunel University, via CORE
    url: https://core.ac.uk/download/334073.pdf
    type: academic
    accessed: 2026-11-16
  - id: s4
    title: "The Improving Annotator: From Beginner to Master"
    publisher: Dan Heisman, Mongoose Press (Readings Books listing)
    url: https://www.readings.com.au/product/9781936277049/the-improving-annotator-from-beginner-to-master--dan-heisman--2011--9781936277049
    type: book
    accessed: 2026-11-16
  - id: s5
    title: "Analyse Your Chess"
    publisher: Colin Crouch, Everyman Chess (Schachversand listing)
    url: https://www.schachversand.de/analyse-your-chess.html
    type: book
    accessed: 2026-11-16
  - id: s6
    title: "Analyse your games"
    publisher: Exeter Chess Club
    url: https://exeterchessclub.org.uk/sites/exeterchessclub.org.uk/files/AnalyseYourGames.pdf
    type: community
    accessed: 2026-11-16
  - id: s7
    title: "Portable Game Notation Specification and Implementation Guide (revised 1994-03-12)"
    publisher: Steven J. Edwards (coordinator), mirrored in the GNU Emacs ELPA repository
    url: https://code.delx.au/gnu-emacs-elpa/blob/65de55274ce8d49fa67bb555050e2481ebcad2c5:/PGN.txt
    type: community
    accessed: 2026-11-16
created: 2026-11-16
---

# Annotating your games

Annotating your games means going back over games you have played and writing down, move by move, what you were thinking, what you rejected, where the balance changed and what you should have done instead. It is one of the oldest improvement habits in chess and one that coaches and authors return to again and again: Colin Crouch built a whole book on the premise that steady progress depends on critical assessment of your own games, annotating 50 of his own games from 2009 and early 2010, including every loss.[^s5] Dan Heisman's *The Improving Annotator* (Mongoose Press, 2011) makes the same case, arguing that reviewing your decisions and their outcomes exposes flaws in the way you think, and uses four decades of his own tournament games to show how a player's annotations mature as he improves.[^s4]

## Why it works

In expertise research this kind of work counts as solitary "serious study", the activity closest to deliberate practice. Ericsson and Charness classed the planning and extended evaluation of chess games as self-directed study with most of the features of deliberate practice.[^s2] In the key study by Charness and colleagues, total hours of serious study predicted current and peak rating more strongly than formal instruction or tournament play, and it was the only predictor of rating among players aged 40 or over.[^s2] The evidence is not simple, though: a longitudinal study by Campitelli and Gobet found that hours of individual practice correlated with national rating, but less strongly than group practice such as tournaments and club play, and the number of chess books a player owned was the strongest single predictor.[^s3] Neither study isolates annotation of one's own games as a separate variable, and a reanalysis notes that training left much of the variance in rating unexplained.[^s2][^s3] What annotation adds to playing is feedback: a game gives a result, while a careful review shows which decisions caused it.[^s4]

## How to do it

The record that makes analysis possible is required by the rules. In standard games under the FIDE Laws of Chess each player must record both sides' moves, move by move, in algebraic notation on a paper or certified electronic scoresheet, which belongs to the organiser; a player with under five minutes and no increment of at least 30 seconds may stop recording.[^s1] During the game, notes, outside advice and analysis on another board are forbidden, so all annotation happens after play.[^s1]

A method commonly recommended to club players runs in stages.[^s6]

1. **Write down your thoughts straight away**, while you still remember them: candidate moves you rejected, replies you overlooked and who you thought was better at each stage.[^s6]
2. **Review the critical moments** on your own, especially the big mistakes and the moves where the assessment swung, for instance from winning to equal.[^s6]
3. **Check the opening**: find where you, or your opponent, left known theory and what was recommended there.[^s6]
4. **Only then use an engine**, to confirm or refute your conclusions and reveal missed tactics; try to understand why it prefers a move, because if the computer does the thinking, only the computer improves.[^s6]
5. **Draw lessons and look for patterns** across games, classifying serious errors as tactical, positional, time-trouble or endgame technique, and asking why each one happened.[^s6]

Stored digitally, annotations normally live in PGN files. The PGN standard provides brace comments, variations in parentheses (recursive annotation variations) and Numeric Annotation Glyphs, so a "!" on import becomes $1 (good move), "?" becomes $2, "!!" $3, "??" $4, "!?" $5 and "?!" $6.[^s7] A minimal annotated fragment, using the opening of the PGN standard's own sample game, looks like this:[^s7]

```pgn
[Event "Annotation format example"]
[Result "*"]

1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6
8. c3 O-O 9. h3 Nb8 {Note here the move you expected, the time you had left
and how you judged the position.} 10. d4 Nbd7 *
```

## Pitfalls

The most common mistake is to switch on the engine first: the review then records the machine's verdict rather than your own reasoning, and the thinking errors that caused the loss stay hidden.[^s6] Another is to annotate only the moves and not the thoughts behind them, which is what makes the exercise revealing.[^s4][^s6] Analysing only wins, or skipping painful losses, defeats the purpose; Crouch deliberately included all of his.[^s5] Finally, a single game's lesson is less useful than a pattern found across many games, so keeping a running list of error types pays off.[^s6]

## Connections

Annotating your games is a form of deliberate practice and part of the serious study that predicts chess expertise.[^s2][^s3] It depends on the game score that the FIDE Laws of Chess require players to keep in algebraic notation, and it is usually stored in Portable Game Notation, whose Numeric Annotation Glyphs encode the familiar ! and ? symbols.[^s1][^s7] A good review covers calculation errors, opening repertoire gaps and time management, the categories club guidance asks players to classify.[^s6] It contrasts with puzzle training: puzzles drill known patterns in positions with a clear answer, while annotation looks for the errors in your own play, which rarely announce themselves.[^s4][^s6]

## Sources

[^s1]: FIDE Rules Commission, "FIDE Laws of Chess" (approved 2022, applied from 1 January 2023), Articles 8 and 11.3.1. https://rcc.fide.com/fide-laws-of-chess_fulltexthtml/ (accessed 2026-11-16)
[^s2]: Burgoyne, A. P., Nye, C. D., Macnamara, B. N., Charness, N. & Hambrick, D. Z. (2019), "The Impact of Domain-Specific Experience on Chess Skill: Reanalysis of a Key Study", *American Journal of Psychology* 132(1), 27-38. https://englelab.gatech.edu/articles/2019/Burgoyne_et_al_2019_AJP.pdf (accessed 2026-11-16)
[^s3]: Campitelli, G. & Gobet, F., "The Role of Practice in Chess: A Longitudinal Study", *Learning and Individual Differences* (author manuscript). https://core.ac.uk/download/334073.pdf (accessed 2026-11-16)
[^s4]: Heisman, D. (2011), *The Improving Annotator: From Beginner to Master*, Mongoose Press. https://www.readings.com.au/product/9781936277049/the-improving-annotator-from-beginner-to-master--dan-heisman--2011--9781936277049 (accessed 2026-11-16)
[^s5]: Crouch, C. (2011), *Analyse Your Chess*, Everyman Chess. https://www.schachversand.de/analyse-your-chess.html (accessed 2026-11-16)
[^s6]: Exeter Chess Club, "Analyse your games". https://exeterchessclub.org.uk/sites/exeterchessclub.org.uk/files/AnalyseYourGames.pdf (accessed 2026-11-16)
[^s7]: Edwards, S. J. (coordinator), "Portable Game Notation Specification and Implementation Guide", revised 1994-03-12, sections 5, 8.2.5 and 10. https://code.delx.au/gnu-emacs-elpa/blob/65de55274ce8d49fa67bb555050e2481ebcad2c5:/PGN.txt (accessed 2026-11-16)
