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
print(f"priemerny vek{sum//(len(content)//2)}")    