import turtle as t


class MyTurtle(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.refresh()
        self.setheading(90)

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def refresh(self):
        self.goto(0,-240)

