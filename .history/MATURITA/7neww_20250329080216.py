"""
birthday = input("enter when you were born in format dd.mm.rrrr: ")
digit = input('enter 4 digit code: ')
gender = input('man/woman: ')"
"""

birthday = '12.07.2005'
cccc = 1234
gender = 'woman'


rr = birthday[8:10] 
mm = birthday[3:5]
dd = birthday[:2]



#rrmmdd/cccc
if gender == 'man':
    print(f'{rr}{mm}{dd}/{cccc}')

if gender == 'woman':
    #mm += 50  --> mm is a string so you cant add numbers to it
    mm = str(int(mm)+50) #convert mm to int, add 50, then again convert to str
    print(f'{rr}{mm}{dd}/{cccc}')

    







































