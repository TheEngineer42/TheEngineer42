from tkinter import*
root = Tk()
root.geometry('500x500')


def single(event):
    button.config(text='Single click')

def double(event):
    button.config(text='double click')


button = Button(root, height=10, width=30, text= "click somewhere", font = "Calibri, 18")
button.pack()



root.bind("<Button-1>", single)
root.bind("Double-Button-1", double)

root.mainloop()