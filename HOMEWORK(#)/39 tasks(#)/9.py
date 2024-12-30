"""
Given two strings. Print the longer 
string as many times as the number of 
characters by which the strings differ.

"""

s1 = input('write down a string 1.: ')
s2 = input('write down a string 2.: ')

print('length of s1 = ',len(s1))
print('length of s2 = ',len(s2))



if (len(s1) -  len(s2)) > 0:
    print(s1*(len(s1) -  len(s2)))

else:
    print(s1*(len(s2) -  len(s1)))


