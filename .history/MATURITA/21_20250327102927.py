from tkinter import*
import random
root = Tk()
root.geometry('500x500')
canvas = Canvas(root, bg = 'white', height= 500, width = 500)
canvas.pack()

y = random.randrange(0,500)
colors = ['green', 'light green', 'dark green']

for i in range(0,500,10):
    canvas.create_rectangle(i+20,y,i+20,500, fill = random.choice(colors))


root.mainloop()