Defining Functions in Python
Functions help in reusability and modularity in Python.

Syntax:
def greet(name):
    return f"Hello, {name}!"
 
print(greet("Alice"))  # Output: Hello, Alice!

Key Points:
Defined using def keyword.
Function name should be meaningful.
Use return to send a value back.

Function Arguments & Return Values
Functions can take parameters and return values.

Types of Arguments:
Positional Arguments
def add(a, b):
    return a + b
 
print(add(5, 3))  # Output: 8

Default Arguments
def greet(name="Guest"):
    return f"Hello, {name}!"
 
print(greet())  # Output: Hello, Guest!

Keyword Arguments
def student(name, age):
    print(f"Name: {name}, Age: {age}")
 
student(age=20, name="Bob")

Lambda Functions in Python
Lambda functions are anonymous, inline functions.

Syntax:
square = lambda x: x * x
print(square(4))  # Output: 16

Example:

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

Recursion in Python
A function calling itself to solve a problem.

Example: Factorial using Recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
 
print(factorial(5))  # Output: 120

Important Notes:
Must have a base case to avoid infinite recursion.
Used in algorithms like Fibonacci, Tree Traversals.


Modules and pip - Using External Libraries
Importing Modules
Python provides built-in and third-party modules.

Example: Using the math module
import math
 
print(math.sqrt(16))  # Output: 4.0

Creating Your Own Module
Save this as mymodule.py:

def greet(name):
    return f"Hello, {name}!"

Import in another file:

import mymodule
print(mymodule.greet("Alice"))  # Output: Hello, Alice!

Installing External Libraries with pip
pip install requests

Example usage:

import requests
 
response = requests.get("https://api.github.com")
print(response.status_code)