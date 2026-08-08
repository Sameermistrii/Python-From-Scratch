Sets and Set Methods
Sets are unordered, unique collections (no duplicates).

Creating a Set:
fruits = {"apple", "banana", "cherry"}

Key Set Methods:
my_set = {1, 2, 3, 4}
 
my_set.add(5)        # {1, 2, 3, 4, 5}
my_set.remove(2)     # {1, 3, 4, 5}
my_set.discard(10)   # No error if element not found
my_set.pop()         # Removes random element

Set Operations:
a = {1, 2, 3}
b = {3, 4, 5}
 
print(a.union(b))       # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}
print(a.difference(b))   # {1, 2}

Use Case: Sets are great for eliminating duplicate values.