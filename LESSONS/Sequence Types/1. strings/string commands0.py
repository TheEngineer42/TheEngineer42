"""
if you hold your cursor on function, it explains what it
does

"""

"""
COMMANDS:
capitalize, swapcase, title, lower, upper, count, startswith, endswith
find, index, strip, lstrip, rstrip, replace
split
"""
text = ('foo Goo moo Doo ala balA ala taLa')

print(len(text))         #33
print(text.capitalize()) #Foo goo moo doo ala bala tala
print(text.swapcase())   #FOO gOO MOO dOO ALA BALa TAlA
print(text.title())      #Foo Goo Moo Doo Ala Bala Tala
print(text.lower())      #foo goo moo doo ala bala tala
print(text.upper())      #FOO GOO MOO DOO ALA BALA TALA


print(text.count('moo'))        #(looks for moo in whole string), answer: 1
print(text.count('moo', 0, 29)) #(looks for moo in range of 0 to 29(whole string)) answer: 1
print(text.count('moo', 0, 6))  # 0
print(text.count('moo', 10, 21))# 0


print(text.startswith('foo'))       #True
print(text.startswith('foo',25,29)) #False
print(text.startswith('Doo'))       #False
print(text.endswith('taLa'))        #True
print(text.endswith('tala'))        #False
print(text.endswith('sdgfg'))       #False


print(text.find('foo'))             #0
print(text.find('ala'))             #3
print(text.find('ghhfhfg'))         #-1(failure)
print(text.find('balA', 10, 29))    #20
print(text.rfind('foo'))            #0 (looks for LAST occurence of 'foo')
print(text.rfind('ala'))            #25(looks for LAST occurence of 'ala')


text1 = ('Hello World! Hello World!')
print(text1.index('Hello'))      #0
print(text1.index('Hello',6,24)) #13
print(text1.index('World'))      #6
print(text1.rindex('Hello'))     #13
#print(text1.index('banana'))    #value error

"""
DIFFERENCE BETWEEN find & index
find - if substring is not found = returns -1
index - if substring is not found = returns value error

"""

text2 = ('    abcd LADAd dsferr LL k     ')
print(text2)            #    abcd LADAd dsferr LL k     |
print(text2.strip())    #abcd LADAd dsferr LL k
print(text2.lstrip())   #abcd LADAd dsferr LL k     | 
print(text2.rstrip())   #    abcd LADAd dsferr LL k

print(text2.replace("abcd", "aaaa", 1)) #    aaaa LADAd dsferr LL k     |
#replace(old, new, how many occurences(in our case only first occurence))

print(text2.split()) #['abcd', 'LADAd', 'dsferr', 'LL', 'k']

