from tkinter import*
root = Tk()
root.geometry('500x500')


n = str(input('enter one word: '))
empty = []

for i in range(len(n)):
    if n[i] == " ":
        empty.append(" ")
    else: 
        new = ord(n[i])+3
        empty.append(chr(new))

label = Label(root, text = f"{n}\n{empty}", font = "Calibri, 18")
label.pack()
    

print("".join(empty))

