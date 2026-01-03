from turtle import Turtle, Screen 

timmy = Turtle()
timmy.color('green')
timmy.shape('turtle')

def dashed_forward(turtle_name, steps):
    step_count = 0
    while(step_count < steps):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()
        step_count += 20 

# make a square 
dashed_forward(timmy, 100)
timmy.left(90)
dashed_forward(timmy, 100)
timmy.left(90)
dashed_forward(timmy, 100)
timmy.left(90)
dashed_forward(timmy, 100)
timmy.left(90)

screen = Screen()
screen.exitonclick()

