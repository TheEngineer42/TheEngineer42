number = input("write you favourite food")


with open('adding.text', 'w') as file:
    file.write(number)

with open('adding.text', 'r') as file:
    text = file.read()
    print(text)
   


