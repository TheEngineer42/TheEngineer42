while True:
    user_input = input("Do you want to continue (y/n):")
    if user_input == "n":
        print("Exitig the program.")
        break
    elif user_input == 'y':
        print("Continuing the program.")

    else:
        print("Invalid input. Please type 'y' or 'n'.")