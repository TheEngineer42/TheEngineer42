from tkinter import*
root = Tk()
root.geometry('200x500')

canvas = Canvas(root, height=500, width=200)
canvas.pack()


canvas.create_rectangle(0,0,200,500, fill = 'black')

for i in range(0,200,10):
    canvas.create_text(10,i+15, text = i, fill = 'white', font = 'Calibrin, 10')




root.mainloop()