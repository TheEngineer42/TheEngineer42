s = [1,3,4,6,7,8,9,4]

sum_div3 = 0
sum2 = []
empty = []

for i in range(len(s)):
    if s[i] % 3 == 0:
        sum_div3 += 1
    
    if i % 2 == 1:
        empty.append(s[i])
    

print(sum_div3)
n = sum(empty)/2
print(n)

s.insert(0, sum_div3)
print(s)

s.append(n)
print(s)