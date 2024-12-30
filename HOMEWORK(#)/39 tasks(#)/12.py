"""
Given a string, replace each even character 
with either 'a' if the character is not 'a' 
or 'b', or 'c' otherwise.
"""

s = str(("xaxbxlxlxbxaxlxbxa")) #strings are IMMUTABLE, means you cannot modify them directly,because of theat we will make new strin
s_new = '' #creating new string, which we can modify

for i in range(len(s)):
    if i % 2 ==1:
        if (s[i] == 'a') or (s[i] == 'b'):
            s_new += 'c'

        else:
            s_new += 'a'
    
    else:
        s_new += s[i]

print(s_new)
    



"""
if s[i] == 'a' or 'b': -> is wrong because python evaluates it as:
    s_new += 'c'

if (s[i] == 'a') or ('b'): -> since non empty string, its always
    s_new += 'c'              True, therefore we always get 'c' in 
                              our s_new

correct would be to write this:
if (s[i] == 'a') or (s[i] == 'b'):...

"""
