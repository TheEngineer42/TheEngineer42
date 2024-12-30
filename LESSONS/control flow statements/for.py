for i in range(5):
    print(i)


"""
///////////////////
FOR LOOP
///////////////////

- allows you to iterate through sequence of elements(list,string,range...)
- executing code, one for each element

"""

for i in range(10):
    print('Hi')


for i in range(5,10):
    print('oi')


for i in range(10,20,2):
    print('bananas')

for i in range(9,2,-1):
    print(i)

print('/////////////////////////')

numbers = [0,1,2,3,4,5,6,7,8,9,10]
for i in range(len(numbers)):
    print(numbers[i])

for num in numbers:
    print(num)