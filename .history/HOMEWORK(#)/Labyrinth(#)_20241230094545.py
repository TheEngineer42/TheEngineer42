from tkinter import*
root = Tk()
root.geometry('700x700')

canvas = Canvas(root, height = 500, width = 500, bg = 'skyblue')
canvas.pack(expand = 1)# same as expand = True

canvas.create_line(20,20, 100,100)

root.mainloop()