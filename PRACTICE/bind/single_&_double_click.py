from tkinter import*
root = Tk()
root.geometry('500x500')


def single(event):
    button.config(text='Single click')

def double(event):
    button.config(text='double click')


button = Button(root, height=5, width=15, text= "click somewhere", font = "Calibri, 18")
button.pack()



button.bind("<Button-1>", single)
button.bind("<Double-Button-1>", double)

root.mainloop()