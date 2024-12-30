"""
Given a string. Print the first three characters and the 
last three characters if the string length is greater than 5. Otherwise, 
print the first character as 
many times as the string length.

"""

s = str(input('write a string: '))
  

if len(s) > 5:
    print(s[0:3])
    print(s[-3:])    #dont use [-3:-1], it wont include last char

else:
    print(s[0]*len(s))


###can i do it wiht for?

