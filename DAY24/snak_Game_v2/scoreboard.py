from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 24, 'normal')


def get_high_score():
    try:
        with open('score.txt') as file:
            return int(file.read())
    except:
        return 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = get_high_score()
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.incriment_score()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} | High Score: {self.high_score}', align=ALIGN, font=FONT)

    def incriment_score(self):
        self.score += 1
        self.update_scoreboard()

    def set_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('score.txt', mode='w')as file:
                file.write(str(self.score))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'Game Over', align=ALIGN, font=FONT)
