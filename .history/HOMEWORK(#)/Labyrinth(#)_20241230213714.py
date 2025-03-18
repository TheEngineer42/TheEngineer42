from tkinter import*
root = Tk()
root.geometry('700x700')
import random

canvas = Canvas(root, height = 500, width = 500, bg = 'skyblue')
canvas.pack(expand = 1)# same as expand = True



for i in range(0,520,20):
    canvas.create_line(i,0,i,500)
    canvas.create_line(0,i,500,i)

#drawing borders manually because they are not visible
canvas.create_line(2,0,2,500)
canvas.create_line(0,2,500,2)

#extracting horizontal pieces
for _ in range(1000):
    n = random.randrange(0,521,20)
    m = random.randrange(0,521,20) 
    canvas.create_line(n+1,m,n+20,m, fill = 'skyblue') #n+1 so that other lines are not damaged

#extracting vertical pieces
for _ in range(1000):
    k = random.randrange(0,521,20)
    l = random.randrange(0,521,20) 
    canvas.create_line(l,k+1,l,k+20, fill = 'skyblue')

root.mainloop()