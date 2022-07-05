from random import randint
from turtle import *

jean = Turtle()
jean.shape("turtle")
screen = Screen()

jean.pensize(1)
jean.speed(0)
screen.colormode(255)

def row():
    for j in range(10):
        jean.pendown()
        jean.color((randint(0, 255)), (randint(0, 255)), (randint(0, 255)))
        jean.begin_fill()
        jean.circle(5)
        jean.end_fill()
        jean.penup()
        jean.fd(20)

for i in range(5):
    row()
    jean.lt(90)
    jean.fd(30)
    jean.lt(90)
    jean.fd(20)
    row()
    jean.rt(90)
    jean.fd(10)
    jean.rt(90)
    jean.fd(20)

jean.hideturtle()

screen.exitonclick()
