"""
Given a string. Output the first, 
last and middle (if any) characters.
"""

s = ("apples and pineapple")
print("s's length:", len(s))
print('first symbol: ', s[0])
print('last symbol: ', s[-1]) #s[20] is not effective

middle_symbol_index = ((len(s))//2)

if s[middle_symbol_index] == " ":
    print("middle symbol is nonexistent")

else:
    print('middle symbol: ', s[middle_symbol_index])



### can be improved to when user inputs, odd and even...