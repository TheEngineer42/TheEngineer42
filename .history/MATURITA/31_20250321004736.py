from tkinter import*
import random
root = Tk()

canvas = Canvas(root, height = 500, width = 500)
canvas.pack()

x = random.randint(0,500)
y = random.randint(0,500)

canvas.create_text(x,y, text = "%", font = 'Calibri, 18')



def plot():
    for i in range(0,500,23):
        canvas.create_rectangle(i,0,i+20,500, fill = 'red', outline = 'white')

    canvas.create_rectangle(0,50,500,100, fill = 'red')
    canvas.create_rectangle(0,400,500,450, fill = 'red')


plot()

root.mainloop()