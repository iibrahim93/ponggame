from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.width(5)
        self.penup()
        self.hideturtle()
        self.setx(0)
        self.sety(-400)
        self.pendown()
        self.showturtle()
        self.left(90)
        self.draw()

    def draw(self):
        while self.ycor() != 400:
            for steps in range(0, 100, 20):
                self.pendown()
                self.forward(10)
                self.penup()
                self.forward(10)

