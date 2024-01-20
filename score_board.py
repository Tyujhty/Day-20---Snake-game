from turtle import Turtle

ALIGN = "center"
FONT = ("Roboto", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.penup()
        self.score = 0
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", False, align=ALIGN, font=FONT)
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()