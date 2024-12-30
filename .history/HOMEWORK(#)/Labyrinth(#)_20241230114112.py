from tkinter import*
root = Tk()
root.geometry('700x700')

canvas = Canvas(root, height = 500, width = 500, bg = 'skyblue')
canvas.pack(expand = 1)# same as expand = True

for i in range(0,500,20):
    canvas.create_line(i,0,i,500)

root.mainloop()