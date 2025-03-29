bills = [100, 50, 25, 10]

cash = int(input('zadajte kolko penazi chcete rozmenit: '))

remainder = cash % 10

for i in bills:
    amount = cash // i
    cash = cash % i
    print(f'pocet {i} euroviek je = {amount}')

if remainder != 0:
    print(f"{remainder}, bohuzial nevieme vydat")