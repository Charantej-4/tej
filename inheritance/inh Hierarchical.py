class animal():
    def eat(self):
        print("animal eats")
class dog(animal):
    def bark(self):
        print("dog barks")
class cat(animal):
    def meow(self):
        print("cat meows")
c=dog()
c.eat()
c.bark()
d=cat()
d.eat()
d.meow()