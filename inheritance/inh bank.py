class BankAccount():
    def account_info(self):
        print("This is a bank account")

class SavingsAccount(BankAccount):
    def account_info(self):
        super().account_info()
        print("This is a savings account")
a1 = SavingsAccount()
a1.account_info()