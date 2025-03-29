from tkinter import*
import random
root = Tk()
root.geometry('500x600')
canvas = Canvas(root, bg = 'white', height= 500, width = 500)
canvas.pack()


colors = ['green', 'light green', 'dark green']
grass_blades = []

for i in range(0,500,10):
    y = random.randrange(20,500)
    canvas.create_rectangle(i,y,i+10,500, fill = random.choice(colors))
    grass_blades.append(y) #adding tuple



frame = Frame(root)
frame.pack()

i= 0

def growing():
    for element in grass_blades:
        canvas.create_rectangle(i,y,i+10,500)
        i += 10


grow = Button(frame, text = 'grow', font = 'Calibri, 14')

grow.pack(side = 'left', padx = 10, pady = 10)

def cutting():
    canvas.create_rectangle(0,0, 500,100, fill = 'white', outline = 'white')

cut = Button(frame, text = 'cut', font = 'Calibri, 14', command = cutting)
cut.pack(side = 'right', padx = 10, pady = 10)




root.mainloop()