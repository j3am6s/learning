from turtle import *

jean = Turtle()
screen = Screen()

screen.listen()

def right():
    jean.fd(10)
def left():
    jean.fd(-10)
def upa():
    jean.lt(10)
def downa():
    jean.rt(10)
def clear():
    jean.clear()
    jean.penup()
    jean.home()
    jean.pendown()

screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(upa, "Up")
screen.onkey(downa, "Down")
screen.onkey(clear, "c")

screen.exitonclick()
