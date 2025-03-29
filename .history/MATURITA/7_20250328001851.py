birthday = input("Enter when you were born in format dd.mm.yyyy: ")
digit = input('Enter 4-digit code: ')
gender = input('Man/Woman: ')

# Extract month from birthday
month_digits = [birthday[3], birthday[4]]
n = "".join(month_digits)
n_int = int(n)

print(n)

# Store the generated number in a list for building the final number
num_list = []

# Construct the number based on gender
if gender == 'man':
    print(f'{birthday[8]}{birthday[9]}{n}{birthday[0]}{birthday[1]}/{digit}')
    num_list.append(birthday[8])
    num_list.append(birthday[9])
    num_list.append(n)
    num_list.append(birthday[0])
    num_list.append(birthday[1])
    num_list.append(digit)

elif gender == 'woman':
    n_new = n_int + 50
    n = str(n_new)
    print(f'{birthday[8]}{birthday[9]}{n}{birthday[0]}{birthday[1]}/{digit}')
    num_list.append(birthday[8])
    num_list.append(birthday[9])
    num_list.append(n)
    num_list.append(birthday[0])
    num_list.append(birthday[1])
    num_list.append(digit)

else:
    print('Error: Invalid gender input')
    exit()  # Exit the program if gender is invalid

# Join list elements into a final number
number = ''.join(num_list)
number_int = int(number)

print(number)

# Check if the number is divisible by 11 to validate the ID number
if number_int % 11 == 0:
    print('Your citizen ID is valid')

    # Write to the correct file
    with open("correct_citizen_numbers.txt", 'a') as file:
        file.write(f"{number_int}\n")
    
    with open('correct_citizen_numbers.txt', "r") as file:
        content = file.read()
        print(content)

else:
    print('Your citizen ID is invalid')

    # Write to the incorrect file
    with open("incorrect_citizen_numbers.txt", 'a') as file:
        file.write(f"{number_int}\n")
