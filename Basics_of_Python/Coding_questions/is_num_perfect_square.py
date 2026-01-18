# Given a positive integer num, write a function that returns True if num is a perfect square else False.
import math 

def is_perfect_square(num: int) -> bool:
    # I should iterate this for some fixed number only 
    if num == 1 or num == 0:
        return True
    
    start = 2
    end = num-1
    while(start <= end):
        mid = (start + end)//2
        if mid**2 == num:
            return True 
        elif mid**2 > num:
            end = mid-1
        else:
            start = mid+1 
    return False


print(is_perfect_square(17))