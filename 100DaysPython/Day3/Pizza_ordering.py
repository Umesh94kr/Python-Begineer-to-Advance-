print("Welcome to Python Pizza deliveries !!")

size = input("What size of Pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total_price = 0

if size == 'S':
    total_price += 10
elif size == 'M':
    total_price += 20 
else:
    total_price += 30 

if pepperoni == 'Y':
    total_price += 5

if extra_cheese == 'Y':
    total_price += 3 

print(f"Total price of your Pizza is : ${total_price}")