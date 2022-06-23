import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)
is_game_on = True
screen.listen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
score = Score()

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bouncex()

    if ball.xcor() > 320 and ball.distance(r_paddle) > 50:
        score.l_point()
        ball.restart_game()

    if ball.xcor() < -320 and ball.distance(r_paddle) > 50:
        score.r_point()
        ball.restart_game()

screen.exitonclick()
