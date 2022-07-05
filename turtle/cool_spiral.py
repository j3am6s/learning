from turtle import *

screen = Screen()

pen = Turtle()
colors = ["red", "cyan", "green", "yellow", "white", "orange"]
screen.bgcolor("black")
pen.speed(10)

for x in range(400):
    pen.color(colors[x%6])
    pen.width(x/100+1)
    pen.forward(x)
    pen.left(59)

screen.exitonclick()
