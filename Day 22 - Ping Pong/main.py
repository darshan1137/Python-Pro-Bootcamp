from turtle import Screen, Turtle, xcor
import time
from paddle import Paddle 
from Ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)
screen.update()

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_is_on  = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Right Paddle Collision
    if ball.distance(right_paddle) < 50 and ball.xcor()>320 or ball.distance(left_paddle) < 50 and ball.xcor()< -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()


    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()

screen.exitonclick()
