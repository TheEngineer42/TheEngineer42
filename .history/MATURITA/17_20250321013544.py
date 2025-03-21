from tkinter import*
root = Tk()
root.geometry('200x500')

canvas = Canvas(root, height=500, width=200)
canvas.create_rectangle(0,0,200,500, fill = 'black')
canvas.pack()




root.mainloop()