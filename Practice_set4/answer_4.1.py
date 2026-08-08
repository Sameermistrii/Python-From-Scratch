# Write a recursive function  factorial(n)  that returns the factorial of a number.
def factorial(n):
    if n ==1:
        return 1
    return n*(n-1)
print(factorial(4))