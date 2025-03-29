n = str(input('enter one word: '))
empty = []

for i in range(len(n)):
    new = ord(n[i])+3
    empty.append(chr(new))
    

print("".join(empty))
a = ("".join(empty))
a.replace('#',' ',1)
print(a)
