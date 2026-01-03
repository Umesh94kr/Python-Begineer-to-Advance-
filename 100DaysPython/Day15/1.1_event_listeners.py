from turtle import Turtle, Screen 

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(100)

def turn_left():
    timmy.left(5)

def turn_right():
    timmy.right(5)

def clockwise():
    timmy.forward(1)
    timmy.right(1)

def anti_clockwise():
    timmy.forward(1)
    timmy.left(1)

screen.listen()
screen.onkey(key='space', fun=move_forward)
screen.onkey(key='Left', fun=turn_left)
screen.onkey(key='Right', fun=turn_right)
screen.onkey(key='q', fun=clockwise)
screen.onkey(key='w', fun=anti_clockwise)
screen.exitonclick()