from tkinter import*
root = Tk()
root.geometry('1100x1100')

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
m1.pack()

def delete_text():
    m1.delete(0, END)

l= Button(root, text = 'Click me to delete text in 3rd entry', height =10,
          width =20, bg = 'sky blue', pady = 10, 
          command = delete_text) 

l.pack()

#........................................
#.................GET....................
#........................................

e3 = Entry(root, font = 'Calibri 30')
e3.pack()

def get_text():
    n = e3.get()
    print(n)

    l = Label(root, height = 5, width = 20, bg = 'salmon', text = n)
    l.place(x=340, y=490)


b = Button(root, text = 'get text from 4th entry', height = 5, width = 20,
           bg = 'lightgreen', command = get_text)
b.pack()


root.mainloop()