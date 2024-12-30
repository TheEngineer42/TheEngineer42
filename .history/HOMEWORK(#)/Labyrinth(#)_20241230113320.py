from tkinter import*
root = Tk()
root.geometry('700x700')

canvas = Canvas(root, height = 500, width = 500, bg = 'skyblue')
canvas.pack(expand = 1)# same as expand = True

for i in range(100,600,20):
    canvas.create_line(i,100,i,600)

root.mainloop()