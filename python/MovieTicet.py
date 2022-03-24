class Ticket:
    def __init__(self, movie_name, movie_price, tickets, language="Geo"):
        self.movie_name = movie_name
        self.movie_price = movie_price
        self.tickets = tickets
        self.language = language


    def __str__(self):
        return f"ფილმის დასახელება:{self.movie_name}   ენა:{self.language}"



class User(Ticket):
    def __init__(self, user_name, balance, movie_name, movie_price, tickets, language="Geo"):
        self.user_name = user_name
        self.balance = balance
        super().__init__(movie_name, movie_price, tickets, language)


    def __str__(self):
        return f"ბატონო/ქალბატონო {self.user_name} თქვენს ანგარიშზე არის {self.balance} ლარი"


    def getTicet(self,*args):
        if self.tickets < raodenoba and self.balance > self.tickets * self.movie_price:
            a = self.balance - self.tickets * self.movie_price
            b = raodenoba - self.tickets
            return f"თქვენ წარმატებით შეიძიენთ {self.tickets} ბილეთი, თქვენს ანგარიშზე დარჩა {a} ლარი \nდარჩენილია {b} ბილეთი "

        else: return f"სამწუხაროდ თქვენ თანხა არ გყოფნით თანხა: {self.balance} \n{self.tickets} არჩეული ბილეთის ფასი: {self.tickets * self.movie_price}"


    def deposit(self,*args):
            balansi = self.balance + shetana
            self.balance = balansi
            return f"თქვენი ბალანსი გაიზარდა და შეადგენს: {self.balance} ლარს"


raodenoba = 25
klienti = str(input("მოგესალმებით ბილეთის ფასი შეადგენს 10 ლარს, ჩაწერეთ თქვენი სახელი და გვარი:  "))
balansi = int(input("ჩაწერეთ თქვენი ბალანსი: "))
ob2 = User(klienti, balansi, "betmeni", 10, 1)

if balansi < 10:
    shetana = int(input("დაწერეთ შესატანი თანხა: "))
    print(ob2.deposit())
    balansi = balansi + shetana


filmi = str(input("აირჩიეთ ფილმი:  "))
ena = str(input("აირჩიეთ ენა:  "))
biletebi = int(input("რამდენი ბილეთი გნებავთ:  "))
ob2 = User(klienti, balansi, filmi, 10, biletebi)
ob1 = Ticket(filmi, 0, 0, ena)

print(ob2.getTicet())
print(ob1)








