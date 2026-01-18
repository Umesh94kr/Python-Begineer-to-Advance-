# Given an integer n, return the number of trailing zeroes in n factorial n!

def trailing_zeros(num: int) -> int:
    count = 0
    while(num != 0):
        if num%10 == 0:
            count += 1
            num /= 10
        else:
            break
    return count 

def calculate_factorial(num: int) -> int:
    if num == 1:
        return 1
    ans = num * calculate_factorial(num-1)
    return ans 

factorial = calculate_factorial(7)
zeros = trailing_zeros(factorial)

print(f"Number of trailing zeros in factorial of 7 are : {zeros}")