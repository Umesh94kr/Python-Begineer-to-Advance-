## 🎯 Problem Statement: Number Guessing Game

# 1. Design and implement a simple **Number Guessing Game** using Python.
# 2. The program should generate a **random number** within a given range, and the player must guess the number correctly within a limited number of attempts.

# ===============================================================================

### 🔢 Game Rules

# 1. The program randomly selects a number between **1 and 100**.
# 2. The player is prompted to guess the number.
# 3. After each guess, the program should provide feedback:
#    - **Too high**
#    - **Too low**
#    - **Correct guess**
# 4. The game continues until:
#    - The player guesses the correct number, or
#    - The player runs out of attempts

# ===============================================================================

### 🏆 Winning & Losing Conditions

# - **Win:** Player guesses the number correctly within the allowed attempts.
# - **Lose:** Player fails to guess the number within the attempt limit.

# ===============================================================================

### ⭐ Bonus

# - Add difficulty levels (easy, medium, hard)
# - Track number of attempts used
# - Allow the player to replay the game

# ===============================================================================

import random 

def random_num_generator_game():
    # generate a random number between 1 to 100 
    random_number = random.randint(1, 100)

    # Set the level of game by mentioning 'hard', 'medium' or 'easy' 
    difficulty = input("Difficulty of Game - 'Hard', 'Medium' or 'Easy' => ")
    if difficulty == 'Hard':
        lifes = 5
    elif difficulty == 'Medium':
        lifes = 7 
    else:
        lifes = 10 

    # Start the guessing game 
    print("Guess the number between 1 to 100. ")
    while(lifes > 0):
        number = int(input("Enter the number "))
        if number == random_number:
            print("You got the number right!")
            break
        elif number > random_number:
            print("Too high!")
        else:
            print("Too Low!")
        
        # reduce the life by 1
        lifes -= 1
    if lifes == 0:
        print("You failed to guess the right number!")

if __name__ == '__main__':
    random_num_generator_game()

