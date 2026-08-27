class person():
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s=student("tej",84)
print(s.name)
print(s.marks)