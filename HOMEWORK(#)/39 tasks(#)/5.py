"""
Given a string. Show the numbers of characters that 
match the last character of the string.

"""

s = str(input('write smth: '))

print(s[-1])
print(s.count(s[-1])-1)
