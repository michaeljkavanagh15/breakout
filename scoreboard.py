from turtle import Turtle
FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(self.score, align='center', font=FONT)

    def increase_score(self, amount):
        self.score += amount
        self.update_scoreboard()

    def you_win(self):
        self.goto(0, 0)
        self.write("YOU WIN", align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)