"""
Given a string. Determine which character comes 
first: 'x' or 'w'. If one of the 
characters is missing, print a message about it.
"""

s=str(input("put some string value, put some x and w, or dont, no numbers: "))

if s.find('x') < s.find('w'):
    print('x comes first')

elif s.find('x') or s.find('w') == -1:
    print('one of the characters is missing')

else:
    print('w comes first')

