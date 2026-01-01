# previously if we want to concatenate an integer or any data type with string then it requires a type conversion but f-strings allow us to concatenate without using type conversion

number = 8 

# previously 
print("My number is : " + str(number))

# after f-string
print(f"My number is : {number}")