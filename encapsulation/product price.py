class product():
    def __init__(self,price):
        self.__price=price
    def get_price(self):
        return self.__price
    def set_price(self,price):
        if price>=0:
            self.__price=price
        else:
            print("invalid price")
s=product(100)
s.set_price(750)
print(s.get_price())
s.set_price(-50)