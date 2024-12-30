"""
The line consists of words separated by one or more spaces. 
Find the word with the longest length.
"""

s = str(input("write down some words, separated by space: "))

list_s = s.split() #separated the string
#print(max(list_s)) #looks for max value based on lexicographical value

longest_word = ''

#for i in range(len(list_s)): ---> you dont need index here, just write for i in range list_s:
for word in list_s: #direct iteration over the elements of the list, each word is assigned a value
    if len(word) > len(longest_word):
        longest_word = word

print('longest word is: ', longest_word)

