# Creating dictionary from existing iterables 
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']

marks_dict = {name : random.randint(0, 100) for name in names}
print(marks_dict)

# students with score greater than or equals to 60 are considered as passed 
passed_students = {name : marks for name, marks in marks_dict.items() if marks >= 60}
print(f"Passed Students : {passed_students}")