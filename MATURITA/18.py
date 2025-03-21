bankovky = [100,50,25,10]

print("zadajte summu, ktoru chcete vyplatit: ")
vstup = input()

suma = int(vstup)
zvysok = suma % 10


for bankovka in bankovky:
    pocet = suma // bankovka
    suma = suma % bankovka
    print(f'pocet{bankovka} euroviek - {pocet}')
if zvysok > 0:
    print(f"Neviem vydat celu sumu, zvysok je: {zvysok}")

