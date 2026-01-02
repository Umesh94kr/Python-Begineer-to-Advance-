############ PROBLEM STATEMENT ###########

# 🎯 Problem Statement: Hangman Game

# Create a simple Hangman game using Python.

# The program should:

# Randomly select a word from a predefined list of words.
# Ask the user to guess one letter at a time.
# Display the word with underscores (_) for letters that have not been guessed.
# If the guessed letter is in the word, reveal it in the correct position(s).
# If the guessed letter is not in the word, reduce the number of remaining attempts.
# End the game when:

# The user correctly guesses all letters in the word (You Win), or
# The user runs out of attempts (Game Over).

################# SOLUTION ###################
words = [
    "apple", "banana", "orange", "grape", "mango", "peach", "cherry", "lemon", "papaya", "guava",
    "python", "coding", "program", "script", "binary", "string", "number", "boolean", "syntax", "debug",
    "river", "mountain", "forest", "desert", "island", "ocean", "valley", "stream", "cliff", "beach",
    "school", "college", "teacher", "student", "lesson", "exam", "result", "subject", "degree", "career",
    "computer", "laptop", "keyboard", "mouse", "screen", "window", "folder", "button", "server", "network",
    "music", "guitar", "piano", "violin", "drums", "artist", "song", "melody", "rhythm", "concert",
    "movie", "camera", "actor", "director", "script", "scene", "drama", "comedy", "thriller", "cinema",
    "travel", "ticket", "passport", "journey", "hotel", "flight", "station", "airport", "luggage", "tour"
]

print("Welcome to Hangman Game!!")

# select a random_word from list
import random
idx = random.randint(0, len(words)-1)
random_word = words[idx]

lifes = len(random_word)
word_to_guess = ["_" for i in range(lifes)]

print(f"Word to guess : {word_to_guess}")

while(lifes > 0):
    # guess the character 
    character = input('Guess the character? ')
    char_found = False
    for i, char in enumerate(random_word):
        if character == char:
            if word_to_guess[i] == '_':
                word_to_guess[i] = character
                char_found = True

    if char_found:
        print("You guessed a character right!")
        print(f"Word : {word_to_guess}")
    else:
        lifes -= 1
        print("You guessed the character wrong!")
        print(f"Remaining lifes : {lifes}/{len(random_word)}")

if lifes == 0:
    print("You Loose!")
else:
    print("You correctly guessed the word : CONGRATS")
    print(f"Word : {word_to_guess}")

    