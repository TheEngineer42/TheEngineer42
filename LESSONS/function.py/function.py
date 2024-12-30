# function = a block of reusable code
#       place() after the function name to invoke it
def happy_birthday(name, age): #name is like temporarty variable
    print(f'Happy birthay to {name}!') # f-string(formatted string literal)
    print('Happy birthday to', name, '!') #same result as string above, but longer
    print(f'You are {age}!')


happy_birthday("Arnold",20)
happy_birthday("Steve",25)
happy_birthday("Job",30)