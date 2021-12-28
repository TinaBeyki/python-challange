import random

print("Welcome to the PyPassword Generator!")
letters_num = int(input("How many letters would you like in your password?\n"))
symbols_num = int(input("How many symbols would you like?\n"))
numbers_num = int(input("How many numbers would you like?\n"))

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '-']

password = " "

mid = letters_num // 2
for i in range(0, mid):
    password += random.choice(letters)

for k in range(0, numbers_num):
    password += random.choice(numbers)

for i in range(mid, letters_num):
    password += random.choice(letters)

for j in range(0, symbols_num):
    password += random.choice(symbols)

print(f"Here is your password: {password}")
