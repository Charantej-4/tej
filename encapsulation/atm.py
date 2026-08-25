class atm():
    def __init__(self,balance,pin):
        self.__balance=balance
        self.__pin=pin
    def get_balance(self):
        return self.__balance
    def check_pin(self,pin):
        if pin==self.__pin:
            return "true"
        else:
            return "false"
    def deposit(self,amount):
        if amount>=0:
            self.__balance+=amount
        else:
            print("invalid deposit amount")
    def withdraw(self,amount,pin):
        if not self.check_pin(pin):
            return "incorrect pin"
        elif amount<=0:
            print("invalid withdraw amount")
        elif amount>self.__balance:
            print("insufficient balance")
        else:
            self.__balance-=amount
a=atm(10000,1234)
a.withdraw(3000,1234)
print(a.get_balance())
a.withdraw(3000,1243)
        
