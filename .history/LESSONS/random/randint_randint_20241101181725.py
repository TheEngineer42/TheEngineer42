import random

"""
randint(): meaning in math: [a,b]

randrange(), 
1) if ONE argument is given: [0,a)
2) if TWO arguments are given: [a,b)    - like randint, but upper limit is out of range
3) if THREE arguments are given: first two are range limits, third one is a step
"""
print('RANDOM.RANDINT')
print(random.randint(0,10))
print(random.randint(-100,10))
print(random.randint(-100,-10))

print("\n")

print('RANDOM.RANDRANGE')
print(random.randrange(10))
print(random.randrange(20))

print()

print(random.randrange(5, 10))
print(random.randrange(90, 100))

print()

print(random.randrange(5, 10, 2))
print(random.randrange(1, 100, 20))
