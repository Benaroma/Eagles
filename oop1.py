class Fruits:
    def __init__(self, name, price, mass):
        self.name = name
        self.price = price
        self.mass = mass

    def display(self):
        print(f"These are {self.name} and cost {self.price} Ksh. per {self.mass}")


myobj = Fruits("Apples", "150", "Kg")
myobj.display()
myobj = Fruits("Apricots", "100", "Kg")
myobj.display()
myobj = Fruits("Avocados", "80", "Kg")
myobj.display()
myobj = Fruits("Oranges", "120", "Kg")
myobj.display()
myobj = Fruits("Mangoes", "50", "Kg")
myobj.display()
