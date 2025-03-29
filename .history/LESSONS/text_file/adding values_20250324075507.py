"""

number = int(input("write you favourite number: "))


with open('adding.text', 'w') as file:
    file.write(str(number))

with open('adding.text', 'r') as file:
    text = file.read()
    print(text)
   

"""
