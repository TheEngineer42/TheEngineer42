n = str(input('enter one word: '))


for i in range(len(n)):
    new = ord(n[i])+3

    empty = []
    empty.append(chr(new))
    
print("".join(empty))

    
