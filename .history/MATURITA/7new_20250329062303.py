"""
birthday = input("enter when you were born in format dd.mm.rrrr: ")
digit = input('enter 4 digit code: ')
gender = input('man/woman: ')"
"""

birthday = '12.37.2005'
digit = 1234
gender = 'man'


month_digits = []
month_digits.append(birthday[3])
month_digits.append(birthday[4])
n = "".join(month_digits)
print(n)

print(month_digits)