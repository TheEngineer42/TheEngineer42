print('write down random word')
s = input()

modified_sentence= ''


for i in range(len(s)):
    if (i+1)%3==0:
        modified_sentence += '#'

    else: 
        modified_sentence += s[i]


print(modified_sentence)