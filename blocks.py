from turtle import Turtle

class Yellow_block(Turtle):
    def __init__(self, x, y):
        super(Yellow_block, self).__init__()
        self.color("yellow")
        self.penup()
        self.shape("square")
        self.shapesize(5.0, 1.0)
        self.setheading(90)
        self.speed('fastest')
        self.setpos(x, y)
        self.points = 10


class Green_block(Turtle):
    def __init__(self, x, y):
        super(Green_block, self).__init__()
        self.color("green")
        self.penup()
        self.shape("square")
        self.shapesize(4.0, 1.0)
        self.setheading(90)
        self.speed('fastest')
        self.setpos(x, y)
        self.points = 20


class Red_block(Turtle):
    def __init__(self, x, y):
        super(Red_block, self).__init__()
        self.color("red")
        self.penup()
        self.shape("square")
        self.shapesize(3.0, 1.0)
        self.setheading(90)
        self.speed('fastest')
        self.setpos(x, y)
        self.points = 30
