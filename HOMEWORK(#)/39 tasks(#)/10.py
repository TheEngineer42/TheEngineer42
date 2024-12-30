"""
Given a string. If it starts with 'abc', 
then replace them with 'www',
otherwise add 'zzz' to the end 
of the string.

"""

s = str(input('write random string: '))


if s.startswith('abc'):
    print(s.replace('abc', 'www', 1)) #1 means only firs occurence
    
else:
    s += 'zzz'
    print(s)

###what if i wanted to replace last 3?






