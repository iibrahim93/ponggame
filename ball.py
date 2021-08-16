from turtle import Turtle
import random

THIRTY = range(0,31)
THREE_SIXTY = range

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.current_x = 10
        self.current_y = 10
        self.speed_num = 0.1






    # make ball move in random directions(forward,backward) or any angle (0-360)
    # I need all the directions a turtle can move in
    # Randomize each move

    def move(self):
        new_x = self.xcor() + self.current_x
        new_y = self.ycor() + self.current_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.current_y *= -1

    def bounce_x(self):
        self.current_x *= -1
        self.speed_num *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.speed_num = 0.1
        self.bounce_x()









