from tkinter import*
root = Tk()
root.geometry('200x500')

canvas = Canvas(root, height=400, width=200)
canvas.pack()


canvas.create_rectangle(0,0,200,400, fill = 'black') #background

for i in range(0,400,20): #creating numbers and lines under hem
    canvas.create_text(15,i+10, text = i//2, fill = 'white', font = 'Calibrin, 10')
    canvas.create_line(10,i+16,40,i+16, fill = 'white')




root.mainloop()