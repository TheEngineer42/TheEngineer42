cash = int(input('zadajte kolko penazi chcete rozmenit: '))
bills = [100, 50, 25, 10]

remainder = cash % 10

for i in bills:
    amount = cash // i
    cash = cash % i
    print(f'pocet {i} euroviek je = {amount}')

if remainder != 0:
    print(f"{cash}, bohuzial nevieme vydat")