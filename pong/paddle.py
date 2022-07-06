from turtle import Turtle

START = [[(-270, 0), (-270, -20), (-270, -40)], [(270, 0), (270, -20), (270, -40)]]

class Paddle:
    def __init__(self, nb):
        self.segment = []
        self.create(nb)
        self.head = self.segment[0]
    def create(self, nb):
        for position in START[nb]:
            jean = Turtle("square")
            jean.color("white")
            jean.penup()
            jean.goto(position)
            jean.setheading(90)
            self.segment.append(jean)
    def move(self, a, b, c, d):
        for i in range(a, b, c):
            self.segment[i].goto(self.segment[i-d].xcor(), self.segment[i-d].ycor())
        self.head.fd(20)
    def up(self):
        if self.head.heading() == 270:
            self.head = self.segment[0]
            self.head.setheading(90)
        self.move(2, 0, -1, 1)
    def down(self):
        if self.head.heading() == 90:
            self.head = self.segment[-1]
            self.head.setheading(270)
        self.move(0, 2, 1, -1)
