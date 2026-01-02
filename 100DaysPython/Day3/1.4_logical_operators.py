# AND / OR / NOT 

# AND allows when both conditions are True 
# OR allows if either one condition is True 
# NOT reverses a condition 

a = True
b = False

if a and a:
    print("AND operator success")
if a and b:
    print("AND operator fail condition")
if a or b:
    print("OR operator success condition")
if not b:
    print("NOT of False is True")