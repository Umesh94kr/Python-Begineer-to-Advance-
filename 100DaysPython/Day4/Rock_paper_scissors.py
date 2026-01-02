import random
print("Welcome to Rock Paper Scissor Game!")

moves = ['rock', 'paper', 'scissor']

# 1 - rock, 2 - paper, 3 - scissor
your_move = input("Rock, Paper or Scissor? ")
computer = random.randint(1, 3)
computer_move = moves[computer-1]

print(f"Your move : {your_move.lower()}")
print(f"Computer move : {computer_move}")

if your_move.lower() == computer_move:
    print("Its a tie!!")
elif your_move.lower() == 'rock':
    if computer_move == 'paper':
        print('You Loose!')
    else:
        print('You Won!')
elif your_move.lower() == 'paper':
    if computer_move == 'scissor':
        print('You Loose!')
    else:
        print('You Won!')
elif your_move.lower() == 'scissor':
    if computer_move == 'rock':
        print('You Loose!')
    else:
        print('You Won!')

    
