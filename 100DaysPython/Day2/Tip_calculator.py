########## TIP CALCULATOR #############
# Asks for total bill
# Asks for amount you'll give as tip 
# Asks for How many people to split in betweeen
# Displays each person's split 

total_amount = float(input("What is the total bill amount in $ "))
tip_percentage = float(input("How much tip you'll like to give : 10%, 12% or 15% "))
num_persons = float(input("Number of people to split the bill between : "))
total_bill_amount = total_amount + (tip_percentage/100)*total_amount

print(f"Each persons split : ${round(total_bill_amount / num_persons, 2)}")

