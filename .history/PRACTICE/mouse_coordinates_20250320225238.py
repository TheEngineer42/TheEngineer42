from tkinter import*
root = Tk()
root.geometry('300x300')

def show_coordinates(event):
    label.confi(text="x:", event.x)



label = Label(root, text="Click anywhere", font = 'Calibri, 18')
label.pack()