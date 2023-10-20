def draw_dashed_line_fun():
    timmy.fd(20)
    timmy.penup()
    timmy.fd(10)
    timmy.pendown()


def draw_square_fun():
    for i in range(4):
        timmy.forward(100)
        timmy.right(90)


def draw_shape_fun(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        timmy.forward(50)
        timmy.right(angle)


def draw_multy_shape_fun(number, colors=None):
    if colors is None:
        colors = ['red']
    for i in range(3, number + 1):
        timmy.color(choice(colors))
        draw_shape_fun(i)


def walk_right_fun():
    timmy.right(90)
    timmy.forward(30)


def walk_left_fun():
    timmy.right(-90)
    timmy.forward(30)


def walk_stright_fun():
    timmy.forward(15)


def walk_backwards_fun():
    timmy.backward(15)


def turn_left_fun():
    timmy.left(15)


def turn_right_fun():
    timmy.right(15)


def random_walk_fun(number_of_feet, pensize, colors):
    dic = {
        '1': walk_left_fun,
        '2': walk_right_fun,
        '3': walk_stright_fun
    }
    timmy.pensize(pensize)
    for _ in range(number_of_feet):
        timmy.color(choice(colors))
        dic[choice(['1', '2', '3'])]()


def get_random_color_fun(len_of_list):
    colors = []
    for _ in range(len_of_list):
        colors.append((choice(range(0, 256)), choice(range(0, 256)), choice(range(0, 256))))
    return colors


def draw_spirograph_fun(number_of_circled, colors):
    angel = 360 / number_of_circled
    for _ in range(number_of_circled):
        timmy.color(choice(colors))
        timmy.circle(100)
        timmy.right(angel)


def clear_drawing_fun():
    timmy.home()
    timmy.clear()


def get_rgb_color_from_image_fun(url_image, number_of_colors):
    colors = []
    for color_ in colorgram.extract(url_image, number_of_colors):
        colors.append((color_.rgb.r, color_.rgb.g, color_.rgb.b))
    return colors


def draw_spot_painting_fun(number_of_dots_in_line, number_of_dots_in_culomn, colors):
    x_position = -300
    y_position = -300
    timmy.penup()
    timmy.goto(x_position, y_position)
    for _ in range(number_of_dots_in_culomn):
        timmy.left(90)
        timmy.forward(40)
        timmy.right(90)
        timmy.goto(x_position, timmy.ycor())
        for __ in range(number_of_dots_in_line):
            timmy.pendown()
            timmy.dot(20, choice(colors))
            timmy.penup()
            timmy.forward(40)


def pen_up_down_fun():
    if timmy.isdown():
        timmy.penup()
    else:
        timmy.pendown()


def drawin_program_fun():
    screen = Screen()
    screen.listen()
    screen.onkey(key='w', fun=walk_stright_fun)
    screen.onkey(key='s', fun=walk_backwards_fun)
    screen.onkey(key='a', fun=turn_left_fun)
    screen.onkey(key='d', fun=turn_right_fun)
    screen.onkey(key='c', fun=clear_drawing_fun)
    screen.onkey(key='space', fun=pen_up_down_fun)
    screen.exitonclick()


def create_turtle_fun(number_of_turtle, colors):
    lis_turtle = []
    for i in range(number_of_turtle):
        lis_turtle.append(Turtle('turtle'))
        lis_turtle[i].color(colors[i])
    return lis_turtle


def place_the_turtle_in_the_screen_fun():
    x = -230
    if len(turtle_lis) % 2 == 0:
        y = ((len(turtle_lis) / 2) * 40) - 20
    else:
        y = ((len(turtle_lis) / 2) * 40)
    for turtle in turtle_lis:
        turtle.penup()
        turtle.goto(x, y)
        y -= 40


def walk_random_distance_fun():
    winner = 0
    is_end = False
    for turtle in range(len(turtle_lis)):
        random_dictanc = randint(1, 10)
        turtle_lis[turtle].forward(random_dictanc)
        if turtle_lis[turtle].xcor() >= 220:
            winner = turtle + 1
            is_end = True
            break
    return winner, not is_end


def turtle_race_fun():
    is_race_on = False
    winner = None
    screen = Screen()
    screen.setup(width=500, height=400)
    user_choice = screen.textinput(title='Make your bet', prompt=f"Choose number between 1 and {len(turtle_lis)} : ")
    place_the_turtle_in_the_screen_fun()
    if user_choice is not None:
        is_race_on = True
    while is_race_on:
        winner, is_race_on = walk_random_distance_fun()
    if winner == int(user_choice):
        print('congratulation')
    else:
        print('good luke in the next races')
    screen.exitonclick()


from random import randint
from turtle import Turtle, Screen, colormode
from random import choice
import colorgram

color = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (255, 110, 17), (250, 137, 98), (250, 103, 228),
         (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164),
         (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129),
         (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
colormode(255)
timmy = Turtle()
timmy.hideturtle()
turtle_lis = create_turtle_fun(8, color)
turtle_race_fun()
