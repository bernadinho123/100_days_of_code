from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courirer", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as score:
            self.high_score = int(score.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)

        self.write(f"Score: {self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as score:
                score.write(f"{self.score}")

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
