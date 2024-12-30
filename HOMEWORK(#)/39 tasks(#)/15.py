"""
Remove all 'x' letters in the line followed by 'abc'.
"""
s = 'xabcdkjxkj'

print('x' in s) #shows that x exists in xabcdkjxkj
print('xabc' in s)

if 'xabc' in s:
    print(s.replace('xabc', 'abc'))
#print(s.replace('x', 'd'))