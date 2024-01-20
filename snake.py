from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    '''Create the snake'''
    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)

    def move_snake(self):
        '''start = len(segments) - 1, stop: 0, step: -1'''
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)
    def right(self):
        self.head.setheading(0)
    def left(self):
        self.head.setheading(180)
    def down(self):
        self.head.setheading(270)
