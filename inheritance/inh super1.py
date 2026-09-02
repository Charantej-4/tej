class Animal:
    def sound(self):
             print("animal sound")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")
d1 = Dog()
d1.sound()