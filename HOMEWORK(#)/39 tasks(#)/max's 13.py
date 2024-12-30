s=input()
if all(s1 in 'abc' for s1 in s):
    print('Obsahuje iba abc')
else:
    print('Neobsahuje iba abc')