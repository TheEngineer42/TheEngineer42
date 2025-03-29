from tkinter import*
import random
root = Tk()
root.geometry('500x500')
canvas = Canvas(root, bg = 'white', height= 500, width = 500)
canvas.pack()


colors = ['green', 'light green', 'dark green']

for i in range(0,500,10):
    y = random.randrange(0,480)
    canvas.create_rectangle(i,y,i+10,500, fill = random.choice(colors))


root.mainloop()