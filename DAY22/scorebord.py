from turtle import Turtle

Y_START = 375
DOWN = 270
Y_END = -375
X = 0
RIGHT_SIDE_X = 80
ALIGN = 'center'
FONT = ('Courier', 40, 'normal')


class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.draw_dashed_line_in_middle_fun(Y_START, Y_END, X)

    def draw_dashed_line_fun(self, y_start=0, y_end=0, x=0):
        self.goto(x, y_start)
        while self.ycor() >= y_end:
            self.pendown()
            self.pensize(12)
            self.setheading(DOWN)
            self.fd(30)
            self.penup()
            self.fd(30)
            self.penup()

    def draw_dashed_line_in_middle_fun(self, y_start=0, y_end=0, x=0):
        if y_start > y_end:
            self.draw_dashed_line_fun(y_start, y_end, x)
        else:
            self.draw_dashed_line_fun(y_end, y_start, x)


class Score(Turtle):
    def __init__(self, direction='r'):
        super().__init__()
        self.score = -1
        self.color('white')
        self.penup()
        if direction == 'r':
            self.goto(RIGHT_SIDE_X, Y_START - 60)
        elif direction == 'l':
            self.goto(-RIGHT_SIDE_X, Y_START - 60)
        self.hideturtle()
        self.incriment_score()

    def update_scoreboard(self):
        self.write(f'{self.score}', align=ALIGN, font=FONT)

    def incriment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align=ALIGN, font=FONT)
