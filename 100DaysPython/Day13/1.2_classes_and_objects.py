# PascalCase -> snake_case -> camelCase

# self - refers to current instance of that class

class Student:
    # constructor - going to be called everytime you create a new object
    def __init__(self, user_id, name, marks):
        # attributes are the thing which object has
        self.id = user_id 
        self.name = name 
        self.marks = marks 

    def say_hello(self):
        print(f"Hello, My name is {self.name}!")


# making an object 
s1 = Student(1, "Angela", 56)
s1.say_hello()

     