from turtle import Screen, shape, Turtle
import pandas as pd
from time import sleep

'''
def get_mouse_click_coor(x, y):
    print(x, y)
onscreenclick(get_mouse_click_coor)
mainloop()
'''
stat_guest = 0

lis = []
def usa():

    global stat_guest, lis
    answer_state = screen.textinput(f'{stat_guest}/50 state Correnct', prompt='what\' another state\'s name?').title()
    if answer_state in data_frame.state.to_list():
        if answer_state not in lis:
            stat_guest += 1
        lis.append(answer_state)
        wilaya = data_frame[data_frame['state'] == answer_state]
        x = wilaya['x'].values[0]
        y = wilaya['y'].values[0]
        pen.goto(x, y)
        pen.write(f'{answer_state}')
    elif answer_state == 'Exit':
        not_find_state = [state for state in data_frame.state.to_list() if state not in lis]
        print(lis)
        print(f'{not_find_state}, {len(not_find_state)}')
        return 1

def search():
    answer_state = screen.textinput('guess the state', prompt='what\' another state\'s name?')
    if answer_state in data_frame.state.to_list():
        wilaya = data_frame[data_frame['state'] == answer_state]
        x = wilaya['x'].values[0]
        y = wilaya['y'].values[0]
        pen.goto(x, y)
        pen.pendown()
        pen.color('red')
        pen.write(f'.', font=('', 20, ''))
        pen.color('green')
    elif answer_state == 'exit':
        return 1


screen = Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
shape(image)
data_frame = pd.read_csv('50_states.csv')
pen = Turtle()
pen.color('green')
pen.penup()
pen.hideturtle()
while True:
    if usa() == 1:
        break

screen.exitonclick()
