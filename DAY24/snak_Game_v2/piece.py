from turtle import Turtle


class Piece(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('triangle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=0.60)
