from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 40
WID = 5
LEN = 1


class Player_bord(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=WID, stretch_len=LEN)
        self.color('white')

    def move_up(self):
        if self.ycor() < 360:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -360:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
