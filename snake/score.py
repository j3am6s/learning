from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        with open("snake/data.txt") as file:
            self.highscore = int(file.read())
        self.score = 0
        self.ecrire()
    def ecrire(self):
        self.clear()
        self.goto(-30, 280)
        self.write(f"Score: {self.score}  High score: {self.highscore}", "center")
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score 
            with open("snake/data.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.ecrire()

    # def over(self):
    #     self.home()
    #     self.write("GAME OVER", "center")

    def add(self):
        self.score += 1
        self.ecrire()
