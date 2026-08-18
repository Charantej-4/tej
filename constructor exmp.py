class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(self.name)
        print(self.salary)
s=employee("tej",30000)
s.display()