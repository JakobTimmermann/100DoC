import turtle as t
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

while game_is_on:
    screen.update()
    time.sleep(0.02)
    ball.move()
    # if detection with wall, x_dir stays the same, y_dir changes sign
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with right paddle
    # if ball beyond y = 340 and paddle is nearby (distance < 50) then paddle_bounce
    if ball.xcor() > 330 and ball.distance(r_paddle.pos()) < 50:
        ball.bounce_x()
        ball.update_velocity(ball.speed + 0.2*ball.speed)
    elif ball.xcor() < -330 and ball.distance(l_paddle.pos()) < 50:
        ball.bounce_x()
        ball.update_velocity(ball.speed + 0.2*ball.speed)
    elif ball.xcor() < -380:
        scoreboard.r_score +=1
        scoreboard.refresh()
        time.sleep(1)
        ball.reset_ball()
    elif ball.xcor() > 380:
        scoreboard.l_score +=1
        scoreboard.refresh()
        time.sleep(1)
        ball.reset_ball()

screen.exitonclick()