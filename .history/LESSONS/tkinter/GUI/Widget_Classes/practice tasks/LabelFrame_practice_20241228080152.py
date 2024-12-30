from tkinter import*
root = Tk()
root.geometry=('500x500')

top = LabelFrame(root, text = 'this is text of LabelFrame')
bot = LabelFrame(root)

l1 = Label(root, width = 7, height = 4, bg = 'skyblue')

top.pack()
l1.pack()
root.mainloop()