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
                 height = 20, # is not working because 'pack' automatically adjusts
                 width = 7,   # the size of the widget to its content
                 highlightbackground = 'orange',
                 highlightcolor = 'red',
                 highlightthickness = '3'
                 )


l1 = Label(top, text = '1', width = 7, height = 4, bg = 'skyblue')


top.pack_propagete(False)
l1.pack()


root.mainloop()