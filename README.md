# Code Cracker Game 🎯

A Python implementation of the classic **Mastermind** code-breaking game. Players attempt to guess a secret color code within a limited number of tries.

## How to Play

The computer generates a secret code consisting of 4 colors. Your goal is to guess the exact sequence within 10 attempts.

### Game Rules

- **Code Length**: 4 colors
- **Available Colors**: R (Red), G (Green), B (Blue), Y (Yellow), W (White), O (Orange)
- **Maximum Attempts**: 10 tries
- **Input Format**: Space-separated color letters (e.g., `R G B Y`)

### Feedback System

After each guess, you'll receive feedback:
- **Correct Positions**: Number of colors that are correct and in the right position
- **Incorrect Positions**: Number of colors that are in the code but in the wrong position

## Installation

### Prerequisites
- Python 3.6 or higher

### Setup
1. Clone or download the code file
2. No additional dependencies required (uses only Python standard library)

## Usage

### Running the Game
```bash
python code_cracker.py
```

### Example Gameplay
```
Welcome to Code Cracker! You have 10 tries to guess the code...
The valid colors are: R, G, B, Y, W, O
Enter your guess as space-separated colors (e.g., 'R G B Y')
--------------------------------------------------

Attempt 1/10
Guess: R G B Y
Correct Positions: 1 | Incorrect Positions: 2

Attempt 2/10
Guess: G R Y B
Correct Positions: 0 | Incorrect Positions: 3

Attempt 3/10
Guess: B Y R G
🎉 Congratulations! You guessed the code in 3 tries!
The code was: B Y R G
```

## Game Features

- **Input Validation**: Ensures valid colors and correct number of guesses
- **Clear Feedback**: Provides helpful hints after each attempt
- **Case Insensitive**: Accepts both uppercase and lowercase input
- **Win/Loss Detection**: Celebrates victories and reveals the code on loss

## Code Structure

### Main Functions

- `generate_code()`: Creates a random 4-color secret code
- `guess_code()`: Handles user input and validation
- `check_code()`: Compares guess against the secret code and provides feedback
- `game()`: Main game loop that orchestrates the entire gameplay

### Configuration

Easy to modify game parameters in the constants section:
```python
COLORS = ["R", "G", "B", "Y", "W", "O"]  # Available colors
TRIES = 10                               # Maximum attempts
CODE_LENGTH = 4                          # Length of secret code
```

## Strategy Tips

1. **Start with diverse colors** to maximize information gained
2. **Pay attention to feedback** - use both correct and incorrect position counts
3. **Eliminate impossible combinations** based on previous feedback
4. **Use logical deduction** rather than random guessing

## Customization

Want to modify the game? Here are some ideas:

- **Difficulty Levels**: Change `CODE_LENGTH` or `TRIES`
- **More Colors**: Add to the `COLORS` list
- **Duplicate Colors**: Modify `generate_code()` to allow repeated colors
- **Scoring System**: Add points based on number of attempts

## Contributing

Feel free to fork, modify, and submit pull requests! Some enhancement ideas:
- GUI version using tkinter
- Difficulty selection menu
- High score tracking
- Hint system for beginners