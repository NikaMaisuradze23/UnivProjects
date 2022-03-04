
class Rectangle:
    def __init__(self, width, hight, color="red"):
        self.width = width
        self.hight = hight
        self.color = color


    def __str__(self):
        return f"მართუკუთხესი სიგრძეა {self.width}, სიგანე {self.hight}, ფერი {self.color}"



    def peimetri(self):
        return 2*(self.width + self.hight)


    def area(self):
        print((self.width * self.hight))

obj1 = Rectangle(4,8,"blue")
print(obj1.peimetri())
obj1.area()



