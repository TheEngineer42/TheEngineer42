"""
Дан одномерный массив числовых
значений, насчитывающий N
элементов. Исключить из массива
элементы, принадлежащие
промежутку [B; C].B и C ввод из
клавиатуры
"""

s = [1,4,7,3,5,7,9,4,0]
B = 2
C = 5

del s[B:C]
print(s)
