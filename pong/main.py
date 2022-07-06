from turtle import Screen
import time
from bground import Bground
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

bground = Bground()
paddle1 = Paddle(0)
paddle2 = Paddle(1)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

while(True):
    screen.update()
    time.sleep(0.01)    
    ball.move()
    for segment in paddle1.segment:
        if ball.distance(segment) < 10:
            ball.refreshpaddle()
    for segment in paddle2.segment:
        if ball.distance(segment) < 10:
            ball.refreshpaddle()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.refreshwall()
    if ball.xcor() > 295 :
        ball.home()
        score.add1()
    if ball.xcor() < -295:
        ball.home()
        score.add2()

screen.exitonclick()
