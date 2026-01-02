# Conditional flows 
# If condition is true then do this otherwise do that

# Here we'll make a simple if-else control whether a person should drive a car or not, if age is above or equals to 18 then he/she can drive but if age is less than 18 then cannot drive.

age = int(input("Tell me your age? "))

if age >= 18:
    print("Can drive the car.")
else:
    print("Cannot drive the car.")