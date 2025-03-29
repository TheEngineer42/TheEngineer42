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


global cislo
cislo = 11

for j in range(10):
    cislo -= 1
    canvas.create_text(10,j*40+80, text = cislo, fill = 'black', font = "Calibri, 12" )

for k in range(1,7):
    canvas.create_text(k*50, 480, text = k, fill = 'black', font = "Calibri, 12" ) 




if ones == 0:
    None
else:
    canvas.create_rectangle(35,500 - 47*ones,55,470)

if twos == 0:
    None
else:
    canvas.create_rectangle(80,500 - 47*twos,100,470)


if threes == 0:
    None
else:
    canvas.create_rectangle(130,500 - 47*threes,150,470)

if fours == 0:
    None
else:
    canvas.create_rectangle(190,500 - 47*fours,210,470)

if fives == 0:
    None
else:
    canvas.create_rectangle(235,500 - 47*fives,255,470)


if sixs == 0:
    None
else:
    canvas.create_rectangle(275,500 - 47*sixs,295,470)

root.mainloop()   


