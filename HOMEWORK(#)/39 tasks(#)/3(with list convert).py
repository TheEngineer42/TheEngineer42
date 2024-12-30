

s = str(input('write a string: '))
chars = list(s)     #converting string into list

if len(s) > 5:
    print(chars[0:3])
    print(chars[-3:])    #dont use [-3:-1], it wont include last char

else:
    print(chars[0]*len(s))