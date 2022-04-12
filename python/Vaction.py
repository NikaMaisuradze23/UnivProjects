class Vaqcina:
    def __init__(self, vaq_saxeli, vaq_oden, mwarmoebeli, asaki):
        self.vaq_saxeli = vaq_saxeli
        self.vaq_oden = vaq_oden
        self.mwarmoebeli = mwarmoebeli
        self.asaki = asaki


    def __str__(self):
        return f"თქვენი ვაქცია არის {self.vaq_saxeli}, მწარმოებელი {self.mwarmoebeli}, ოდენობა {self.vaq_oden}"



class User:
    def __init__(self, piradinom, saxeli, asaki, gaketebuli, gaketebulis_oden=0):
        self.piradinom = piradinom
        self.saxeli = saxeli
        self.aski =asaki
        self.gaketebuli = gaketebuli
        self.gaketebulis_oden = gaketebulis_oden


    def __str__(self):
         return f"ბატონო/ქალბატონო {self.saxeli} თქვენი პირადი ნომერია {self.piradinom}"



    def vaqcinis_gaketeba(self,*args):
        result = vaqcina_oden - 1
        return f"ბატონო/ქალბატონო {self.saxeli} თქვენ წამრატებით აიცერით !! კლინიკაში დარჩენილია {result} ვაქცინა"



vaqcina = str(input("ჩაწერეთ რომელი ვაქცინა გნებავთ: "))
vaqcina_oden = 100
mwarmoebeli = str(input("რომელი მწარმოებელი გინდათ ჩინეთი თუ ამერიკა: "))
asaki = int(input("დაწერეთ თქვენი ასაკი: "))

obVaqc = Vaqcina(vaqcina, vaqcina_oden, mwarmoebeli, asaki)
print(obVaqc)



if asaki > 17:
        pirad = int(input("დაწერეთ პირადი ნომერი: "))
        saxeli = str(input("დაწერეთ თქვენი სახელი: "))
        gaketebuli = str(input("რა ვაქცინები გაქვთ გაკეთებული: "))
        gaketebuli_oden = int(input("რამდენი ვაქცინა გაქვთ გაკეთებული ?"))

        obUser = User(pirad, saxeli, asaki, gaketebuli, gaketebuli_oden)
        print(obUser)
        print(obUser.vaqcinis_gaketeba())


else: print("თქვენ არასრულწლოვანი ხართ.")








