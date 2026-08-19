class person():
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("age is invalid")
s=person("teja",25)
print(s.name)
print(s.get_age())
print(s.set_age(10))