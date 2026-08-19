class bankaccount():
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        if balance>1000:
            self.__balance=balance
        else:
            print("balance invalid")
s=bankaccount(1000)
s.set_balance(1500)
print(s.get_balance())
s.set_balance(500)