class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def work(self):
        super().work()
        print("Developer is writing code")
d1 = Developer()
d1.work()