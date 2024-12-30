from tkinter import*
root = Tk()
root.geometry=('500x500')

top = LabelFrame(root, text = 'this is text of LabelFrame')
bot = LabelFrame(root)

l1 = Label(top, text = '1', width = 7, height = 4, bg = 'skyblue')
l2 = Label(bot, text = '2', width = 7, height = 4, bg = 'lightgreen')

top.pack()
l1.pack()
root.mainloop()