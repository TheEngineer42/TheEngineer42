from tkinter import*

root = Tk()
w = LabelFrame(root)

l1 = Label(w, text = 1)
l2 = Label(w, text = 2)

w.pack()
l1.pack(LEFT)
l2.pack(LEFT)
