import tkinter 

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width = 2000, height = 2000)
canvas.pack()

canvas.create_oval(50,50,280,220)#head
canvas.create_polygon(40,500,75,220,255,220,290,500, fill = 'white')#body
canvas.create_oval(100,320,160,495)

root.mainloop()