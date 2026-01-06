## many positional arguements

def add(*args):
    print(type(args))
    sum_result = 0
    for n in args:
        sum_result += n
    return sum_result

print(f"Adding 2 numbers : {add(1, 2)}")
print(f"Adding 3 numbers : {add(2, 3, 4)}")
print(f"Adding 4 numbers : {add(4, 5, 6, 7)}")