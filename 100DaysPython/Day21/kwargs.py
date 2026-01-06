## **kwargs - many keyword arguements 

def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    return n
    

print(calculate(1, add=3, multiply=2))


## Make a class car where its init method takes **kwargs
class Car:
    def __init__(self, nick_name,  **kwargs):
        self.name = nick_name
        self.make = kwargs['make']
        self.model = kwargs['model']

    def car_intro(self):
        print(f"Hey this is {self.make}, model : {self.model}")

my_car = Car("Carzie", make="Nissan", model="EV")
print(my_car.name)
my_car.car_intro()