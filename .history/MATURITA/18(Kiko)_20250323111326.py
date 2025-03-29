banknotes = [100,50,25,10]

cash =int(input('Prosim, zadajte mnozstvo penazi ktore chcete rozmenit: '))
remainder = cash % 10 #money that ATM cant change

for i in banknotes:
    amount = cash // i 
    cash = cash % i
    print(f"pocet {i} euroviek -{amount}")
    

if remainder != 0:
    print(f"{cash % 10} bohuzial nevieme rozmenit")
