# Password Generator

import random


# List of available characters the program can use to generate the password.
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = [ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', '?', '/', '|']
numbers = '0123456789'


while True:
        # Welcomes and prompts the user for the number of characters they want in their password.
        print("Welcome to the Password Generator!")
        print("How many letters would you like in your password? ")
        num_chars = int(input())
        if num_chars < 0:
            print("Please enter either 0 or a positive number for the number of letters.")
            continue
        elif num_chars > 100:
            print("Please enter a number less than or equal to 100 for the number of letters.")
            continue
        elif num_chars > 0 and num_chars <= 100:
            break
while True:
            # Checks if the user wants to include symbols in the password.
            print("Would you like to include symbols? (yes/no)")
            symbols_choice = input()
            if symbols_choice== 'yes':
                print("How many symbols would you like?")
                num_symbols = int(input())
            elif symbols_choice == 'no':
                num_symbols = 0
            else: 
                print("Invalid input. Please enter 'yes' or 'no'.")
                break
            if num_symbols < 0 or num_symbols > 50:
                print("Please enter a number between 0 and 50 for the number of symbols.")
                continue
            elif num_symbols >= 0 and num_symbols <= 50:
                break



# Checks if the user wants to include numbers in the password.
print("Would you like to include numbers? (yes/no)")
numbers_choice = input()        
if numbers_choice == 'yes':
    print("How many numbers would you like?")
    num_numbers = int(input())
elif numbers_choice == 'no':
    num_numbers = 0
else: 
    print("Invalid input. Please enter 'yes' or 'no'.")
    exit()
if num_numbers < 0 or num_numbers > 10:
    print("Please enter a number between 0 and 10 for the amount of numbers.")
    exit()   



# Generates a list of random characters based on the user's input.
password_letters= (random.choices(letters, k=num_chars))
password_symbols= (random.choices(symbols, k=num_symbols))
password_numbers= (random.choices(numbers, k=num_numbers))

# Combines the lists of characters into one list and shuffles it.
unshufled_password = password_letters + password_symbols + password_numbers
random.shuffle(unshufled_password)

# Connverts the shuffled list of characters into a string.
Shuffled_password = ''.join(unshufled_password)

# Prints the final password to the user.
print(f"Your password is: {Shuffled_password}")

if Shuffled_password == '':
    print("Congratulations, you are retarded and just wasted your time, try selecting at least one character next time.")

