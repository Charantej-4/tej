class Vehicle():
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    def drive(self):
        print("Car is moving")
class Bike(Vehicle):
    def ride(self):
        print("Bike is moving")
c1 = Car()
b1 = Bike()
c1.start()
c1.drive()
b1.start()
b1.ride()