from tkinter import*
root = Tk()
root.geometry("400x400")

def enter_leave(event):
    if event.type == '7':
        lab1.config(text="IN")

    else:
        lab1.config(text="OUT")

    


lab1 = Label(root, height=10, width =15, bg = 'white', text="")
lab1.pack()

lab1.bind("<Enter>", enter_leave)
lab1.bind("<Leave>", enter_leave)


root.mainloop()