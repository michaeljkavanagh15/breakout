from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super(Paddle, self).__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(8.0, 1.0)
        self.setheading(90)
        self.speed('fastest')
        self.setpos(x, y)

    def move_left(self):
        if self.xcor() > -320:
            new_x = self.xcor() - 60
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() < 320:
            new_x = self.xcor() + 60
            self.goto(new_x, self.ycor())
