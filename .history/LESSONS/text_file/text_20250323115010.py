

with open("myfile.txt", "w") as file:
    file.write("Hello, this is my first file text\n")
    file.write("I can also add multiple lines\n")


#"w" mode creates a new file ((or overwrites if it exists))
#(or overwrites if it exists)

"""
- open("example.txt", "w") opens the file in write mode ("w")
- as file assigns the file object to the variable file
- with ensures that the file is automatically closed after 
the block of code finishes, so you don’t need to explicitly 
call file.close()

"""

with open('myfile.txt', "r") as file:
    content = file.read()
    print(content)




"By default, when you create or open a file using open() "
"in Python without specifying a path, the file is stored in "
"the current working directory—the folder where your Python "
"script is running."

"To Find the Current Working Directory"
"You can use Python's os module to find out where the file is stored:"
import os
print(os.getcwd()) #