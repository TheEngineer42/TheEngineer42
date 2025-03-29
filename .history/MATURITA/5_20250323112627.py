from tkinter import*
root = Tk()
root.geometry('500x500')

canvas = Canvas(root, height=500, width=500)
canvas.create_oval(50,50,70,70)


def drawing(event):
    a = event.x
    b = event.y
    canvas.create_oval(a,b,a+50,b+50, fill = 'blue')





root.bind("<Button-1>",drawing)

root.mainloop()