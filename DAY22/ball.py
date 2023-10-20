# Model of the ball being played with
# from main import SCREEN_WIDTH, SCREEN_HEIGHT

# constant
WIDTH = 360
HIGHT = 360
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
X_MOVE = 10
Y_MOVE = 10
# import
from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = self.choice([X_MOVE, -X_MOVE])
        self.y_move = self.choice([Y_MOVE, -Y_MOVE])
        self.speed('fastest')
        self.shape('circle')
        self.penup()
        self.color('red')

    def choice(self, lis):
        return choice(lis)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def go_to_start_pointe(self):
        self.x_move = self.choice([X_MOVE, -X_MOVE])
        self.y_move = self.choice([Y_MOVE, -Y_MOVE])
        self.goto(0, 0)

    def move_condition(self):
        if self.ycor() >= 750 / 2 or self.ycor() <= -750 / 2:
            self.y_move *= -1
            self.move()
        else:
            self.move()
