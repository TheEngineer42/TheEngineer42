from tkinter import*
root = Tk()
root.geometry("300x300")
root.title("METANIT.COM")

def single_click(event):
    button["text"] ="Single Click"



def double_click(event):
    button["text"] ="Double Click"

button = ttk.Button(text = "Click here!") #gives every widget more modern look
button.pack()

button.bind("<Button-1>", single_click)
button.bind("<Button-2>", single_click)





root.mainloop()