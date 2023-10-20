from tkinter import *

# ----------- CONSTANTS ------------#
PINK = '#e2979e'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
min1 = 0
check_mark_txt = ''
is_started = False
Timer = None


def check_reps():
    global reps, min1, check_mark_txt
    min1 = 0
    if reps % 8 != 0:
        if reps % 2 == 0:
            timer.config(font=(FONT_NAME, 21, 'bold'), bg=YELLOW)
            timer['text'] = 'Short Break'
            timer['fg'] = PINK
            min1 = SHORT_BREAK_MIN
            check_mark_txt += '✔'
            check_mark['text'] = check_mark_txt
        else:
            timer.config(font=(FONT_NAME, 21, 'bold'), bg=YELLOW)
            timer['text'] = 'Work'
            timer['fg'] = GREEN
            min1 = WORK_MIN

    else:
        timer.config(font=(FONT_NAME, 29, 'bold'), bg=YELLOW)
        timer['text'] = 'Long Break'
        timer['fg'] = RED
        min1 = LONG_BREAK_MIN
        check_mark_txt += '✔'
        check_mark['text'] = check_mark_txt


# ---------------------------- Timer Reset ---------------------------- #
def reset_timer():
    global reps, min1, check_mark_txt, is_started, Timer
    window.after_cancel(Timer)
    reps = 0
    min1 = 0
    check_mark_txt = ''
    check_mark['text'] = check_mark_txt
    is_started = False
    canvas.itemconfig(timer_text, text=f'25:00')
    timer['text'] = 'Timer'
    timer['fg'] = GREEN


# ---------------------------- Timer Mechanism ---------------------------- #
def start_timer():
    global reps, min1, is_started
    if not is_started:
        is_started = True
        reps += 1
        check_reps()
        # after
        window.after(1000, count_down, min1-1, 59)


# ---------------------------- Countdown Mechanism ---------------------------- #
def count_down(Min, s):
    global reps, min1, check_mark_txt, is_started, Timer
    if s < 10:
        if Min < 10:
            canvas.itemconfig(timer_text, text=f'0{Min}:0{s}')
        else:
            canvas.itemconfig(timer_text, text=f'{Min}:0{s}')
    else:
        if Min < 10:
            canvas.itemconfig(timer_text, text=f'0{Min}:{s}')
        else:
            canvas.itemconfig(timer_text, text=f'{Min}:{s}')

    if s > 0 or Min > 0:
        if s == 0 and Min > 0:
            Min -= 1
            s = 60
        Timer = window.after(1000, count_down, Min, s - 1)
    else:
        if reps < 8:
            is_started = False
            start_timer()



# ---------------------------- UI SETUP ---------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
# timer label
timer = Label(text='Timer', fg=GREEN)
timer.config(font=(FONT_NAME, 29, 'bold'), bg=YELLOW)
timer.grid(column=1, row=0)
# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text='25:00', fill='white', font=(FONT_NAME, 29, 'bold'))
canvas.grid(column=1, row=1)
# button start
start = Button(text='Start', command=start_timer)
start.grid(column=0, row=2)
# button reset
reset = Button(text='reset', command=reset_timer)
reset.grid(column=2, row=2)
# check mark label
check_mark = Label(text='', fg=GREEN)
check_mark.config(bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
check_mark.grid(column=1, row=3)

window.mainloop()
