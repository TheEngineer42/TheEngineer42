from tkinter import*
root= Tk()
root.minsize(width = 500, height = 400)

def b1(event):
    root.title('left mouse click')

def b3(event):
    root.title('right mouse click')

def move(event):
    x = event.x
    y = event.y
    s = "mouse movement {}x{}".format(x,y)
    root.title(s)


root.bind("<Button-1>", b1)
root.bind("Button-3", b3)
root.bind("Motion", move)

root.mainloop()