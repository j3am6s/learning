from turtle import *

s = Screen()
s.bgcolor("black")

t = Turtle()
t.speed(0)
t.color("red")
t.width(2)

c = t.clone()
c.color("orange")

for i in range(25):
    t.fd(i)
    t.rt(i)
    t.circle(i*4)
    c.fd(i)
    c.rt(i)
    c.circle(i*2)

s.exitonclick()
