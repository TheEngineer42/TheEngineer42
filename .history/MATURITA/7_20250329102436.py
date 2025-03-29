def data():
    global number
    birthday = input("zadajte kedy ste sa narodili vo formate dd.mm.rrrr: ")
    cccc = input('enter 4 digit code: ')
    gender = input('man/woman: ')
    print('========================')
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

    else:
        print('Vase rodne cislo je nespravne')
            
        file = open("nespravne_rodne_cisla.txt", 'a')
        file.write(number +  "\n")
        file.close()


def files():
    
    with open("spravne_rodne_cisla.txt", 'r') as file:
        content1 = file.read()
        print(f"Spravne rodne cisla:\n{content1}")
    
    # Read and print incorrect numbers from the file
    with open("nespravne_rodne_cisla.txt", 'r') as file:
        content2 = file.read()
        print(f"Nepravne rodne cisla:\n{content2}")

        
while True:
    print("\n ======Novy Clovek======")
    data()
    modulo()
    files()

    continue_program = input('\n Chcete zadat este data --> "ano"/"nie"\n Chcete vymazat existujuce? --> "vymazat"\nOdpoved: ')
    if continue_program == "nie":
        break

    elif continue_program == "vymazat":
        with open("spravne_rodne_cisla.txt", 'w') as file:
            pass

        with open("nespravne_rodne_cisla.txt", 'w') as file:
            pass




    
    




 
