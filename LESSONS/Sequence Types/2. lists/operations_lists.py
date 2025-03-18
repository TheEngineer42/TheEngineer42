"""
OPERATIONS:
+,*, sum

"""


print([1,2,3,4]+[5,6,7,8]) #[1, 2, 3, 4, 5, 6, 7, 8]

print([7,8]*3)             #[7, 8, 7, 8, 7, 8]
print([0]*10)              #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]




s = 'abcdefg'
#s[1] = 'x' - wont be possible(object does not support item assignment)


numbers = [1,2,3,4,5,6,7]
numbers[1] = 101
print(numbers) #[1, 101, 3, 4, 5, 6, 7]
 
