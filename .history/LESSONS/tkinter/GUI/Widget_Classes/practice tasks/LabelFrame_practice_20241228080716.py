from tkinter import*
root = Tk()
root.geometry=('500x500')

top = LabelFrame(root, 
                 text = 'this is text of LabelFrame',
                 fg = 'purple'
                 )


l1 = Label(top, text = '1', width = 7, height = 4, bg = 'skyblue')


top.pack()
l1.pack()


root.mainloop()