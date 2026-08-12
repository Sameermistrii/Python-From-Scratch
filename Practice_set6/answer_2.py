""" Create a class  Person  with a constructor ( __init__ ) that accepts  name  and  age
as arguments and stores them as instance attributes.
Create an object and print the person’s name and age""" 

class Person:
    def __init__ (self, name ,age):
        self.name = name
        self.age = age 

person1 = Person("Sam",21)
print(person1.name)
print(person1.age)