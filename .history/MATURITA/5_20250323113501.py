from tkinter import*
root = Tk()
root.geometry('500x500')
import random

colors = ['blue','red','green','orange','yellow','purple','black','pink','white']

canvas = Canvas(root, height=500, width=500)



def drawing(event):
    color = random.choice(colors)
    a = event.x
    b = event.y
    canvas.create_oval(a-10,b-10,a+10,b+10, fill = color)
    canvas.pack()

def erasing(event):
    canvas.create_rectangle(0,0,500,500, fill = 'white')
    canvas.pack()



root.bind("<Button-1>",drawing)
root.bind('<space>', erasing)

root.mainloop()