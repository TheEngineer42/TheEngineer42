"""
birthday = input("enter when you were born in format dd.mm.rrrr: ")
digit = input('enter 4 digit code: ')
gender = input('man/woman: ')"
"""

birthday = '12.07.2005'
digit = 1234
gender = 'man'


month_digits = []
month_digits.append(birthday[3])
month_digits.append(birthday[4])
n = "".join(month_digits)

#rrmmdd/cccc
if gender == 'man':
    print(f'{birthday[8]}{birthday[9]}{n}{birthday[0]}{birthday[1]}/{digit}')





































