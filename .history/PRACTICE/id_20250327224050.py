def generate_rodne_cislo(datum, cccc, gender):
    day, month, year = datum.split('.')
    year_short = year[2:]
    
    if gender.lower() == "zena":
        month = str(int(month) + 50)
    
    rodne_cislo = f"{year_short}{month.zfill(2)}{day.zfill(2)}/{cccc}"
    kontrolne_cislo = f"{year_short}{month.zfill(2)}{day.zfill(2)}{cccc}"
    
    if int(kontrolne_cislo) % 11 == 0:
        with open("spravne_rodne_cisla.txt", "a") as file:
            file.write(rodne_cislo + "\n")
    else:
        with open("vadne_rodne_cisla.txt", "a") as file:
            file.write(rodne_cislo + "\n")
    
    return rodne_cislo

# Príklad použitia
datum = "12.03.1985"
cccc = "1234"
gender = "zena"

rodne_cislo = generate_rodne_cislo(datum, cccc, gender)
print("Generované rodné číslo:", rodne_cislo)