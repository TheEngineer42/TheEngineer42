i = 1

while i <= 3:
    print(i, "<=3")
    i += 1


"""
while loop allow allows to execute code as long as condition in
construct stays true

if condition is false, loop execution is terminated
"""

n = int(input("set number n: "))
s = 0
k=n #we dont have to use k here, its just to preserve original n, 
    #k is copy of n
while k>2:
    s = s + k
    k = k - 1

print(s)