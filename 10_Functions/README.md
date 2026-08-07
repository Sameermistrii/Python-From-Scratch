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

