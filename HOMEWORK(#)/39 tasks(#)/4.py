"""
Form a string of 10 characters. Even numbers should be 
in even positions, and letters in odd positions.

"""
characters_list= []
even_numbers = [2,2,4,4,8]
letters = ['a','b','c','d','e',]

for i in range(10):
    if i % 2 == 0:
        characters_list.append(letters[i//2]) #dont use print here 

    else:
        characters_list.append(str(even_numbers[i//2]))


print(characters_list)
string = ("".join(characters_list))
print(string)
    
    
       



     
