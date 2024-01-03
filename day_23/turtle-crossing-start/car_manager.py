from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
flag = True


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()

    def generate_cars(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_cars = Turtle("square")
            new_cars.color(random.choice(COLORS))
            new_cars.shapesize(stretch_wid=1, stretch_len=2)
            new_cars.penup()
            new_cars.goto(280, random.randint(-260, 300))
            self.cars.append(new_cars)

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            new_y = car.ycor()
            car.goto(new_x, new_y)

