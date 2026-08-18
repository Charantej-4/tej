class student():
    def setdata(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
s1=student()
s2=student()
s1.setdata("tej",20)
s2.setdata("sai",22)
s1.display()
s2.display()
