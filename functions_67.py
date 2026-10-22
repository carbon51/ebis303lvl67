#Eli Baker
#Wordle assignment functions

import random

#Selects and returns the secret word
def choose_word():
    words = ["stone", "crate", "layer", "align", "trick", "proud", "quiet", "swift", "flame"]
    secret_word = random.choice(words)
    return secret_word

#Get and validate the user's guess
def get_guess():
    guess = input("Enter a 5 letter word: ").lower()

    while len(guess) != 5 or not guess.isalpha():
        print("Word must be exactly 5 letters long.")
        guess = input("Enter a 5 letter word: ").lower()

    return guess

#Evaluate user guess
def evaluate_guess(guess, secret_word):
    feedback = []

    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback.append("G")
        elif guess[i] in secret_word:
            feedback.append("Y")
        else:
            feedback.append("-")

    return feedback

# Display guess and feedback
def display_guess(guess, feedback):
    print("Guess:", guess.upper())
    print("Feedback:", " ".join(feedback))


# Determine if player has won
def has_won(feedback):
    if feedback == ["G", "G", "G", "G", "G"]:
        return True
    else:
        return False