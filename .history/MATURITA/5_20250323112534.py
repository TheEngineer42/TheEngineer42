from tkinter import*
root = Tk()
root.geometry('500x500')

canvas = Canvas(root)

def drawing(event):
    a = event.x
    b = event.y
    canvas.create_oval(a,b,a+50,b+50, fill = 'blue')





root.bind("<Button-1>",drawing)

root.mainloop()