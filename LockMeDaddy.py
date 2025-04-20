#Password Generator

import random

symbols = [ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', '?', '/', '|']
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

print("Welcome to the Password Generator!")
print("How many characters would you like in your password? ")
num_chars = int(input())
print("Would you like to include symbols? (yes/no)")
symbols_choice = input()
if symbols_choice== 'yes':
    print("How many symbols would you like?")
    num_symbols = int(input())
else: num_symbols = 0

print("Would you like to include numbers? (yes/no)")
numbers_choice = input()        
if numbers_choice == 'yes':
    print("How many numbers would you like?")
    num_numbers = int(input())
else: num_numbers = 0



password_letters= (random.choices(letters, k=num_chars))
password_symbols= (random.choices(symbols, k=num_symbols))
password_numbers= (random.choices(numbers, k=num_numbers))

#Combines the lists of characters into one list and shuffles it.
unshufled_password = password_letters + password_symbols + password_numbers
random.shuffle(unshufled_password)

#Connverts the shuffled list of characters into a string.
Shuffled_password = ''.join(unshufled_password)

#Prints the final password to the user.
print(f"Your password is: {Shuffled_password}") 