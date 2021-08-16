from turtle import Screen
from line import Line
from ball import Ball
from user_paddle import UserPaddle
from score import Scoreboard
import time



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

test = screen.window_width()
print(test)

line = Line()
r_paddle = UserPaddle((350, 0))
l_paddle = UserPaddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
game_is_on = True

while game_is_on:
    time.sleep(ball.speed_num)
    screen.update()
    ball.move()



    #  Collision with top and bottom of the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    #  collision with r_paddle & l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # Detect if ball goes pass r paddle
    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.add_l()

    # Detect if ball goes pass l paddle
    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.add_r()




screen.exitonclick()