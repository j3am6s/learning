from turtle import *
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

race = False
bet = screen.textinput(title="Make your bet", prompt="Which will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -100
turtle_list = []

for i in range(len(colors)):
    jean = Turtle("turtle")
    jean.color(colors[i])
    jean.penup()
    jean.goto(-220, y)
    y+= 40
    turtle_list.append(jean)

if bet:
    race = True

while race:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            race = False
            win = turtle.pencolor()
            if win == bet:
                print("You won!")
            else:
                print(f"You lost! {win} won...")
        distance = randint(0, 10)
        turtle.fd(distance)

screen.exitonclick()
