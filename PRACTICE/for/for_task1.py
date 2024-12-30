s=('python')

for i in range(len(s)):
    print(((len(s)-i))*'*',s[:i + 1], sep='')