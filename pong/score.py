from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score1 = 0
        self.score2 = 0
        self.ecrire()
    def ecrire(self):
        self.clear()
        self.goto(-12, 280)
        self.write(f"{self.score1}     {self.score2}", "center")
    def add1(self):
        self.score1 += 1
        self.ecrire()
    def add2(self):
        self.score2 += 1
        self.ecrire()
