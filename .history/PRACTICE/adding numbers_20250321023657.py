from tkinter import*
root = Tk()
root.geometry('500x500')


def adding(event):
    x=0
    a=x
    x +=1
    
    lab.config(text =a)



button=Button(root,text="click me, to add number", font='Calibri, 15')
button.pack(pady = 10)

lab = Label(root, text="Hi, click the button to see what happens", font='Calibri, 15')
lab.pack()

button.bind("<Button-1>", adding)


root.mainloop()