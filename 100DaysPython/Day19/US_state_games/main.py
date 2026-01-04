import turtle
import pandas as pd 
from turtle import Turtle, Screen 
import os 

BASE_DIR = os.path.dirname(__file__)
IMAGE_PATH = os.path.join(BASE_DIR, 'blank_states_img.gif')
CSV_PATH = os.path.join(BASE_DIR, '50_states.csv')

screen = Screen()
screen.title("U.S State games")

screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

df = pd.read_csv(CSV_PATH)
start = 0

states = []
for state in df['state']:
    states.append(state.lower())

def get_xy(answer_state, df):
    for i, state in enumerate(df['state']):
        if answer_state.lower() == state.lower():
            return df.loc[i]['x'], df.loc[i]['y']

while(start < len(df)):
    answer_state = screen.textinput(title="Guess the State!", prompt="What's another state name? ")
    if answer_state.lower() in states:
        start += 1
        print(f"Yes, {answer_state} is a US State.")
        new_pen = Turtle()
        new_pen.penup()
        new_pen.hideturtle()
        new_pen.pencolor("Black")
        x, y = get_xy(answer_state, df)
        screen.tracer(0)
        new_pen.goto(x, y)
        screen.update()
        new_pen.write(
            f"{answer_state}",
            align="center",
            font=("Arial", 16, "bold")
        )
    else:
        print(f"No state in US exist as {answer_state}")
    

screen.exitonclick()



