from tkinter import*


root = Tk()


ent1 = Entry(root, bg = 'red', bd = 10, font = ('Arial', 18))
ent2 = Entry(root, bg = 'blue', bd = 10, font = ('Arial', 18))

ent1.pack()
ent2.pack()


root.mainloop()