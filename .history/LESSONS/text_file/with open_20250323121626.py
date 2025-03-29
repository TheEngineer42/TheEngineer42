with open("example.txt", "w") as file:
    file.write("Hello, World!")


"""
- open("example.txt", "w") opens the file in write mode ("w").
- as file assigns the file object to the variable file.
- with ensures that the file is automatically closed after the block
  of code finishes, so you don’t need to explicitly call file.close()

"""

#If you use open() without with, you must manually close the file:
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()  # You must close it manually

#If you forget to close it, the file might stay open,
#leading to memory leaks or data corruption.