from animale import Animale
from turtle import Screen
from way import Way
from time import sleep
from scorebord import Scoreboard, game_over
NUMBER_OF_CARS = 5
screen = Screen()
screen.setup(830, 620)
screen.tracer(0)
y = -250
ways = []
ways_number = 0
score = Scoreboard()
tow_side = False
for i in range(10):
    if i == 0 or i == 9:
        tow_side = True
    else:
        tow_side = False
    ways_number += 1
    way = Way(y_start_position=y, number=ways_number, tow_side=tow_side)
    y += 50
    ways.append(way)
is_playing = True
animale = Animale()
### animale
number_of_cars = 0
chance = 10
screen.listen()
screen.onkey(animale.move_up, 'w')
screen.onkey(animale.move_down, 's')
screen.onkey(animale.move_right, 'd')
screen.onkey(animale.move_left, 'a')
go = True
for i in range(27):
    for way in ways:
        way.move_car(max_num=NUMBER_OF_CARS+number_of_cars)
while is_playing:
    sleep(0.1)
    screen.update()
    for way in ways:
        way.move_car(max_num=NUMBER_OF_CARS+number_of_cars)
    if animale.way_number % 10 == 1 and animale.way_number != 1 and animale.ycor() > 0:
        animale.go_to_start()
        for way in ways:
            way.number += 10
        animale.way_number -= 1
        chance -= 1
        if chance < 7:
            number_of_cars += 2
            chance = 10
        print(f'{chance}//{NUMBER_OF_CARS+number_of_cars}')
    score.set_score(animale.way_number)
    for car in ways[(animale.way_number - 1) % 10].cars:
        if animale.distance(car) < 15:
            game_over()
            is_playing = False

# way.move_car()


screen.exitonclick()
