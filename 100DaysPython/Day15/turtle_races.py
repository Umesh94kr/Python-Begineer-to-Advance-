from turtle import Turtle, Screen 
import random

screen = Screen()
screen.setup(width=500, height=400) # adjust the size of window 
colors = ['red', 'blue', 'green', 'yellow', 'violet', 'purple']

user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle you want to bet on? : {colors} : ")

y_positions= [-70, -40, -10, 20, 50, 80]
turtles = []

for turtle_idx in range(6):
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.color(colors[turtle_idx])
    timmy.penup()
    timmy.goto(x=-230, y=y_positions[turtle_idx])
    turtles.append(timmy)

if user_bet:
    is_race_on=True 

while(is_race_on):

    for timmy in turtles:
        if timmy.xcor() > 230:
            winning_color = timmy.pencolor()
            if user_bet == winning_color.lower():
                print("Your turtle won the race!")
            else:
                print(f"You loose!, {winning_color} turtle won the race!")
            is_race_on = False
            screen.clear()
            break 
        dist = random.randint(0, 10)
        timmy.forward(dist)


screen.exitonclick()