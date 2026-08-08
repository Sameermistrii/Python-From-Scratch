"""3. Tuples and Operations on Tuples
Create a tuple  coordinates = (10, 20)  and print both elements.
Try to modify the tuple by setting  coordinates[0] = 50  — note what
happens.
Convert the tuple to a list, change its first element to  50 , and convert it back
to a tuple"""

coordinates = (10, 20)

# Print both elements
print(coordinates[0])
print(coordinates[1])

# Try modifying the tuple
# coordinates[0] = 50
# TypeError: tuple does not support item assignment

# Convert tuple → list
replace = list(coordinates)

# Change first element
replace[0] = 50

# Convert list → tuple
coordinates = tuple(replace)

print(coordinates)