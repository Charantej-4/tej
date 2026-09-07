class Employee():
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def write_code(self):
        print("Developer is writing code")
class Tester(Employee):
    def test_code(self):
        print("Tester is testing code")
d1 = Developer()
t1 = Tester()
d1.work()
d1.write_code()
t1.work()
t1.test_code()