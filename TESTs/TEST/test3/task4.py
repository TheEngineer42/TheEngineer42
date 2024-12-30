"""
Заданы М строк символов, которые
вводятся с клавиатуры. Из заданных
строк, каждая из которых представляет
одно слово, составить одну длинную
строку, разделяя слова пробелами
"""


M = int(input("how many words you want to enter: "))
empty_list = []


for num in range(M):
    word = str(input("write your word: "))
    empty_list.append(word)

print(" ".join(empty_list))

