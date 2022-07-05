from turtle import *

s = Screen()
s.bgcolor("black")

t = Turtle()
t.speed( 0)
t.color("white")

#avec espace au milieu
for i in range(72):
    t.rt(5)
    t.fd(1)
    t.circle(100)

t.penup()
t.color("cyan")
t.goto(-1, -12)
t.width(2)
t.pendown()

#sans espace au milieu
for i in range(40):
    t.rt(10)
    t.circle(75)

s.exitonclick()
