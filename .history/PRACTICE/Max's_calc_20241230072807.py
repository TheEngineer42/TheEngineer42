from tkinter import*
def plus():
    a1=int(ent1.get())
    b1=int(ent2.get())
    c1=a1+b1
    lab['text']=c1
def minus():
    a2=int(ent1.get())
    b2=int(ent2.get())
    c2=a2-b2
    lab['text']=c2
def multiply():
    a3=int(ent1.get())
    b3=int(ent2.get())
    c3=a3b3
    lab['text']=c3
def divide():
    a4=int(ent1.get())
    b4=int(ent2.get())
    c4=a4//b4
    lab['text']=c4
root=Tk()
ent1=Entry(root,
           bg='white',
           bd=5,
           font=('Arial',15),
           )

ent2=Entry(root,
           bg='white',
           bd=5,
           font=('Arial',15),
           )

but1=Button(root,
            bg='lightgray',
            text='+',
            font=('Arial',15),
            width=3,
            activebackground='gray',
            command=plus)

but2=Button(root,
            bg='lightgray',
            text='-',
            font=('Arial',15),
            width=3,
            activebackground='gray',
            command=minus)

but3=Button(root,
            bg='lightgray',
            text='',
            font=('Arial',15),
            width=3,
            activebackground='gray',
            command=multiply)

but4=Button(root,
            bg='lightgray',
            text='/',
            font=('Arial',15),
            width=3,
            activebackground='gray',
            command=divide)

lab=Label(root,font=('Arial',15))

ent1.pack()
ent2.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
lab.pack()

root.mainloop()