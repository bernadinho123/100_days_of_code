from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.goto(200, 200)
        self.write(f"level:{self.score}", align="right", font=("Courier", 30, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.goto(200, 200)
        self.write(f"level:{self.score}", align="right", font=("Courier", 30, "normal"))

    def point_scored(self):
        self.score +=1
        self.update_scoreboard()