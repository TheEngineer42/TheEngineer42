from tkinter import*
root = Tk()
root.geometry('700x700')

canvas = Canvas(root, height = 500, width = 500, bg = 'skyblue')
canvas.pack(expand = 1)# same as expand = True



for i in range(0,520,20):
    canvas.create_line(i,0,i,500)
    canvas.create_line(0,i,500,i)

#drawing borders manually because they are not visible
canvas.create_line(1,0,1,500)
canvas.create_line(0,0,500,0)


root.mainloop()