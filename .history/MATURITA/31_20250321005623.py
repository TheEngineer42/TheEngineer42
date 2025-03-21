from tkinter import*
import random
root = Tk()

canvas = Canvas(root, height = 500, width = 500)
canvas.pack()

x = random.randint(0,500)
y = random.randint(0,500)

canvas.create_text(x,y, text = "%", font = 'Calibri, 18')          #"%" random position



def plot():                                                        #making wall
    canvas.create_rectangle(0,50,500,75, fill = 'red')
    canvas.create_rectangle(0,425,500,450, fill = 'red')

    for i in range(0,500,23):
        canvas.create_rectangle(i,0,i+20,500, fill = 'red', outline = 'white')

    
root.after(3000, plot)                                             #waiting for 3 sec, to activate

def game(event):
    if x <= event.x <= x+20:
        label = Label(text='you won')
        label.pack()
    
    else:
        label = Label(text='you lost')
        label.pack()

root.bind("<Button-1>",game)

root.mainloop()