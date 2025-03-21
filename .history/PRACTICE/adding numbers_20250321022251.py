from tkinter import*
root = Tk()
root.geometry('500x500')






button=Button(root,text="click me, to add number", font='Calibri, 15')
button.pack(pady = 10)

lab = Label(root, text="Hi, click the button to see what happens", font='Calibri, 15')
lab.pack()



root.mainloop()