import random
from tkinter import*
root = Tk()

canvas = Canvas(root, width = 500 , height = 500) 
canvas.pack()


canvas.create_rectangle(0,0,500,500, fill = 'black')


root.mainloop()


