from tkinter import*
root = Tk()
root.geometry('500x500')

top = LabelFrame(root, 
                 text = 'this is text of LabelFrame',
                 fg = 'purple',
                 bg = 'skyblue',
                 bd = '7',
                 cursor = 'arrow',
                 relief = 'sunken',
                 height = 7,
                 width = 7
                 )


l1 = Label(top, text = '1', width = 7, height = 4, bg = 'skyblue')


top.pack()
l1.pack()


root.mainloop()