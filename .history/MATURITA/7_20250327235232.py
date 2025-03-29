birthday = input("enter when you were born in format dd.mm.rrrr: ")
digit = input('enter 4 digit code: ')
gender = input('man/woman: ')


month_digits = []
month_digits.append(birthday[3])
month_digits.append(birthday[4])
n = "".join(month_digits)
n_int = int("".join(month_digits))
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
    number = str(''.join(list))
    number_int = int("".join(list))
    print(number)


elif gender == 'woman':
    
    n = int("".join(month_digits))
    n_new = n + 50
    n = n_new  
    print(f'{birthday[8]}{birthday[9]}{n}{birthday[0]}{birthday[1]}/{digit}')
    list.append(birthday[8])
    list.append(birthday[9])
    list.append(str(n))
    list.append(birthday[0])
    list.append(birthday[1])
    list.append(digit)

    print(list)
    number =''.join(list)
    number_int = int("".join(list))

    print(number)

else:
    print('error')


if number_int % 11 == 0:
    print('vas obciansky je platny')


else:
    print('vas obciansky je neplatny')