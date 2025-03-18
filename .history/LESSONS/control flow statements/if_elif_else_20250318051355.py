number = int(input('write you number: '))



if number >= 100:
    print(number, 'is greater than 100')

elif 100 > number >= 50:  # you can write conditioin in here
    print(number, 'is between 100 and 50') 


else:
    print(number, 'is less than 50')


"""
/////////////////////////
IF ELIF ELSE - CONSTRUCT
/////////////////////////

- allows you to select one of several blocks of code to execute

HOW IT WORKS:
- if the first is true, then the corresponding is executed, but the code after 
that is not executed
- if first condition is false, then another condition is checked. This continues 
until it does not find real condition
- if all conditions are false, the block of code defined in 'else' is executed




"""

