def addition(num1, num2):
    return num1 + num2 

def multiply(num1, num2):
    return num1 * num2 

def subtract(num1, num2):
    return num1 - num2 

def divide(num1, num2):
    return num1 / num2

operations = {
    '+' : addition,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}

num1 = float(input("Enter first number? "))
opr = input("Enter the operator '+', '-', '/', '*' ->>> ")
num2 = float(input("Enter second number? "))

print(operations[opr](num1, num2))
