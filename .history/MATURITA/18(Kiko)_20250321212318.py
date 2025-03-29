bills = [100,50,25,10]

print("zadajte summu, ktoru chcete vyplatit: ")
money = input()

sum = int(money)
remainder = sum % 10


for i in bills:
    amount = sum // i
    sum = sum % i
    print(f'pocet{i} euroviek - {amount}')
if remainder > 0:
    print(f"Neviem vydat celu sumu, zvysok je: {remainder}")



