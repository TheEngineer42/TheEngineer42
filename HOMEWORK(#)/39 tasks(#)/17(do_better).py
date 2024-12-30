'''
Given a string consisting of words separated 
by characters listed in the second line. Show all words.
'''

text = 'word!apple.purpose:life'
separator = '!.:'

print(text.replace('!', ' ').replace('.', ' ').replace(':', ' ')) 


