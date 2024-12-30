s="python"
for i in range(len(s)):
    print(s[:i + 1], (len(s)-i)*'*', sep='')
    