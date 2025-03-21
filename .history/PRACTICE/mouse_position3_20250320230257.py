from tkinter import*
root = Tk()
root.geometry('500x500')

def show(event):
    label.config(text=f"x:{event.x}, y:{event.y}")


label = Label(root, text="Calibri, 18")
label.pack()

root.bind("<Button-1>",show)


root.mainloop()