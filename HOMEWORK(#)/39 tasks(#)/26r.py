"""
The line consists of words 
separated by one or more spaces. 
Swap the longest word with the shortest.
"""

s = ('words separated   by  smth') # dont forget to make a list out of it
list_s = (s.split())


longest_word = []
shortest_word = list_s[0] #starting from the first word

for word in list_s:
    if len(word) > len(longest_word):
        longest_word = word

    if len(word) < len(shortest_word):
        shortest_word = word
    
print('longest word: ', longest_word)
print('shortest word: ', shortest_word)

medium = []
medium = longest_word

for i in range(len(list_s)):
    if list_s[i] == longest_word:
        list_s[i] = shortest_word
    elif list_s[i] == shortest_word:
        list_s[i] = medium

result = ' '.join(list_s)
print(result)






