from tkinter import *

window = Tk()
window.title('Mile To Kilometer Converter')
window.minsize(width=300, height=80)
window.config(padx=10, pady=10)
# create label 0,0
label = Label()
label.grid(column=0, row=0)
# create entry 0,1
entry = Entry(width=20)
entry.grid(column=1, row=0)
# entry.config(padx=20, pady=10)
# create label 0,2
label1 = Label(text='is equal to')
label1.grid(column=0, row=1)
label1.config(padx=20)
# create label 1,0
label2 = Label(text='0')
label2.grid(column=1, row=1)
# create label 1,1
label3 = Label(text='Km')
label3.grid(column=2, row=1)
# create label 1,2
label4 = Label(text='Miles')
label4.grid(column=2, row=0)


# calcule function
def calcule():
    try:
        num = float(entry.get())
        label2['text'] = round(num * 1.609, 2)
    except:
        label2['text'] = 'There is something wrong'


# create button 1,2
button = Button(text='Calculate', command=calcule)
button.grid(column=1, row=2)
window.mainloop()
