"""
CASTING
"""
x = str(3)   #x will be '3'
y = int(3)   #y will be 3
z = float(3) #z will be 3.0


"""
GETTING THE TYPE
"""
print(type(x)) #shows data type of variable
print(type(y))
print(type(z))


"""
MANY VALUES TO MULTIPLE VARIABLES
"""
x, y, z = "apple", "bannana", "cherry"

print(x)
print(y)
print(z)

a = b = c = "avocado"
print(a)


print()

"""
UNPACK A COLLECTION
"""
fruits = ["apple", "bannana", "cherry"]
m, n, k = fruits

print(m)
print(n)
print(k)
