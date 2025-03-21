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

    
root.after(2000, plot)                                             #waiting for 3 sec, to activate

def game(event):
    if x <= event.x <= x+25:
        label = Label(text='you won', height= 10, width = 15, font = 'Calibri, 18')
        label.place(x=200,y=200)
    
    else:
        label = Label(text='you lost', height= 10, width = 15, font = 'Calibri, 18')
        label.place(x=250,y=250)

root.bind("<Button-1>",game)

root.mainloop()