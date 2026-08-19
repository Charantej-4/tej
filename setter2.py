class python():
    def __init__(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks=marks
        else:
            print("marks are invalid")
s=python(90)
s.set_marks(95)
print(s.get_marks())
s.set_marks(110)