"""
Given a string, determine whether 
the string contains only characters 'a', 'b', 'c' or not.
"""
s = 't'
x = 0

for i in range(len(s)):
    if ord(s[i]) == ord('a') or ord(s[i]) == ord('b') or ord(s[i]) == ord('c'):
        x += 1

print('////////////////////')

if x == len(s):
    print("string contains only 'a', 'b', 'c'")
else:
    print("string DOESNT contain only 'a', 'b', 'c'" )


### redo with "in" thing


