class python():
    def __init__(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        self.__marks=marks
s=python(100)
print(s.get_marks())
s.set_marks(80)
print(s.get_marks())
    
