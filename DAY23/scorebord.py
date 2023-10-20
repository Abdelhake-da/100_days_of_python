from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 24, 'normal')


def game_over():
    game_over = Turtle()
    game_over.goto(0, 0)
    game_over.write(f'Game Over', align=ALIGN, font=FONT)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('black')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.set_score(self.score)

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align=ALIGN, font=FONT)

    def set_score(self, score):
        self.clear()
        self.score = score
        self.update_scoreboard()
