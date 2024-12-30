"""
Given a text, find the greatest 
number of consecutive spaces in it.

"""

s = input('write sentence with many consecutive spaces: ')
empty = 0



for i in range(len(s)):
    if (i+1)*' ' in s:
        empty += 1

print('greatest umber of consecutive spaces is: ', empty)


