from tkinter import *

root = Tk()
root.geometry('200x700')

# Create the black panel as a container
black_panel = Label(root, height=1, width=1, bg='black')
black_panel.pack(expand=1, fill='both')  # Fill the space

# Create the Canvas as a child of the black panel
red_panel = Canvas(black_panel, width =50, height= 20, bg='red')  # A red rectangle Canvas
red_panel.pack(expand=1, anchor = N)  # Place it inside the black panel

# Buttons (outside the black panel)
button1 = Button(root, height=2, width=10, text='Gas')
button2 = Button(root, height=2, width=10, text='Break')

button1.pack()
button2.pack()

root.mainloop()
