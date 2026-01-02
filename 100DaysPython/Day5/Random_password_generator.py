# Asks how many symbols you want in password 
# Asks how many number you want in password 
# Asks number of small letter in password
# Asks number of capital letters in password 

# Capital letters (A–Z)
capital_letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

# Small letters (a–z)
small_letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

# Symbols
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '+', '=', '{', '}', '[', ']', '|',
    ':', ';', '"', "'", '<', '>', ',', '.', '?', '/'
]

# Numbers
numbers = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
]

print("="*60)
print("Welcome to random password generation game !")
num_capital_letters = int(input('How many capital letters you want in your password? '))
num_small_letters = int(input("How many small letters you want in your password? "))
num_symbols = int(input("How many symbols you want in your password? "))
num_numbers = int(input("How many numbers you want in your password? "))

###### total capitals, smalls, numbers, symbols we have 
total_capitals = len(capital_letters)
total_smalls = len(small_letters)
total_symbols = len(symbols)
total_numbers = len(numbers)

import random
# IDEA - for each position of password we'll use random number from (1 to 4) 
# if 1 we'll input a random Capital letter
# if 2 we'll input a random Small letter 
# if 3 we'll input a random Symbol letter
# if 4 we'll input a random Number

# Also keep track of whether number of characters user want is exceeded or not
total_password_len = num_capital_letters + num_numbers + num_small_letters + num_numbers

password = ""
password_len = 0
while(password_len < total_password_len):
    # what to put at this position - Capital_letter (1), Small_letter (2), Symbol (3), Number (4)
    random_num = random.randint(1, 4)
    if random_num == 1:
        if num_capital_letters > 0:
            idx = random.randint(0, total_capitals-1)
            password += capital_letters[idx]
            num_capital_letters -= 1
            password_len += 1
        else:
            continue 
    elif random_num == 2:
        if num_small_letters > 0:
            idx = random.randint(0, total_smalls-1)
            password += small_letters[idx]
            num_small_letters -= 1
            password_len += 1
        else:
            continue
    elif random_num == 3:
        if num_symbols > 0:
            idx = random.randint(0, total_symbols-1)
            password += symbols[idx]
            num_symbols -= 1
            password_len += 1
        else:
            continue
    elif random_num == 4:
        if num_numbers > 0:
            idx = random.randint(0, total_numbers-1)
            password += str(numbers[idx])
            num_numbers -= 1
            password_len += 1
        else:
            continue

print(f"Your password is : {password}")

        