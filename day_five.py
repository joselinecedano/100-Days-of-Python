'''
 This is a password generator that takes in the number of letters, symbols, and numbers the user wants in their password and generates a password based on those inputs.
'''

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = [] # empty list to store the random characters for the password
for char in range(1, nr_letters + 1):
  password_list += random.choice(letters)
for symb in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)
for num in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)
random.shuffle(password_list)  # shuffle the list to randomize the order of the characters 

password = "" 
for char in password_list:
  password += char # add each character to the password string so we can print it out as a string and not as a list of characters ex: ['a', 'b', 'c']
print(f"Your password is: {password}")

# Output:
'''
Welcome to the PyPassword Generator!
How many letters would you like in your password?
1
How many symbols would you like?
1
How many numbers would you like?
1
Your password is: 9A#
'''
