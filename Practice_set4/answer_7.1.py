def fibonacci(n):
    # Base case
    if n == 0 or n == 1:
        return n

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


n = 6

for i in range(n):
    print(fibonacci(i))