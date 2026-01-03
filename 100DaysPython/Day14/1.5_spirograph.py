from turtle import Turtle, Screen 
import random

timmy = Turtle()

for i in range(360):
    r = random.random()
    g = random.random()
    b = random.random()
    timmy.pencolor((r, g, b))
    timmy.circle(100)   # radius = 100
    timmy.left(1)

screen = Screen()
screen.exitonclick()