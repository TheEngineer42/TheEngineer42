from tkinter import *

root = Tk()
root.geometry('400x400')

# Background label (bottom layer)
background_label = Label(root, bg="black", fg="white", width=30, height=10)
background_label.pack(expand=1, fill='both')  # Fill the entire space

# Foreground label (top layer)
foreground_label = Label(root, height = 10, width = 30, bg="red", fg="white")
foreground_label.place(relx=0.5, rely=0.5, anchor= N)  # Center it on the background label

root.mainloop()
