import turtle as t
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(t.Turtle):

    def __init__(self, start_position, max_speed=0.5):
        """
        :type start_position: tuple
        :type max_speed: float
        :param start_position: (x,y) defines the x and y coordinate of the starting position
        :param max_speed: Maximum speed
        """
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.move_speed = max(max(1, max_speed/3.), random.random()*max_speed)
        self.penup()
        self.goto(start_position)
        self.setheading(180)

    def move(self):
        self.forward(self.move_speed)

