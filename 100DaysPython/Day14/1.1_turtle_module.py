from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')

# move forward by 100 steps 
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)

screen = Screen()

screen.exitonclick() # on clicking the screen you'll exit 