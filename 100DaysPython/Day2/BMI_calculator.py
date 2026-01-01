# BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:

# bmi is equal to the person's weight divided by the person's height squared.

height = input("Enter your height in m ")
weight = input("Enter your weight in kg ")

# Data type of height and weight is string (because they are taken from input function and it turns every entry into string) 
# So we need type conversion to float 
height_new = float(height)
weight_new = float(weight)

print("BMI : " + str(round(weight_new / (height_new ** 2), 2)))


