from tkinter import*
root = Tk()
root.geometry('500x500')

def show(event):
    label.config(text=f'x:{event.x}, y:{event.y}')


label = Label(root, text = "move mouse", font = "Calibri, 18")
label.pack()

root.bind("<Motion>", show)

root.mainloop()

