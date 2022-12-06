import random
import time
import turtle as t
from car import Car
from myturtle import MyTurtle
from scoreboard import Scoreboard


def setup_screen(number_of_cars=15, initial_speed_level=2):
    initial_cars = []
    for _ in range(number_of_cars):
        initial_position = (random.randint(-500,500), random.randint(-200, 250))
        car = Car(start_position=initial_position, max_speed=initial_speed_level)
        initial_cars.append(car)
    return initial_cars


screen = t.Screen()
screen.setup(width=1000, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard()
myturtle = MyTurtle()
screen.onkey(myturtle.move_up, "Up")

game_is_on = True
generating_probability = 0.985
speed_level = 2

while game_is_on:
    myturtle.refresh()
    scoreboard.clear()
    scoreboard.refresh()
    cars = setup_screen(number_of_cars=15,initial_speed_level=speed_level)
    screen.update()
    time.sleep(1)
    while myturtle.ycor() < 280 and game_is_on:
        screen.update()
        time.sleep(0.01)
        if random.random() > generating_probability:
            start_position = (530, random.randint(-200, 250))
            cars.append(Car(start_position=start_position, max_speed=speed_level))
        for n, car in enumerate(cars):
            car.move()
            if car.xcor() < -520:
                cars.pop(n)
            # detect collision
            if car.xcor() + 25 > myturtle.xcor() > car.xcor() - 25 and car.ycor() + 10 > myturtle.ycor() > car.ycor() -10:
                screen.update()
                scoreboard.game_over()
                game_is_on = False
                break
    if game_is_on:
        speed_level += 1
        generating_probability -= 0.005
        print(generating_probability)
        print("Next Level")
        for car in cars:
            car.hideturtle()
        scoreboard.score +=1
screen.update()

screen.exitonclick()