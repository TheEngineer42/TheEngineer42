"""
[expression for item in iterable]

"""


numbers = [i for i in range (10)]
print(numbers)              #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zeros = [0 for i in range (10)] #Create a list of ten elements, 
                                #where each element is the number 0.
print(zeros)                #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

cubes = [i**3 for i in range(10,21)]
print(cubes)                #[1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000]
                            #this thing in here created LIST

for i in range(10,21):      #this thing in here prints each cube but in a column
    print(i**3)



chars = [c for c in 'abcdefg'] 
print(chars)                #['a', 'b', 'c', 'd', 'e', 'f', 'g']
#Explanation: abcdefg is a string. 
#String is iretable(going through one character at a time)
# for c in 'abcdefg':
#    print(c)
# 
# this will print:
#a
#b
#c
#d
#e
#f
#g
#
# ----> it looped over each character
# - so in first iteration c is assigned 'a'
# - in second iteration c is assigned 'b'
#
#
#
#
# chars = [c for c in 'abcdefg'] c(first one) is 
# the value you are adding to the list
#
#So, this means:
#
#Take each character (c) from 'abcdefg'.
#Add it to the list.

# [c for c in 'abcdefg'] = [new_item for item in iterable]

#1. 'item' is each element from the 'iterable'(like a character in a string
#2. 'new item' is what you want to collect and store in the new list

#the 'iterable' is 'abcdefg'
#c is the variable used in the loop
#each value of 'c'(like 'a','b', etc.) is directly collected into the list 'chars'






