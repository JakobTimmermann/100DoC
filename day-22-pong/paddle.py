import turtle as t
MOVE_DISTANCE = 20


class Paddle(t.Turtle):

    def __init__(self, position):
        """
        :type position: tuple
        """
        super().__init__()
        self.color('white')
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        print(self.ycor())
        if self.ycor() < 239:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -239:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
