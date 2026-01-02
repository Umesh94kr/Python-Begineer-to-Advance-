######### USE OF NESTED IF-ELSE ###########

age = int(input("Tell your age? "))
driving_liscence = input("Do you have a driving lisence? Yes or No ")

if age >= 18:
    if driving_liscence == "Yes":
        print("You can drive the car!")
    else:
        print("Get a lisence first.")
else:
    print("You are below 18, so you can't drive the car.")

######### USE OF elif ###########
# when you have multiple if statements 

marks = float(input("What are your marks?"))

if marks > 90:
    print('Excellent')
elif marks > 70:
    print('Good')
elif marks > 50:
    print('OK')
else:
    print('Failed')