birthday = input("enter when you were born in format dd.mm.rrrr: ")
digit = input('enter 4 digit code: ')
gender = input('man/woman: ')


month_digits = []
month_digits.append(birthday[3])
month_digits.append(birthday[4])
n = "".join(month_digits)
n_int = int("".join(month_digits))
print(n)

values = []

#rrmmdd/cccc
if gender == 'man':
    global number
    print(f'{birthday[8]}{birthday[9]}{n}{birthday[0]}{birthday[1]}/{digit}')
    values.append(birthday[8])
    values.append(birthday[9])
    values.append(n)
    values.append(birthday[0])
    values.append(birthday[1])
    values.append(digit)

    print(values)
    number = str(''.join(values))
    number_int = int("".join(values))
    print(number)


elif gender == 'woman':
    
    n = int("".join(month_digits))
    n_new = n + 50
    n = str(n_new)  
    print(f'{birthday[8]}{birthday[9]}{n}{birthday[0]}{birthday[1]}/{digit}')
    values.append(birthday[8])
    values.append(birthday[9])
    values.append(str(n))
    values.append(birthday[0])
    values.append(str(birthday[1]))
    values.append(str(digit))

    print(values)
    number =''.join(values)
    number_int = int("".join(values))

    print(number)

else:
    print('error')


if number_int % 11 == 0:
    print('vas obciansky je platny')
    file = open("spravne_rodne_cisla.txt", 'w')
    file.write(str(number_int))
    file.close()
    
    with open('spravne_rodne_cisla.txt', "r") as file:
        content = file.read()
        print(content)

    



else:
    print('vas obciansky je neplatny')
    
    file = open("nespravne_rodne_cisla.txt", 'w')
    file.write(str(number_int))
    file.close()
