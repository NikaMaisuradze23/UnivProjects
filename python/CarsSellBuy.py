class Car:
    def __init__(self, model, makeYear, fuelType, color="black"):
        self.color = color
        self.model = model
        self.makeYear = makeYear
        self.fuelType = fuelType


    def sell(self):
        return f"თქვენი მანქანა {self.model} ,{self.makeYear} ,{self.fuelType},{self.color} წარმატებით გაიყიდა"


    def buy(self):
        return f"თქვენ მანქანა {self.model} ,{self.makeYear} ,{self.fuelType},{self.color} წარმატებით იყიდეთ"


obj1 = Car("E-class", 1990, "Dizel")
obj2 = Car("X5", 2008, "Dizeli", "Blue")
print(obj1.sell())
print(obj2.buy())

