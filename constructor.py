class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
s1=student("tej",21)
s2=student("sai",42)
s1.display()
s2.display()