from tkinter import*


def enter_leave(event):
    if event.type == '7':
        event.widget['text'] = 'In'

    elif event.type == '8':
        event.widgetp['text'] = 'Out'

root = Tk()


lab1 = Label(width = 20, height = 3, bg = 'white')
lab1.pack()

lab1.bind('<Enter>', enter_leave)
lab1.bind('<Leave>', enter_leave)


lab2 = Label(width = 20, height = 3, bg = 'black', fg = 'white')
lab1.pack()

lab2.bind('<Enter>', enter_leave)
lab2.bind('<Leave>', enter_leave)

root.mainloop()