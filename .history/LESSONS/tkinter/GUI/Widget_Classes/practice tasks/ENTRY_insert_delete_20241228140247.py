from tkinter import*
root = Tk()
root.geometry('500x500')

#........................................
#.................INSERT.................
#........................................

e1 = Entry(root, font = 'Calibri 30')
e1.pack()

e2 = Entry(root, font = 'Calibri 30', justify = 'right') #puts text to the right
e2.pack()


e1.insert(0, 'text') ########

e2.insert(0, 'number') ######




#........................................
#.................DELETE.................
#........................................

m1 = Entry(root, font = 'Calibri 30')

l= Button(root, text = 'Click me to delete text', height = 20,width =20)
l.pack()

root.mainloop()