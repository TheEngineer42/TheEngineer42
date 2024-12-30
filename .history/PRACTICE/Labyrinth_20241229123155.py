import tkinter
root = tkinter.Tk()

canvas = tkinter.Canvas(width = 700, height = 700)
canvas.pack()


for i in range (10,500,20):
    canvas.create_line(10,i,490,i)
    canvas.create_line(i,10,i,490)



for i in range(10,500,20):
    canvas.create_line(10,i,500,i)
    canvas.create_line(i,10,i,500)


root.mainloop()