from tkinter import*
root = Tk()
root.geometry()

button = Button(root, text= "click somewhere")
button.pack()

def single(event):
    button.config(text='Single click')

