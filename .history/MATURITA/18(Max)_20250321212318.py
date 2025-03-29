s1=int(input('Zadajte sumu, ktorú Vám vyplatím'))

if s1//100:
    print(('počet 100 euroviek - '),s1//100)
    s1=s1%100
else:
    print('počet 100 euroviek - 0')
if s1//50:
    print(('počet 50 euroviek - '),s1//50)
    s1=s1%50
else:
    print('počet 50 euroviek - 0')
if s1//20:
    print(('počet 20 euroviek - '),s1//20)
    s1=s1%20
else:
    print('počet 20 euroviek - 0')
if s1//10:
    print(('počet 10 euroviek - '),s1//10)
    s1=s1%10
else:
    print('počet 10 euroviek - 0')
if s1!=0:
    print('ostatné sa nedajú vydať')