square = lambda x: x*x 
'''
As good as writing
def square(x):
    return x*x
'''
sum = lambda x, y: x+y
'''
As good as writing
def sum(x, y):
    return x + y
'''

print(square(3))
print(sum(3, 62))

#my example you can also get take user input and use it in lambda function
x = int(input("Enter a number to square: "))  
square = lambda x: x*x
print(square(x))
