import turtle as t
FONT = ("Arial", 14, "normal")
ALIGNMENT = "center"


class Scoreboard(t.Turtle):

    def __init__(self, ):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(0, 240)
        self.write(f"{self.l_score}        {self.r_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
