

from tkinter import*
root = Tk()
root.geometry('300x300')

label = Label(root, text="Click anywhere", font = 'Calibri, 18')
label.pack()


def show_coordinates(event):
    label.config(text=f'X:{event.x}, Y:{event.y}')





root.bind("Button-1", show_coordinates)

root.mainloop()