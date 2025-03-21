from tkinter import*
root = Tk()
root.geometry('300x300')

def show_coordinates(event):
    label.confi(text=f'X:{event.x}, Y:{event.y}')



label = Label(root, text="Click anywhere", font = 'Calibri, 18')
label.pack()

root.bind("Button-1", show_coordinates)

root.mainloop()