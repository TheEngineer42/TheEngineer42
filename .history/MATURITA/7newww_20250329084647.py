"""
birthday = input("enter when you were born in format dd.mm.rrrr: ")
cccc = input('enter 4 digit code: ')
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
    number = f'{rr}{mm}{dd}{cccc}'
    

if gender == 'woman':
    #mm += 50  --> mm is a string so you cant add numbers to it
    mm = str(int(mm)+50)
    print(f'{rr}{mm}{dd}/{cccc}')

    
    number = f"{rr}{mm}{dd}{cccc}" #dont forget that here number is a string
    

if int(number) % 11 == 0: #and here to be able to use %, you need to convert it to integer
    print('Your number is correct')

    file = open("spravne_rodne_cisla.txt", 'a')
    file.write(number +  "\n")
    file.close()

    

else:
    print('Your number is incorrect')
    print('Your number is correct')
    file = open("nespravne_rodne_cisla.txt", 'w')
    file.write(number +  "\n")
    file.close()

file = open("spravne_rodne_cisla.txt", 'r')
content1=file.read()
print(f"Correct numbers:\n{content1}")
file.close()

file = open("nespravne_rodne_cisla.txt", 'r')
content2=file.read()
print(f"Correct numbers:\n{content2}")
file.close()

 
