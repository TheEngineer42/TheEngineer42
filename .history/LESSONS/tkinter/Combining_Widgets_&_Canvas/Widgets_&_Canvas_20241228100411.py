from tkinter import*
root = Tk()
root.geometry('500x500')

canvas = Canvas(root, width = 200, height = 200, bg = 'lightblue')
canvas.pack(LEFT)

root.create_rectangle()

root.mainloop()