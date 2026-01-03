from turtle import Turtle, Screen 
import random

timmy = Turtle()
timmy.color('green')
timmy.shape('turtle')

for _ in range(1000):
    r = random.random()
    b = random.random()
    g = random.random()
    timmy.pencolor((r, g, b))
    timmy.pensize(10)
    zero_or_one = random.randint(0, 3)
    if zero_or_one == 0:
        timmy.left(90)
    elif zero_or_one == 1:
        timmy.left(0)
    elif zero_or_one == 2:
        timmy.left(180)
    else:
        timmy.right(90)

    timmy.forward(10)

screen = Screen()
screen.exitonclick()