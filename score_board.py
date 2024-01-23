from turtle import Turtle

ALIGN = "center"
FONT = ("Roboto", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.penup()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score} ", False, align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()