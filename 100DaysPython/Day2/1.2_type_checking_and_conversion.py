# to check 'type' of a data type you need to use 'type(variable_name')'
name = "Umesh"
print(type(name)) # this will be a str

# type conversion 
num = "8"
print(type(num)) # this will be a str 
# converting a string to integer 
num_int = int(num)
print(type(num_int))

# converting an integer to str
num = 8
print(type(num))

num_str = str(num)
print(type(num_str))
# print("My number is " + num)
# above line will give an error as string can't be concatenated with an integer

# But this will work (after type conversion)
print("My number is " + num_str)