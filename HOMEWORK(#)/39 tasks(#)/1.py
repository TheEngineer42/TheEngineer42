"""
Given a string. Print it 3 times separated 
by commas and show the number 
of characters in it.

"""

s = "this a string"
result = ", ".join(3*[s])
print(result)
print("Number of charcters: ", len(result))


