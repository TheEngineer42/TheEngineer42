from tkinter import*
root = Tk()
root.geometry('500x500')




lab = Label(root, text="Hi, click the button to see what happens", font='Calibri, 15')

button=Button(root,text="click me, to add number", font='Calibri, 15')
button.pack()



root.mainloop()