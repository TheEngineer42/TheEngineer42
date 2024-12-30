from tkinter import*
import random

root = Tk()
root.geometry('500x500')

canvas = Canvas(root, width = 500, height = 500, bg = 'blue')


def random_canvas():
    a = random.randint(0,500)
    b = random.randint(0,500)
    c = random.randint(0,500)
    d = random.randint(0,500)
    canvas.create_rectangle(a,b,c,d)

w = Button(root, text = 'Click me!', height = 5, width = 15, bg = 'skyblue',
           command = random_canvas)


canvas.pack()
w.place(x=200, y =200) #puts button into middle
root.mainloop()


