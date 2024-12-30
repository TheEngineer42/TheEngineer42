from tkinter import*
root = Tk()
root.geometry('500x500')

e1 = Entry(root, font = 'Calibri 30')
e1.pack()

e2 = Entry(root, font = 'Calibri 30', justify = 'right')
e2.pack()



e1.insert(0, 'text') ########

e2.insert(0, 'number') ######

root.mainloop()