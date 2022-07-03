STARTING_POSITION = (0, -280)

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
    def move(self):
        self.fd(10)
    def refresh(self):
        self.goto(0, -280)

