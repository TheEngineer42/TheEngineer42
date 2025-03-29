def data():
    global number
    birthday = input("enter when you were born in format dd.mm.rrrr: ")
    cccc = input('enter 4 digit code: ')
    gender = input('man/woman: ')
    rr = birthday[8:10] 
    mm = birthday[3:5]
    dd = birthday[:2]

    if gender == 'man':
        print(f'rodne cislo: {rr}{mm}{dd}/{cccc}')
        number = f'{rr}{mm}{dd}{cccc}'
        

    if gender == 'woman':
        #mm += 50  --> mm is a string so you cant add numbers to it
        mm = str(int(mm)+50)
        print(f'rodne cislo: {rr}{mm}{dd}/{cccc}')
        number = f"{rr}{mm}{dd}{cccc}" #dont forget that here number is a string
    
def modulo():
    if int(number) % 11 == 0: #and here to be able to use %, you need to convert it to integer
        print('Vase rodne cislo je platne')

        file = open("spravne_rodne_cisla.txt", 'a')
        file.write(number +  "\n")
        file.close()

while True:
    print("\n ======Novy Clovek======")
    data()
    modulo()

    continue_program = input('\n Chcete zadat este data? Odpovedzte "ano"/"nie"')
    if continue_program != "ano":
        break



    else:
        print('Vase rodne cislo je nespravne')
        
        file = open("nespravne_rodne_cisla.txt", 'a')
        file.write(number +  "\n")
        file.close()
    




 
