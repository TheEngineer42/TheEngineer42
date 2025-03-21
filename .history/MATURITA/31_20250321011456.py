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

    
root.after(1000, plot)                                             #waiting for 3 sec, to activate

def game(event):
    if event.x < x:
        label = Label(text='go right \n --> \n :(', height= 6, width = 15, font = 'Calibri, 18')
        label.place(x=150,y=150)  

    elif event.x > x+20:
        label = Label(text='go left \n <--\n :(', height= 6, width = 15, font = 'Calibri, 18')
        label.place(x=150,y=150)     

    elif x <= event.x <= x+25:
        label = Label(text='!!!YOU WON!!!', height= 6, width = 15, font = 'Calibri, 18')
        label.place(x=150,y=150)
    
    else:
        label = Label(text='you lost', height= 6, width = 15, font = 'Calibri, 18')
        label.place(x=150,y=150)

    def label_delete():
        label.destroy()

    root.after(600, label_delete)

    







root.bind("<Button-1>",game)

root.mainloop()