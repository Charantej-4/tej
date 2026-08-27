class animal():
    def eat(self):
        print("animal is eating")
class dog(animal):
    def bark(self):
        print("dog is barking")
s=dog()
s.eat()
s.bark()