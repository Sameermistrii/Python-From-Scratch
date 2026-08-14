def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper 
    return decorator

@repeat(7)
def say_hello(a):
    print(f"Hello! {a}")

'''
It replaces the function say_hello with this:
def decorator(func):
    def wrapper(a):
        for i in range(n):
            say_hello(a)
    return wrapper
'''

say_hello("Sameer")