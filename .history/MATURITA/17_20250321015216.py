from tkinter import*
root = Tk()
root.geometry('100x200')

canvas = Canvas(root, height=200, width=100)
canvas.pack()


canvas.create_rectangle(0,0,100,200, fill = 'black')

for i in range(0,200,10):
    canvas.create_text(15,i+10, text = i, fill = 'white', font = 'Calibrin, 18')




root.mainloop()