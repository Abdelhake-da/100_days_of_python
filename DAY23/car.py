from turtle import Turtle


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move(self):
        self.forward(-30)
