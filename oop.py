# object is a variable with access to a class

class Car:

    def __init__(self, make, model, year,colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def onyehsa(self):
        print(f" My dream car is a {self.make} and my model is a {self.model} manufactured in {self.year} which is {self.colour}.")


myobj = Car("Toyota", "Vitz", "2020","Glittered-dark purple")
myobj.onyehsa()
myobj2 = Car("Mazda","CX-5","2022","black")
myobj2.onyehsa()
