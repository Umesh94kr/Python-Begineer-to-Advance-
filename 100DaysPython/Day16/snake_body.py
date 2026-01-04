from turtle import Turtle
import random
import json 
import os 
BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR, "high_score.json")

class SnakePart:
    def __init__(self):
        self.snake_part = Turtle()
        self.snake_part.shape('square')
        self.snake_part.penup()
        r = random.random()
        g = random.random()
        b = random.random()
        self.snake_part.color((r, g, b))
        self.direction = "right"

class SnakeBody:
    def __init__(self):
        self.head = SnakePart()
        self.head.snake_part.shapesize(outline=5)
        self.head.direction = "right"
        self.snake_list = [self.head]
        self.score = 0

    def keep_moving(self):
        self.head.snake_part.forward(10)
        
    
    def go_up(self):
        if self.head.direction == "right":
            self.head.snake_part.left(90)
            self.head.direction = "up"
        elif self.head.direction == "left":
            self.head.snake_part.right(90)
            self.head.direction = "up"
        else:
            pass
    def go_down(self):
        if self.head.direction == "right":
            self.head.snake_part.right(90)
            self.head.direction = "down"
        elif self.head.direction == "left":
            self.head.snake_part.left(90)
            self.head.direction = "down"
        else:
            pass

    def go_left(self):
        if self.head.direction == "up":
            self.head.snake_part.left(90)
            self.head.direction = "left"
        elif self.head.direction == "down":
            self.head.snake_part.right(90)
            self.head.direction = "left"
        else:
            pass

    def go_right(self):
        if self.head.direction == "up":
            self.head.snake_part.right(90)
            self.head.direction = "right"
        elif self.head.direction == "down":
            self.head.snake_part.left(90)
            self.head.direction = "right"
        else:
            pass

    def wrap_around_screen(self, screen_width=500, screen_height=400):
        x = self.head.snake_part.xcor()
        y = self.head.snake_part.ycor()

        half_width = screen_width // 2
        half_height = screen_height // 2

        if x > half_width:
            self.head.snake_part.setx(-half_width)
        elif x < -half_width:
            self.head.snake_part.setx(half_width)

        if y > half_height:
            self.head.snake_part.sety(-half_height)
        elif y < -half_height:
            self.head.snake_part.sety(half_height)

class Food:
    def __init__(self):
        self.food = Turtle()
        self.x = 0
        self.y = 0
        self.food.shape('circle')
        self.food.penup()

    def get_food(self):
        # target width
        neg_or_pos = random.randint(0, 1)
        if neg_or_pos == 0:
            x_target = -1*random.randint(0, 500//2) + 10
        else:
            x_target = random.randint(0, 500//2) - 10

        # target height
        neg_or_pos = random.randint(0, 1)
        if neg_or_pos == 0:
            y_target = -1*random.randint(0, 400//2) + 10
        else:
            y_target = random.randint(0, 400//2) - 10

        self.x = x_target 
        self.y = y_target

        self.food.setx(x_target)
        self.food.sety(y_target)

from turtle import Turtle

class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.color("Black")
        self.pen.goto(0, 170)  # top of screen
        self.get_high_score()
        self.update_score()

    def get_high_score(self):
        with open(FILE_PATH, 'r') as f:
            data = json.load(f)
            self.high_score = int(data["high_score"])

    def update_score(self):
        self.pen.clear()
        self.pen.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Arial", 16, "bold")
        )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score 
        with open(FILE_PATH, "w") as f:
            json.dump({"high_score": self.high_score}, f, indent=4)
    
        self.pen.goto(0, 0)
        self.pen.write(
            "GAME OVER",
            align="center",
            font=("Arial", 24, "bold")
        )

            
