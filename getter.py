class student():
    def __init__(self,name,rollno):
        self.name=name
        self.__rollno=rollno
    def get_rollno(self):
        return self.__rollno
s=student("charan",101)
print(s.name)
print(s.get_rollno())