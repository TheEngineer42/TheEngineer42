birthday = input("enter when you were born in format dd.mm.rrrr: ")
digit = input('enter 4 digit code: ')
gender = input('man/woman: ')


empty = []
empty.append(birthday[8])
empty.append(birthday[9])
n = "".join(empty)



if gender == 'man':
    n = n+50
    print(f"{birthday}/{digit} 50")

elif gender == 'woman':
    print(f"{birthday}/{digit}")

else:
    print('error')

