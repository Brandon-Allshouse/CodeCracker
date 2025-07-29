import random

# Game configuration constants
COLORS = ["R", "G", "B", "Y", "W", "O"]  # Available colors: Red, Green, Blue, Yellow, White, Orange
TRIES = 10  # Maximum number of attempts allowed
CODE_LENGTH = 4  # Length of the secret code to guess

def generate_code():
    """
    Generate a random secret code of specified length.
    
    Returns:
        list: A list of random colors from COLORS with length CODE_LENGTH
    """
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code

def guess_code():
    """
    Get and validate user input for their color guess.
    
    Continues prompting until a valid guess is entered:
    - Must be exactly CODE_LENGTH colors
    - All colors must be valid (in COLORS list)
    
    Returns:
        list: A list of valid color guesses
    """
    while True:
        # Get user input, convert to uppercase, and split by spaces
        guess = input("Guess: ").upper().split(" ")
        
        # Check if guess has correct number of colors
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue
        
        # Validate each color in the guess
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again")
                break
        else:
            # If we didn't break out of the loop, all colors are valid
            break
    
    return guess

def check_code(guess, real_code):
    """
    Compare the player's guess against the real code.
    
    Args:
        guess (list): The player's color guess
        real_code (list): The actual secret code
    
    Returns:
        tuple: (correct_positions, incorrect_positions)
            - correct_positions: colors in right position
            - incorrect_positions: correct colors in wrong position
    """
    # Count occurrences of each color in the real code
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0
    
    # Build frequency map of colors in real code
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
    
    # First pass: count correct positions and decrement color counts
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1
    
    # Second pass: count incorrect positions (right color, wrong position)
    for guess_color, real_color in zip(guess, real_code):
        # Skip if this position was already counted as correct
        if guess_color != real_color:
            # Check if this color exists elsewhere in the code
            if guess_color in color_counts and color_counts[guess_color] > 0:
                incorrect_pos += 1
                color_counts[guess_color] -= 1
    
    return correct_pos, incorrect_pos

def game():
    """
    Main game loop that runs the Code Cracker game.
    
    Generates a secret code and gives the player TRIES attempts to guess it.
    Provides feedback after each guess showing correct and incorrect positions.
    """
    print(f"Welcome to Code Cracker! You have {TRIES} tries to guess the code...")
    print(f"The valid colors are: {', '.join(COLORS)}")
    print("Enter your guess as space-separated colors (e.g., 'R G B Y')")
    print("-" * 50)
    
    # Generate the secret code
    code = generate_code()
    
    # Game loop - give player multiple attempts
    for attempts in range(1, TRIES + 1):
        print(f"\nAttempt {attempts}/{TRIES}")
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        # Check if player won
        if correct_pos == CODE_LENGTH:
            print(f"🎉 Congratulations! You guessed the code in {attempts} tries!")
            print(f"The code was: {' '.join(code)}")
            break
        
        # Provide feedback
        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
    else:
        # This runs if the loop completed without breaking (player lost)
        print(f"\n💀 Game Over! You ran out of tries.")
        print(f"The code was: {' '.join(code)}")

# Entry point - run the game if this script is executed directly
if __name__ == "__main__":
    game()