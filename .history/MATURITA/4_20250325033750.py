from tkinter import*
root = Tk()
root.geometry('500x500')

entry = Entry(root, font = "Calibri, 18")
entry.pack()




def main(event):
    empty = []
    n = str(entry.get())

    for i in range(len(n)):
        if n[i] == " ":
            empty.append(" ")
        else: 
            new = ord(n[i])+3
            empty.append(chr(new))

    global label        
    label = Label(root, text = f"Povodny text: {n}\n Zasifrovany text: {"".join(empty)}", font = "Calibri, 18")
    label.pack(expand = 1)

    with open("Ceasar.txt", "w") as file:
        file.write("".join(empty))
    
    with open("Ceasar.txt", "r") as file:
        content = file.read()
        print(content)



def clean():
    entry.delete(0, END)
    label.config(text='')
    


entry.bind("<Return>", main)           



button1 = Button(root, text = "delete", font = "Calibri, 18", command = clean)
button1.pack()

def delete(event):
    with open("Ceasar.txt", "w") as file:
        pass #will delete everything

button2 = Button(root, text = "delete data from file", font = "Calibri, 18", command = clean)
button2.pack()





button2.bind("<Button-1>", delete)

root.mainloop()
