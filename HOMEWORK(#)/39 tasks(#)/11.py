"""
Given a string. If its length is greater than 10, 
then leave only the first 6 characters in the string, 
otherwise add 'o' characters 
to the string until the length is 12.
"""

s = str(input("write a string: "))

if len(s) > 10:
    print(s[:6])

else:
    while len(s)<12:
        s += 'o'
    print(s)


