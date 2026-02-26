target = 100
for number in range(1, target):
    if number % 3 == 0 and number % 5 == 0:
        print("fizz buzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)

import random

print("welcome to password generator")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

nr_letters = int(input("how many letters do you want in your password\n"))
nrs_numbers = int(input("how many numbers do you want in your password\n"))
nrs_symbols = int(input("how many symbols do you want in your password\n"))

password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nrs_numbers + 1):
    password += random.choice(numbers)

for char in range(1, nrs_symbols + 1):
    password += random.choice(symbols)

print(f"your password is : {password}")
