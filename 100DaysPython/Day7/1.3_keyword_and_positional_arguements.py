# Keyword arguements are defined by keys while calling the function

def sum(num1, num2):
    return num1 + num2 

print(sum(num1=1, num2=5))

# Positional arguements recognizes the value of inputs by position 
def calculate_age(current_year, birth_year):
    return current_year - birth_year 

print(calculate_age(2026, 2004))