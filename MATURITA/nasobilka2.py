from tkinter import*
root = Tk()
import random


label = Label(root, text = '')

for i in range(1,11):
    for j in range(1,11):
        print('%4d' %(i*j),end='')
    print()

a = random.randint(1,11)
b = random.randint(1,11)
c=a*b

print(f"{a}, * {b}, =")
z = int(input())

if z == c:
    print('spraven')

else:
    print('nespravne')