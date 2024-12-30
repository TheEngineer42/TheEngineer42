from tkinter import*
root = Tk()
root.geometry('500x500')

w = Button(root, text = 'Click me!', height = 5, width = 15, bg = 'skyblue')

w.pack(expand = 1) #puts button into middle
root.mainloop()


