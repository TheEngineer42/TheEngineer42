def generate_rodne_cislo():
    datum = input("Zadajte dátum narodenia (dd.mm.rrrr): ")
    cccc = input("Zadajte štvormiestne číslo: ")
    gender = input("Zadajte pohlavie (muz/zena): ")
    
    day, month, year = datum.split('.')
    year_short = year[2:]
    
    if gender.lower() == "zena":
        month = str(int(month) + 50)
    
    rodne_cislo = f"{year_short}{month.zfill(2)}{day.zfill(2)}/{cccc}"
    kontrolne_cislo = f"{year_short}{month.zfill(2)}{day.zfill(2)}{cccc}"
    
    if int(kontrolne_cislo) % 11 == 0:
        with open("spravne_rodne_cisla.txt", "a") as file:
            file.write(rodne_cislo + "\n")
        print("Rodné číslo je platné a bolo uložené do spravne_rodne_cisla.txt")
    else:
        with open("vadne_rodne_cisla.txt", "a") as file:
            file.write(rodne_cislo + "\n")
        print("Rodné číslo je neplatné a bolo uložené do vadne_rodne_cisla.txt")
    
    print("Generované rodné číslo:", rodne_cislo)

# Spustenie programu
generate_rodne_cislo()

