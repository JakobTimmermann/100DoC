import turtle as t
FONT = ("Arial", 14, "normal")
ALIGNMENT = "center"


class Scoreboard(t.Turtle):

    def __init__(self, ):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(0, 240)
        self.write(f"Current Level: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
