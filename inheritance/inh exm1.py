class Teacher():
    def teach(self):
        print("Teacher is teaching")
class Student():
    def study(self):
        print("Student is studying")
class TeachingAssistant(Teacher, Student):
    def assist(self):
        print("Teaching assistant is helping")
t1 = TeachingAssistant()
t1.teach()
t1.study()
t1.assist()