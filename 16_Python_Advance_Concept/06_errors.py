# while True:
#     try: 
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"The division is {a / b}")

#     except ValueError:
#         print("Please dont perform bad typecasts")
    
#     except ZeroDivisionError:
#         print("Hey dont divide by 0")

#     except Exception as e:
#         print("Unknown error occurred!", e)

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if b == 0:
    raise ValueError("Please dont divide by 0")

print(f"The division is {a / b}")