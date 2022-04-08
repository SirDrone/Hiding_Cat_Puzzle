# Cat_Puzzle
A recreation of a coding interview question purportedly posed by Microsoft/Google.

The puzzle goes that there is a cat among a row of boxes (though another version uses doors).
Each day, we are allowed to pick one of the boxes to see if the cat is inside.
If we're right, we win!  If not, the cat will move to a box adjacent to the one it was actually in, and we have to come back the next day to find it.
Our goal is to reliably decipher a solution where, even in the worst-case, we can minimize the number of days necessary to find the cat.

### This program can:
- Replicate the above cat puzzle\*
- Provide a programmer with step-by-step debugging/analysis of their strategy if desired

*\*If correct, the concept for this puzzle belongs to Microsoft/Google, and any other respective entities.*

### Requirements to run the puzzle:
- We'll first need to ensure we have a terminal or CMD environment
- We'll also need Python3 installed

### Officially running the puzzle [from the terminal within the correct folder]:
     python3 frontend.py

### How does the program work you may ask?
- The program starts with taking in what it needs (e.g. total_boxes, the challenge mode, verbosity/debugging, etc.)
- Next, it picks which box the cat is hiding in
- It asks the player which box they think the cat is hiding in, and does so until the player is correct
    - Caveat, the cat will move to an adjacent box
    - "Absurd" mode makes the cat become as dodgy as possible
        - The cat will be able to undo certain bad moves unless completely cornered
        - This sounds like cheating, but works to recreate a "worst-case" (where you guess incorrectly usually and need a strategy)
    - "Debug" mode can help the player assess their choices and strategy as an "absurd" game progresses
- You can also just play a custom game (such as "Normal" mode) for fun, or increase/decrease the total number of boxes

### Limitations:
- This is but a terminal/command line program
- This program does not intend to solve the challenge itself, merely recreate it for easier solving or analysis

### Feeling completely stumped at finding a consistent solution?
- There is a great guide posted here if you yield:
    - https://mindyourdecisions.com/blog/2017/07/09/can-you-solve-the-hiding-cat-puzzle-tech-interview-question
