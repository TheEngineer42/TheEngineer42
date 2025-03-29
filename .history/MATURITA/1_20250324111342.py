import random

a = int(input('write number of throws: '))

for i in range(a):
    n = random.randint(1,6)

    ones = []
    twos = []
    threes = []
    fours = []
    fives = []
    sixs = []

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
        
    
    
      


    
    

