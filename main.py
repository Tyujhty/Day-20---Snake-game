from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score
import time

'''Screen setup'''
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #Collision with food with snake
    if snake.head.distance(food) < 15:
        score_board.add_score()
        food.refresh()


screen.exitonclick()
