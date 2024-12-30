a = 7
b = 8
c = 9

f = int()



if a == b:
    c = a + b
    f = b + c

elif b > c:
    a = a + b
    f = a + c

else:
    b = c + b
    f = a + b

print('F= ', f)
