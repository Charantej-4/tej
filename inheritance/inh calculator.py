class Calculator:
    def calculate(self, a, b):
        print("Sum:", a + b)
class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        super().calculate(a, b)
        print("Multiplication:", a * b)
c1 = AdvancedCalculator()
c1.calculate(10, 5)