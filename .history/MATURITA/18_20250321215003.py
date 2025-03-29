banknotes = [100,50,25,10]

cash =int(input('Prosim, zadajte mnozstvo penazi ktore chcete rozmenit: '))
remainder = cash % 10 #money that ATM cant change

for i in banknotes:
    amount = cash // i #checking how many banknotes of respective value there will be in given money
    amount = amount % i #same as if were to substract i*from money, also updating value of amount
    print(f"pocet {i} euroviek -{amount}")

if remainder != 0:
    print(f"{cash % 10} bohuzial nevieme rozmenit")
