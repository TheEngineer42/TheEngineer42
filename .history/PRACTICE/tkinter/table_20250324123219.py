import random
from tkinter import*
root = Tk()

canvas = Canvas(root, width = 500 , height = 500) 
canvas.pack()



for j in range(0,10):
    canvas.create_text(10,j*50, text = j, fill = 'black', font = "Calibri, 15" )
   

root.mainloop()


