s = 'jlkkajKJAkjffkjiowqemncosirqiwehsdfkjwriowasclpeieawois'

print("write random number")

n = input()
rambo = ''

for i in range(len(s)):
    if (i+1)%n==0:
        rambo += '/n'

    else:
        rambo += s[i]

print(rambo)