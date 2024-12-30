from tkinter import*
root = Tk()
root.geometry('500x500')

x = Entry(root, text = 'Calibri 15')
x.pack()

m = x.insert(0, 'text')
m.pack()

root.mainloop()