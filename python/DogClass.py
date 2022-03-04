class Dog:
    def __init__(self, Breed, Size, Age, Color="black"):
        self.Breed = Breed
        self.Size = Size
        self.Age = Age
        self.Color = Color

    def sleep(self):
        return f"თქვენი ძაღლს ძინავს !! \nმონაცემები: \nჯიში: {self.Breed} \nზომა: {self.Size} \nასაკი: {self.Age} \nფერი: {self.Color}"


    def eat(self):
        return f"თქვენი ძაღლი ჭამს !! \nმონაცემები: \nჯიში: {self.Breed} \nზომა: {self.Size} \nასაკი: {self.Age} \nფერი: {self.Color}"

    def sit(self):
        return f"თქვენი ძაღლი ზის !! \nმონაცემები: \nჯიში: {self.Breed} \nზომა: {self.Size} \nასაკი: {self.Age} \nფერი: {self.Color}"


    def Run(self):
        return f"თქვენი ძაღლი დარბის !! \nმონაცემები: \nჯიში: {self.Breed} \nზომა: {self.Size} \nასაკი: {self.Age} \nფერი: {self.Color}"



obj1 = Dog("მეცხვარე", "დიდი", 18)
obj2 = Dog("ბანჯგვლიანი ნაგაზი", "დვანიაშკა", 18, "ლურჯი")
obj3 = Dog("პუდელ", "ახმახი", 20, "თეთრი")
obj4 = Dog("ჩოვ ჩოვი", "საშუალო", 3, "ყავისფერი")
print(obj1.sleep())
print(obj2.eat())
print(obj3.sit())
print(obj4.Run())



