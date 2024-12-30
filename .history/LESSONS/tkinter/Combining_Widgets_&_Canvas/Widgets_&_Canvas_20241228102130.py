from tkinter import*
root = Tk()
root.geometry('500x500')

canvas = Canvas(root, width = 200, height = 200, bg = 'lightblue')
canvas.pack(side = TOP, anchor = W)

canvas.create_rectangle(20,20,100,70, fill = 'blue')

w = Button(root, text = 'Button', bg = 'skyblue', height = 5, width = 15)


w.place(x = 50, y = 60)
root.mainloop()