from turtle import Screen
from snake_body import SnakeBody, Food, SnakePart, ScoreBoard
from turtle import Turtle
import time
import random

def display_food(screen):
    screen.tracer(0)
    food = Food()
    food.get_food()
    return food 

def check_food_is_eaten(snake, food):
    if (snake.head.snake_part.xcor() >= food.x-20 and snake.head.snake_part.xcor() <= food.x+20) and (snake.head.snake_part.ycor() >= food.y-20 and snake.head.snake_part.ycor() <= food.y+20):
        food.food.hideturtle()
        print("Food Eaten!!")
        return True
    return False


def add_new_part(snake):
        new_part = SnakePart()
        last_part = snake.snake_list[-1]
        if last_part.direction == "up":
            new_part.snake_part.setx(last_part.snake_part.xcor())
            new_part.snake_part.sety(last_part.snake_part.ycor()-10)
            new_part.direction = "up"
        elif last_part.direction == "down":
            new_part.snake_part.setx(last_part.snake_part.xcor())
            new_part.snake_part.sety(last_part.snake_part.ycor()+10)
            new_part.direction = "down"
        elif last_part.direction == "right":
            new_part.snake_part.setx(last_part.snake_part.xcor()-10)
            new_part.snake_part.sety(last_part.snake_part.ycor())
            new_part.direction = "right"
        elif last_part.direction == "left":
            new_part.snake_part.setx(last_part.snake_part.xcor()+10)
            new_part.snake_part.sety(last_part.snake_part.ycor())
            new_part.direction = "left"
        snake.snake_list.append(new_part)

def shift_positions(snake):
        
        i = len(snake.snake_list)-1
        for current_part in reversed(snake.snake_list[1:]):
            ahead_snake = snake.snake_list[i-1]
            current_part.snake_part.setx(ahead_snake.snake_part.xcor())
            current_part.snake_part.sety(ahead_snake.snake_part.ycor())
            cordinates[ahead_snake.snake_part.xcor()] = ahead_snake.snake_part.ycor()
            current_part.direction = ahead_snake.direction
            i -= 1

        # first head snake
        head_snake = snake.snake_list[0]
        if head_snake.direction == "up":
            head_snake.snake_part.sety(head_snake.snake_part.ycor()+10)
        elif head_snake.direction == "down":
            head_snake.snake_part.sety(head_snake.snake_part.ycor()-10)
        elif head_snake.direction == "right":
            head_snake.snake_part.setx(head_snake.snake_part.xcor()+10)
        elif head_snake.direction == "left":
            head_snake.snake_part.setx(head_snake.snake_part.xcor()-10)

def check_self_collision(snake):
    head = snake.snake_list[0].snake_part
    for segment in snake.snake_list[1:]:
        if head.distance(segment.snake_part) < 8:
            return True
    return False

####### GAME CONFIGURATIONS #######################
screen = Screen()
screen.setup(width=500, height=400) # adjust the size of window 

snake = SnakeBody()
is_game_on = True

screen.listen()
screen.onkey(key="Up", fun=snake.go_up)
screen.onkey(key="Down", fun=snake.go_down)
screen.onkey(key="Left", fun=snake.go_left)
screen.onkey(key="Right", fun=snake.go_right)

food = display_food(screen)

score_board = ScoreBoard()

############ GAME LOOP ###################

while(is_game_on):
    cordinates = {}
    screen.update()
    time.sleep(0.08)
    ## check if snake eats the food 
    if check_food_is_eaten(snake, food):
        snake.score += 1
        food = display_food(screen)
        score_board.increase_score()
        # add a new head
        add_new_part(snake)
        
    if len(snake.snake_list) > 1:
        cordinates = shift_positions(snake)
    else:
        snake.keep_moving()

    ### check collision of Head
    if check_self_collision(snake):
        score_board.game_over()
        print("Boom!")
        print(f"Your Score is {snake.score}")
        is_game_on = False

    snake.wrap_around_screen()

screen.exitonclick()