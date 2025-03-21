from tkinter import*
root = Tk()
root.geometry('300x300')

def show(event):
    label.config(text=f"X:{event.x}, Y:{event.y}")


label = Label(root, text="Click anywhere")
label.pack()

root.bind('<Button-1>', show)



root.mainloop()