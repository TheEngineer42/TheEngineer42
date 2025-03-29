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
    c = random.choice(colors)
    canvas.create_rectangle(i,y,i+10,500, fill = c )
    grass_blades.append((i,y,c)) #adding tuple



frame = Frame(root)
frame.pack()



def growing():
    global grass_blades
    canvas.delete('all')

    new_grass = []
    for i,y,c in grass_blades:
        y_new = y - 10
        
        
        canvas.create_rectangle(i,y_new,i+10,500, fill = c)
        new_grass.append((i,y_new,c))

    grass_blades = new_grass 





grow = Button(frame, text = 'grow', font = 'Calibri, 14', command = growing)

grow.pack(side = 'left', padx = 10, pady = 10)

def cutting():
    global grass_blades
    
    new_grass = []
    
    for i,y,c in grass_blades:
            if y<50:
                y_new = 50
                canvas.create_rectangle(i,0,i+10,y_new, fill = 'white', outline = 'white')
                canvas.create_rectangle(i,y_new,i+10,500, fill = c)
                

    
    



cut = Button(frame, text = 'cut', font = 'Calibri, 14', command = cutting)
cut.pack(side = 'right', padx = 10, pady = 10)




root.mainloop()