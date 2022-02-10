"""Inheritance : When we have to use the same kind of functions
for other classes, define the function on the parent class and declare it with the
new class
"""

class Mammal:
    def kind():
        print("This is a Mammal")

class Dog(Mammal):
    pass #Helps to pass with an empty class

class Cat(Mammal):
    def statement():
        print("This is a cat")

variable=Cat
variable.kind()
variable.statement()