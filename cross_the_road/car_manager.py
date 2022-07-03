COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

from turtle import Turtle
from random import randint, choice

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2, 1)
        self.penup()
        self.goto(300, randint(-260, 280))
        self.setheading(180)
        self.color(choice(COLORS))
    def move(self, a):
        self.fd(a)
