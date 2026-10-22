#Eli Baker
#Wordle assignment game

import functions_67 as f

print("Welcome to Mystery Wordle!")
print("Guess the five-letter word.")
print("G = correct letter and position")
print("Y = correct letter, wrong position")
print("- = letter is not in the word")

secret_word = f.choose_word()
guesses = []
max_guesses = 6
won = False

while len(guesses) < max_guesses and not won:
    print(f"\nAttempt {len(guesses) + 1} of {max_guesses}")

    guess = f.get_guess()

    # Check if guess was already used
    if guess in guesses:
        print("You already guessed that word. Try again.")
        continue

    # Add valid guess to list
    guesses.append(guess)

    # Evaluate and display guess
    feedback = f.evaluate_guess(guess, secret_word)
    f.display_guess(guess, feedback)

    # Check if player won
    won = f.has_won(feedback)

# End game
if won:
    print(f"You guessed it in {len(guesses)} tries.")
else:
    print(f"Game over, the word was {secret_word.upper()}.")