import random
from tkinter import*
root = Tk()

canvas = Canvas(root, width = 500 , height = 500) 
canvas.pack()



for j in range(10,0):
    canvas.create_text(10,j*50+10, text = j, fill = 'black', font = "Calibri, 12" )
   

root.mainloop()


