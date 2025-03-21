from tkinter import*
root = Tk()
root.geometry('500x500')

def single_click(event):
    root.title('left click')


def double_click(event):
    root.title('right click')


def motion(event):
    root.title(f'x:{event.x}, y:{event.y}')



root.bind("<Button-1>", single_click)
root.bind("<Button-3>", double_click)
root.bind("<Motion>", motion)


root.mainloop()