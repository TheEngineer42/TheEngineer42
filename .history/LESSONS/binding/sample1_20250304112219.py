from tkinter import* #imports Python's standard GUI(Graphical User Interface) library
root = Tk() #initializes the main window(root window)
root.geometry('500x500')

def change(event):
    b['fg'] = 'red'
    b['activeforeground'] = 'blue'

b = Button(text = 'red', width = '10', height = 3)
b.bind('<Button-1>', change) #used to bind an event to a function
b.bind('<Return>', change)  #means pressing Enter key
#when either of these events occur, the 'change ' function is executed

#Button-1 = leftt mouse button click

b.pack()

root.mainloop()

#event is not a function. It's an object that contains information about what triggered the event.


#bind(event, function) - allow you to attach specific events to a function
#command is an option used in Button, Menu, etc., to specify a function that runs when the widget is clicked.