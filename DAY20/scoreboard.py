from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.incriment_score()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align=ALIGN, font=FONT)

    def incriment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align=ALIGN, font=FONT)
