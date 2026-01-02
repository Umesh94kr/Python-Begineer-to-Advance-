# 🏝️ Treasure Island Game (If–Else Logic)

# You’re on a mission to find the hidden treasure. Make the right choices to survive!

# Rules of the game:

# You start at a crossroad.

# If you choose "left", you move forward.
# If you choose "right", the game ends. ❌

# You reach a lake.

# If you choose "wait" for a boat, you safely cross.
# If you choose "swim", the game ends. ❌

# You arrive at a house with three doors: red, blue, and yellow.

# Red → Fire 🔥 (Game Over)
# Blue → Beasts 🐍 (Game Over)
# Yellow → Treasure 💰 (You Win!)

####################### SOLUTION ##################### 
print("Welcome to treasure island game 🏝️")
print("-"*89)
print("You’re on a mission to find the hidden treasure. Make the right choices to survive!")
print("You start at a crossroad.")

choose_direction = input("Choose 'left' or 'right'? ")

if choose_direction == 'left':
    print("You move forward and reached a lake.")
    swim = input("Do you want to wait for boat or swim? Choose 'wait' or 'swim' - ")
    if swim == 'wait':
        print("You safetly crossed the river. You arrived at house with 3 doors Red, Blue, and Yellow.")
        gate = input("Choose one from Red, Blue and Yellow - ")
        if gate == 'Red':
            print("Fire 🔥! Game Over")
        elif gate == 'Blue':
            print("Beasts 🐍! Game Over")
        elif gate == 'Yellow':
            print("Treasure 👑! YOU WON !!!")
    else:
        print("You became lunch of Crocs 🐊! GAME OVER")
else:
    print("GAME OVER!")

