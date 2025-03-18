from tkinter import* #imports Python's standard GUI(Graphical User Interface) library
root = Tk() #initializes the main window(root window)
root.geometry('500x500')

def change(event):
    b['fg'] = 'red'
    b['activeforeground'] = 'blue'

b = Button(text = 'red', width = '10', height = 3)
b.bind('<Button-1>', change) #used to bind an event to a function
b.bind('<Return>', change)

#Button-1 = leftt mouse button click

b.pack()

root.mainloop()