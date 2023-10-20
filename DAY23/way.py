from turtle import Turtle, colormode
from car import Car
from random import randint, choice


def creat_new_car(y, lenw):
    color = choice(
        [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (255, 110, 17), (250, 137, 98), (250, 103, 228)])
    colormode(255)
    car = Car()
    car.color(color)
    dis = (lenw / 2) + y
    car.goto(380, dis)
    return car


class Way(Turtle):
    def __init__(self, lenw=50, y_start_position=0, number=1, tow_side=True):
        super().__init__()
        self.lenw = lenw
        self.y_start_position = y_start_position
        self.number = number
        self.hideturtle()
        self.cars = []
        self.speed('fastest')
        self.draw_road_limits(y_start_position, lenw, tow_side)

    def incriment_number(self):
        self.number += 1

    def draw_road_limits(self, y, lenw, tow_side):
        self.penup()
        if tow_side:
            self.penup()
            self.goto(-400, y + lenw)
            self.pendown()
            while self.xcor() <= 400:
                self.draw_dashed_line_fun()
        self.penup()
        self.goto(-400, y)
        self.pendown()
        while self.xcor() <= 400:
            self.draw_dashed_line_fun()

    def draw_dashed_line_fun(self):
        self.fd(20)
        self.penup()
        self.fd(10)
        self.pendown()

    def move_car(self, max_num, chance=10):
        if (randint(1, chance) == 1 or len(self.cars) == 0) and len(self.cars) < max_num:
            self.cars.append(creat_new_car(self.y_start_position, lenw=self.lenw))
        if self.cars[0].xcor() < -380:
            self.cars[0].hideturtle()
            del self.cars[0]
        for car in self.cars:
            car.move()
