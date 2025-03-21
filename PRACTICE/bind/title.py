from tkinter import*
root = Tk()
root.geometry('500x500')

def left_click(event):
    root.title('left click')


def right_click(event):
    root.title('right click')

def double_click(event):
    root.title('double click')


def motion(event):
    root.title(f'x:{event.x}, y:{event.y}')



root.bind("<Button-1>", left_click)
root.bind("<Button-3>", right_click)
root.bind("<Double-Button-1>", double_click)
root.bind("<Motion>", motion)


root.mainloop()