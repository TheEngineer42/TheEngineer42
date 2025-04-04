"""
TUPLES

- data structure in python that allows to to store multiple values
  in a 'single variable'
- values cannot be changed once they are created


KEY POINTS:
- tuples are created by placing values inside parentheses (),
  separated by commas
- they can store values of different data types, such as numbers,
  strings or other tuples
- they are ordered, meaning the order of elements is maintained
  ( If you access the tuple, you'll get the elements in the 
    same order they were added.(20,0) = '20' will always be the first
    '0' will always be second)
- you can access tuple elements using indices, like in lists []

WHY USE TUPLES:
IMMUTABILITY --> cannot be modiefied after creation -> useful for storing
                 fixed data
PERFORMANCE  --> tuples are generally faster than lists, because of 
                 immutability
"""

my_tuple = (42, 72)

x, y = my_tuple

print(x)
print(y)

print(my_tuple[0])
print(my_tuple[1])