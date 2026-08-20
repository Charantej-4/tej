class bankaccount():
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("invalid amount")
    def withdraw(self,amount):
        if amount>0:
            if amount<=self.__balance:
                self.__balance-=amount
            else:
                print("insufficient balance")
s=bankaccount(5000)
s.deposit(2000)
print(s.get_balance())
s.withdraw(3000)
print(s.get_balance())
s.withdraw(10000)
        
