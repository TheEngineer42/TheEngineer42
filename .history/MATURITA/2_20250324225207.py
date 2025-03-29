with open("prihlaseni.txt", 'w') as file:
    file.write('Martina \n 16\nRoman\n14\nAdam\n15\nJana\n14\nMaria\n15\nErik\n15')

with open("prihlaseni.txt") as file:
    content = file.read()
    print(content)