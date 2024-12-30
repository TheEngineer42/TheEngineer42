s =  'python'


for i in range(len(s)):
    #print(s[:i+1],'*'*(len(s)-(i+1)), sep='')

    
    print("*"*(len(s)-(i+1)), s[:i+1][::-1], s[:i+1],'*'*(len(s)-(i+1)), sep='')
