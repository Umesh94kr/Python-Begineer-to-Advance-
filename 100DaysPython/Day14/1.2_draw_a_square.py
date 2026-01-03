from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')

# functions to turn left and right 
def move_left(turtle_name):
    turtle_name.left(90)
    turtle_name.forward(100)

def move_right(turtle_name):
    turtle_name.right(90)
    turtle_name.forward(100)


timmy.forward(100)
move_left(timmy)
move_left(timmy)
move_left(timmy)


screen = Screen()
screen.exitonclick()
