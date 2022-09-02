from turtle import Screen
from paddle import Paddle
from blocks import Yellow_block, Red_block, Green_block
from ball import Ball
from scoreboard import Scoreboard
import time

t = .05
MOVE_UP = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


paddle = Paddle(-20, -250)

red_block_list = []
for i in range(1, 10):
    red_block = Red_block(-370 + (i*73), 250)
    red_block_list.append(red_block)

green_block_list = []
for i in range(1, 8):
    green_block = Green_block(-380 + (i*94), 210)
    green_block_list.append(green_block)

yellow_block_list = []
for i in range(1, 7):
    yellow_block = Yellow_block(-380 + (i*107), 170)
    yellow_block_list.append(yellow_block)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.move_left, "a")
screen.onkey(paddle.move_right, "d")

game_on = True

while game_on:
    time.sleep(t)
    screen.update()
    ball.move()

    # detect wall
    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect Paddle
    if ball.distance(paddle) < 81 and ball.ycor() < -230:
        ball.bounce_y()
        t -= .001

    # Detect OOB
    if ball.ycor() < -255:
        scoreboard.game_over()
        game_on = False

    # Detect Block
    for block in red_block_list:
        if ball.distance(block) < 25:
            ball.bounce_y()
            scoreboard.increase_score(block.points)
            block.goto(500, 500)
            red_block_list.remove(block)

    for block in yellow_block_list:
        if ball.distance(block) < 40:
            ball.bounce_y()
            scoreboard.increase_score(block.points)
            block.goto(500, 500)
            yellow_block_list.remove(block)

    for block in green_block_list:
        if ball.distance(block) < 35:
            ball.bounce_y()
            scoreboard.increase_score(block.points)
            block.goto(500, 500)
            green_block_list.remove(block)

    # Detect win
    if green_block_list == [] and yellow_block_list == [] and red_block_list == []:
        scoreboard.you_win()
        game_on = False

screen.exitonclick()
