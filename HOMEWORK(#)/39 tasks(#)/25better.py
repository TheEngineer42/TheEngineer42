"""
Given a string, insert a space after each character.
"""

s = 'Given a string, insert a space after each character.'
new_s = '' #dont forget to initialize it as a string and not as a integer

for char in s:
    new_s += char + " "

print(new_s)