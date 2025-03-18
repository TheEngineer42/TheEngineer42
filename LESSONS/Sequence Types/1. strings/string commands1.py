"""
COMMANDS:
isalpha(), isdigit(), isalnum(), islower(), isupper(), isspace()
"""


s1 = "Hello"
s2 = "Hello123"
s3 = "Hello World"
s4 = ""
s5 = "123432"

print(s1.isalpha()) #True
print(s2.isalpha()) #False
print(s3.isalpha()) #False
print(s4.isalpha()) #False
print(s5.isalpha()) #False

print("//////////////")

print(s1.isdigit()) #False
print(s2.isdigit()) #False
print(s3.isdigit()) #False
print(s4.isdigit()) #False
print(s5.isdigit()) #True

print("//////////////")

print(s1.isalnum()) #T
print(s2.isalnum()) #T
print(s3.isalnum()) #False #space is neither letter nor number
print(s4.isalnum()) #False
print(s5.isalnum()) #True

print("//////////////")
print("//////////////")



m1 = 'abc'
m2 = 'abc1$d'
m3 = 'Abc1$D'
m4 = "123432"


print(m1.islower()) #T #ignores all non letter symbols
print(m2.islower()) #T
print(m3.islower()) #F
print(m4.islower()) #F

print("//////////////")

print('1234'.islower()) #F
print('+-*/'.islower()) #F
print('ab#%'.islower()) #T

print("//////////////")


m5 = 'ABC'
m6 = 'ABC1$D'
m7 = 'Abc1$D'

print(m1.isupper()) #F
print(m5.isupper()) #T
print(m6.isupper()) #T
print(m7.isupper()) #F

print("//////////////")


n1 = '       '
n2 = 'abc1$d'

print(n1.isspace()) #T
print(n2.isspace()) #F





