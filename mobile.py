class mobile():
    def __init__(self,brand,price):
        self.__brand=brand
        self.__price=price
    def get_brand(self):
        return self.__brand
    def get_price(self):
        return self.__price
    def set_price(self,price):
        if price>=0:
            self.__price=price
        else:
            print("invalid price")
s=mobile("Samsung",1000)
print(s.get_brand())
print(s.get_price())
s.set_price(1200)
print(s.get_price())



        