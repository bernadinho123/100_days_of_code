import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
sleep = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car = CarManager()
timmy = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(timmy.move_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(sleep)
    screen.update()
    car.generate_cars()
    car.move_cars()
    for c in car.cars:
        if timmy.distance(c) < 25:
            timmy.write("Game Over", move=False, align='center', font=("Arial", 30, "normal"))
            game_is_on = False
    if timmy.ycor() > 280:
        scoreboard.point_scored()
        timmy.goto(0, -283)
        sleep = sleep*0.6

screen.exitonclick()
