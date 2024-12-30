from tkinter import*
root = Tk()
root.geometry('500x500')

top = LabelFrame(root, 
                 text = '1',
                 fg = 'purple',
                 bg = 'skyblue',
                 bd = '7',
                 cursor = 'arrow',
                 relief = 'sunken',
                 height = 150, # is not working because 'pack' automatically adjusts
                 width = 300,   # the size of the widget to its content
                 highlightbackground = 'orange',
                 highlightcolor = 'red',
                 highlightthickness = '3',
                 padx = 20,
                 pady = 20,
                 labelanchor = 'wn'
                 )


l1 = Label(top, text = '1', width = 7, height = 4, bg = 'skyblue')


top.focus_set()# --> if you want to see the highlightcolor
top.pack_propagate(False) #height and width wont take effect because pack automatically adjusts the
                          #size of the widget to its content
top.pack()
l1.pack()


root.mainloop()