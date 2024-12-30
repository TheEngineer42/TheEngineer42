import tkinter as tk
import random

root = tk.Tk()
root.geometry('500x500') #gives size of cube

random_amout = random.randrange(5,10)


for i in range (random_amout):
    frame = tk.Frame(root)
    frame = tk.LabelFrame(text = 'hi')
    l1 = tk.Label(width = random.randrange(0,9), height = 20, bg = 'lightgreen')
    l1.pack(expand = 1, side=tk.LEFT)
    frame.pack()



root.mainloop()



