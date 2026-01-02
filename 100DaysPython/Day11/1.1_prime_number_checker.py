# Prime Number Checker

# Prime numbers are numbers that can only be cleanly divided by themselves and 1. 

# You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.  It should return True or False.

# 7 is a primer number because it is only divisible by 1 and itself.

# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1.

def check_prime(number):
    if number == 2:
        return True
    is_prime = True
    for i in range(2, number):
        if number%i == 0:
            is_prime = False

    return is_prime

print(f"Is 7 a prime number or not? {check_prime(7)}")
print(f"Is 6 a prime number or not? {check_prime(6)}")
