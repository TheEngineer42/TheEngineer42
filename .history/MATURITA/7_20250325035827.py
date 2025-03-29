birthday = input("enter when you were born in format dd.mm.rrrr: ")
digit = input('enter 4 digit code: ')
gender = input('man/woman: ')

if gender == 'man':
    print(f"{birthday}/{digit} 50")

elif gender == 'woman':
    print(f"{birthday}/{digit}")

else:
    print('error')

