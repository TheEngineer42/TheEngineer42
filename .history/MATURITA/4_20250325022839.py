n = str(input('enter one word: '))
empty = []

for i in range(len(n)):
    new = ord(n[i])+3
    empty.append(chr(new))
    
nn = ("".join(empty))
nn.replace('#'," ", all)      
