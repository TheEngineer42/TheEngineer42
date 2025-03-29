import random
from tkinter import*
root = Tk()
root.geometry('500x500')
canvas = Canvas(root, width = 500 , height = 500) 
canvas.pack()

a = int(input('write number of throws: '))

ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixs = 0

for i in range(a):
    global n
    n = random.randint(1,6)



    if n==1:
        
        ones += 1
        print(f"{i+1}. hod. Uz {ones}-krat padlo cislo {n}")


    if n==2:
        twos += 1
        print(f"{i+1}. hod. Uz {twos}-krat padlo cislo {n}")

    if n==3:
        threes += 1
        print(f"{i+1}. hod. Uz {threes}-krat padlo cislo {n}")

    if n==4:
        fours += 1
        print(f"{i+1}. hod. Uz {fours}-krat padlo cislo {n}")

    if n==5:
        fives += 1
        print(f"{i+1}. hod. Uz {fives}-krat padlo cislo {n}")

    if n==6:
        sixs += 1
        print(f"{i+1}. hod. Uz {sixs}-krat padlo cislo {n}")
        
    
#for _ in range(n):
#   print(f"Cislo {n} padlo ")   

print(f"Cislo 1 padlo {ones}-krat")
print(f"Cislo 2 padlo {twos}-krat")
print(f"Cislo 3 padlo {threes}-krat")
print(f"Cislo 4 padlo {fours}-krat")
print(f"Cislo 5 padlo {fives}-krat")
print(f"Cislo 6 padlo {sixs}-krat")      


for j in range(0,10):
    canvas.create_text(10,j*50, text = j, fill = 'black', font = 'Calibri, 10')
    


canvas.create_text(15,i+10, text = i//2, fill = 'white', font = 'Calibri, 10')

