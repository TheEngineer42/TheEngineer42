my_list = list(range(2,12,2))
print(my_list)

print(my_list[0])   #2
print(my_list[1])   #4
print(my_list[2])   #6
print(my_list[3])   #8
print(my_list[4])   #10


print()

print(my_list[-1])  #10
print(my_list[-2])  #8
print(my_list[-3])  #6
print(my_list[-4])  #4
print(my_list[-5])  #2


print(my_list[1:3]) #[4, 6]
print(my_list[2:5]) #[6, 8, 10]

fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
fruits[2:5] #creates a new one, old one stays the same
print(fruits) #['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']

print(fruits[2:5]) #['banana', 'cherry', 'kiwi']
