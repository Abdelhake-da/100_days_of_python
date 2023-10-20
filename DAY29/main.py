from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

WHITE = '#ffffff'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_e.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
from os import path


def clear():
    website_e.delete(0, END)
    # email_e.delete(0, END)
    password_e.delete(0, END)


def save_password():
    if len(str(website_e.get()).strip()) == 0 \
            or len(str(email_e.get()).strip()) == 0 \
            or len(str(password_e.get()).strip()) == 0:
        messagebox.showinfo(title='error', message='You must to fill all the boxes')
    else:
        if messagebox.askokcancel(title=website_e.get(),
                                  message=f'These are the details entered:'
                                          f'\nEmail: {email_e.get()}'
                                          f'\nPassword: {password_e.get()}'
                                          f'\nIs it ok to save?'):
            website = "{0:^30}".format(website_e.get())
            email = "{0:^40}".format(email_e.get())
            password = "{0:^30}".format(password_e.get())
            if path.exists('password_manager.txt'):

                with open('password_manager.txt', 'a')as file:
                    file.write(f'\n{website}|{email}|{password}')
            else:
                with open('password_manager.txt', 'a')as file:
                    file.write("{0:^30}".format('Website') + '|' +
                               "{0:^40}".format('Email/User Name') + '|' +
                               "{0:^30}".format('Password'))
                    file.write(f'\n{website}|{email}|{password}')
            clear()


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg=WHITE)
# canvas (c=1, r=0)
logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)
# website label (c=0, r=1)
website_l = Label(text='Website: ', bg=WHITE)
website_l.grid(column=0, row=1)
# email/Username label (c=0, r=2)
email_l = Label(text='Email/Username: ', bg=WHITE)
email_l.grid(column=0, row=2)
# password label (c=0, r=3)
password_l = Label(text='Password: ', bg=WHITE)
password_l.grid(column=0, row=3)
# entry website (c=1 and 2:(columnspan=2), r=1)
website_e = Entry(width=50)
website_e.grid(column=1, row=1, columnspan=2)
website_e.focus()
# entry email/Username (c=1 and 2, r=2)
email_e = Entry(width=50)
email_e.insert(0, 'abdelhake.da@gmail.com')
email_e.grid(column=1, row=2, columnspan=2)
# entry password (c=1, r=3)
password_e = Entry(width=32)
password_e.grid(column=1, row=3)
# button generate password (c=2, r=3)
generate_b = Button(text='Generate Password',command= generate_password)
generate_b.grid(column=2, row=3)
# button add (c=1 and 2, r=4)
add_b = Button(text='Add', width=43, command=save_password)
add_b.grid(column=1, row=4, columnspan=2)
# mainloop
window.mainloop()
