from tkinter import*
import random

root = Tk()
root.geometry('500x500')

canvas = Canvas(root, width = 500, height = 500, bg = 'blue')

w = Button(root, text = 'Click me!', height = 5, width = 15, bg = 'skyblue')


canvas.pack()
w.place(anchor = CENTER) #puts button into middle
root.mainloop()


