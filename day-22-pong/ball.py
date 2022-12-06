import turtle as t
import random
INITIAL_SPEED = 2


class Ball(t.Turtle):

    def __init__(self, speed=INITIAL_SPEED):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.speed = speed
        self.x_move = self.speed
        self.y_move = self.speed

    def move(self, ):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move()

    def bounce_x(self):
        self.x_move *= -1
        self.move()

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.update_velocity(INITIAL_SPEED)

    def update_velocity(self, speed):
        self.speed = speed
        print(f"Current speed is {self.speed}")
        if self.x_move < 0:
            self.x_move = -self.speed
        elif self.x_move > 0:
            self.x_move = self.speed
        if self.y_move< 0:
            self.y_move = -self.speed
        elif self.y_move > 0:
            self.y_move = self.speed
