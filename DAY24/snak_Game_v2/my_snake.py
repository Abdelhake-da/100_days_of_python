from turtle import Turtle
from piece import Piece

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def draw_bordre():
    pen = Turtle()
    pen.penup()
    pen.setposition(-293, 260)
    pen.pendown()
    pen.pensize(3)
    pen.color('white')
    for i in range(2):
        pen.forward(575)
        pen.right(90)
        pen.forward(540)
        pen.right(90)
    pen.hideturtle()


class Snake:
    def __init__(self):
        self.body = []
        draw_bordre()
        self.creat_snake_fun()
        self.head = self.body[0]
        self.tail = self.body[len(self.body) - 1]

    def add_piece_fun(self, shape='triangle', num=0):
        pice = Piece()
        pice.shape(shape)

        if num % 2 == 0:
            pice.color('red')
        else:
            pice.color('white')
        pice.penup()
        if num == 1 or num == 0 or num == 2:
            pice.goto(-(len(self.body) * 10), 0)
        else:
            pice.goto(self.tail.xcor() + 10, self.tail.ycor())
        self.body.append(pice)

    def creat_snake_fun(self):
        self.add_piece_fun(num=len(self.body))
        for i in range(2):
            self.add_piece_fun(shape='square', num=len(self.body))

    def reset(self):
        for piece in self.body:
            piece.hideturtle()
        self.body.clear()
        self.creat_snake_fun()
        self.head = self.body[0]
        self.tail = self.body[len(self.body) - 1]

    def move(self):
        for pice in range(len(self.body) - 1, 0, -1):
            new_x = self.body[pice - 1].xcor()
            new_y = self.body[pice - 1].ycor()
            self.body[pice].goto(new_x, new_y)
            self.body[pice].setheading(self.body[pice - 1].heading())

        self.head.forward(MOVE_DISTANCE)

    def turn_up_fun(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down_fun(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_right_fun(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_left_fun(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_tial_fun(self):
        self.add_piece_fun('square', num=len(self.body))
        self.tail = self.body[len(self.body) - 1]
