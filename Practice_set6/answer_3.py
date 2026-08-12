"""
Create a base class  Animal  with a method  sound()  that prints  "Some sound" .
Create a derived class  Dog  that overrides  sound()  to print  "Bark!" .
Create an object of  Dog  and call  sound() 
"""

class Animal:
    def speak(self):
        print("Animal Sound")
class Dog(Animal):
    def speak(self):
        print("woof!")
dog1 = Dog()
dog1.speak()