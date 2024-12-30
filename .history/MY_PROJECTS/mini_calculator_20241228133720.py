n = int(input('write down first number: '))
m = int(input('write down second number: '))

print('first number is', n)
print('second number is', m)

x = input('choose operation: +,-,/,*: ')

if x == '+':
    sum = n + m
    print(f'{n} + {m} = {sum}')

elif x == '-':
    sum = n - m
    print(f'{n} - {m} = {sum}')  

elif x == '/':
    sum = n/m
    print(f'{n} / {m} = {sum}') 

elif x == '*':
    sum = n*m
    print(f'{n} * {m} = {sum}') 

else:
    print('ERROR') #you can add bitmap here for ERROR





#add n to some list 
# n + m5
