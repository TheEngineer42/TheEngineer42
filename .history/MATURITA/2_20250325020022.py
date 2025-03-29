with open("prihlaseni.txt", 'w') as file:
    file.write('Martina \n16\nRoman\n14\nAdam\n15\nJana\n14\nMaria\n15\nErik\n15')



with open("prihlaseni.txt") as file:
    content = file.readlines() #counts amount of line in file

for line in content:
    print(line.strip())

print(f"pocet prihlasenych osob: {len(content)//2}")

sum = 0

for i in range (1,len(content),2):
    sum += int(content[i].strip())

a = len
print(f"priemerny vek: {sum//(len(content)//2)}")

#check every second line
#convert age to integer
#if teh age is less than 15:
#write word on previous line
under15 = 0
over15 = 0 


for i in range(1,len(content),2):
    age = int(content[i].strip())
    if age <15:
        under15 += 1

    elif age>= 15:
        over15 += 1

print(f'pocet tich co maju pod 15 je: {under15}') 
print(f'pocet tich co maju nad 15 je: {over15}') 

price = 100
print(f"Vasa cena je {price*over15+(price//2)*under15}")
