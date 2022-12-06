import turtle as t
FONT = ("Arial", 12, "normal")
ALIGNMENT = "center"


class Scoreboard(t.Turtle):

    def __init__(self, high_score_file="data.txt"):
        super().__init__()
        self.score = 0
        self.high_score_file = high_score_file
        with open(self.high_score_file) as data:
            self.high_score = int(data.read())
        self.goto(0, 260)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}  |  Highscore {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(self.high_score_file, "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
