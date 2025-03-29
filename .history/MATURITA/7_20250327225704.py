birthday = input("enter when you were born in format dd.mm.rrrr: ")
digit = input('enter 4 digit code: ')
gender = input('man/woman: ')


empty = []
empty.append(birthday[3])
empty.append(birthday[4])
n = int("".join(empty))
print(n)

#rrmmdd/cccc
if gender == 'man':
    print(f'{birthday[8]}{birthday[9]}{n}{birthday[0]}{birthday[1]}/{digit}')


elif gender == 'woman':
    n_new = n + 50
    n = n_new  
    print(f'{birthday[8]}{birthday[9]}{n}{birthday[0]}{birthday[1]}/{digit}')

else:
    print('error')

