from tkinter import*
root = Tk()
root.geometry('500x500')

canvas = Canvas(root, height=500, width=500)
canvas.create_oval(50,50,70,70)
canvas.pack()


def drawing(event):
    a = event.x
    b = event.y
    canvas.create_oval(a-20,b-20,a,b, fill = 'blue')
    canvas.pack()





root.bind("<Button-1>",drawing)

root.mainloop()