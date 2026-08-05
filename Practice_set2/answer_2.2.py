num1 = int(input("Enter the first number: "))
num2 = (input("Enter the operator (+, -, *, /): "))
num3 = int(input("Enter the second number: "))  

status = num2

match status:
    case "+":
        print(f"{num1} + {num3} = {num1 + num3}")

    case "-":
        print(f"{num1} - {num3} = {num1 - num3}")

    case "*":
        print(f"{num1} * {num3} = {num1 * num3}")   

    case "/": #always remember this special case for division, because we cannot divide by zero
        if num3 != 0:  
            print(f"{num1} / {num3} = {num1 / num3}")  
        else:
            print("Error: Division by zero is not allowed.")     

    case _:
        print("Invalid operator. Please use +, -, *, or /.")
        



