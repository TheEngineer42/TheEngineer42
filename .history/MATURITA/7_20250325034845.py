def generate_birth_number(date: str, suffix: str, gender: str) -> str:
    day, month, year = map(int, date.split('.'))
    year_short = year % 100  # posledné dve číslice roku
    
    if gender.lower() == "žena":
        month += 50  # Pre ženy sa k mesiacu pripočíta 50
    
    birth_number = f"{year_short:02}{month:02}{day:02}{suffix}"
    formatted_birth_number = f"{year_short:02}{month:02}{day:02}/{suffix}"
    
    return birth_number, formatted_birth_number

def is_valid_birth_number(birth_number: str) -> bool:
    return int(birth_number) % 11 == 0

def save_birth_number(birth_number: str, is_valid: bool):
    filename = "spravne_rodne_cisla.txt" if is_valid else "vadne_rodne_cisla.txt"
    with open(filename, "a") as file:
        file.write(birth_number + "\n")

def main():
    date = input("Zadajte dátum narodenia (dd.mm.rrrr): ")
    suffix = input("Zadajte štvormiestne číslo: ")
    gender = input("Zadajte pohlavie (muž/žena): ")
    
    birth_number, formatted_birth_number = generate_birth_number(date, suffix, gender)
    
    if is_valid_birth_number(birth_number):
        print(f"Rodné číslo {formatted_birth_number} je platné.")
    else:
        print(f"Rodné číslo {formatted_birth_number} je neplatné.")
    
    save_birth_number(formatted_birth_number, is_valid_birth_number(birth_number))

if __name__ == "__main__":
    main()