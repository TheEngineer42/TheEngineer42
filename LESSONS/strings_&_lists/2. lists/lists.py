s = [11, 67, 'abc', 3.14, 42, 1968]


print(s[0])
print(s[1])
print(s[-1])
print(s[-6])

#sequantial approach[start:end:step]

print(s[:-1])   #[11, 67, 'abc', 3.14, 42]
print(s[1:-1])  #[67, 'abc', 3.14, 42]
print(s[1:3])   #[67, 'abc']
print(s[-3:-1]) #[3.14, 42]

print(s[-1:-3]) #[]
print(s[::2]) #[11, 'abc', 42]
print(s[:3]) #[11, 67, 'abc']
print(s[4:]) #[42, 1968]

#print(s[]) -> error
print(s[:]) #[11, 67, 'abc', 3.14, 42, 1968]

"""
////////////////
DELETING ELEMENTS
////////////////

"""

del s[3:5]
print(s) # [11, 67, 'abc', 1968]


"""
////////////////
CHANGING ELEMENTS VIA ENTRY
////////////////

"""

s1 = [11, 67, 'abc', 3.14, 42, 1968]
s1[1:4] = ['hop', 9]
print(s1) # [11, 'hop', 9, 42, 1968]
