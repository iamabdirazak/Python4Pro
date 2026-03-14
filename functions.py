def greet(name):
    return f"Hello, {name}!"

print(greet("Abdirazak"))

def add(a, b):
    return a + b
print(add(5, 3))

def power ( base, exponent):
    return base ** exponent
print(power(exponent = 2, base = 3))

def total(*args):
    return sum(args)
print(total(1, 2, 3, 4, 5))

def user(**kwargs):
    return kwargs
print(user(name="Abdirazak", age=26, city="Borama"))

# Lambda function to calculate the square of a number
square = lambda x: x ** 2
print(square(5))

def operation(a, b):
    add = lambda x, y: x + y
    subtract = lambda x, y: x - y
    mult = lambda x, y: x * y
    return add(a, b), subtract(a, b), mult(a, b)
print(operation(10, 5))

# Higher-order function that takes another function as an argument

def apply_operation(func, a, b):
    return func(a, b)

# Using the higher-order function with a lambda function for addition
result = apply_operation(lambda x, y: x + y, 10, 5)
print(result)

# map function to apply a lambda function to a list of numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# filter function to filter out even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# reduce function to calculate the product of a list of numbers
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)

# Recursive function to calculate the factorial of a number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(f"factorial = {factorial(2)}")