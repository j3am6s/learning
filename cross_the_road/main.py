import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

player = Player()
score = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
x=0
cars = []
a=5
b=6

while game_is_on:
    time.sleep(0.1)
    screen.update()
    x+=1
    if x==b:
        x=0
        car = CarManager()
        cars.append(car)
    for car in cars:
        car.move(a)
        if car.distance(player) < 25:
            game_is_on = False
    if player.ycor()>280:
        player.refresh()
        a+=5
        score.add()        

screen.exitonclick()
