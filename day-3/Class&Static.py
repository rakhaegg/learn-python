class Rectangle:
    def __init__(self , width , height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height


    # Class Mehod

    @classmethod
    def new_square(cls , side_length):
        return cls(side_length , side_length)

square = Rectangle.new_square(5)

print(square.calculate_area())




class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod

    # Tanpa menggunakan parameter self
    
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam" , "pineapple"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)