from tkinter import*
from tkinter import PhotoImage #PhotoImage is class in tkinter

#PhotoImage(used to handle images), allows to load files like .png, .gif


root = Tk()
earth = PhotoImage(file="C:\\Users\\vkash\\OneDrive\\Obrázky\\Screenshot 2024-11-12 223433.png")

label = Label(root, image=earth)
label.pack()

root.mainloop()