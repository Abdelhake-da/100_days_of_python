from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Animale(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.way_number = 0
        self.setheading(UP)
        self.shape('turtle')
        self.goto(0, -275)

    def move_up(self):
        if self.ycor() + 50 < 300:
            self.setheading(UP)
            new_x = self.xcor()
            new_y = self.ycor() + 50
            self.goto(new_x, new_y)
            self.incriment_way_number()


    def move_down(self):
        if self.ycor() - 50 > -300:
            self.setheading(DOWN)
            new_x = self.xcor()
            new_y = self.ycor() - 50
            self.goto(new_x, new_y)
            self.decriment_way_number()


    def move_left(self):
        if self.xcor() - 50 > -410:
            self.setheading(LEFT)
            new_x = self.xcor() - 50
            new_y = self.ycor()
            self.goto(new_x, new_y)

    def move_right(self):
        if self.xcor() + 50 < 410:
            self.setheading(RIGHT)
            new_x = self.xcor() + 50
            new_y = self.ycor()
            self.goto(new_x, new_y)

    def incriment_way_number(self):
        self.way_number += 1

    def decriment_way_number(self):
        self.way_number -= 1

    def go_to_start(self):
        self.goto(self.xcor(), -275)
