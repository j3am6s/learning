from turtle import Turtle

START = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20

class Snake:
    def __init__(self):
        self.segment = []
        self.create()
        self.head = self.segment[0]
    def create(self):
        for position in START:
            self.add(position)
    def add(self, position):
        jean = Turtle("square")
        jean.color("white")
        jean.penup()
        jean.goto(position)
        self.segment.append(jean)
    def extend(self):
        self.add(self.segment[-1].position())
    def move(self):
        for i in range(len(self.segment)-1, 0, -1):
            self.segment[i].goto(self.segment[i-1].xcor(), self.segment[i-1].ycor())
        self.head.fd(DISTANCE)
    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create()
        self.head = self.segment[0]
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
