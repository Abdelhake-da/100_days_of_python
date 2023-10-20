from tkinter import Tk, Label, Button, Entry, END, Text, Spinbox, IntVar, Checkbutton, Radiobutton, Listbox

window = Tk()  # for create window
window.title('my first gui program')
window.minsize(width=500, height=300)
# create label
my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.pack()
my_label['text'] = 'hello abdelhake'
my_label.config(text='hola')


# event
def button_clicked():
    my_label['text'] = inPut.get()


# create button
button = Button(text='am here', command=button_clicked)
button.pack()

# create entry
inPut = Entry(width=30)
inPut.insert(END, string='Some text to begin with.')  # Adds some text to begin with.
inPut.pack()
print(inPut.get())

# text
text = Text(height=5, width=35)
text.focus()  # Puts cursor in textbox.
text.insert(END, 'Example of multi-line text entry.')
# Get's current value in textbox at line 1, character 0
print(text.get('1.0', END))
text.pack()


# spinbox
def spinbox_used():
    print(spinbox.get())  # gets the current value in spinbox.


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# scale

# checkbutton
def checkbutton_used():
    # print 1 if on button checked, otherwise 0.
    print(checked_stat.get())


# variable to hold on to checked state,0 is off, 1 is on.
checked_stat = IntVar()
checkbutton = Checkbutton(text='Is On?', variable=checked_stat, command=checkbutton_used)
checked_stat.get()
checkbutton.pack()


# radiobutton
def radio_used():
    print(radio_state.get())


# variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text='Option1', value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text='Option2', value=2, variable=radio_state, command=radio_used)
radiobutton2.pack()
radiobutton1.pack()


# listbox
def listbox_used(event):
    # gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ['apple', 'pear', 'orange', 'banana']
for item in fruits:
    listbox.insert(fruits.index(item), item.title())
listbox.bind('<<ListboxSelect>>', listbox_used)
listbox.pack()
# place : you can provide a X and Y value
# grid : it imagines that your entire program is a grid and you can divide it into any number of columns and rows
window.mainloop()  # main loop is the thing that will keep the window on screen
