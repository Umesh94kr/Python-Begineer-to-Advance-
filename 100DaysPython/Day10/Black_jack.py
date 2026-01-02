## Logic to make this Game 

cards = ["2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "KH", "JH", "QH", "AH", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "KD", "JD", "QD", "AD", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "KS", "JS", "QS", "AS", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "KC", "JC", "QC", "AC"]

import random 

print("Lets play BlackJack 🂸")
cards_drawn = set()

# first_draw
user_card_list = []
computer_card_list = []

user_card = cards[random.randint(0, len(cards)-1)]
cards_drawn.add(user_card)
user_card_list.append(user_card)

computer_card = cards[random.randint(0, len(cards)-1)]
# logic to only drawn card which is not already drawn
while(computer_card in cards_drawn):
    computer_card = cards[random.randint(0, len(cards)-1)]
cards_drawn.add(computer_card)
computer_card_list.append(computer_card)

# get score of a card 
def get_card_score(card, score):
    if card[0] == 'K' or card[0] == 'J' or card[0] == 'Q':
        return 10 
    elif card[0] == 'A':
        if score <= 10:
            return 11 
        else:
            return 1 
    else:
        return int(card[0])
    
# Now calculate first scores
user_score = get_card_score(user_card, 0)
computer_score = get_card_score(computer_card, 0)

print(f"User Cards : {user_card_list}")
print(f"User Score : {user_score}")

play=True
while(play):

    print(f"Computer Cards : {computer_card_list}")
    print(f"Computer score : {computer_score}")

    if computer_score > 21:
        print("You Won! - Dealer Busted")
        break

    print(f"========================================================")

    user_card = cards[random.randint(0, len(cards)-1)]
    while(user_card in cards_drawn):
        user_card = cards[random.randint(0, len(cards)-1)]
    cards_drawn.add(user_card)
    user_card_list.append(user_card)

    computer_card = cards[random.randint(0, len(cards)-1)]
    # logic to only drawn card which is not already drawn
    while(computer_card in cards_drawn):
        computer_card = cards[random.randint(0, len(cards)-1)]
    cards_drawn.add(computer_card)
    computer_card_list.append(computer_card)

    user_score += get_card_score(user_card, user_score)
    print(f"User cards : {user_card_list}")
    print(f"User score : {user_score}")

    computer_score += get_card_score(computer_card, computer_score)

    if user_score == 21:
        print("You Won!")
        break
    elif user_score > 21:
        print("You Busted! - Dealer Won!")
        break

    want_to_play = input("Do you want to play or stop the game! 'Yes' or 'No' - ")
    if want_to_play == 'No':
        play = False
        print(f"User Cards : {user_card_list}")
        print(f"Computer Cards : {computer_card_list}")
        print(f"User Score : {user_score}")
        print(f"Computer Score : {computer_score}")

        if user_score > computer_score:
            print(f"You Won !!")
        elif user_score == computer_score:
            print(f"This is a tie!")








