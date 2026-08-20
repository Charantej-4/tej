class person():
    def __init__(self,age):
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if 0<=age<=100:
            self.__age=age
        else:
            print("age invalid")
s=person(25)
s.set_age(30)
print(s.get_age())
s.set_age(110)