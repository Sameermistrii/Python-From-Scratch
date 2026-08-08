"""Create a list of numbers from  1  to  10 .
Print the first three numbers using slicing.
Print the last three numbers using slicing

num = [i*1 for i in range(1,11)]
print(num)
print(num[0:3])                    #wrong apporach
print(num[-1:-4:-1])

"""

num = list(range(1, 11))

print(num[:3])
print(num[-3:])