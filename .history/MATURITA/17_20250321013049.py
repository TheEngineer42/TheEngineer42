from tkinter import*
root = Tk()
root.geometry('200x500')


canvas = Canvas(root)
canvas.create_rectangle(0,200,200,500, fill = 'black')
canvas.pack()



root.mainloop()