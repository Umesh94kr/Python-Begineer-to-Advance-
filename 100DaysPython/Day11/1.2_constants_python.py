# constants are defined by Capital letters 
PI = 3.14159
GRAVITY = 9.8
MAX_SCORE = 100

# ideally for constants seperate module should be made and constants should be imported from that 
import constants
name = constants.USER_NAME 
email = constants.EMAIL 
phone_number = constants.PHONE 

print(f"Name of Person : {name}")
print(f"Email of person : {email}")
print(f"Phone number of person : {phone_number}")