n = str(input('enter one word: '))
empty = []

for i in range(len(n)):
    new = ord(n[i])+3
    empty.append(chr(new))
    

print("".join(empty))
n = ("".join(empty))
n.replace('#',' ',1)
