from tkinter import*
root = Tk()
root.geometry("300x300")
root.title("METANIT.COM")

def single_click(event):
    button["text"] ="Single Click"



def double_click(event):
    button["text"] ="Double Click"

button = Button(text = "Click here!", width = '10', height = 3) 
button.pack()

button.bind("<Button-1>", single_click)
button.bind("<Button-2>", double_click)





root.mainloop()