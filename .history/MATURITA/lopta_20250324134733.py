from tkinter import*
import random

root  = Tk()
root.geometry('600x600')
canvas = Canvas(bg = 'white')
canvas.pack(fill = BOTH, expand = 1)

vx = 5
vy = 5

x = random.randint(50,600)
y = 0


def update():
    global x,y, vx,vy
    x += vx
    y += vy
    canvas.create_oval(x,y,x+50,y+50, fill = 'blue')
    root.after(30,update)

update()