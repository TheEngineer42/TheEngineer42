from tkinter import*
root = Tk()
root.geometry('200x500')

canvas = Canvas(root, height=500, width=200)
canvas.pack()


canvas.create_rectangle(0,0,200,500, fill = 'black')

for i in range(0,500,25):
    for n in range(0,200,10):
        canvas.create_text(15,i+10, text = n, fill = 'white', font = 'Calibrin, 18')




root.mainloop()