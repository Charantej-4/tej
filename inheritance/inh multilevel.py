class animal():
    def sound(self):
        print("animal sound")
class dog(animal):
    def bark(self):
        print("dog barks")
class cat(dog):
    def meow(self):
        print("cat meows")
c=cat()
c.sound()
c.bark()
c.meow()