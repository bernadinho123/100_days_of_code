import random
import turtle
from turtle import Turtle, Screen


def make_square(size, object):
    object.forward(size)
    object.right(90)
    object.forward(size)
    object.right(90)
    object.forward(size)
    object.right(90)
    object.forward(size)
    object.right(90)


def make_pentagon(size, object):
    object.forward(size)
    object.right(72)
    object.forward(size)
    object.right(72)
    object.forward(size)
    object.right(72)
    object.forward(size)
    object.right(72)
    object.forward(size)
    object.right(72)


def make_hexagon(size, object):
    object.forward(size)
    object.right(60)
    object.forward(size)
    object.right(60)
    object.forward(size)
    object.right(60)
    object.forward(size)
    object.right(60)
    object.forward(size)
    object.right(60)
    object.forward(size)
    object.right(60)


def make_heptagon(size, object):
    object.forward(size)
    object.right(360 / 7)
    object.forward(size)
    object.right(360 / 7)
    object.forward(size)
    object.right(360 / 7)
    object.forward(size)
    object.right(360 / 7)
    object.forward(size)
    object.right(360 / 7)
    object.forward(size)
    object.right(360 / 7)
    object.forward(size)
    object.right(360 / 7)


def make_octagon(size, object):
    object.forward(size)
    object.right(45)
    object.forward(size)
    object.right(45)
    object.forward(size)
    object.right(45)
    object.forward(size)
    object.right(45)
    object.forward(size)
    object.right(45)
    object.forward(size)
    object.right(45)
    object.forward(size)
    object.right(45)
    object.forward(size)
    object.right(45)


def make_nonagon(size, object):
    object.forward(size)
    object.right(40)
    object.forward(size)
    object.right(40)
    object.forward(size)
    object.right(40)
    object.forward(size)
    object.right(40)
    object.forward(size)
    object.right(40)
    object.forward(size)
    object.right(40)
    object.forward(size)
    object.right(40)
    object.forward(size)
    object.right(40)
    object.forward(size)
    object.right(40)


def make_decagon(size, object):
    object.forward(size)
    object.right(36)
    object.forward(size)
    object.right(36)
    object.forward(size)
    object.right(36)
    object.forward(size)
    object.right(36)
    object.forward(size)
    object.right(36)
    object.forward(size)
    object.right(36)
    object.forward(size)
    object.right(36)
    object.forward(size)
    object.right(36)
    object.forward(size)
    object.right(36)
    object.forward(size)
    object.right(36)


tim = Turtle()
tim.shape('turtle')
tim.color('green')
# make_square(100, tim)
#
# make_pentagon(100, tim)
#
# make_hexagon(100, tim)
#
# make_heptagon(100, tim)
#
# make_octagon(100, tim)
#
# make_nonagon(100, tim)
#
# make_decagon(100, tim)
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    x = (r, g, b)
    return x


# colours = ["dark green", "dark green", "dark green", "dark blue", "light slate gray", "yellow", "medium violet red"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed('fastest')
# for i in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
for i in range(0, 360, 10):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(i)

screen = Screen()
screen.exitonclick()
