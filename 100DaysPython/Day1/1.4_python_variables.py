# variable is something which stores a value 
name = "Jack"
number = 80
decimal_number = 90.092

# all these name, number, and decimal_number are variables which store some values 

print(name)
print(number)
print(decimal_number)

# some rules for variable naming 
# 1. Must start with a letter (a–z, A–Z) or underscore _
# 2. Cannot contain spaces or special characters (user-name ❌) 
# 3. Case sensitive (user_name and USER_NAME are different)     
# 4. Cannot be a python keyword (class = 5, for = 10)         

####### EXERCISE #############

# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.

####### SOLUTION #############

glass1 = "milk"
glass2 = "juice"

print("Glass1 " + glass1)
print("Glass2 " + glass2)

# now we'll swap these values
dummy_glass1 = glass1 
glass1 = glass2 
glass2 = dummy_glass1 

print("Glass1 " + glass1)
print("Glass2 " + glass2)