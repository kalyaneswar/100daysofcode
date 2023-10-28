# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

random_letter = random.sample(letters, nr_letters)
random_number = random.sample(numbers,nr_numbers)
random_symbols = random.sample(symbols,nr_symbols)

new_letter = ''
for i in range(0, nr_letters):
    new_letter += random_letter[i]
    # print(new_letter)
new_number = ''
for i in range(0, nr_numbers):
    new_number += random_number[i]
    # print(new_number)
new_symbol = ''
for i in range(0, nr_symbols):
    new_symbol += random_symbols[i]
    # print(new_symbol)

print(f"{new_letter}{new_number}{new_symbol}")

# easy --> method 2
password = ""
for char in range(1,nr_letters +1):
    random_char = random.choice(letters)
    password += random_char
    # print(password)
for num in range(1,nr_numbers +1):
    random_num = random.choice(numbers)
    password += random_num
    # print(password)
for sym in range(1,nr_symbols +1):
    password += random.choice(symbols)
    # print(password)
print(password)
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for char in range(1,nr_letters +1):
    random_char = random.choice(letters)
    password_list += random_char
    # print(password)
for num in range(1,nr_numbers +1):
    random_num = random.choice(numbers)
    password_list += random_num
    # print(password)
for sym in range(1,nr_symbols +1):
    password_list += random.choice(symbols)
    # print(password)
print(password_list)
random.shuffle(password_list)
print(password_list)

final_password = ""
for final_passwd in password_list:
    final_password += final_passwd
print(final_password)