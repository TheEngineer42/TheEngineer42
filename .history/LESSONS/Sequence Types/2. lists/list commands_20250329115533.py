"""
COMMANDS:
insert, index, remove, pop, insert, count, reverse, clear, len, copy
sum, min, max, append, extend, del, len
"""

list = ['Thomas', 'Jack', 'Tony']
list.insert(0, 'Steve')
list.insert(5, "David")
print(list)                 #['Steve', 'Thomas', 'Jack', 'Tony', 'David']

position_of_Steve = list.index('Steve')
print(position_of_Steve)    #0

position_of_Tony = list.index('Tony')
print(position_of_Tony)     #3


list.remove('Jack')
print(list)                 #['Steve', 'Thomas', 'Tony', 'David']

removed_item = list.pop(1)
print(removed_item)         #Thomas
print(list)                 #['Steve', 'Tony', 'David']


list.insert(1, "Adam")
list.insert(5, "Tony")
print(list)                 #['Steve', 'Adam', 'Tony', 'David', 'Tony']

amount_of_Steve = list.count("Steve")
amount_of_Tony = list.count("Tony")
print(amount_of_Steve, amount_of_Tony) #1 2

print(list)                 #['Steve', 'Adam', 'Tony', 'David', 'Tony']

list.reverse()
print(list)                 #['Tony', 'David', 'Tony', 'Adam', 'Steve']

list_copy = list.copy()     #['Tony', 'David', 'Tony', 'Adam', 'Steve']
print(list_copy)

list.clear()
print(list)                 #[]


print(len(list))            #0



"""
/////////////////////
SUM, MIN, MAX
/////////////////////
"""

numbers = [1,2,3,4,5,6,7,8,9,10]
print('sum of all numbers: ', sum(numbers)) #sum of all numbers:  55
print('min. element = ', min(numbers))      #1
print('max. element = ', max(numbers))      #10




"""
/////////////////////
APPEND, EXTEND + difference
/////////////////////
"""


my_numbers = [1,1,2,3,5,8,13]
my_numbers.append(21)

print(my_numbers)    #[1, 1, 2, 3, 5, 8, 13, 21]

my_numbers.append(34)
print(my_numbers)    #[1, 1, 2, 3, 5, 8, 13, 21, 34]


new_numbers=[0,2,4,6,8,10]
odds = [1,3,5,7]
new_numbers.extend(odds)
print(new_numbers) #[0, 2, 4, 6, 8, 10, 1, 3, 5, 7]


"""
difference between extend and append
"""
words1 = ['truth', 'justice', 'honor']
words2 = ['truth', 'justice', 'honor']

words1.append('temptation')
words2.extend('temptation')

print(words1) #['truth', 'justice', 'honor', 'temptation']
print(words2) #['truth', 'justice', 'honor', 't', 'e', 'm', 'p', 't', 'a', 't', 'i', 'o', 'n']

"""
del, len
"""

numeralia = [1,2,3,4,5,6,7,8,9]
del numeralia[5]
print(numeralia)  #[1, 2, 3, 4, 5, 7, 8, 9]

numeralia1 = [1,2,3,4,5,6,7,8,9]
del numeralia1[2:7]
print(numeralia1) #[1, 2, 8, 9]

votes = ['y','n','y','n','n','n','y','n']
amount_of_votes = len(votes)
print(f"amont of votes: {amount_of_votes}")