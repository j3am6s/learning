from tkinter import colorchooser
from turtle import *

#make screen
screen = Screen()
#change bgcolor
screen.bgcolor("black")


#assign turtle to variable "turtle"
turtle = Turtle()
#change shape : length, width, outline
turtle.shapesize(2, 2, 2)
#change pen width
turtle.pensize(3)
#change shape turtle (Square, Arrow, Circle, Turtle, Triangle, Classic)
turtle.shape("turtle")
turtle.shape("classic")
#change speed (0 to 10)
turtle.speed(0)

#make a lil square
turtle.color("red")
#remplir la shape
turtle.begin_fill()
for i in range(4):
    turtle.fd(50)
    turtle.lt(90)
turtle.end_fill()
#leave turtle imprint
turtle.stamp()
turtle.up() #or turtle.penup()

#make a huge ass cross
#color(outside + pen, inside)
turtle.color("blue", "lightBlue")
turtle.goto(-100, -100)
turtle.down()
turtle.goto(100, 100)
turtle.up()
turtle.goto(-100, 100)
turtle.down()
turtle.goto(100, -100)
turtle.up()

#draw preset shape : circle, parameter is radius
turtle.goto(-50, -50)
turtle.color("green")
turtle.down()
turtle.circle(25)
turtle.up()

#draw preset shape : dot (filled circle), parameter is diameter
turtle.goto(-50, 50)
turtle.color("orange")
turtle.down()
turtle.dot(50)
turtle.up()

#pour écrire plus vite
#turtle.pen(fillcolor="pink", speed=4)

#go home = (0, 0)
turtle.home
turtle.color("white")

#erase the drawings
turtle.clear()

#reset to initial parameters
turtle.reset()
screen.bgcolor("white")

#play w/ user input
if input("Would you like me to draw a shape? Type yes or no: ") == "yes":
    turtle.circle(50)
else:
    print("Okay")

#create a clone
clone = turtle.clone()
turtle.circle(100)
clone.circle(50)


#exit on click, as it says dumbass
screen.exitonclick()
