n = str(input('enter one word: '))
empty = []

for i in range(len(n)):
    if n[i] == " ":
        empty.append(" ")
    else: 
        new = ord(n[i])+3
        empty.append(chr(new))
    

print("".join(empty))

