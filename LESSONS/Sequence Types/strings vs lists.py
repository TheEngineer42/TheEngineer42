'''
String: a sequence of characters used to represent text
'hello', 'i am typing'
'''

my_string = 'hello'

'''
List: a collection/sequence of items, which can be of any data type(strings, integers,
floats or even other lists) (list can contain items of different data types)
[1, 2, 3, 4], ['apple', 1, 2, 'ship']
'''

my_list = [1, 2, 3, 4]


'''
strings: 
- immutable (once its created, it's characters cannot be changed)
- when we perform operations on strings, python creates and returns a new 
  string instead of modifyin the original one

lists: 
- mutable(you can modify, add, remove elements after the list has been created)
- you can change them in place
- when we use methods that modify list like(insert(), append(), remove()),
  we alter the original list, without creating a new one. Therefore as a resul,
  they return none.
'''


my_list = [1, 2, 3, 4]
my_list[0] = 10

"""
COMMON OPERATIONS
STRING: concatenation(+), repetition(*), .upper(), .lower(), .find()...
LIST: .append(), .insert(), .remove()...

"""

"""
ACCESS ELEMENTS -> index []
- in STRING you can acces individual characters
- in LIST you can acces elements

"""

string = ('hello')
print(string[1])

list = [10, 20, 30]
print(list[0])

"""
ITERATION
"""
for char in 'hello':
    print(char)


for item in [1, 2, 3]:
    print(item)