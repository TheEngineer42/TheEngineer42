import random
from tkinter import*
root = Tk()
root.geometry('500x500')
canvas = Canvas(root, width = 500 , height = 500) 
canvas.pack()


for j in range(0,10):
    canvas.create_text(15,j*50, text = j, fill = 'black', font = 'Calibri, 10')
    

