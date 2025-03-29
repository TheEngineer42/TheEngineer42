"""
Each time you interact with a file, you need to open it and close it. 
The with open() handles this automatically: It opens the file at 
the beginning of the block.It closes the file when the block 
ends (even if an error occurs).

"""

# Writing to a file
with open("myfile.txt", "w") as file:
    file.write("Hello, world!")

# Reading from a file
with open("myfile.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a file
with open("myfile.txt", "a") as file:
    file.write("This is an additional line.")