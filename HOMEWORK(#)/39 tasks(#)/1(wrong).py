"""
Given a string. Print it 3 times separated 
by commas and show the number 
of characters in it.

"""

s = "this is a string"
list = 3 * [s]
print(list)
print("Number of charcters: ", len(list)) # this is wrong, you will get 3 as
#answer because you made a list out of it

"""
[3*s] - single long string, ONE item
3*s - ONE item
3 * [s] - three copies of "s"

sep - is used between MULTIPLE arguments

"""
