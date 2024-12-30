from tkinter import*
root = Tk()
root.geometry('500x500')

canvas = Canvas(root, width = 200, height = 200, bg = 'lightblue')
canvas.pack(side = TOP, anchor = W)

canvas.create_rectangle(20,20,100,70, fill = 'blue')



root.mainloop()