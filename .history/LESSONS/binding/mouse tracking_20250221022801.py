from tkinter import *

def track_mouse(event):
    label.config(text=f"X: {event.x}, Y: {event.y}")

root = Tk()
root.geometry("500x500")

label = Label(root, text="Move your mouse", font=("Arial", 14))
label.pack(pady=20)

# Bind mouse motion event to track_mouse function
root.bind("<Motion>", track_mouse)

root.mainloop()