class person():
    def __init__(self,name):
        self.name=name
class student(person):
    pass
s=student("charan")
print(s.name)