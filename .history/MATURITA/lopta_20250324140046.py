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

    if x> 550:
        vx*=-1 #vx = vx*-1

    if y> 550:
        vy*=-1

    if x<50:
        vx = vx * -1
    
    if y<50:
        vy = vy * -1


    canvas.delete('ball')
    canvas.create_oval(x,y,x+50,y+50, fill = 'blue', tag = 'ball')
    root.after(30,update)

update()

root.mainloop()