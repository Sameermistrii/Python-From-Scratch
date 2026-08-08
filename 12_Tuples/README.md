Tuples and Operations on Tuples
Tuples are ordered but immutable collections (cannot be changed after creation).

Creating a Tuple:
my_tuple = (10, 20, 30)
single_element = (5,)  # Tuple with one element (comma required)

Accessing Tuple Elements:
print(my_tuple[1])  # Output: 20

Tuple Unpacking:
a, b, c = my_tuple
print(a, b, c)  # Output: 10 20 30

Common Tuple Methods:
Method	Description	Example	Output
count(x)	Returns the number of times x appears in the tuple	(1, 2, 2, 3).count(2)	2
index(x)	Returns the index of the first occurrence of x	(10, 20, 30).index(20)	1
my_tuple = (1, 2, 2, 3, 4)
print(my_tuple.count(2))  # Output: 2
 
print(my_tuple.index(3))   # Output: 3

Why Use Tuples?
Faster than lists (since they are immutable)
Used as dictionary keys (since they are hashable)
Safe from unintended modifications

