import turtle as t
import random
import colorgram

colors = colorgram.extract('image.jpeg', 100)
colors = [color.rgb for color in colors[1:]]

t.colormode(255)
tim = t.Turtle()
tim.width(5)
tim.speed("fastest")
tim.penup()
tim.goto(-400,-400)


def paint_row(turtle,spacing):
    for k in range(10):
        turtle.dot(20, random.choice(colors))
        turtle.forward(spacing)


def get_to_starting_point(turtle,spacing):
    turtle.left(90)
    turtle.forward(spacing)
    turtle.left(90)
    turtle.forward(spacing*10)
    turtle.left(180)


def paint_painting(turtle,spacing=50):
    for k in range(10):
        paint_row(turtle,spacing)
        get_to_starting_point(turtle, spacing)


paint_painting(tim)
screen = t.Screen()
screen.exitonclick()