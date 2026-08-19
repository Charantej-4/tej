class employee():
    def __init__(self,salary):
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
            print("salary invalid")
s=employee(10000)
s.set_salary(15000)
print(s.get_salary())
s.set_salary(-5000)