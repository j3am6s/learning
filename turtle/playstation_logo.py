from turtle import *

screen = Screen()
screen.bgcolor("black")

turtle = Turtle()
turtle.pensize(5)


def triangle():
    turtle.pendown()
    turtle.color("green")
    turtle.fd(50)
    turtle.lt(120)
    turtle.fd(50)
    turtle.lt(120)
    turtle.fd(50)
    turtle.lt(120)
    turtle.fd(50)

def circle():
    turtle.color("red")
    turtle.pendown()
    turtle.circle(23)

def cross():
    turtle.color("blue")
    turtle.pendown()
    turtle.goto(61, 46)
    turtle.penup()
    turtle.goto(20, 46)
    turtle.pendown()
    turtle.goto(61, 0)

def square():
    turtle.color("orange")
    turtle.pendown()
    for i in range(5):
        turtle.fd(46)
        turtle.lt(90)

def disappear():
    turtle.color("black")
    turtle.rt(90)
    turtle.fd(20)

turtle.penup()
turtle.goto(-100, 0)
triangle()

turtle.penup()
turtle.fd(35)
circle()

turtle.penup()
turtle.fd(35)
cross()

turtle.penup()
turtle.fd(20)
square()

turtle.penup()
disappear()

screen.exitonclick()
