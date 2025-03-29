from tkinter import*
root = Tk()
root.geometry('500x500')

entry = Entry(root, font = "Calibri, 18")
entry.pack()

n = entry.get()
empty = []

def main(event):
    for i in range(len(n)):
        if n[i] == " ":
            empty.append(" ")
        else: 
            new = ord(n[i])+3
            empty.append(chr(new))

entry.bind("<Return>", main)           

label = Label(root, text = f"Povodny text: {n}\n Zasifrovany text: {"".join(empty)}", font = "Calibri, 18")
label.pack(expand = 1)

button = Button(root, text = "clean", font = "Calibri, 18")




    


root.mainloop()
