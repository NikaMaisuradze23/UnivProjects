class Bank_Account:
    def __init__(self, account_name, balance, jami=0):
        self.account_name = account_name
        self.balance = balance
        self.jami = jami



    def deposti(self,*args):
        self.jami = self.balance + shetana
        return f"ბატონო/ქალბატონო {self.account_name}, ოპერაცია წარმატებით დასრულდა \nთქვენს ანგარიშზე არის {self.jami} ლარი"

    def withdraw(self,*args):
        if self.balance < gamotana:
            return f"თქვენს ანგარიშზე საკმარისი თანხა არ არის, ბალანსი: {self.balance}"

        self.balance = self.balance - gamotana
        return f"ბატონო/ქალბატონო {self.account_name}, ოპერაცია წარმატებით დასრულდა \nთქვენს ანგარიშზე არის {self.balance} ლარი"


name = str(input("შეიტანეთ კლიენტის სახელი გვარი:  "))
tanxa = int(input("რა თანხა გავქთ ახლა ანგარიშზე ?  "))



operacia = int(input("თანხის შეტანა: 1, თანხის გამოტანა: 2  "))
if operacia == 1:
    shetana = int(input("რა თანხის შეტანა გსურთ ?  "))
    user = Bank_Account(name, tanxa)
    print(user.deposti())

if operacia == 2:
    gamotana = int(input("რა თანხის გამოტანა გსურთ ? "))
    user = Bank_Account(name, tanxa)
    print(user.withdraw())

