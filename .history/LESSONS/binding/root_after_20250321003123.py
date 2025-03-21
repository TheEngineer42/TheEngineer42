from tkinter import*
root = Tk()
root.geometry('500x500')

def update():
    label.config(text = "Updated after 3 seconds")

label = Label(root, text = 'Waiting for updates...')
label.pack()

root.after(3000, update)
root.mainloop()