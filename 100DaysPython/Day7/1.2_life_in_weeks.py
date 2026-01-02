# Write a Python program that calculates how many weeks a person has left to live, assuming the average lifespan is 90 years.

# The program should:

# Ask the user to enter their current age.
# Calculate the remaining years left until the age of 90.
# Convert the remaining years into weeks (assuming 52 weeks per year).
# Display the total number of weeks remaining.

#################### SOLUTION #######################

def life_in_weeks(age):
    # if person is supposed to live 90 years, then remaining years
    remaining_age = 90 - age 
    weeks_in_year = 52 # There are 52 weeks in a year
    remaining_life_weeks = remaining_age * weeks_in_year
    return remaining_life_weeks

age = int(input("Enter your age? "))
print(f"Weeks remaining : {life_in_weeks(age)}")
