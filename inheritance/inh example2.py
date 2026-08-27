class animal():
    def eat(self):
        print("eating")
class dog(animal):
    def bark(self):
        print("dog is barking")
class cat(animal):
    def meow(self):
        print("cat is meowing")
c1=dog()
c1.eat()
c1.bark()

c2=cat()
c2.eat()
c2.meow()
