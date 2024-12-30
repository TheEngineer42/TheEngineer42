from tkinter import*
root = Tk()
root.geometry('500x500')

x = Entry(root, font = 'Calibri 30')
x.pack()

x.insert(0, 'text')


root.mainloop()