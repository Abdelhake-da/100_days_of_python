from turtle import Screen
from my_snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('my snake game')
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()

screen.onkey(snake.turn_right_fun, 'd')
screen.onkey(snake.turn_left_fun, 'a')
screen.onkey(snake.turn_up_fun, 'w')
screen.onkey(snake.turn_down_fun, 's')
is_game_on = True
score = 0
speed = 0.1
while is_game_on:
    screen.update()
    time.sleep(speed)
    snake.move()
    # detect5
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.incriment_score()
        if scoreboard.score <= 50:
            speed /= 1.07
        snake.add_tial_fun()
    if snake.head.xcor() >= 295 or snake.head.xcor() <= -305 or snake.head.ycor() < -290 or snake.head.ycor() > 270:
        is_game_on = False
        scoreboard.game_over()
    for piece in snake.body[1:]:
        if snake.head.distance(piece) < 10:
            is_game_on = False
            scoreboard.game_over()
screen.exitonclick()
