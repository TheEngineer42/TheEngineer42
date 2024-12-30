from tkinter import*

root = Tk()
root.geometry('400x700')

black_panel = Label(root, height = 35, width = 25, bg = 'black')
red_panel = Canvas(root, width= 80, height = 30, bg = 'red')



button1 = Button(root, height = 2, width= 10, text = 'Gas')
button2 = Button(root, height = 2, width= 10, text = 'Break')


black_panel.pack(expand = 1)
red_panel.pack(expand=1)

button1.pack(expand = 1)
button2.pack(expand = 1)



root.mainloop()