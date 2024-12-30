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
                 height = 150, # is not working because 'pack' automatically adjusts
                 width = 300,   # the size of the widget to its content
                 highlightbackground = 'orange',
                 highlightcolor = 'red',
                 highlightthickness = '3',
                 padx = 20,
                 pady = 20
                 )


l1 = Label(top, text = '1', width = 7, height = 4, bg = 'skyblue')


top.focus_set()# --> if you want to see the highlightcolor
top.pack_propagate(False) # 
top.pack()
l1.pack()


root.mainloop()