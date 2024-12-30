for char in 'hello':
    print(char)

print()

s = ('INFORMATIKA')

print(s[2])
print(s[5])
print(s[7])
#print(s[11])  - will be out of range
print(s[3:7])
print(s[6:7])
print(s[:3])
print(s[8:])

print()


l = ('12589346187552190')
print(l[2]+l[4:6]+l[8]+l[10]+l[14]+l[15:]) #59317190

k = [1,2,5,8,9,3,4,6,1,8,7,5,5,2,1,9,0]
print(k[2]+k[4:6]) #TypeError: unsupported operand type(s) for +:'int' and 'list'