"""
A while loop is used to repeat a block of code while
a condition is True. It checks the condition before 
each iteration and continues as long as the condition 
remains true.
"""

"""
while some_condition:
    # code to execute while the condition is True
"""

"""
True is always considered a condition that will
never fail, i.e., it will always evaluate as True.
So, when you write while True:, you're creating an infinite loop, 
meaning the loop will keep running forever unless you explicitly 
tell it to stop.
"""

while True:
    print("This will keep printing forever!")
    break

#This will print the message indefinitely until you stop it 
#for instance, by pressing Ctrl+C in your terminal).

#how do you stop it?