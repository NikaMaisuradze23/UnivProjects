from math import sqrt

class Point:

    def __init__(self, x1, x2 , y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


    def __str__(self):
        return f"პირველი კორდინატი:({self.x1},{self.y1}) \nმეორე კორდინატი:({self.x2},{self.y2}) "


    def mandzili(self,*args):
        result = sqrt((self.x1 - self.x2)**2 +(self.y1 - self.y2)**2)
        return f"კორდინატებს შორის მანძილი არის: {result}"

kordinati1 = int(input("ჩაწერეთ x1: "))
kordinati2 = int(input("ჩაწერეთ y1: "))
kordinati3 = int(input("ჩაწერეთ x2: "))
kordinati4 = int(input("ჩაწერეთ y2: "))

kord = Point(kordinati1, kordinati2, kordinati3, kordinati4)
print(kord)
print(kord.mandzili())



