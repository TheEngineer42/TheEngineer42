from tkinter import*
root = Tk()
root.geometry('500x500')


def single(event):
    button.config(height=20, width=30, text='Single click')

def double(event):
    button.config(text='double click')


button = Button(root, text= "click somewhere")
button.pack()



root.bind("<Button-1>", single)
root.bind("Double-Button-1", double)

root.mainloop()