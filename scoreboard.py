from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.high_score=int(f.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreBoard()

    def update_scoreBoard(self):
        self.clear()
        self.write(f"Score:{self.score}, High Score:{self.high_score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreBoard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreBoard()
