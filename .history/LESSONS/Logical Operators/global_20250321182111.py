x = 10  # Global variable

def change_x():
    global x  # Declare x as global
    x = 20    # Modify the global variable x

change_x()
print(x)  # Now x will be 20 because we modified it inside the function

#In Python, the global keyword is used to declare a variable as global inside
#a function. This means that when you modify the variable inside
#the function, the changes will be reflected outside the function as well.
"""
/////////////////////////////////////////////////////////////////////
"""

x = 10  # Global variable

def update_x():
    x = 20  # This creates a local variable, doesn't change the global x

update_x()
print(x)  # Output: 10 (global x is unchanged)