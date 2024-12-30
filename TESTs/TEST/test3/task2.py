"""
Дан одномерный массив числовых
значений, насчитывающий N
элементов. Определить, имеются ли в
массиве два подряд идущих нуля.
"""

s = [1,4,7,3,5,7,9,4,0]

found_zero = False

for i in range(len(s)-1):
    if s[i] + s[i+1] == 0:
        found_zero = True

if found_zero:
        print('true') 

else:
        print('false')