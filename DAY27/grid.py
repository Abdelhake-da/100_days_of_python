from tkinter import *

window = Tk()  # for create window
window.title('my first gui program')
window.minsize(width=500, height=300)
# create label
my_label = Label(text='I am a label', font=('Arial', 12, 'bold'))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=10)
# create button
button = Button(text='am here')
button.grid(column=2, row=0)
# create button
button1 = Button(text='am here')
button1.grid(column=1, row=1)
# create entry
inPut = Entry(width=30)
inPut.insert(END, string='Some text to begin with.')  # Adds some text to begin with.
inPut.grid(column=3, row=2)
window.mainloop()
