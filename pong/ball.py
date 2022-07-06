from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(0.8, 0.8)
        self.speed(6)
    def refreshpaddle(self):
        if self.heading() > 90 and self.heading() < 270:
            self.setheading(randint(-90, 90))
        else:
            self.setheading(randint(90, 270))
    def refreshwall(self):
        if self.heading() > 90 and self.heading() < 270:
            self.setheading(randint(90, 270))
        else:
            self.setheading(randint(-90, 90))
    def move(self):
        self.fd(5)
