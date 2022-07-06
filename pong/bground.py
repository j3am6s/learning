from turtle import Turtle

class Bground(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, -280)
        self.setheading(90)
        for i in range(30):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)
