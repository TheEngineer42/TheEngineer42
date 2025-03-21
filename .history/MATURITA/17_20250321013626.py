from tkinter import*
root = Tk()
root.geometry('200x500')

canvas = Canvas(root)
canvas.pack()


canvas.create_rectangle(0,0,200,500, fill = 'black')





root.mainloop()