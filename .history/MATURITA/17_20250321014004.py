from tkinter import*
root = Tk()
root.geometry('200x500')

canvas = Canvas(root, height=500, width=200)
canvas.pack()


canvas.create_rectangle(0,0,200,500, fill = 'black')

for i in range(0,500,20):
    canvas.create_text(0,i, text = 'a', fill = 'white')




root.mainloop()