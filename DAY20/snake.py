from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def draw_bordre():
    pen = Turtle()
    pen.penup()
    pen.setposition(-290, 260)
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

    def creat_snake_fun(self):
        pice = Turtle()
        pice.shape()
        pice.color('white')
        pice.penup()
        pice.goto(-(len(self.body) * 20), 0)
        self.body.append(pice)
        for i in range(2):
            pice = Turtle()
            pice.shape('square')
            pice.color('white')
            pice.penup()
            pice.goto(-(len(self.body) * 20), 0)
            self.body.append(pice)

    def move(self):
        for pice in range(len(self.body) - 1, 0, -1):
            new_x = self.body[pice - 1].xcor()
            new_y = self.body[pice - 1].ycor()
            self.body[pice].goto(new_x, new_y)

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
        pice = Turtle()
        pice.shape('square')
        pice.color('white')
        pice.penup()
        pice.goto(self.tail.xcor() + 20, self.tail.ycor())
        self.body.append(pice)
        self.tail = self.body[len(self.body) - 1]
