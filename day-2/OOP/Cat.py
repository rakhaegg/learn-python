class Animal:
    def __init__(self , name , color):
        self.name = name
        self.color = color



class Cat(Animal):
    legs = 4
    
    def purr(self):
        print("Pur......")
    """
    METHOD
    """
    
class Dog(Animal):
    def bark(self) : 
        print("WOLF")


felix = Dog("Fido" , "Brown")
print(felix.color)
"""
METHOD
"""
felix.bark()