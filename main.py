from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

game_is_on = True



while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(left_paddle) < 60 and ball.xcor() == -320 or ball.distance(right_paddle) < 60 and ball.xcor() == 320:
        ball.hit()


    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()
        speed = 0.1

    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()
        speed = 0.1

screen.exitonclick()
