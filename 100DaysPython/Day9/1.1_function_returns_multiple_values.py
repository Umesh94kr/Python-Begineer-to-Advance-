# this function returns multiple outputs

def sum_multiply(num1, num2):
    """
    Docstring for sum_multiply
    
    :param num1: Description
    :param num2: Description
    """
    addition = num1 + num2
    multiplication = num1 * num2 
    return addition, multiplication 

add, mul = sum_multiply(2, 3)

print(f"Addition : {add}")
print(f"Multiplication : {mul}")