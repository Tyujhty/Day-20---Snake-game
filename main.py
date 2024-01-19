from turtle import Screen, Turtle

'''Screen setup'''
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

all_turtles = []
starting_positions = [(0,0), (-20, 0), (-40, 0)]

for position in starting_positions:
    snake_segment = Turtle(shape="square")
    snake_segment.color("white")
    snake_segment.goto(position)

screen.exitonclick()
