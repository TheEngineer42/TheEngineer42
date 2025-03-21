x = 10  # Global variable

def change_x():
    global x  # Declare x as global
    x = 20    # Modify the global variable x

change_x()
print(x)  # Now x will be 20 because we modified it inside the function
