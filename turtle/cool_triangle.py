from turtle import *
from random import *

screen = Screen()
t = Turtle()
screen.colormode(255)
t.speed(0)
t.width(1)
screen.bgcolor(50, 0, 70)
t.pencolor(255, 255, 0)

def shape(angle, side, limit):
    direction = 200
    t.fd(side)
    if side % (direction*2) == 0:
        angle += 2
        print(side)
    elif side % direction == 0:
        angle -= 2
        print(side)
    t.rt(angle)
    side += 2
    if side < limit:
        shape(angle, side, limit)

shape(119, 0, 600)

t.done()

screen.exitonclick()
