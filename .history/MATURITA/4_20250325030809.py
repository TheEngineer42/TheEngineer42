from tkinter import*
root = Tk()
root.geometry('500x500')

entry = Entry(root, font = "Calibri, 18")
entry.pack()


empty = []

def main(event):
    n = str(entry.get())

    for i in range(len(n)):
        if n[i] == " ":
            empty.append(" ")
        else: 
            new = ord(n[i])+3
            empty.append(chr(new))
            
    label = Label(root, text = f"Povodny text: {n}\n Zasifrovany text: {"".join(empty)}", font = "Calibri, 18")
    label.pack(expand = 1)

entry.bind("<Return>", main)           



button = Button(root, text = "clean", font = "Calibri, 18")
button.pack()




    


root.mainloop()
