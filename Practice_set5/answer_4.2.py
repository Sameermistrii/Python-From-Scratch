""" my_set = {1, 2, 3, 3, 4},  Add  5  to the set, remove  2 , and check if  4  is in the set"""

my_set = {1, 2, 3, 3, 4}

my_set.add(5)
my_set.remove(2)

print(my_set)
print(4 in my_set)