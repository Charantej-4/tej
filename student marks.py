class student():
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    def get_name(self):
        return self.__name
    def set_name(self,name):
        if name!="":
            self.__name=name
        else:
            return "invalid name"
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks=marks
        else:
            return "marks invalid"
    def get_grade(self):
        if self.__marks>=90:
            return "A"
        elif self.__marks>=80:
            return "B"
        elif self.__marks>=70:
            return "C"
        elif self.__marks>=60:
            return "D"
        else:
            return "F"
s=student("teja",79)
print(s.get_name())
print(s.get_marks())
print(s.get_grade())
    
