# Input data (you can replace this with actual input())
birthday = '12.07.2005'
cccc = 1234
gender = 'woman'

rr = birthday[8:10]
mm = birthday[3:5]
dd = birthday[:2]

# Function to process the person's number based on gender
def person():
    global number  # Declare number as global to use it in other functions
    if gender == 'man':
        print(f'{rr}{mm}{dd}/{cccc}')
        number = f'{rr}{mm}{dd}{cccc}'
    elif gender == 'woman':
        mm = str(int(mm) + 50)  # Add 50 to the month if it's a woman
        print(f'{rr}{mm}{dd}/{cccc}')
        number = f"{rr}{mm}{dd}{cccc}"

# Function to check if the number is divisible by 11 and write it to the correct file
def modulo():
    global number  # Access the number generated in the person() function
    if int(number) % 11 == 0:
        print('Your number is correct')

        # Open the file in append mode and write the number
        with open("spravne_rodne_cisla.txt", 'a') as file:
            file.write(number + "\n")
    else:
        print('Your number is incorrect')
        
        # Open the file in append mode and write the number
        with open("nespravne_rodne_cisla.txt", 'a') as file:
            file.write(number + "\n")

# Function to read and print the contents of both files
def files():
    # Read and print correct numbers from the file
    with open("spravne_rodne_cisla.txt", 'r') as file:
        content1 = file.read()
        print(f"Correct numbers:\n{content1}")
    
    # Read and print incorrect numbers from the file
    with open("nespravne_rodne_cisla.txt", 'r') as file:
        content2 = file.read()
        print(f"Incorrect numbers:\n{content2}")

# Call the functions in the correct order
person()  # First, process the person's number
modulo()  # Check if the number is correct and write it to the file
files()   # Finally, read and print the contents of the files
