from scorebord import Scorebord, Score
from ball import Ball
from player_bord import Player_bord
from turtle import Screen
from time import sleep

SCREEN_WIDTH = 0.95
SCREEN_HEIGHT = 0.9
PLACE_PLAYER_BORD = 700
# creat the screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT, starty=3, startx=0)
screen.bgcolor('black')
screen.title('my_second_game')

screen.tracer(0)
#
player1 = Player_bord()
player2 = Player_bord()
player1.goto(PLACE_PLAYER_BORD, 0)
player2.goto(-PLACE_PLAYER_BORD, 0)
right_score = Score('r')
left_score = Score('l')
scorebord = Scorebord()
ball = Ball()
#
screen.listen()
screen.onkey(player2.move_up, 'w')
screen.onkey(player2.move_down, 's')
screen.onkey(player1.move_up, 'o')
screen.onkey(player1.move_down, 'l')
is_on_game = True
while is_on_game:
    sleep(0.03)
    screen.update()
    ball.move_condition()
    if (ball.distance(player1) < 50 and ball.xcor() == 680) or (ball.distance(player2) < 70 and ball.xcor() == -680):
        ball.x_move *= -1
    elif ball.xcor() > 680:
        right_score.incriment_score()
        ball.go_to_start_pointe()
    elif ball.xcor() < -680:
        left_score.incriment_score()
        ball.go_to_start_pointe()

# while True:
#     ball.move_condition()


# exit when clicked at the mousse
screen.exitonclick()
