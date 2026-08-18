class car():
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print(self.brand)
        print(self.model)
        print(self.price)
s1=car("bmw","m2",5000000)
s2=car("audi","q7",6000000)
s1.display()
s2.display()