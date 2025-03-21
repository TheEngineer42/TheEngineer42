from tkinter import*
root = Tk()
root.geometry('300x300')

def show_coordinates(event):
    label.config(text=f"X: {event.x}, Y: {event.y}") #updates coordinates after click
    #config. is a method in Tkinter used to update the properties of
    #a widget after it has been created



label = Label(root, text = 'Click anywhere', font = ('Calibri, 14'))
label.pack()

root.bind("<Button-1>", show_coordinates) #when we click, our function activates

root.mainloop()