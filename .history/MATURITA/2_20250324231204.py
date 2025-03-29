with open("prihlaseni.txt", 'w') as file:
    file.write('Martina \n16\nRoman\n14\nAdam\n15\nJana\n14\nMaria\n15\nErik\n15')



with open("prihlaseni.txt") as file:
    content = file.readlines() #counts amount of line in file

for line in content:
    print(line.strip())

print(f"pocet prihlasenych osob: {len(content)//2}")