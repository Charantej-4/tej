class Animal():
    def sound(self):
        print("Animal sound")
class dog(Animal):
    def sound(self):
        print("Dog barks")
d=dog()
d.sound()