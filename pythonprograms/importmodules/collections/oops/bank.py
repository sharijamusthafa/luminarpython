class person:
    def setvalue(self,pname,age):
        self.personame=pname
        self.page=age
    def printvalue(self):
        print(self.personame)
        print(self.page)
class Bank(person):
    bname="IFSC"
    def __init__(self,accountno):
        self.accno=accountno

        self.balance=5000

    def withdraw(self,amount):
         self.balance-=amount
         if(self.balance<amount):
             print("Insufficient balance")
         else:
             print("Remaining balance is ",self.balance)
    def deposit(self,amount):
        self.balance+=amount
        print("Account credicted with RS",amount)
        print("Remaining balance is",self.balance)
    def balanceEnquiry(self):
         print("Account number",self.accno)
         print("Name",self.name)
         print("Bank balance",self.balance)
         print("bank name",self.bankname)
obj=Bank(134567)
obj.setvalue("arjun",22)
obj.printvalue()
#obj.deposit(10000)
#obj.withdraw(60000)
n=1
while(n==1):
    print("\n1.check account details\n2.withdraw\n3.deposit\n4.exit")
    x=int(input("Enter your choice"))
    if x==1:
        obj.balanceEnquiry()
    elif x==2:
        y = int(input("enter amount to withdrawy"))
        obj.withdraw(y)
    elif x == 3:
        y = int(input("enter amount to deposit"))
        obj.deposit(y)
    elif x==4:
        n=0
        break
    else:
        print("invalid entry")

