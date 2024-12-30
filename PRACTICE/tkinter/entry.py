#import tkinter

from tkinter import*
#import tkinter as tk



root=Tk()


def show1():
    lab['text'] = ent.get()
   
root=Tk()

ent = Entry(root, bg = 'red', bd = 5, font = ('Arial', 18)) #what you write as a user
but = Button(root, bg='white',text='run',font =('Arial',18), command = show1) #command -> your button will execute respective code in our def show1
lab = Label(root, font=('Arial', 18)) #upper red part



ent.pack()
but.pack()
lab.pack()



root.mainloop()
"""
Label1 = Label(root,
                 bg = 'red',
                 width = 30,
                 height = 15,
                 text = 'Mushroom soup',
                 font = ('Arial', 18))

Label1.pack()
root.mainloop()                
"""



"""
def change():
    but1['text'] = 'sorry'


root = Tk()

but1 = Button(root,
           bg = 'blue',
           width = 30,
           height = 10,
           text = 'hello',
           fg = 'green',
           activebackground = 'yellow',
           activeforeground = 'pink',
           command = change)

but1.pack()


root.mainloop()

"""