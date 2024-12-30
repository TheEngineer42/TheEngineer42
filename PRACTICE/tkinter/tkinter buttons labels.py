from tkinter import*




root=Tk()

Label1 = Label(root,
                 bg = 'red',
                 width = 20,
                 height = 15,
                 text = 'Mushroom soup',
                 font = ('Arial', 18))

Label2 = Label(root, bg = 'blue', width = 20, height = 10, text = 'Apple soup', font = ('arial', 15))


button1 = Button(root, bg = 'red', width = 25, height = 30, activebackground = 'yellow', activeforeground = 'blue')



               
Label1.pack()
Label2.pack()
button1.pack()

               
root.mainloop()