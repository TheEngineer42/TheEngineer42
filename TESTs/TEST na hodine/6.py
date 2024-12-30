a = int(input('write down first number: '))
b = int(input('write down second number: '))
c = int(input('write down third number: '))

for i in range(c):
    print(a * '*')

print('\n')

for i in range(b):
    print(c * '+')

print('\n')

for i in range(a):
    print(b * '-')



