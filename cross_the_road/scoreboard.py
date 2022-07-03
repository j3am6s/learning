from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 0
        self.ecrire()
    def ecrire(self):
        self.clear()
        self.goto(-280, 280)
        self.write(f"Level: {self.level}", "center")
    def add(self):
        self.level += 1
        self.ecrire()
