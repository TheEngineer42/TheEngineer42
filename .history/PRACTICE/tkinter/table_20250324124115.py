import random
from tkinter import*
root = Tk()

canvas = Canvas(root, width = 500 , height = 500) 
canvas.pack()


global cislo
cislo = 11

for j in range(0,10):
    cislo -= 1
    canvas.create_text(10,j*50, text = cislo, fill = 'black', font = "Calibri, 12" )
   

root.mainloop()


