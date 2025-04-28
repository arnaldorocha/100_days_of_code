# **kwargs: many keyword arguments
# This file contains a function that demonstrates the use of **kwargs in Python.
# It is used to pass a variable number of keyword arguments to a function.
# The function will print the name and value of each keyword argument passed to it.
# It is a simple demonstration of how to use **kwargs in Python.
# The function is called `print_kwargs` and it takes a variable number of keyword arguments. 
# It prints the name and value of each keyword argument passed to it.


# *args is a special syntax in Python that allows you to pass a variable number of arguments to a function.

def add(*args):
    """
    Add all the arguments together.
    """
    print(args[0])

    # sum = 0
    # for n in args:
    #     sum += n
    # return sum

    return sum(args)
print(add(1, 2, 3, 4, 5))  # Output: 15

def calculate(n, **kwargs):
    print(kwargs)
    
#     # kwargs is a dictionary of keyword arguments
#     # kwargs = {'add': 3, 'multiply': 5}
#     # kwargs['add'] = 3
#     # kwargs['multiply'] = 5

#for key, value in kwargs.items():
#         print(f"{key} = {value}")

    n += kwargs.get('add')
    n *= kwargs.get('multiply')
    print(n)
    
calculate(2, add = 3, multiply = 5)  # Output: 8


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.year = kw.get('year')
        self.color = kw.get('color')
        self.price = kw.get('price')

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color}) - ${self.price}"   
    
car1 = Car(make='Toyota', model='Camry', year=2020, color='Blue', price=20000)
print(car1)