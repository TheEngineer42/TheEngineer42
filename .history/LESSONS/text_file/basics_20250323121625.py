###################################
#1. Create and Write to a Text File
###################################


with open("myfile.txt", "w") as file:
    file.write("Hello, this is my first file text\n")
    file.write("I can also add multiple lines\n")
    
#"w" mode creates a new file ((or overwrites if it exists))
#(or overwrites if it exists)

"""
- open("example.txt", "w") opens the file in write mode ("w")
- as file assigns the file object to the variable file
- 'with' ensures that the file is automatically closed after 
the block of code finishes, so you don’t need to explicitly 
call file.close()

"""


##########################################
#2. Append Information to an Existing File
##########################################


with open("myfile.txt", "a") as file:
    file.write("This is another sentence")

# "a" mode ensures content is added without deleting existing data.

#####################################
#3. Read a File to Verify the Content
#####################################


with open('myfile.txt', "r") as file:
    content = file.read()
    print(content)

# "r" mode reads the file.



"By default, when you create or open a file using open() "
"in Python without specifying a path, the file is stored in "
"the current working directory—the folder where your Python "
"script is running."

"To Find the Current Working Directory"
"You can use Python's os module to find out where the file is stored:"
import os
print(os.getcwd()) #C:\Users\vkash\OneDrive\Desktop\Maturita (we ball)\CS\Python