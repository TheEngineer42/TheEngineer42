from tkinter import*
root = Tk()
root.geometry('500x550')
import random

colors = ['blue','red','green','orange','yellow','purple','black','pink','white']

canvas = Canvas(root, height=500, width=500)
canvas.pack()

open("coordinates.txt", "w").close()


def drawing(event):
    color = random.choice(colors)
    a = event.x
    b = event.y
    canvas.create_oval(a-10,b-10,a+10,b+10, fill = color)
    

    file = open("kreslenie.txt", 'a')
    file.write(f"{a-10} \n{b-10}\n")
    file.close()

    with open("kreslenie.txt", "r") as file:
        content = file.read()
        print(content)

    

def erasing(event):
    #canvas.create_rectangle(0,0,500,500, fill = 'white')
    #canvas.pack()

    canvas.delete("all")
    with open("kreslenie.txt", "w") as file:
        pass #will delete everything


button = Button(root, text = 'delete data', font = "Calibri, 18")
button.pack()
button.bind("<Button-1>",erasing)




canvas.bind("<Button-1>",drawing)
root.bind('<space>', erasing)




root.mainloop()