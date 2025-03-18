from tkinter import*
root = Tk()

root.geometry("300x300")

def track_position(event):
    label.config(text= f"x:{event.x}, y:{event.y}")

label = Label(root, text = "move your mouse", font = ("Calibri", 14))
label.pack()

root.bind("<Motion>", track_position)
root.mainloop()