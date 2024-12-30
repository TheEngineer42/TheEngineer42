from tkinter import *

root = Tk()
root.geometry('500x500')

# Create the canvas
canvas = Canvas(root, width=200, height=200, bg='lightblue')
canvas.pack(side=TOP, anchor=W)

# Create a rectangle on the canvas
canvas.create_rectangle(20, 20, 100, 70, fill='blue')

# Create the button
w = Button(root, text='Button', bg='skyblue', height=5, width=15)

# Place the button on top of the canvas
w.place(x=100, y=20)  # You can adjust these coordinates as needed

root.mainloop()
