# 🚨 Error Handling in Python

# Error handling lets your program handle unexpected situations without crashing.
# Python uses try / except blocks for this.

# try:
#     # code that may cause an error
# except:
#     # code that runs if an error occurs

# ================================================================================

try:
    x = int(input("Enter a number: "))
    print(round(10 / x, 2))
except Exception as e:
    print(f"Something went wrong! Error : {e}")

# ================================================================================

# 🧹 finally Block
# Runs no matter what (error or not).

try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution finished")

# ================================================================================

# 🚫 Raising Errors Manually

age = int(input("Enter age: "))
if age < 0:
    raise ValueError("Age cannot be negative")