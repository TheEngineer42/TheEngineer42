"""
Given a string, remove the k-th character in it.
"""

s = str(input('write some random string: '))
k = int(input('write the k-th character you would like to be deleted: '))

print(s.replace(s[k-1], ''))