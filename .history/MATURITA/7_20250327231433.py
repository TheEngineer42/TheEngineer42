birthday = input("enter when you were born in format dd.mm.rrrr: ")
digit = input('enter 4 digit code: ')
gender = input('man/woman: ')


empty = []
empty.append(birthday[3])
empty.append(birthday[4])
n = "".join(empty)
print(n)

list = []

#rrmmdd/cccc
if gender == 'man':
    global number
    print(f'{birthday[8]}{birthday[9]}{n}{birthday[0]}{birthday[1]}/{digit}')
    list.append(birthday[8])
    list.append(birthday[9])
    list.append(n)
    list.append(birthday[0])
    list.append(birthday[1])
    list.append(digit)

    print(list)
    number = ''.join(list)
    print(number)


elif gender == 'woman':
    n = int("".join(empty))
    n_new = n + 50
    n = n_new  
    print(f'{birthday[8]}{birthday[9]}{n}{birthday[0]}{birthday[1]}/{digit}')
    list.append(birthday[8])
    list.append(birthday[9])
    list.append(n)
    list.append(birthday[0])
    list.append(birthday[1])
    list.append(digit)

    print(list)
    number = ''.join(list)
    print(number)

else:
    print('error')


for i in number:
    a += i


print('a = ', a)