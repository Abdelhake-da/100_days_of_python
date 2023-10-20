from tkinter import *
from tkinter import messagebox
from random import *

import pyperclip
import json

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


# TODO __ Cleat All Text_Fild Function
def clear():
    website_e.delete(0, END)
    # email_e.delete(0, END)
    password_e.delete(0, END)


# TODO __ Read File Function
def read_json(file_n):
    with open(file_n, 'r')as file:
        data = json.load(file)
    return data


# TODO __ Create New File Function
def write_json(file_n, data, ask=True):
    answer = True
    if ask:
        answer = messagebox.askokcancel(title='Save Password',
                                        message=f'Are you want to save this website password ?')

    if answer:
        try:
            data = {data['website']: [data['account']]}
        except KeyError:
            pass
        finally:
            with open(file_n, 'w')as file:
                json.dump(data, file, indent=4)


# TODO __ Update Function
def update_json(file_n, data):
    ask = True
    old_data = read_json(file_n)
    # TODO (check if the website is already exist in the file)
    if data['website'] in old_data.keys():
        lis = [item['email'] for item in old_data[data['website']]]
        # TODO (check if the email is already exist in the file with the same website)
        if data['account']['email'] not in lis:
            old_data[data['website']].append(data['account'])
        else:
            # TODO (ask if the user want to change the password or leave it as is)
            if messagebox.askokcancel(title='Change Password',
                                      message='Are you sure you want to change the password?'):
                for i in range(len(lis)):
                    if lis[i] == data['account']['email']:
                        old_data[data['website']][i]['password'] = data['account']['password']
                ask = False
    else:
        old_data[data['website']] = [data['account']]
    write_json(file_n, old_data, ask)


# TODO __ Function For The Add Button
def save_password():
    website = website_e.get()
    email = email_e.get()
    password = password_e.get()
    if len(website.strip()) == 0 \
            or len(email.strip()) == 0 \
            or len(password.strip()) == 0:
        messagebox.showinfo(title='error', message='You must to fill all the boxes')
    else:
        new_data = {'website': website,
                    'account': {'email': email,
                                'password': password}}

        if path.exists('password_manager.json'):
            update_json('password_manager.json', new_data)
        else:
            print(new_data['account'])
            write_json('password_manager.json', new_data)
        clear()


# TODO __ Function For The Search Button
def search():
    old_data = read_json('password_manager.json')
    website = website_e.get()
    email = email_e.get()
    if len(website.strip()) == 0 or len(email.strip()) == 0:
        messagebox.showinfo(title='error', message='You must to fill the email and website boxes')
    else:
        if website in old_data.keys():
            lis = [item['email'] for item in old_data[website]]
            for i in range(len(lis)):
                if lis[i] == email:
                    password = old_data[website][i]['password']
                    messagebox.showinfo(title='Search', message=f'website: {website}\n'
                                                                f'email: {email}\n'
                                                                f'password: {password}')
                    break
                elif i == len(lis) - 1:
                    messagebox.showinfo(title='Search', message='Search not found')
        else:
            messagebox.showinfo(title='Search', message='Search not found')


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
generate_b = Button(text='Generate Password', command=generate_password)
generate_b.grid(column=2, row=3)
# button add (c=1 and 2, r=4)
add_b = Button(text='Add', width=43, command=save_password)
add_b.grid(column=1, row=4, columnspan=2)
# button search (c=2,r=1 and 2 ,rowspan=2)
search_b = Button(text='Search', height=2, width=14, command=search)
search_b.grid(column=2, row=1, rowspan=2)
# mainloop
window.mainloop()
